# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

def _store_movie_for_test():
    # 한글 제목, 영어 제목, 이미지링크, 개봉연도, 감독, 평점, 스토리, 런타임
    movie_infos = [["해리 포터와 마법사의 돌", "Harry Potter And The Sorcerer's Stone", "https://ssl.pstatic.net/imgmovie/mdi/mit110/0306/30688_P28_142632.jpg", 2001, "크리스 콜럼버스", 9.36, "해리 포터(다니엘 래드클리프 분)는 위압적인 버논 숙부(리챠드 그리피스 분)와 냉담한 이모 페투니아 (피오나 쇼 분), 욕심 많고 버릇없는 사촌 더즐리(해리 멜링 분) 밑에서 갖은 구박을 견디며 계단 밑 벽장에서 생활한다. 이모네 식구들 역시 해리와의 동거가 불편하기는 마찬가지. 이모 페투니아에겐 해리가 이상한(?) 언니 부부에 관한 기억을 떠올리게 만드는 달갑지 않은 존재다. 11살 생일이 며칠 앞으로 다가왔지만 한번도 생일파티를 치르거나 제대로 된 생일선물을 받아 본 적이 없는 해리로서는 특별히 신날 것도 기대 할 것도 없다. 11살 생일을 며칠 앞둔 어느 날 해리에게 초록색 잉크로 쓰여진 한 통의 편지가 배달된다. 그 편지의 내용은 다름 아닌 해리의 11살 생일을 맞이하여 전설적인“호그와트 마법학교”에서 보낸 입학초대장이었다. 그리고 해리의 생일을 축하하러 온 거인 해그리드는 해리가 모르고 있었던 해리의 진정한 정체를 알려주는데. 그것은 바로 해리가 굉장한 능력을 지닌 마법사라는 것! 해리는 해그리드의 지시대로 자신을 구박하던 이모네 집을 주저없이 떠나 호그와트행을 택한다. 런던의 킹스크로스 역에 있는 비밀의 9와 3/4 승장장에서 호그와트 특급열차를 탄 해리는 열차 안에서 같은 호그와트 마법학교 입학생인 헤르미온느 그레인저(엠마 왓슨 분)와 론 위즐리 (루퍼트 그린트 분)를 만나 친구가 된다. 이들과 함께 호그와트에 입학한 해리는, 놀라운 모험의 세계를 경험하며 갖가지 신기한 마법들을 배워 나간다. 또한 빗자루를 타고 공중을 날아다니며 경기하는 스릴 만점의 퀴디치 게임에서 스타로 탄생하게 되며, 용, 머리가 셋 달린 개, 유니콘, 켄타우루스, 히포그리프(말 몸에 독수리 머리와 날개를 가진 괴물)등 신비한 동물들과 마주치며 모험을 즐긴다. 그러던 어느 날 해리는 호그와트 지하실에 `영원한 생을 가져다주는 마법사의 돌'이 비밀리에 보관되어 있다는 것을 알게되고, 해리의 부모님을 죽인 볼드모트가 그 돌을 노린다는 사실도 알게 된다. 볼드모트는 바로 해리를 죽이려다 실패하고 이마에 번개모양의 흉터를 남긴 장본인이다. 해리는 볼드모트로부터 마법의 돌과 호그와트 마법학교를 지키기 위해 필사의 노력을 하는데...", 152], ["해리 포터와 비밀의 방", "Harry Potter And The Chamber Of Secrets", "https://ssl.pstatic.net/imgmovie/mdi/mit110/0339/C3930-06.jpg", 2002, "크리스 콜럼버스", 8.9, "해리 포터에겐 이번 여름방학이 별로 즐겁질 못했다. 마법이라면 질색을 하는 페투니아 이모(피오나 쇼 분)와 버논 이모부(리차드 그리피스 분)의 구박도 그렇지만, 무엇보다 속상한 건 단짝이었던 론 위즐리(루퍼트 그린트 분)와 헤르미온느 그레인저(엠마 왓슨 분)가 그 사이 자신을 까맣게 잊었는지 자신의 편지에 답장 한 통 없다는 것. 그러던 어느날 꼬마 집요정 도비가 해리의 침실에 나타나 뜻밖의 얘기를 한다. 호그와트 마법학교로 돌아가면 무서운 일을 당할 거라는 것. 도비는 해리를 학교에 못 가게 하려고 자신이 여태까지 론과 헤르미온느의 답장을 가로채 왔음을 고백한다. 그러나 도비와 더즐리 가족의 방해에도 불구, 해리는 론과 그의 형제들이 타고 온 하늘을 나는 자동차를 타고 이모집을 탈출, 따뜻한 가족애가 넘치는 론 위즐리의 집으로 간다. 개학을 앞두고 학교에 가는 날, 론과 해리는 뭔가의 방해로 9와 3/4 승강장에 못 들어가는 바람에 개학식에 지각할 위기에 처한다. 결국 하늘을 나는 자동차 포드 앵글리아를 타고 천신만고끝에 학교에 도착했으나 공교롭게도 차가 학교 선생님들이 소중히 여기는 '커다란 버드나무' 위에 불시착하는 바람에 화가 난 스네이프 교수로부터 퇴학 경고를 받게 된다. 한편 1학년 때 해리가 보여준 영웅적인 활약상은 학교 전체에 소문이 나고, 그 덕에 해리는 원치 않는 관심의 초점이 된다. 론의 여동생 지니, 사진작가 지망생 콜린 크리비 등의 신입생과 어둠의 마법 방어술을 가르치는 신임 교수 질데로이 록허트가 새롭게 해리포터의 팬이 된다. 남의 시선 끌기를 좋아하는 잘난척하는 성격 탓에 주변에서 따돌림 당하는 록허트 교수는 해리와 친해지고 싶어 안달하지만, 그 역시 학교에서 일어나는 무서운 사건에 대해 뾰족한 설명을 못해준다. 모든 이목은 해리에게 집중되고, 결국 급우들은 해리를 의심하기에 이른다. 물론 론과 헤르미온느, 그리고 수수께끼의 일기장에 마음을 뺏긴 론의 동생 지니만은 끝까지 해리를 믿는다. 자신을 믿는 친구들을 실망시킬 수는 없는 법. 해리는 -도움을 준다며 되려 걸리적 대는 록허트 교수가 다소 방해가 되긴 하지만- 어둠의 세력과 맞서 싸울 결심을 하는데..", 162], ["해리 포터와 아즈카반의 죄수", "Harry Potter And The Prisoner Of Azkaban", "https://ssl.pstatic.net/imgmovie/mdi/mit110/0355/35546_P88_142722.jpg", 2004, "알폰소 쿠아론", 8.74, "13세가 된 ‘해리 포터(다니엘 래드클래프)’는 아버지의 험담을 하는 이모부의 누이 마지 아줌마를 거대한 괴물 풍선으로 만들어 버리고 만다. 일반 세상에서 마법 사용이 금지되어 있는 법을 어긴 해리는 마법부의 징계가 두려워 도망을 치다가 만나게 된 마법부 장관은 ‘시리우스 블랙’(게리 올드만)이 아즈카반의 감옥을 탈출해 해리를 찾고 있다는 소식을 전한다. 시리우스 블랙은 어둠의 마왕인 볼드모트 경을 해리의 부모님에게 이끌어 죽음으로 몰고 간 당사자. 설상가상으로 영혼을 빨아들이는 아즈카반의 무시무시한 간수 ‘디멘터’가 호그와트에 머물며 해리를 위협한다. 그러나 새로 부임한 어둠의 마법 방어술 교수 ‘루핀’(데이빗 튤리스)이 가르쳐준 '패트로누스' 마법으로 해리는 디멘터에게 대적할 힘을 얻는다. 시리우스 블랙과의 불가피한 대결은 다가오고, 해리는 자신과 시리우스 블랙 사이에 얽혀있는 엄청난 비밀을 직면하게 되는데… 해리를 위협하는 어둠의 세력, 그에 맞서는 해리의 활약! 놀라움으로 가득한 마법의 세계가 다시 펼쳐진다!", 141], ["해리 포터와 불의 잔", "Harry Potter And The Goblet Of Fire", "https://ssl.pstatic.net/imgmovie/mdi/mit110/0378/37883_P158_182652.jpg", 2005, "마이크 뉴웰", 8.03, "해리 포터 일생일대 최대 난관! 요즘 들어 매일 꾸는 악몽 때문에 이마의 상처에 더욱 통증을 느끼는 해리(다니엘 래드클래프)는 친구 론(루퍼트 그린트)과 헤르미온느(엠마 왓슨)와 함께 퀴디치 월드컵에 참가해 악몽에서 벗어날 수 있게 돼 마냥 기쁘다. 그러나 퀴디치 캠프장 근방 하늘에 불길한 기운, 바로 마왕 볼드모트의 상징인 '어둠의 표식'이 나타난다. 볼드모트가 13년 전에 자취를 감춘 뒤 감히 모습을 드러내지 못했던 그의 추종자 데스 이터들이 그 표식을 불러낸 것이다. 두려움으로 가득 찬 해리는 안전한 호그와트 마법학교로 돌아가고 싶어한다. 덤블도어 교장(마이클 갬본 경)이라면 자신을 지켜줄 수 있을 것이기에… 최강의 챔피언을 찾아라! 트리위저드 마법경연대회! 그러나 올해는 예년과 상황이 좀 다르다. 덤블도어 교장은 유럽의 세 개 명문 마법학교의 결속을 다지기 위해 그간 중단됐던 호그와트에서 '트리위저드 대회'를 개최한다고 발표한다. 트리위저드 대회는 마법의 최고 명문 3개 학교에서 선발된 챔피언 한 명씩 출전해 트리위저드 컵을 놓고 목숨을 건 경합을 벌이는 마법사들 세계에서 가장 흥미진진하고 위험한 마법경연대회. 마법의 '불의 잔'이 각 학교 출전자를 선발하는 의식이 열리고 현란한 불꽃의 축제 속에 불의 잔은 마침내 세 학생의 이름을 호명한다. 강인한 불가리아 덤스트랭 학교의 퀴디치 경기 슈퍼스타인 빅터 크룸(스타니슬라브 이아네브스키)과 우아한 보바통 마법아카데미의 플뢰르 델라쿠르(클레멘스 포에시), 그리고 호그와트의 최고 인기남 케드릭 디고리(로버트 패틴슨). 그러나 세 명의 이름이 다 호명된 후, 뜻밖에도 불의 잔은 또 한 명의 이름을 내뱉는다. 바로 '해리포터'! 피할 수 없는 숙명의 대결! 그러나 해리는 시합 출전자의 나이 제한인 17세보다 세 살이나 어린 14세. 게다가 불의 잔 속에 자신의 이름을 넣은 적이 없다며 거부하지만 불의 잔의 단호한 뜻에 따라 어쩔 수 없이 출전하게 된다. 이 일로 해리에겐 의혹과 시기의 시선이 집중되고 추문 폭로기사 전문기자 리타 스키터는 해리에 대한 모함성 기사를 써서 이를 더욱 부채질한다. 친구 론마저도 해리가 유명해지고 싶어서 불의 잔을 조작했다고 믿기 시작한다. 해리를 위험에 처한 누군가의 음모라고 생각한 덤블도어 교장은 신임 '어둠의 마법 방어술' 교수 '매드아이 무디'(브랜든 글리슨)에게 해리를 잘 지키라고 지시한다. 해리는 트리위저드 대회의 불 뿜는 용 피하기, 거대한 호수 깊이 잠수하기, 살아있는 미로를 빠져 나오기라는 세가지 과제에 대비한 마법 훈련에 돌입한다. 그러나 그보다 해리에게 더 힘든 숙제는 크리스마스 무도회에 함께 참석할 파트너를 구하는 문제다. 해리에겐 용이나 인어, 그라인딜로우와 싸우는 편이 사랑스러운 여학생 초 챙(케이티 렁)에게 무도회의 파트너가 돼달라고 부탁하는 것보다 훨씬 쉬운 일. 한편 론은 헤르미온느에 대한 자신의 감정이 예전과 다르다는 걸 미처 깨닫지 못하고… 불의 잔을 향한 최강의 스펙터클이 펼쳐진다! 그러던 중 호그와트 교정에서 누군가 살해되면서 상황은 급변한다. 볼드모트의 악몽으로 두려움에 휩싸인 해리는 덤블도어를 찾아가지만 그 역시도 뚜렷한 해답을 제시하지 못한다. 경기가 진행되고 해리와 다른 출전자들이 마지막 과제를 풀기 위해 안간힘을 쓰고 있을 때 무언가가 계속 이들을 주시한다. 승리가 목전에 다가온 그 순간, 이제까지의 모든 진실이 밝혀지고 해리포터에게는 진정한 악과의 피할 수 없는 대결이 기다리고 있는데….", 156], ["해리 포터와 불사조 기사단", "Harry Potter And The Order Of The Phoenix", "https://ssl.pstatic.net/imgmovie/mdi/mit110/0570/E7095-00.jpg", 2007, "데이빗 예이츠", 7.03, "길고도 지루한 여름 날 호그와트 마법학교 다섯 번째 해를 기다리고 있는 해리포터(다니엘 래드클리프). 이모부 더즐리 식구들과 참고 사는 것도 지겨운데다 친구 론(루퍼트 그린트)과 헤르미온느(엠마 왓슨)에게서는 편지 한 통 오지 않는다. 그러던 중 예상치 못했던 편지 한 장이 도착한다. 그것은 해리가 학교 밖인 리틀 위닝에서 얄미운 사촌 두들리, 즉 머글 앞에서 디멘터들의 공격을 막는 마법을 사용했기 때문에 호그와트 마법학교에서 퇴학 당하게 되었다는 소식이었다. 앞이 캄캄한 해리. 갑자기 어둠의 마법사 오러들이 나타나 해리를 불사조 기사단의 비밀 장소로 데리고 간다. 시리우스(게리 올드만)를 위시한 불사조 기사단을 만난 해리는 과거, 부모님들의 활약상을 알게 되어 힘을 얻고, 자신을 퇴학시키기 위해 마법부 장관 코넬리우스 퍼지(로버트 하디)가 법정에 세우지만 덤블도어 교장(마이클 갬볼 경)의 중재 덕분에 무죄 판결까지 받는다. 하지만 예언자 일보는 볼드모트(랄프 파인즈)가 돌아왔다는 해리의 말이 새빨간 거짓말이라며 비난하고 학생들 역시 해리를 의심하며 따돌린다. 게다가 자신이 가장 힘들어 할 때 도움을 주던 덤블도어 교장까지도 이유 없이 해리를 멀리하고… 한편, 덤블도어도 못마땅한데 해리의 퇴학마저 무산이 되자 마법부 장관은 ‘어둠의 마법방어술’ 과목에 돌로레스 엄브릿지(이멜다 스털톤)를 교수로 임명한다. 하지만 엄브릿지의 마법방어술 수업은 학생들이 어둠의 힘으로부터 스스로를 지켜내기는커녕 오히려 곤경에 빠지게 한다. 이에 헤르미온느와 론은 해리의 능력을 믿고 자칭 ‘덤블도어의 군대’라고 명명한 비밀단체를 조직한다. 해리는 어둠의 마법에 맞서 스스로를 지켜낼 수 있는 방법을 학생들에게 가르쳐주며 앞으로 닥칠 격전에 대비시킨다. 그러나 밤마다 불길한 사건을 예견하는 악몽에 시달리는 해리. 이제 볼드모트와의 대결이 머지 않았음을 느끼게 된다. 시리우스가 공격 당하는 악몽을 꾼 해리는 덤블도어 군대와 함께 마법부 미스터리 부서 예언의 방으로 향한다. 그리고 이어 나타난 죽음을 먹는 자들…. 빛의 마법과 어둠의 마법간의 불꽃 튀는 대결 해리포터와 불사조 기사단, 호그와트의 운명이 그들에게 달렸다!", 137], ["해리 포터와 혼혈 왕자", "Harry Potter And The Half-Blood Prince", "https://ssl.pstatic.net/imgmovie/mdi/mit110/0679/67900_P01_130458.jpg", 2009, "데이빗 예이츠", 6.97, "어둠의 세력이 더욱 강력해져 머글 세계와 호그와트까지 위협해온다. 위험한 기운을 감지한 덤블도어 교수는 다가올 전투에 대비하기 위해 해리 포터와 함께 대장정의 길을 나선다. 볼드모트를 물리칠 수 있는 유일한 단서이자 그의 영혼을 나누어 놓은 7개의 호크룩스를 파괴하는 미션을 수행해야만 하는 것! 또한 덤블도어 교수는 호크룩스를 찾는 기억여행에 결정적 도움을 줄 슬러그혼 교수를 호그와트로 초청한다. 한편 학교에서는 계속된 수업과 함께 로맨스의 기운도 무르익는다. 해리는 자신도 모르게 지니에게 점점 끌리게 되고, 새로운 여자 친구가 생긴 론에게 헤르미온느는 묘한 질투심을 느끼는데... 남겨진 결전을 위한 최후의 미션, 볼드모트와 해리 포터에 얽힌 치명적인 비밀, 선택된 자만이 통과할 수 있는 대단원을 향한 본격적인 대결이 시작된다!", 153], ["해리 포터와 죽음의 성물 - 1부", "Harry Potter And The Deathly Hallows: Part 1", "https://ssl.pstatic.net/imgmovie/mdi/mit110/0679/67901_P52_160214.jpg", 2010, "데이빗 예이츠", 8.21, "덤블도어 교장의 죽음 이후, 마법부는 죽음을 먹는 자들에게 점령당하고 호그와트는 위기에 빠진다. 이에 해리와 론, 헤르미온느는 볼드모트를 물리칠 수 있는 유일한 단서이자 그의 영혼이 담긴 ‘성물’ 호크룩스를 찾기 위한 위험한 여정에 나선다. 그러나 영혼이 연결되어 있는 볼드모트와 해리. 볼드모트를 파괴하면 해리의 목숨 또한 위태로워질지 모른다! 죽느냐 죽이느냐, 이제 그 마지막 대결은 극한을 향해 치닫는데…", 146], ["해리 포터와 죽음의 성물 - 2부", "Harry Potter And The Deathly Hallows: Part 2", "https://ssl.pstatic.net/imgmovie/mdi/mit110/0475/47528_P50_144916.jpg", 2011, "데이빗 예이츠", 9.32, "모든 것을 끝낼 최후의 전투! 판타지의 아름다운 역사가 드디어 마침표를 찍는다! 덤블도어 교장이 남긴 ‘죽음의 성물’의 단서를 쫓던 해리 포터는 볼드모트가 그토록 찾아 다닌 절대적인 힘을 가진 지팡이의 비밀을 통해 드디어 마지막 퍼즐을 완성한다. 볼드모트의 영혼이 담긴 다섯 번째 ‘호크룩스’를 찾기 위해 마법학교 호그와트로 돌아온 해리와 친구들은 그들을 잡으려는 보안마법에 걸려 위기를 맞지만 덤블도어의 동생인 에버포스의 도움으로 벗어난다. 그리고 그에게서 덤블도어와 어둠의 마법사 그린델왈드에 관한 놀라운 과거에 대해 알게 된다. 한편, 볼드모트는 해리에 의해 호크룩스들이 파괴되었음을 느끼고 호그와트로 향한다. 해리를 주축으로 한 불사조 기사단과 죽음을 먹는 자들 간의 마법전투가 벌어지고 여기에 거대거미 아크로맨투라와 거인족 등 마법 생물들이 볼드모트 편으로 가세하면서 호그와트는 거대한 전쟁터로 변한다. 전쟁의 틈에서 해리는 덤블도어를 죽인 스네이프의 엄청난 비밀과 볼드모트를 죽일 마지막 호크룩스에 대한 단서를 알게 되는데...", 131]]

    movies = []
    for i in range(len(movie_infos)):
        movie = {}
        movie['kor_title'] = movie_infos[i][0]
        movie['eng_title'] = movie_infos[i][1]
        movie['image_link'] = movie_infos[i][2]
        movie['pub_year'] = movie_infos[i][3]
        movie['director'] = movie_infos[i][4]
        movie['rating'] = movie_infos[i][5]
        movie['story'] = movie_infos[i][6]
        movie['run_time'] = movie_infos[i][7]
        movies.append(movie)
        
    movies_data = OrderedDict()
    movies_data['test_movies'] = movies
    with open('temp_movies.json', 'w', encoding="utf-8") as make_file:
        json.dump(movies_data, make_file, ensure_ascii=False, indent="\t")


