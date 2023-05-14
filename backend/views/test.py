from flask_login.utils import login_required
from flask_restx import Resource, Namespace, fields
from models import *

Test = Namespace(
    name='Test',
    description="심리 테스트 진행 페이지에서 사용하는 API",    
)

question_fields = Test.model('Question', {
    'question': fields.String(description="심리 테스트 문항", example="1. 심심한 당신, 어떤 영화를 볼까요?"),
    'img_url': fields.String(description="이미지 url", example="img/for_test/0.png"),
    'options': fields.List(fields.String)
})

min_page = 1
max_page = 13

@Test.route('/<int:page>')
@Test.doc(params={'page': '어떤 페이지에 해당하는 심리 테스트 문항을 볼 것인지 나타내는 페이지 넘버'})
class TestPage(Resource):
    @login_required
    @Test.response(200, 'Success', question_fields)
    @Test.response(500, 'fail')
    def get(self, page):
        """
        page 에 해당하는 문제 데이터 전달,
        1 페이지는 question에만 데이터 있고(스토리 설명) options는 null입니다.
        """
        
        if page > max_page or page < min_page:
            return {'get': 'There is no '+str(page)+" question & options"}, 500

        question = db.session.query(Question).filter(Question.id == page).first()
        options = db.session.query(Option).filter(Option.question_id == page).all()
        
        options = [str(getattr(o, Option.content.name)) for o in options]
        
        return {
            'question': question.content,
            'img_url': question.img_url,
            'options': options
        }