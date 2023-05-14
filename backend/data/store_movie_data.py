# -*- coding: utf-8 -*-
import os
import sys
from app import db
from models import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import json

def store_movie_json():
    with open('./data/real/naver_movie_story.json', 'r', encoding="utf-8") as f:
        movies = json.load(f)
        
        movie_id = 1
        for movie in movies['data']:
            rtime = movie['rtime'].strip()
            try:
                rtime = int(rtime[:-1])
            except:
                continue
            kor_title = movie['title']
            eng_title = movie['subtitle']
            image_link = movie['image']
            pub_year = movie['pubDate']
            director = movie['director']
            rating = movie['rating']
            story = movie['story']

            if kor_title and eng_title and image_link and pub_year and director and rating and story:
                m = db.session.query(Movie).filter(Movie.kor_title == kor_title, Movie.eng_title == eng_title, Movie.director == director).first()

                if m:
                    continue
                else:
                    db.session.add(Movie(movie_id, movie['title'], movie['subtitle'], movie['image'], movie['pubDate'], movie['director'], movie['rating'], movie['story'], rtime))

            genres = movie['genre'].split()
            for genre in genres:
                db.session.add(MovieGenre(genre, movie_id))

            actors = movie['actors'][1:-1].split(',')
            for actor in actors:
                db.session.add(ActorInMovie(actor.strip()[1:-1], movie_id))
            db.session.commit()

            char_n_mbti = movie['mbti'].split(',')
            char_n_mbti.pop()
            for cNm in char_n_mbti:
                character_name = cNm[:-6]
                character_mbti = cNm[-5:-1]
                if character_mbti != "XXXX":
                    # db에 해당 캐릭터가 있나? 검사 후 없으면 저장. 있으면 지금 영화 출연 정보도 있나? 검사후 없으면 저장.
                    id = db.session.query(Character.id).filter(Character.name == character_name, Character.mbti == character_mbti).first()
                    if id is None:
                        db.session.add(Character(character_mbti, character_name))
                        db.session.commit()
                        id = db.session.query(Character.id).filter(Character.name == character_name, Character.mbti == character_mbti).first()
                    
                    char_in_movie = db.session.query(CharacterInMovie).filter(CharacterInMovie.character_id == id.id, CharacterInMovie.movie_id == movie_id).first()
                    if char_in_movie is None:
                        db.session.add(CharacterInMovie(id.id, movie_id))
                        db.session.commit()
            
            movie_id += 1
            db.session.commit()
    db.session.commit()


def store_chracter_image():

    with open('./data/real/mbti.json', 'r', encoding="utf-8") as f:
        characters = json.load(f)

        for character in characters:
            c = db.session.query(Character).filter(Character.name == character['role'], Character.mbti == character['mbti']).first()
            img_url = character['img_url'].strip()
            if c and img_url:
                c.image_link = img_url
            elif c and img_url is None:
                c.image_link = "https://www.personality-database.com/images/profile_transparent.png"
    
    db.session.commit()


def set_to_default_char_image():
    null_images = db.session.query(Character).filter((Character.image_link == None) | (Character.image_link == "")).all()
    for i in null_images:
        i.image_link = "https://www.personality-database.com/images/profile_transparent.png"
    db.session.commit()