def _store_actor_in_movie_for_test():
    # actor name, movie id
    actor_infos = [["다니엘 래드클리프", 1], ["다니엘 래드클리프", 2], ["다니엘 래드클리프", 3], ["다니엘 래드클리프", 4], ["다니엘 래드클리프", 5], ["다니엘 래드클리프", 6], ["다니엘 래드클리프", 7], ["다니엘 래드클리프", 8], ["엠마 왓슨", 1], ["엠마 왓슨", 2], ["엠마 왓슨", 3], ["엠마 왓슨", 4], ["엠마 왓슨", 5], ["엠마 왓슨", 6], ["엠마 왓슨", 7], ["엠마 왓슨", 8], ["루퍼트 그린트", 1], ["루퍼트 그린트", 2], ["루퍼트 그린트", 3], ["루퍼트 그린트", 4], ["루퍼트 그린트", 5], ["루퍼트 그린트", 6], ["루퍼트 그린트", 7], ["루퍼트 그린트", 8], ["헬레나 본햄 카터", 5], ["헬레나 본햄 카터", 6], ["헬레나 본햄 카터", 7], ["헬레나 본햄 카터", 8], ["케네스 브래너", 2], ["해리 멜링", 1],  ["해리 멜링", 2],  ["해리 멜링", 3],  ["해리 멜링", 5],  ["해리 멜링", 7], ["로버트 패틴슨", 4], ["톰 펠튼", 1], ["톰 펠튼", 2], ["톰 펠튼", 3], ["톰 펠튼", 4], ["톰 펠튼", 5], ["톰 펠튼", 6], ["톰 펠튼", 7], ["톰 펠튼", 8], ["이멜다 스턴톤", 5], ["이멜다 스턴톤", 7], ["제임스 펠프스", 1], ["제임스 펠프스", 2], ["제임스 펠프스", 3], ["제임스 펠프스", 4], ["제임스 펠프스", 5], ["제임스 펠프스", 6], ["제임스 펠프스", 7], ["제임스 펠프스", 8], ["올리버 펠프스", 1], ["올리버 펠프스", 2], ["올리버 펠프스", 3], ["올리버 펠프스", 4], ["올리버 펠프스", 5], ["올리버 펠프스", 6], ["올리버 펠프스", 7], ["올리버 펠프스", 8], ["셜리 헨더슨", 2], ["셜리 헨더슨", 4], ["보니 라이트", 1], ["보니 라이트", 2], ["보니 라이트", 3], ["보니 라이트", 4], ["보니 라이트", 5], ["보니 라이트", 6], ["보니 라이트", 7], ["보니 라이트", 8], ["매튜 루이스", 1], ["매튜 루이스", 2], ["매튜 루이스", 3], ["매튜 루이스", 4], ["매튜 루이스", 5], ["매튜 루이스", 6], ["매튜 루이스", 7], ["매튜 루이스", 8], ["케이티 렁", 4], ["케이티 렁", 5], ["케이티 렁", 6], ["케이티 렁", 7], ["스타니슬라브 이아네브스키", 4], ["매기 스미스", 1], ["매기 스미스", 2], ["매기 스미스", 3], ["매기 스미스", 4], ["매기 스미스", 5], ["매기 스미스", 6], ["매기 스미스", 8], ["이반나 린치", 5], ["이반나 린치", 6], ["이반나 린치", 7], ["이반나 린치", 8], ["토비 존스", 2], ["토비 존스", 7], ["토비 존스", 8], ["리처드 해리스", 1], ["리처드 해리스", 2], ["마이클 갬본", 3], ["마이클 갬본", 4], ["마이클 갬본", 5], ["마이클 갬본", 6], ["마이클 갬본", 7], ["마이클 갬본", 8], ["알란 릭맨", 1], ["알란 릭맨", 2], ["알란 릭맨", 3], ["알란 릭맨", 4], ["알란 릭맨", 5], ["알란 릭맨", 6], ["알란 릭맨", 7], ["알란 릭맨", 8]]

    actors = []
    for i in range(len(actor_infos)):
        actor = {}
        actor['actor_name'] = actor_infos[i][0]
        actor['movie_id'] = actor_infos[i][1]
        actors.append(actor)

    actors_data = OrderedDict()
    actors_data['test_actor_in_movie'] = actors
    with open('temp_actors.json', 'w', encoding="utf-8") as make_file:
        json.dump(actors_data, make_file, ensure_ascii=False, indent="\t")


