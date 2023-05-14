from flask import request, session
from flask_restx import Resource, Namespace, fields
from models import *
from flask_login import login_required, current_user
from collections import Counter
from sqlalchemy import func


Result = Namespace(
    name='Result',
    description="결과 페이지에서 사용하는 API"
)

mbti_fields = Result.model('User MBTI', {
    'user_mbti': fields.String(description="사용자 MBTI", example="ENTP")
})

answers_fields = Result.inherit('User Answers or direct input mbti', mbti_fields, {
    'answers': fields.List(fields.String)
})

same_mbti_top10_fields = Result.model('Same MBTI Top 10 Movies', {
    'top10_for_same_mbti_users': fields.List(fields.List(fields.String)),
    'top10_in_naver': fields.List(fields.List(fields.String)),
    'word_cloud': fields.String(description="워드 클라우드 link")
})


@Result.route('/')
class ShowResult(Resource):
    def clear_characters_in_session(self):
        """
        session에서 same_characters와 compatible_characters를 None으로 변경
        """
        session.pop('same_characters', None)
        session.pop('compatible_characters', None)

    def get_user(self):
        """
        user id가 current_user id와 같은 user 객체 반환
        """
        return User.query.filter(User.id == current_user.id).first()

    def result_list_to_mbti_indicator(self, answers):
        """
        테스트 진행 답변 기반으로 mbti 계산.
        """
        result = [[], [], [], []]
        for i in range(len(answers)):
            mbti_indicator = db.session.query(Option.mbti_indicator).filter(Option.question_id == i+2, Option.content.like(answers[i]+'%')).first()
            mbti_indicator = str(getattr(mbti_indicator, Option.mbti_indicator.name))
            
            if mbti_indicator in ('I', 'E'):
                result[0].append(mbti_indicator)
            elif mbti_indicator in ('N', 'S'):
                result[1].append(mbti_indicator)
            elif mbti_indicator in ('T', 'F'):
                result[2].append(mbti_indicator)
            elif mbti_indicator in ('P', 'J'):
                result[3].append(mbti_indicator)
            else:
                return False
        return result

    def calculate_mbti(self, result):
        """
        사용자 mbti 계산
        """
        user_mbti = ""
        for li in result:
            user_mbti += Counter(li).most_common(n=1)[0][0]            
        
        return user_mbti
    
    def answer_list_to_str(self, answers):
        return "".join(str(_) for _ in answers)

    def store_answer(self, user_id, answers):
        answer = Answer(user_id, answers)
        db.session.add(answer)
        

    @login_required
    @Result.response(200, 'Success', mbti_fields)
    def get(self):
        """
        사용자 mbti 전달
        """
        # 테스트 결과 -> 사용자 mbti 전달
        user = User.query.filter(User.id == current_user.id).first()
        return {
            'user_mbti': user.mbti
        }, 200


    @login_required
    @Result.expect(answers_fields)
    @Result.response(200, 'success')
    @Result.response(500, 'fail')
    def post(self):
        """
        테스트 진행 후 결과 데이터 저장. 
        answers가 ["a", "b", ..."] 형태 리스트 형태로 전달된다고 가정. 
        answers 또는 user_mbti 둘 중 하나는 null값이 아니어야 함. 
        바로 결과보기의 경우 user_mbti 값만, 테스트 진행한 경우 answers 값만 post 요청하면 됨.
        """
        answers = request.json.get('answers')
        user_mbti = request.json.get('user_mbti')

        # answers가 None이 아니고 user_mbti가 None
        if answers and user_mbti is None:
            mbti_indicators = self.result_list_to_mbti_indicator(answers)
            if not mbti_indicators:
                print('잘못된 데이터입니다.')
                return {"post": "wrong data"}, 500
        
            user_mbti = self.calculate_mbti(mbti_indicators)
            
            if current_user.is_authenticated:
                answers = self.answer_list_to_str(answers)
                self.store_answer(current_user.id, answers)
            else:
                print("current_user is None")

        # 테스트를 진행했든, 바로 user_mbti를 입력 받았든 알게 된 user_mbti를 db에 저장
        user = self.get_user()
        user.mbti = user_mbti

        db.session.commit()
        self.clear_characters_in_session()

        return {"post": "success"}


