# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from models import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from app import db
import json


def store_questions():
    questions = ["으, 오랜만에 좋은 아침이에요! 늘어지게 자고 일어났더니\n삐 - 언제나 다름없이 재난문자가 울리네요 .. 휴\n아무래도 오늘도 집에 있어야 겠어요..", "1. 오늘은 학교 동창 친구들을 만나기로 약속한 날! 하지만 근래에 코로나 감염율이 늘어나고 있으니 주말동안 외출을 삼가해 달라는 재난 문자가 왔어요. \n결국 약속이 취소되고 말았어요.", "2. 아쉬운 마음은 뒤로 하고, 일단 배가 고파서 배달음식을 시켜야겠어요.\n늘 먹던 치킨메뉴를 주문하려고 메뉴에 들어갔더니 처음보는 메뉴가 추가되어 있네요.", "3. 집에만 있다보니 심심해졌어요. 영화를 보고 싶은데 무슨 영화가 좋을까요?", "4. 흥미 진진한 영화 ! 영화를 보면서 무슨 생각을 할까요?", "5. 위기에 빠진 주인공이 눈물을 흘리기 시작했어요… 여러분은 어떤 생각을 할까요?", "6. 정말 좋은 영화였어요! 여러분은 친구에게 이 영화를 어떻게 추천할까요?", "7. 영화에서는 다들 마스크를 쓰지 않던데 … 코로나가 빨리 끝났으면 좋겠어요!", "8. 그나저나, 내일은 백신 접종을 하는 날이에요. 당신의 행동은?", "9. 다음날 친구와 함께 병원에 왔는데, 주위 간호사 분들을 통해 코로나 확진자 수가 급증하고 있다는 소식이 들려오네요. 당신의 생각은?", "10. 대기하던 중, 코로나 백신을 먼저 맞은 친구가 연락이 왔어요. 몸도 으슬으슬하고 팔도 많이 아프다네요 .. 이때 답변은?", "11. 백신을 맞고 집으로 가는 길, 친구가 우리 집쪽에 볼 일이 있다며 같이 가자고 해요.", "12. 집에 가는 동안 친구가 말을 거네요. \n\"코로나만 끝나면, 진짜 진짜 애들 다 모아서 밤새 놀자.\"\n친구가 언급한 친구들 중에는 조금 어색한 친구들이 껴있어요."]

    img_url = ["img/for_test/"+str(i+1)+".png" for i in range(13)]

    for i in range(len(questions)):
        question = Question(questions[i], img_url[i])
        db.session.add(question)
        db.session.commit()


def store_options():
    options = [("a. 아쉽지만 혼자만의 휴일도 나쁘지 않다. 오늘 혼자 볼 영화나 골라야지", "b. 너무 아쉽다ㅠㅠ 모처럼 휴일인데 어떻게 혼자 보내... 심심한 휴일이 될 것 같다."), ("a. 믿고있어! 늘 주문하는 믿음의 메뉴를 시킨다.", "b. 궁금한건 못참지! 새로운 메뉴에 도전한다."), ("a. 전에 보기로 마음먹었던 영화", "b. 지금 끌리는 영화"), ("a. 내가 저 주인공이 되어봤으면 …", "b. 영화 재밌다! 영화보면서 뭘 좀 먹을까?"), ("a. 흑흑 나도 눈물이 나는걸 …", "b. 어떻게 하면 위기에서 탈출할 수 있을지 같이 고민한다."), ("a. 내가 영화를 보면서 느낀 느낌대로 !", "b. 영화의 작품성이 얼마나 훌륭했는지 !"), ("a. 코로나가 끝나길 바라며 내일 할 일을 정리한다.", "b. 코로나가 끝나면 하고싶은 것들을 상상한다."), ("a. 일단 맞고나서 생각한다.", "b. 타이레놀을 구비해두고 주변 친구, 가족들에게 말해두고 택시를 탈지 버스를 탈지 계획을 세운다."), ("a. 확진자 수가 늘어나고있군.. 집에만 있어야겠다!", "b. 알고보면 나도 확진 아니야?? 확진되면 격리 기간동안 뭐하지? OTT 서비스 결제할까? 욕먹는거 아닐까? 주식은 오르려나 내리려나.."), ("a. 하루이틀 있으면 나아져! 타이레놀 꼭 사먹고!", "b. 많이 아파? 걱정된다 …"), ("a. 오, 안 심심하고 좋지 뭐!", "b. 아... 집은 좀 생각 정리하면서 혼자 걷고 싶었는데"), ("a. 좋아! 완전 재밌겠다! 이 기회에 친해지고 좋지 무조건 사람 많은게 최고!", "b. 아...난 친한 사람들끼리만 가고 싶은데, 일단은 알겠다고 하고 진짜 모르는 사람들 오면 못간다고 해야지...")]

    mbti_indicator = [("I", "E"), ("J", "P"), ("J", "P"), ("N", "S"), ("F", "T"), ("F", "T"), ("S", "N"), ("P", "J"), ("S", "N"), ("T", "F"), ("E", "I"), ("E", "I")]

    for i in range(len(options)):
        option_1 = Option(i+2, options[i][0], mbti_indicator[i][0])
        option_2 = Option(i+2, options[i][1], mbti_indicator[i][1])
        db.session.add(option_1)
        db.session.add(option_2)
        db.session.commit()