def _store_movie_genre():
    # genre, movie id
    genre_infos = [["판타지", 1], ["판타지", 2], ["판타지", 3], ["판타지", 4], ["판타지", 5], ["판타지", 6], ["판타지", 7], ["판타지", 8], ["장르 2", 1], ["장르 3", 1], ["장르 555", 5]]
    
    genres = []
    for i in range(len(genre_infos)):
        genre = {}
        genre['genre'] = genre_infos[i][0]
        genre['movie_id'] = genre_infos[i][1]
        genres.append(genre)
    
    genres_data = OrderedDict()
    genres_data['test_movie_genre'] = genres
    with open('temp_genres.json', 'w', encoding="utf-8") as make_file:
        json.dump(genres_data, make_file, ensure_ascii=False, indent="\t")


def _store_character():
    # mbti, name, image_link
    char_infos = [["ISFP", "Harry Potter", "https://www.personality-database.com/profile_images/708.png?=undefined"], ["ESTJ", "Hermione Granger", "https://www.personality-database.com/profile_images/710.png?=undefined"], ["ESFP", "Ron Weasley", "https://www.personality-database.com/profile_images/709.png?=undefined"], ["ESFP", "Bellatrix Lestrange", "https://www.personality-database.com/profile_images/4045.png?=undefined"], ["ESFP", "Gilderoy Lockhart", "https://www.personality-database.com/profile_images/3546.png?=undefined"], ["ESFP", "Dudley Dursley", "https://www.personality-database.com/profile_images/13735.png?=undefined"], ["ESFJ", "Cedric Diggory", "https://www.personality-database.com/profile_images/3822.png?=undefined"], ["ESTJ", "Draco Malfoy", "https://www.personality-database.com/profile_images/713.png?=undefined"], ["ESTJ", "Dolores Umbridge", "https://www.personality-database.com/profile_images/2946.png?=undefined"], ["ENTP", "Fred Weasley", "https://www.personality-database.com/profile_images/718.png?=undefined"], ["ENTP", "George Weasley", "https://www.personality-database.com/profile_images/719.png?=undefined"], ["ISFP", "Moaning Myrtle", "https://www.personality-database.com/profile_images/45174.png?=undefined"], ["ISFJ", "Ginny Weasley", "https://www.personality-database.com/profile_images/2683.png?=undefined"], ["ISFJ", "Neville Longbottom", "https://www.personality-database.com/profile_images/714.png?=undefined"], ["ISFJ", "Cho Chang", "https://www.personality-database.com/profile_images/54494.png?=undefined"], ["ISTP", "Viktor Krum", "https://www.personality-database.com/profile_images/22134.png?=undefined"], ["ISTJ", "Minerva McGonagall", "https://www.personality-database.com/profile_images/2936.png?=undefined"], ["INFP", "Luna Lovegood", "https://www.personality-database.com/profile_images/717.png?=undefined"], ["INFP", "Dobby", "https://www.personality-database.com/profile_images/715.png?=undefined"], ["INFJ", "Albus Dumbledore", "https://www.personality-database.com/profile_images/712.png?=undefined"], ["INTJ", "Severus Snape", "https://www.personality-database.com/profile_images/716.png?=undefined"]]

    print(len(char_infos))

    chars = []
    for i in range(len(char_infos)):
        character = {}
        character['mbti'] = char_infos[i][0]
        character['name'] = char_infos[i][1]
        character['image_link'] = char_infos[i][2]
        chars.append(character)
    
    chars_data = OrderedDict()
    chars_data['test_character'] = chars
    with open('temp_characters.json', 'w', encoding="utf-8") as make_file:
        json.dump(chars_data, make_file, ensure_ascii=False, indent="\t")


