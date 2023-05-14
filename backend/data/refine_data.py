import os
import sys
from app import db
from models import Movie, Character
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def delete_null_image_in_DB():
    null_image_url = "https://www.personality-database.com/images/profile_transparent.png"
    db.session.query(Character).filter(Character.image_link == null_image_url).delete()                
    db.session.commit()


def delete_html_entity():
    kor_titles = db.session.query(Movie).filter(Movie.kor_title.like('%&amp;%')).all()
    eng_titles = db.session.query(Movie).filter(Movie.eng_title.like('%&amp;%')).all()
    
    for kor_title in kor_titles:
        title = kor_title.kor_title
        title = title.replace('&amp;', '&')
        kor_title.kor_title = title

    for eng_title in eng_titles:
        title = eng_title.eng_title
        title = title.replace('&amp;', '&')
        eng_title.eng_title = title
    db.session.commit()