def store_compatibility():
    mbti_list = ["ENTP", "ISFJ", "ESFJ", "INTP", "ENFJ", "ISTP", "ESTP", "INFJ", "ESFP", "INTJ", "ENTJ", "ISFP", "ESTJ", "INFP", "ENFP", "ISTJ"]

    for i in range(0, len(mbti_list), 2):
        db.session.add(Compatibility(mbti_list[i], mbti_list[i+1]))
        db.session.add(Compatibility(mbti_list[i+1], mbti_list[i]))
        db.session.commit()

def _store_user_for_test():

    users = [["test1", "1234", "ISFP"], ["test2", "1234", "ESTJ"], ["test3", "1234", "ESFP"], ["test4", "1234", "ENTP"], ["test5", "1234", "ISFJ"], ["test6", "1234", "INFP"], ["test7", "1234", "ISTJ"], ["test8", "1234", "INTJ"]]
    for user in users:
        db.session.add(User(user[0], user[1], user[2]))
    db.session.commit()


def _store_answers_for_test():
    answers = "abababababab"
    db.session.add(Answer("test", answers))
    db.session.commit()


def _store_test_data():
    # 영화, 배우, 장르, 캐릭터, 영화-캐릭터 json 파일 이용한 테스트 데이터 적재
    # temp_movies.json
    # temp_actors.json
    # temp_genres.json
    # temp_characters.json
    # temp_movie_characters.json
    # temp_satisfaction.json
    
    # with open('./data/temp_movies.json', 'r', encoding="utf-8") as f:
    #     movies = json.load(f)
    #     for m in movies['test_movies']:
    #         db.session.add(Movie(m['kor_title'], m['eng_title'], m['image_link'], m['pub_year'], m['director'], m['rating'], m['story'], m['run_time']))
    
    # with open('./data/temp_actors.json', 'r', encoding="utf-8") as f:
    #     actors = json.load(f)
    #     for actor in actors['test_actor_in_movie']:
    #         db.session.add(ActorInMovie(actor['actor_name'], actor['movie_id']))

    # with open('./data/temp_genres.json', 'r', encoding="utf-8") as f:
    #     genres = json.load(f)
    #     for genre in genres['test_movie_genre']:
    #         db.session.add(MovieGenre(genre['genre'], genre['movie_id']))
    
    # with open('./data/temp_characters.json', 'r', encoding="utf-8") as f:
    #     characters = json.load(f)
    #     for character in characters['test_character']:
    #         db.session.add(Character(character['mbti'], character['name'], character['image_link']))

    # with open('./data/temp_movie_characters.json', 'r', encoding="utf-8") as f:
    #     characters = json.load(f)
    #     for character in characters['test_movie_character']:
    #         db.session.add(CharacterInMovie(character['character_id'], character['movie_id']))
    
    with open('./data/temp_satisfaction.json', 'r', encoding="utf-8") as f:
        satisfactions = json.load(f)
        for satisfaction in satisfactions['test_satisfaction']:
            db.session.add(Satisfaction(satisfaction['user_id'], satisfaction['movie_id'], satisfaction['user_rating']))
    
    db.session.commit()


def store_init_data():
    store_questions()
    store_options()
    _store_user_for_test()
    _store_answers_for_test()
    _store_test_data()
    store_compatibility()
