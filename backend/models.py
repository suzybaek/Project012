from app import db
from datetime import datetime
from pytz import timezone

# 사용자 테이블
class User(db.Model):
    id = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    pw = db.Column(db.String(60), nullable=False)
    mbti = db.Column(db.String(10))

    answer = db.relationship('Answer', backref=db.backref('user'))
    satisfaction = db.relationship('Satisfaction', backref=db.backref('user'))

    is_authenticated = True
    is_active = True

    def get_id(self):
        return self.id

    def __init__(self, id, pw, mbti):
        self.id = id
        self.pw = pw
        self.mbti = mbti


# 심리 테스트 문항 테이블
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False , autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(300))

    option = db.relationship('Option', backref=db.backref('question'))

    def __init__(self, content, img_url):
        self.content = content
        self.img_url = img_url


# 심리 테스트 문항에 대한 옵션 테이블
class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False , autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    content = db.Column(db.Text, nullable=False)
    mbti_indicator = db.Column(db.String(5), nullable=False) # mbti 유형 지표 예) I, E, N, S, T, F, J, P
    
    def __init__(self, question_id, content, mbti_indicator):
        self.content = content
        self.question_id = question_id
        self.mbti_indicator = mbti_indicator


# 심리 테스트 문항에 대한 사용자 답변 테이블
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False , autoincrement=True)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'))
    answers = db.Column(db.String(20), nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.now(timezone('Asia/Seoul')))

    def __init__(self, user_id, answers):
        self.user_id = user_id
        self.answers = answers


# 영화 테이블
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    kor_title = db.Column(db.String(50), nullable=False)
    eng_title = db.Column(db.String(70), nullable=False)
    image_link = db.Column(db.Text)
    pub_year = db.Column(db.Integer)
    director = db.Column(db.String(30))
    rating = db.Column(db.Float)
    story = db.Column(db.Text)
    run_time = db.Column(db.Integer)

    actor_in_movie = db.relationship('ActorInMovie', backref=db.backref('movie'))
    character_in_movie = db.relationship('CharacterInMovie', backref=db.backref('movie'))
    movie_genre = db.relationship('MovieGenre', backref=db.backref('movie'))
    satisfaction = db.relationship('Satisfaction', backref=db.backref('movie'))

    def __init__(self, id, kor_title, eng_title, image_link, pub_year, director, rating, story, run_time):
        self.id = id
        self.kor_title = kor_title
        self.eng_title = eng_title
        self. image_link = image_link
        self. pub_year = pub_year
        self.director = director
        self.rating = rating
        self. story = story
        self.run_time = run_time


# 영화 장르 테이블
class MovieGenre(db.Model):
    genre = db.Column(db.String(20), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', ondelete='CASCADE'), primary_key=True)

    def __init__(self, genre, movie_id):
        self.genre = genre
        self.movie_id = movie_id


# 어떤 영화에 어떤 배우가 나왔는지에 대한 테이블
class ActorInMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False , autoincrement=True)
    actor_name = db.Column(db.String(20), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', ondelete='CASCADE'))

    def __init__(self, actor_name, movie_id):
        self.actor_name = actor_name
        self.movie_id = movie_id


# 영화 캐릭터 테이블
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False , autoincrement=True)
    mbti = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    image_link = db.Column(db.Text)
    
    def __init__(self, mbti, name, image_link=""):
        self.mbti = mbti
        self.name = name
        self.image_link = image_link


# 어떤 영화 캐릭터가 어떤 영화에 나왔는지에 대한 테이블
class CharacterInMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False , autoincrement=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id', ondelete='CASCADE'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, character_id, movie_id):
        self.character_id = character_id
        self.movie_id = movie_id 


# 사용자별 특정 영화에 대한 만족도 테이블
class Satisfaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False , autoincrement=True)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id', ondelete='CASCADE'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', ondelete='CASCADE'))
    user_rating = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, movie_id, user_rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.user_rating = user_rating


# mbti 별 천생연분인 mbti 나타내는 테이블
class Compatibility(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False , autoincrement=True)
    user_mbti = db.Column(db.String(10), nullable=False)
    compatible_mbti = db.Column(db.String(10), nullable=False)

    def __init__(self, user_mbti, compatible_mbti):
        self.user_mbti = user_mbti
        self.compatible_mbti = compatible_mbti