def _store_character_in_movie():
    # character_id, movie_id
    char_infos = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 8], [5, 2], [6, 1],  [6, 2],  [6, 3],  [6, 5],  [6, 7], [7, 4], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [9, 5], [9, 7], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [12, 2], [12, 4], [13, 1], [13, 2], [13, 3], [13, 4], [13, 5], [13, 6], [13, 7], [13, 8], [14, 1], [14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 7], [14, 8], [15, 4], [15, 5], [15, 6], [15, 7], [16, 4], [17, 1], [17, 2], [17, 3], [17, 4], [17, 5], [17, 6], [17, 8], [18, 5], [18, 6], [18, 7], [18, 8], [19, 2], [19, 7], [19, 8], [20, 1], [20, 2], [20, 3], [20, 4], [20, 5], [20, 6], [20, 7], [20, 8], [21, 1], [21, 2], [21, 3], [21, 4], [21, 5], [21, 6], [21, 7], [21, 8]]
    chars = []
    for i in range(len(char_infos)):
        character = {}
        character['character_id'] = char_infos[i][0]
        character['movie_id'] = char_infos[i][1]
        chars.append(character)
    
    chars_data = OrderedDict()
    chars_data['test_movie_character'] = chars
    with open('temp_movie_characters.json', 'w', encoding="utf-8") as make_file:
        json.dump(chars_data, make_file, ensure_ascii=False, indent="\t")