@login_required
@Result.route('/top10')
class Top10Movies(Resource):
    def get_genre(self, movie_id):
        genres = db.session.query(MovieGenre.genre).filter(MovieGenre.movie_id == movie_id).all()
        genres = [str(getattr(row, MovieGenre.genre.name)) for row in genres]
        return genres

    def append_genre(self, length, movie_infos, get_movie_id):
        for i in range(length):
            movie_id = get_movie_id(i)
            movie_infos[i].append(self.get_genre(movie_id))
        return movie_infos
    
    def top10_to_same_mbti_user(self, mbti):
        same_mbti_users = db.session.query(User.id).filter(User.mbti == mbti)
            
        # TODO: 유저 평점도 넘겨야 할 경우, 수정 필요
        top10_movie_in_same_mbti = db.session.query(Satisfaction.movie_id).filter(Satisfaction.user_id.in_(same_mbti_users)).group_by(Satisfaction.movie_id).order_by(func.avg(Satisfaction.user_rating).desc()).limit(10)
        top10_movie_infos = db.session.query(Movie.id, Movie.kor_title, Movie.eng_title, Movie.image_link, Movie.pub_year, Movie.director, Movie.rating, Movie.story, Movie.run_time).filter(Movie.id.in_(top10_movie_in_same_mbti)).all()
        top10_movie_infos = [list(row) for row in top10_movie_infos]

        def get_movie_id(i):
            return str(getattr(top10_movie_in_same_mbti[i], Satisfaction.movie_id.name))

        # 장르 삽입
        top10_movie_infos = self.append_genre(top10_movie_in_same_mbti.count(), top10_movie_infos, get_movie_id)
        
        return top10_movie_infos


    def top10_in_naver_same_mbti_char(self, mbti):
        # 유저 mbti와 같은 캐릭터 뽑아내기
        characters = db.session.query(Character.id).filter(Character.mbti == mbti)
        movies = db.session.query(CharacterInMovie.movie_id).filter(CharacterInMovie.character_id.in_(characters))
        movies_info = db.session.query(Movie.id, Movie.kor_title, Movie.eng_title, Movie.image_link, Movie.pub_year, Movie.director, Movie.rating, Movie.story, Movie.run_time).filter(Movie.id.in_(movies)).order_by(Movie.rating.desc()).limit(10).all()
        total_movies_info = [list(row) for row in movies_info]

        def get_movie_id(i):
            return total_movies_info[i][0]

        # 장르 삽입
        total_movies_info = self.append_genre(len(movies_info), total_movies_info, get_movie_id)
        
        return total_movies_info

    @Result.response(200, 'Success', same_mbti_top10_fields)
    @Result.response(500, 'fail')
    def get(self):
        """
        1. 현재 사용자와 같은 유형에게 인기있는 영화 Top 10 정보, 
        2. 사용자와 같은 유형의 캐릭터가 나오는 영화 중 네이버 평점 top 10 영화 정보,
        3. 사용자와 같은 유형의 캐릭터가 나오는 영화 중 네이버 평점 top 10 영화 줄거리로 만든 워드 클라우드 전달하는 api.
        * 영화 정보 : 한글 제목(str), 영어 제목(str), 이미지 url(str), 개봉일(int), 감독(str), 평점(float), 스토리(str), 런타임(int), 장르(str list)
        """
        
        return {
            'top10_for_same_mbti_users': self.top10_to_same_mbti_user(current_user.mbti),
            'top10_in_naver': self.top10_in_naver_same_mbti_char(current_user.mbti),
            'word_cloud_src': "img/word_clouds/wordcloud_" + str(current_user.mbti)+".jpg"
        }