def _store_satisfaction():
    # user_id, movie_id, user_rating
    satis_infos = [["test1", 1, 10], ["test1", 2, 9.8], ["test1", 3, 5.7], ["test1", 4, 8.9], ["test1", 5, 7.6], ["test1", 6, 8.5], ["test1", 7, 10], ["test1", 8, 8.6], ["test2", 1, 2.7], ["test2", 2, 9.2], ["test2", 3, 9.7], ["test2", 4, 5.7], ["test2", 5, 7.7], ["test2", 6, 7.5], ["test2", 7, 9], ["test2", 8, 5.8] , ["test3", 1, 6.1], ["test3", 2, 5.8], ["test3", 3, 5.7], ["test4", 4, 3.9], ["test5", 5, 4.6], ["test6", 6, 7.5], ["test7", 7, 1.5], ["test8", 8, 5.6]]
    satiss = []
    for i in range(len(satis_infos)):
        satis = {}
        satis['user_id'] = satis_infos[i][0]
        satis['movie_id'] = satis_infos[i][1]
        satis['user_rating'] = satis_infos[i][2]
        satiss.append(satis)
    
    satis_data = OrderedDict()
    satis_data['test_satisfaction'] = satiss
    with open('temp_satisfaction.json', 'w', encoding="utf-8") as make_file:
        json.dump(satis_data, make_file, ensure_ascii=False, indent="\t")


# _store_movie_for_test()
# _store_actor_in_movie_for_test()
# _store_movie_genre()
# _store_character()
# _store_character_in_movie()
# _store_satisfaction()