
init python:
    class character:
        def __init__(self, name, h_point):
            self.name=name
            self.h_point=h_point

    class ejooo:
        def __init__(self, name, h_point, y_point):
            self.name=name
            self.h_point=h_point
            self.y_point=y_point

        def y_plus(self):
            self.y_point+=1


    class play:
        def __init__(self, m_point, b_point):
            self.m_point=m_point
            self.b_point=b_point

        #호감도 올리는 함수
        def plus(self, character):
            character.h_point+=self.m_point

        #호감도 낮추는 함수
        def minus(self,character):
            character.h_point-=self.b_point

        #매력포인트 올리는 함수
        def m_plus(self):
            self.m_point+=5
            self.b_point-=5
            if self.b_point < 0:
                self.b_point=0

        #비호감 포인트 올리는 함수
        def m_minus(self):
            self.m_point-=5
            self.b_point+=5
            if self.m_point < 0:
                self.m_point=0

#####호감도 표시바########
init:
    screen lovePoint:
        hbox:
            xalign 0.5
            yalign 0.4
            text "현재 호감도"
        frame:
            xalign 0.5
            yalign 0.6
            vbox:
                hbox:
                    text "혜원"
                    bar:
                        value hone.h_point
                        range 100
                hbox:
                    text "이주"
                    bar:
                        value ejoo.h_point
                        range 100
                hbox:
                    text "나나"
                    bar:
                        value nana.h_point
                        range 100
                textbutton "돌아가기" action Return()



#######캐릭터##########################################

#나나
image nana idle = "nana_idle.png"
image nana surprise = "nana_surprise.png"
image nana slip = "nana_slip.png"
image nana shadow = "nana_shadow.png"
image nana smile = "nana_smile.png"
image nana crying = "nana_crying.png"
image nana sweat = "nana_sweat.png"
image nana rise = "nanarise.png"
image nana risehand = "nanarisehand.png"
image nana risex = "nanarisex.png"
image nana surpriseh = "nana_surpriseh.png"
image nana_c1 idle = "nana_c1_idle.png"
image nana pikabu = "nana_pikabu.png"
image nana_c1 disgusting = "nana_c1_disgusting.png"
image nana_c1 smile = "nana_c1_smile.png"
image nana_c1 sweat = "nana_c1_sweat.png"
image nana_c2 crying = "nana_c2_crying.png"
image nana_c2 idle = "nana_c2_idle.png"
image nana_c2 disgusting = "nana_c2_disgusting.png"
image nana_c2 idleh = "nana_c2_idleh.png"
image nana_c2 back = "nana_c2_back.png"
image nana_c2 backclap = "nana_c2_backclap.png"
image nana_c2 scream = "nana_c2_scream.png"
image nana_patient idle = "nana_patient_idle.png"
image nana_patient surprise = "nana_patient_surprise.png"
image nana_patient smile = "nana_patient_smile.png"
image nana_patient vomiting = "nana_patient_vomiting.png"
image nana_patient shadow = "nana_patient_shadow.png"
image nana_patient back = "nana_patient_back.png"
image nana_patient surpriseh = "nana_patient_surpriseh.png"
image nana_patient shadowh = "nana_patient_shadowh.png"
image nana_ending idle = "nana_ending_idle.png"
image nana_ending idleh = "nana_ending_idleh.png"
image nana_ending shadow = "nana_ending_shadow.png"
image nana_ending shadowh = "nana_ending_shadowh.png"
image nana_ending smile = "nana_ending_smile.png"
image nana_ending smileh = "nana_ending_smileh.png"
image nana_ending brave = "nana_ending_brave.png"
image nana_ending braveh = "nana_ending_braveh.png"
image nana_ending surpriseh = "nana_ending_surpriseh.png"


#김혜원
image hone_uniform angry = "hone_uniform_angry.png"
image hone_uniform idle = "hone_uniform_idle.png"
image hone_uniform bsmile = "hone_uniform_bsmile.png"
image hone_uniform question = "hone_uniform_question.png"
image hone_uniform idleh = "hone_uniform_idleh.png"
image hone_uniform shadow = "hone_uniform_shadow.png"
image hone_uniform shadowh = "hone_uniform_shadowh.png"
image hone_uniform angryh = "hone_uniform_angryh.png"
image hone_uniform bigside:
    im.FactorScale("hone_uniform_bigside.png",1.5)
image hone_uniform bigfront:
    im.FactorScale("hone_uniform_bigfront.png",1.5)
image hone_c1 question = "hone_c1_question.png"
image hone_c1 idle = "hone_c1_idle.png"
image hone_c1 smile = "hone_c1_smile.png"
image hone_c1 idleh = "hone_c1_idleh.png"
image hone_c1 angry = "hone_c1_angry.png"
image hone_ending idle = "hone_ending_idle.png"
image hone_ending idleh = "hone_ending_idleh.png"
image hone_ending shadow = "hone_ending_shadow.png"
image hone_ending shadowh = "hone_ending_shadowh.png"
image hone_ending smile = "hone_ending_smile.png"
image hone_ending smileh = "hone_ending_smileh.png"
image hone_ending surpriseh = "hone_ending_surpriseh.png"

#정이주
image ejoo slip = "ejoo_slip.png"
image ejoo_uniform shadow = "ejoo_uniform_shadow.png"
image ejoo_uniform shadowhurt = "ejoo_uniform_shadowhurt.png"
image ejoo_uniform shadowh = "ejoo_uniform_shadowh.png"
image ejoo_uniform idle = "ejoo_uniform_idle.png"
image ejoo_uniform idleh = "ejoo_uniform_idleh.png"
image ejoo_uniform balloon = "ejoo_uniform_balloon.png"
image ejoo_uniform bingbing = "ejoo_uniform_bingbing.png"
image ejoo_uniform smile = "ejoo_uniform_smile.png"
image ejoo_uniform sweat = "ejoo_uniform_sweat.png"
image ejoo_c1 idle = "ejoo_c1_idle.png"
image ejoo_c1 idleh = "ejoo_c1_idleh.png"
image ejoo_c1 shadow = "ejoo_c1_shadow.png"
image ejoo_c1 shadowh = "ejoo_c1_shadowh.png"
image ejoo_c1 smile = "ejoo_c1_smile.png"
image ejoo_c1 surprise = "ejoo_c1_surprise.png"
image ejoo_ending idle = "ejoo_ending_idle.png"
image ejoo_ending idleh = "ejoo_ending_idleh.png"
image ejoo_ending shadow = "ejoo_ending_shadow.png"
image ejoo_ending shadowh = "ejoo_ending_shadowh.png"
image ejoo_ending smile = "ejoo_ending_smile.png"
image ejoo_ending smileh = "ejoo_ending_smileh.png"
image ejoo_ending surpriseh = "ejoo_ending_surpriseh.png"
image ejoo_ending 1 = "ejoo_ending_1.png"
image ejoo_ending 2 = "ejoo_ending_2.png"
image ejoo_ending 3 = "ejoo_ending_3.png"
image ejoo_ending 4 = "ejoo_ending_4.png"
image ejoo_ending 5 = "ejoo_ending_5.png"
image ejoo_ending 6 = "ejoo_ending_6.png"
init:
    image ejoo_ending y:
        'ejoo_ending_1.png'
        pause 0.05
        'ejoo_ending_2.png'
        pause 0.05
        'ejoo_ending_3.png'
        pause 0.05
        'ejoo_ending_4.png'
        pause 0.05
        'ejoo_ending_5.png'
        pause 0.05
        'ejoo_ending_6.png'
        pause 0.05
        repeat
image ejoo_ending brave = "ejoo_ending_brave.png"
image ejoo_ending braveh = "ejoo_ending_braveh.png"
image ejoo_ending driver = "ejoo_ending_driver.png"
image ejoo_ending hand1 = "ejoo_ending_hand1.png"
image ejoo_ending hand2 = "ejoo_ending_hand2.png"
image ejoo_ending 7 = "ejoo_ending_7.png"
image ejoo_ending y1:
    "ejoo_ending_y1.png"
    linear 0.18 zoom 2.0






#엄마
image mom angry = "mom_angry.png"
image mom smile = "mom_smile.png"

#동아리회장
image dh scream = "dh_scream.png"

#담임선생님
image teacher scream = "teacher_scream.png"
image teacher idle = "teacher_idle.png"

#친구
image friend_uniform idle = "friend_uniform_idle.png"
image friend_uniform question = "friend_uniform_question.png"
image friend_uniform smile = "friend_uniform_smile.png"
image friend_ending idle = "friend_ending_idle.png"

#할머니
image grandmother smile = "grandmother_smile.png"
image grandmother question = "grandmother_question.png"
image grandmother angry = "grandmother_angry.png"

#######배경############################################
image room_morning = "background/room_morning.jpg"
image t_room = "background/t_room.png"
image crosswalk = "background/crosswalk.jpg"
image alley = "background/alley.jpg"
image classroom = "background/classroom.jpg"
image classroom_front = "background/classroom_front.jpg"
image bokdo = "background/bokdo.png"
image black = "background/black.jpg"
image stair = "background/stair.jpg"
image foodroom = "background/foodroom.jpg"
image foodroom_chair = "background/foodroom_chair.jpg"
image clothshop = "background/clothshop.jpg"
image hongdae = "background/hongdae.jpg"
image perfumeshop = "background/perfumeshop.jpg"
image hongdae_night = "background/hongdae_night.jpg"
image computerroom = "background/computerroom.jpg"
image school_front = "background/school_front.jpg"
image theend = "background/theend.png"
image bearbrick:
    im.FactorScale("bearbrick.png",0.7)
    yalign 0.4
image sol = "background/sol.jpg"
image bear:
    im.FactorScale("bear.png",0.5)
    yalign 0.3
image countryside = "background/countryside.jpg"
image countrysideroom = "background/countryside_room.jfif"
image pants:
    im.FactorScale("pants.png",0.8)
    yalign 0.2
image necklace:
    im.FactorScale("necklace.png",0.9)
    yalign 0.3
image countrysidedinner = "background/countryside_dinner.jpg"
image super = "background/super.jpg"
image countryside_nightroad = "background/countryside_nightroad.jpeg"
image teeth = "background/teeth.png"
image countryside_bridge = "background/countryside_bridge.jfif"
image nana_diving1 = "background/nanadiving1.png"
image nana_diving2 = "background/nanadiving2.png"
image nana_diving3 = "background/nanadiving3.png"
image nana_diving4 = "background/nanadiving4.png"
image countryside_night = "background/countryside_night.jpg"
image cgv_roby = "background/cgv_roby.jpg"
image cgv_popcorn = "background/cgv_popcorn.jpg"
image cgv = "background/cgv.jpg"
image cgv1 = "background/cgv1.png"
image cgv2 = "background/cgv2.png"
image cgv3 = "background/cgv3.png"
image studyroom = "background/studyroom.png"
image studyroom_out = "background/studyroom_out.jpg"
image vendingmachine = "background/vendingmachine.jpg"
image hone_whisper1 = "background/hone_whisper1.png"
image hone_whisper2 = "background/hone_whisper2.png"
image bonjook = "background/bonjook.jfif"
image bonjook_inside = "background/bonjook_inside.jpg"
image hospital_roby = "background/hospital_roby.jpg"
image hospital_morning = "background/hospital_morning.jpg"
image hospital_night = "background/hospital_night.jpg"
image hospital_desk = "background/hospital_desk.jpg"
image ejooending = "background/ejooending.jpg"
image ending1 = "background/ending1.jpg"
image ending2 = "background/ending2.jpg"


#캐릭터 정의
define n = Character("나나")
define h = Character("김혜원")
define e = Character("정이주")
define m = Character("엄마")
define t = Character("담임선생님")
define dh = Character("동아리회장")
define g = Character("할머니")
define f = Character("친구")


label start:

    python:
        nana=character("나나",50)
        hone=character("김혜원",50)
        ejoo=ejooo("정이주",50,0)
        player=play(5, 5)

$player_name = renpy.input("이름을 입력해주세요.")

scene room_morning
play music "audio/normal.mp3" loop
"[3월 3일]"
"'창문 사이로 들어오는 따뜻한 햇빛...'"
"'전혀 피곤하지 않은 몸...'"
"'밖에서 들려오는 아줌마들의 수다소리...'"
"..."
"지각이다!!!!"
show mom angry
m "[player_name], 밥 먹고 가야지!"
"늦었어요!"
hide mom_angry
"재빨리 교복으로 갈아입고 대충 씻은 채 집 밖으로 뛰어간다."
scene crosswalk
hide room_morning
"바뀌지 않는 횡단보도를 확인한다"
"젠장! 이러다가 늦겠어!"
"안되겠다. 다른 길로 가야겠어!"
"몸을 틀어 다른 길로 뛰어간다"
"골목에서 꺾는다"
scene alley
hide crosswalk
"그 순간"
scene alley with vpunch
"쾅!"
show nana slip with dissolve
"???" "아야야...이따이요..."
"으윽... 뭐지...?"
"고개를 들어보니 금발에 흰 피부... 그리고 일본의 교복을 입고 있는 여자가 있었다."
"헉! 죄송합니다! 죄송합니다!"
"하지만 갈 길이 바쁘기에 재빨리 일으켜드리고 학교로 뛰어간다"
show nana shadow with dissolve
"???" "저 교복은... 혹시...?"
scene classroom
hide alley
"교실로 들어왔더니 아슬아슬하게 세이프했다"
"휴...하마터면 벌점 받을 뻔 했네..."
"???" "야! 너 또 지각한 거야?"
"'아주 오래전부터 지긋지긋하게 들은 목소리의 여자...'"
"뭐야... 또 너냐? 잔소리좀 하지마 너도 어제 지각할 뻔 했으면서;"
show hone_uniform angry with dissolve
h "미안한데 난 지각할 뻔한 상황이 있었던 거지 18년동안 한 번도 지각 안 했거든?"
show hone_uniform idle with dissolve
h "그리고 너 오늘 지각맞아."
h "우리반 시계 고장나서 5분 늦거든"
"'이 여자는 나의 소꿉친구인 짜증나는 모범생 김혜원이다...'"
"뭐라고?"
"하... 담임쌤이 또 한소리 하시겠네..."
h "아! 그리고 오늘 전학생 오는데 소문에 의하면 다른 나라에서 왔다던데?"
"외국인?"
"하 모르겠고 이쁜 여자애였으면 좋겠다~~"
h "에휴... 이쁜 여자가 오면 뭐하냐"
show hone_uniform bsmile
h "넌 나말고 다른 여자랑 말도 못섞는 쑥맥에 모쏠이면서ㅋㅋ"
"아 뭐래! 아니거든??"
hide hone_uniform bsmile
show teacher scream with dissolve
t "조용히 해라! 다들 자리에 가서 앉아!"
show teacher idle at left
t "오늘은 먼 곳에서 전학생이 왔다. 자, 들어오렴"
"???" "하--잇!"
show nana shadow at right with dissolve
"터벅터벅..."
'금발에 흰 피부... 큰 눈까지...'
"아닛?! 저 사람은?"
"???" "모두들 오하이욧!"
show nana idle with dissolve
n "나의 이름은 야부키 나나! 일본에서 왔어!"
show nana surprise
n "모두들 잘부탁...앗!"
n "넌 오늘 아침에!"
"(흠칫)"
show hone_uniform question at left with dissolve
hide teacher idle
h "뭐야...[player_name], 너 쟤랑 아는 사이야...?"
"뭐... 오늘 아침에 좀... 그런 일이 있었어..."
show teacher idle at left
hide hone_uniform question
t "[player_name], 나나와 서로 아는 사이같구나."
show teacher scream
t "나나는 잠깐 교무실로 오고 [player_name]! 너도 지각했으니 교무실로 따라와!"
t "그럼 오늘 아침조회는 이만 마친다."
"하..."
scene t_room
hide classroom
"[교무실]"
show teacher idle at left with dissolve
show nana idle at right with dissolve
t "지각의 사정은 알겠고, 너네 둘이 어떻게 아는 사이인 거니?"
"아... 그게 말이죠..."
show nana surprise
n "아침에 이 남자애가 나한테 몸을 들이댔다!"
show nana crying with dissolve
n "기세가 너무 강력해 울음이 나올 뻔 했지만"
show nana smile
n "나를 따뜻하게 감싸주었다!"
"야! 너 무슨 소리를 하는 거야!! 그렇게 말하면 오해하시잖아!!"
show nana idle
t "[player_name]... 도대체 무슨 짓을 하고 다니는 거냐..."
"아! 선생님 그게 아니라 아침에 뛰다가 부딪혀서 일으켜준 것 뿐이라구요...!"
t "흠... 어쨌든 이것도 인연이니..."
show teacher scream
t "[player_name]! 너가 나나한테 이것저것 학교에 대해 알려줘라"
"네???"
show nana smile
n "야호!"
"하하..."
"'뭔가 엄청 피곤한 일들이 일어날 것만 같은 예감이 든다...'"
scene bokdo
hide t_room
"[복도]"
show nana idle
"반가워 [player_name]군! 나의 감으로 보아 너와 나는 운명인 것 같아!"

#nana1
menu:
    "운명같은 소리하네...":
        show nana sweat
        n "하하... 나만 그렇게 느꼈낭..."
        n "빨리 교실로 올라가자...!"
        $player.minus(nana)
    "그래 나도 뭔가 그런 느낌이 들어":
        show nana smile
        n "역시! 나만 그렇게 느낀 게 아니였구나!"
        n "ㅎㅎ 앞으로 잘 부탁해!"
        "그래 일단 교실로 올라가자"
        $player.plus(nana)
scene classroom
hide bokdo
"[교실]"
"휴..."
show hone_uniform question at left with dissolve
h "야 [player_name], 담임선생님께서 뭐라고 하셨어?"
"그냥 전학생 잘 챙겨주래"
show hone_uniform idle
h "흠... 뭐 나쁜 애처럼은 안 보인다!"
show nana surprise at right with dissolve
n "[player_name]군! 이 예쁜 여자애는 누구야?"
n "혹시 여친...?ㅎㅎ"

#hone1
menu:
    "뭐, 김혜원이 예쁘긴하지":
        show hone_uniform idleh
        h "!!!"
        h "ㅁ... 뭐래는 거야 갑자기...!"
        show hone_uniform shadowh with dissolve
        h "얘랑은 아직 사귀는 사이는 아니긴...해..."
        h "아직은(중얼)"
        "응? 방금 뭐라고 했어?"
        show hone_uniform idleh
        h "ㅇ...아무것도 아니야!"
        $player.plus(hone)
    "아니; 이렇게 흔한 얼굴이 어디봐서 예쁘다는 거야?":
        show hone_uniform angry
        h "뭐래 이 못생긴게!"
        h "얘랑은 전~~~혀 사귀는 사이 아니고 사귈 수 있는 사이도 아니야!"
        "참나, 나도 마찬가지거든?"
        $player.minus(hone)
show nana smile
n "헤헤, 둘 다 사이 좋아보인다!"
n "귀엽게 생긴 넌 이름이 뭐야?"
show hone_uniform idleh
h "ㄱ... 김혜원이라고 해"
n "혜원짱 반가워! 친하게 지내자!ㅎㅎ"
h "아 ㅇ...응!(부끄)"
show hone_uniform idle
h "아참!"
h "너네들 다음주가 무슨 날인지 알아?"
show nana surprise
"[player_name], 나나" "무슨 날인데?"
h "동아리 신청기간이잖아!"
"아아 벌써 시간이 그렇게 됐나?"
show nana smile
n "난 [player_name]군이랑 같은 동아리 할래!"
h "[player_name], 너 댄스동아리 나가고 다른 동아리 들어간다매?"
h "어떤 동아리 하게?"
"음... 내 진로랑 관련있는 게 좋을 것 같아서 코딩동아리나 하려고"
show nana sweat
n "헤에 코딩? 난 어려워서 [player_name]군이랑 같은 동아리 못하겠다..."
h "하긴 넌 꿈이 개발자라고 했지?"
"응 맞아. 근데 우리 학교에 코딩동아리가 뭐가 있지?"
h "음...플라텍 어때? 거기에 전교 1등 선배도 계시고 생기부도 잘 채워주신대"
"플라텍? 흠..."
scene black
hide classroom
"[3월 10일]"
scene stair
hide black
"흠 플라텍 면접보는 반이 2학년 5반?"
"복도를 걸어가며 반을 찾는다"
"계단 앞을 지나가려는 그 순간"
stop music
show ejoo slip with dissolve
"???" "아아앗!"
"응?"
"계단에서 단발머리의 여학생이 넘어지려한다"

#ejoo1
menu:
    "자신도 다칠 수 있으니 슬쩍 피한다":
        "위험해!"
        "(스윽)"
        show ejoo slip with hpunch
        "우당당탕"
        hide ejoo slip
        show ejoo_uniform shadowhurt
        "???" "아야야..."
        "어우 아프겠다; 조심 좀 하지"
        "일어설 수 있겠어요?"
        show ejoo_uniform shadow
        "???" "아아... 네..."
        show ejoo_uniform shadowhurt
        "???" "히익! 늦었다!"
        hide ejoo_uniform shadowhurt with easeoutleft
        "단발머리의 여학생은 다급히 뛰어갔다"
        $player.minus(ejoo)
    "뛰어난 운동신경을 발휘해 잡아준다":
        "위험해!"
        "괜찮으세요?"
        hide ejoo slip
        show ejoo_uniform shadowh
        "???" "아앗...고맙습니다...///"
        show ejoo_uniform shadowhurt
        "???" "아참 늦겠어!"
        hide ejoo_uniform shadowhurt with easeoutleft
        "단발머리의 여학생은 고맙다는 말을 하고 다급히 뛰어갔다."
        $player.plus(ejoo)
        $ejoo.y_plus()
"뭐지...?"
"아참 동아리면접 늦겠다!!!"
scene black
hide stair
"늦은 줄 알고 동아리 면접보는 곳으로 뛰어갔지만"
"시간을 잘못봐서 3학년 면접시간보다 한 시간 빠른 2학년 면접보는 시간에 와버렸다"
play music "audio/normal.mp3" loop
scene classroom_front
hide black
"하... 어쩔 수 없지. 이 앞에서 기다려야겠다"
"[한 시간후]"
"드르륵..."
"앗 저 애가 마지막 2학년인가?"
"응? 너는..."
if ejoo.h_point==55:
    show ejoo_uniform shadowh with easeinleft
    "???" "앗 아까전에는 고마웠습니다...!"
    "아아 아니야 그것보다 너도 플라텍 면접본 거야?"
    "???" "앗 넵!"
    "???" "코딩에 관심이 많아서요..."
    "하하 우리 같은 동아리 선후배 사이가 될 수도 있겠네"
    "넌 이름이 뭐야?"
    show ejoo_uniform idleh with dissolve
    e "ㅈ... 정이주예요!"
    "그래 내 이름은 [player_name]..."
    "앗, 면접보러 들어가야 되는데! 그럼 안녕!"
    show ejoo_uniform idle
    e "ㄴ...넵!"
    stop music
    show ejoo_uniform shadowh with dissolve
    e "[player_name]선배..."
elif ejoo.h_point == 45:
    show ejoo_uniform shadow with easeinleft
    "???" "아...아까전에 그 사람..."
    "아아, 너도 플라텍 면접 본 거야?"
    "???" "네..."
    "혹시 같은 동아리 할 수도 있으니까 서로 이름말하는 거 어때? "
    "내 이름은 [player_name]야! 너는?"
    show ejoo_uniform idle
    e "제 이름은... 정이주예요..."
    "그래 너랑 같이 동아리 활동 했으면 좋겠다."
    "앗, 면접보러 가야되는데! 그럼 안녕!"
    e "네..."
    stop music
    e "[player_name]선배..."
scene black
hide classroom_front
"다행히 면접에 늦지않았고 뛰어난 화술로 면접에 통과해 동아리에 합격했다"
call screen lovePoint
"[다음날]"
scene classroom
hide black
play music "audio/normal.mp3" loop
"아 제발 같이 먹자니까???"
show hone_uniform angry at left with dissolve
h "내가 왜 너랑 같이 밥을 먹어줘야 하는데!"
"아 오늘 나랑 같이 밥 먹는 애가 조퇴해서 나 혼자 밥먹게 생겼다고ㅠㅠㅠ"
h "그럼 나 말고 다른 애한테 부탁하면 되잖아!"

#hone2
menu:
    "아 너 말고 친구가 없어서 그래... 나도 같이 먹기 싫은데(중얼)":
        show hone_uniform shadow
        h "(빠직)"
        show hone_uniform angry
        h "뭐라고? 같이 먹기 싫으면 혼자 먹던가! 너 같은 애 제일 싫어!"
        "아 미안미안ㅠㅠㅠ 제발~~~"
        show nana idle at right with easeinright
        n "혜원짱 그러지말고 같이 먹는 게 어때?"
        show nana smile
        n "나도 [player_name]군이랑 같이 밥 먹고 싶은데ㅎㅎ"
        "역시 나나 밖에 없어ㅠㅠㅠ"
        show hone_uniform idle
        h "후... 그럼 이번 한 번만이다..."
        "응응! 알겠어!"
        $player.minus(hone)
    "ㄴ...너랑 같이 밥 한 번 먹어보고 싶어서 그런다!":
        show hone_uniform idleh
        h "ㅁ... 뭐라고?"
        "그러니까 김혜원이랑 같이 밥 먹고 싶다고!!!"
        h "야야 잠깐---!"
        show hone_uniform shadowh with dissolve
        h "ㅇ... 알겠으니까 그만... 창피하단말이야...///"
        show nana surprise at right with easeinright
        n "어라? 혜원짱 우리 오늘은 [player_name]군이랑 같이 밥 먹는 거야?"
        show hone_uniform idleh with dissolve
        h "어... 뭐, 그렇게 됐어"
        show nana smile
        n "야호! 빨리 급식먹으러 가자!"
        "그래그래 빨리 가자!"
        $player.plus(hone)
scene foodroom
hide classroom
"[급식실]"
"아앗... 좀 늦어서 하마터면 1학년이랑 같이 줄을 설 뻔 했네..."
if ejoo.h_point == 55:
    "(콕콕)"
    "음 뭐지? 누군가 뒤에서 찌르는데..."
    show ejoo_uniform idleh with dissolve
    e "선배, ㅇ... 안녕하세요..."
    "어어 반갑다 이주야! 너도 플라텍 붙었다매? 축하해!"
    e "ㄱ... 감사합니다...///"
    "이제 우리 동아리시간마다 볼 수 있겠다!"
    e "ㄱ... 그러게요...///"
    show ejoo_uniform idle with dissolve
    e "아 선배... 이거..."
    show bearbrick with dissolve
    "응? 뭐야 이건 베어브릭이잖아???"
    hide bearbrick with dissolve
    show ejoo_uniform idleh
    e "그때 계단에서 넘어질 때... 안 다치게 잡아주셔서..."
    show ejoo_uniform shadowh with dissolve
    e "감사의 표시에요..."
    "헤에... 그런데 이렇게 비싼 걸 받아도 되는 거야?"
    show ejoo_uniform idleh
    e "제 취미가... 베어브릭 수집이라... 집에 많아서 괜찮아요...///"
    "그래? 그럼 고맙게 받을게! 가방에 달아야겠다!"
elif ejoo.h_point == 45:
    "앗 넌!"
    show ejoo_uniform idle with dissolve
    e "아... [player_name]선배... 안녕하세요..."
    "보니까 너도 동아리 붙었더라? 이제 같이 활동하면서 보겠다ㅋㅋ"
    e "ㄱ... 그러게요..."
show ejoo_uniform idle
"급식판을 들려고 했는데 맨 위에 있는 급식판에 무언가 묻어있다"

#ejoo2
menu:
    "맨 위의 급식판 아래에 있는 급식판을 슥 꺼내 가져간다":
        "급식실 아주머니" "맛있게 먹으렴~"
        "앗, 이주야. 맨 위의 급식판 그대로 가져온 거야?"
        "거기에 뭐 묻어있었는데... 똑바로 좀 보지..."
        show ejoo_uniform shadow with dissolve
        e "..."
        "그럼 맛있게 먹어~!"
        e "네... 선배도 맛있게 드세요..."
        $player.minus(ejoo)
    "맨 위의 급식판 밑에 있는 급식판을 이주에게 준다":
        "아주머니 여기에 뭐가 묻어있어요"
        "밑에 있는 급식판을 집으며"
        "이주야 자, 여기"
        show ejoo_uniform idleh with dissolve
        e "앗... ㄱ...감사합니다...///"
        "그래 그럼 이주야 밥 맛있게 먹어~"
        e "네...ㅅ...선배도 맛있게 드세요...!"
        $player.plus(ejoo)
        $ejoo.y_plus()
scene foodroom_chair
hide foodroom
show hone_uniform question at left with dissolve
h "야 [player_name], 아까 그 귀엽게 생긴 여자애는 누구야?"
"아아 이주? 그냥 동아리 후배야"
show nana smile at right with dissolve
n "우리 학교 밥 진짜 맛있는 것 같다! 우걱우걱"
h "나나가 우리 학교 밥이 마음에 들었나 보네!"
"하하 그러게"
"바로 그때"
hide hone_uniform question
hide nana smile
show nana rise with dissolve
"나나의 입가에 밥풀이 붙어있다. 어떻게 해야될까"

#nana2
menu:
    "밥풀을 자연스럽게 떼서 입에 넣는다.":
        "정말 나나는 칠칠치 못하다니까"
        show nana risehand with dissolve
        "(스윽)"
        show nana risex with dissolve
        "꿀꺽"
        hide nana risex
        show hone_uniform shadow at left
        show nana surpriseh at right
        "나나, 김혜원" "!"
        h "[player_name]... 너 지금 ㅁ... 뭐한 거야?"
        "응? 그냥 밥풀이 붙어있길래 왜?"
        n "...///"
        n "나 먼저 가볼게!"
        hide nana surpriseh with easeoutright
        "나나는 얼굴을 붉힌 채 뛰어간다"
        "응? 왜저러지?"
        show hone_uniform angry
        h "뭐가 왜 저러지야!"
        show hone_uniform shadow with dissolve
        h "ㄴ... 너는 진짜..."
        show hone_uniform angry
        h "제일 싫어!!!!!"
        hide hone_uniform angry with easeoutleft
        "김혜원도 급식실을 나간다"
        "야아ㅏㅇ아아! 너네들 다 가버리면"
        "혼밥이라고..."
        $player.plus(nana)
    "게걸스럽게 먹지 말라고 한다":
        "와...나나야 게걸스럽게 먹지 좀 마;"
        hide nana rise
        show hone_uniform idle at left
        show nana sweat at right
        n "아... ㅎㅎ 미안해... 조심히 먹을게..."
        show hone_uniform angry
        h "야 [player_name], 말 좀 예쁘게 해!"
        "내가 뭐?"
        h "어휴 진짜... 저런 애를 누가 사겨줄지..."
        "음 오늘 밥 맛잇넹"
        $player.minus(nana)
scene black with dissolve
hide foodroom_chair
"[다음날]"
call screen lovePoint
scene room_morning
hide black
"흐음..."
"컴퓨터로 페이스북에 올라온 게시물을 확인한다"
"여자에게 인기가 많아지려면... 옷을 잘입고 향수를 뿌리면 좋다...?"
"좋았어! 오늘은 쇼핑이다!"
stop music
scene clothshop
hide room_morning
play music "audio/hongdaemusic.mp3" loop
"[홍대의 어느 옷가게]"
"흐음... 어떤 옷을 사지?"
#mpoint1
menu:
    "와이드 팬츠":
        "역시 요즘에 많이 입는 트렌디한 와이드팬츠지!"
        "이걸로 주세요"
        "[매력포인트가 증가했습니다.]"
        $player.m_plus()
    "주머니가 매우 크게 달린 민트색 반바지":
        "음 이게 좋겠어!"
        "이걸로 주세요!"
        "[매력포인트가 감소하였습니다]"
        $player.m_minus()
scene hongdae
hide clothshop
"좋았어... 그 다음은 향수인가..."
"향수가게가 여기 어딘가에 있을텐데..."
"???" "야 [player_name]!"
"응? 어디서 나를 부르는데?"
show hone_c1 question with dissolve
h "야 너가 웬일로 홍대에 왔냐?"
"후훗... 나도 이제 여친사귈 준비를 할까해서"
if player.m_point == 10:
    show hone_c1 idle
    h "오 뭐야, 와이드팬츠?"
    h "너가 웬일로 정상적인 옷을 다입었냐?"
    "원래 나의 뛰어난 패션감각을 숨기고 다녔던 것 뿐이라고~"
else:
    show hone_c1 smile
    h "얔ㅋㅋㅋㅋㅋㅋ 그 촌스러운 옷은 뭐얔ㅋㅋ"
    "ㅇ... 이게 뭐 어때서!"
"근데 너 오늘..."

#hone3
menu:
    "옷이 그게 뭐냐? 꽃무늬? 너가 할머니냐?":
        show hone_c1 angry
        h "이 옷이 뭐 어때서!"
        h "[player_name] 제일 싫어 극혐!"
        hide hone_c1 angry with easeoutleft
        "왜 저래... 모르겠고 빨리 향수가게나 찾아야겠다~"
        $player.minus(hone)
    "좀... 예쁘네...":
        show hone_c1 idleh
        h "ㅁ... 뭐야 갑자기 칭찬을 다하고..."
        "아니 그냥 진짜 오늘 예뻐보여서..."
        "김혜원 친구들" "혜원아 뭐해! 빨리 가자~"
        show hone_c1 idle
        h "어 알겠어!"
        show hone_c1 idleh with dissolve
        h "너도 오늘 멋져..."
        h "그럼 학교에서 봐 [player_name]!"
        hide hone_c1 with easeoutleft
        "ㅎㅎ 빨리 향수가게나 찾아야겠다"
        $player.plus(hone)
scene perfumeshop
hide hongdae
"[향수가게]"
"흐음... 향수종류가 많네..."
"어떤 걸 사야되지?"

#mpoint2
menu:
    "존바바토스 아티산 맨오드뚜왈렛":
        "음! 이걸로 해야겠다"
        scene hongdae
        hide perfumeshop
        "가게를 나온다"
        play sound "audio/boom.mp3"
        show nana pikabu with vpunch
        n "왁!"
        hide nana pikabu
        show nana_c1 idle
        "깜짝이야!"
        "여기는 웬일이야?"
        n "난 쇼핑하러 왔지ㅎㅎ"
        n "어? 잠깐만..."
        n "[player_name]군 향수도 뿌려? 향기 되게 좋다!"
        "ㅎㅎ 그래?"
        n "응! 여자들이 좋아하는 향이야!"
        $player.m_plus
        "[매력포인트가 증가했습니다]"
    "블루 드 샤넬":
        "음! 이걸로 해야겠다"
        scene hongdae
        hide perfumeshop
        "가게를 나온다"
        play sound "audio/boom.mp3"
        show nana pikabu with vpunch
        n "왁!"
        hide nana pikabu
        show nana_c1 idle
        "깜짝이야!"
        "여기는 웬일이야?"
        n "난 쇼핑하러 왔지 ㅎㅎ"
        n "어? 잠만... 킁킁"
        show nana_c1 disgusting
        n "윽, [player_name]군한테서 아빠스킨냄새나..."
        "ㅂ... 별로야?"
        n "대부분의 여자들은 시트러스의 상큼한 향과 적당히 우디한 따뜻함이 느껴지는\n향을 좋아하지..."
        show nana_c1 idle
        n "[player_name]군이 고른 향수는 MISS데쓰!"
        $player.m_minus
        "[매력포인트가 감소했습니다.]"
n "저기... [player_name]군? 혹시 오늘 시간되면\n나랑 놀지 않을래?"

#nana3
menu:
    "내가 왜?":
        show nana_c1 sweat
        n "아 미안! 내가 너무 눈치가 없었다!ㅎㅎ..."
        n "..."
        n "그럼 학교에서 봐 [player_name]군!"
        hide nana_c1 with easeoutleft
        "그래 난 집이나 가봐야겠다"
        $player.minus(nana)
    "좋아!":
        show nana_c1 smile
        n "야호! 빨리 가서 놀자!"
        n "나 [player_name]군이랑 놀 수 있어서\n심장이 두근두근해!"
        "나도! ㅎㅎ"
        hide nana_c1
        "그렇게 나나와 홍대에서 시간 가는 줄도 모르고 신나게 놀았다."
        scene hongdae_night
        hide hongdae
        show nana_c1 smile
        n "잘 가 [player_name]군!"
        hide nana_c1 smile with dissolve
        "응 나나도 잘가!"
        "이제 집에 가야겠다!"
        $player.plus(nana)
if ejoo.y_point == 2:
    "그런데 아침부터 계속 누가 날 보고있는 것 같은 느낌이 드는데..."
    "설마..."
    "오늘 나의 초이스로 여자들이 관심을 보이는 건가??"
    "ㅎㅎㅎㅎㅎ그럼 곤란한뎋ㅎㅎㅎ아잏ㅎㅎㅎㅎ"
stop music
scene black
call screen lovePoint
hide hongdae_night
"[1주일 후]"
play music "audio/normal.mp3" loop
scene computerroom
hide black
"[동아리실]"
show dh scream with dissolve
dh "자 오늘은 여기까지만 합시다!"
"동아리부원들" "수고하셨습니다!"
hide dh scream with dissolve
show ejoo_uniform idle with dissolve
e "으음..."
"왜그래 이주야?"
e "오늘 배운 재귀호출이 이해가 잘 되지 않아서요..."

#ejoo3
menu:
    "친절하게 알려준다.":
        "아 이주야 이건 꼬리잡기 게임을 생각하면\n이해하기 쉬워"
        "이렇게 서로의 꼬리를 물며 함수가 실행되는 거지"
        show ejoo_uniform idleh with dissolve
        e "아...! 이해됐어요!"
        e "[player_name]선배 되게 친절하게 알려주셔서"
        show ejoo_uniform shadowh with dissolve
        e "ㄱ...감사합니다..."
        "아니야ㅋㅋ 나중에 모르는 거 있으면 나한테 물어봐!"
        show ejoo_uniform idleh
        e "ㄴ...네!"
        $player.plus(ejoo)
        $ejoo.y_plus()
    "그것도 모르냐면서 구박한다":
        "아니 이주야, 이건 아까 회장님이 잘 알려주셨잖아"
        "내 눈에는 너가 제대로 집중 안 하는 것처럼 보이는데?"
        show ejoo_uniform shadow with dissolve
        e "아...ㅈ... 죄송합니다..."
        "보니까 이대로면 다른 부원들의 발목만 잡을 것 같으니까 노력 좀 했으면 좋겠어."
        e "네...ㅈ..조심하겠습니다..."
        $player.minus(ejoo)
hide ejoo_uniform
show dh scream
dh "아 그리고 이번 여름 축제때 우리 동아리는 두 조로 나뉘어서 준비할 거야."
"저게 무슨 소리지?"
dh "이번 축제에는 스크래치를 이용해서 만든 게임과 RC카를 이용한 게임을 준비할 계획이야!"
dh "절반은 스크래치를 이용해 게임을 만들거고"
dh "나머지는 아두이노를 사용해 RC카를 이용한 게임을 만들 거야!"
dh "다음 모임까지 어떤 걸 준비하고 싶은 지 얘기해줘!"
dh "그럼 해산!"
hide dh
"흐음...뭘 하는 게 좋을까..."
"이주야 넌 뭐 할 거야?"
show ejoo_uniform idleh with dissolve
e "ㅈ...저는 RC카요..."
"RC카?"
"음...재밌겠네! 나도 그걸로 해야겠다!"
"그럼 이주야 오늘부터 준비해볼까??"
stop music fadeout 2.5
show ejoo_uniform shadow with dissolve
e "ㅇ...안 돼요..."
"?!"
"이주야 설마 나랑 하기 싫다는 거야?"
e "ㄱ... 그게..."
"어쩔 수 없지..."
e "ㅅ...시..."
"뭐라고 이주야? 싫다고? 하 나도 너랑 하기 싫어졌어."
show ejoo_uniform idle
e "시험기간이라고요!!!!"
"엥?"
e "다음주 시험이잖아요...\n 그래서 다음 모임은 시험 끝나고 있는 거고요..."
"벌써 시험기간이였어?!?!"
"하... 공부 좀 해야겠는 걸?"
scene black
hide computerroom
"[다음날]"
play music "audio/normal.mp3" loop
scene classroom
hide black
play sound "audio/dingdongdang.mp3"
"딩동댕 딩동 딩디디딩(하교시간)"
show friend_uniform idle with dissolve
f "야 [player_name]! 빨리 피방가자!"
"너네끼리 가라..."
show friend_uniform question with dissolve
f "뭐야... 갑자기 왜 빼?"
"공부해야돼. 이번엔 성적 잘 받을 거야."
f "평소에 공부에 손도 안 대던 애가 갑자기 성적?"
"여친을 사귀기 위해서는 똑똑해야 한댔어!"
show friend_uniform smile
f "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ너가 여친 못사귀는 이유는 거울보면 나오는뎈ㅋㅋ"
"ㅈ...조용히해! 나 공부할 거야!"
scene school_front
hide classroom
"팩폭에 상처받아 학교 밖으로 뛰쳐나간다."
"두고봐... 좋은 성적 받아서 여친 꼭 사귀고 말테니까..."
show hone_uniform question with dissolve
h "야 [player_name]! 너 공부한다매?"
show hone_uniform idle
"'그렇지!'"
"야야 김혜원 나 공부 좀 알려주면 안 돼? 너 전교 1등이잖아ㅠㅠ"
show hone_uniform question
h "공부 알려달라고?"
show hone_uniform bsmile
h "음... 조금 알려주도록 할까...?"
"야호!"
"그럼 빨리 우리 집으로 가자"
show hone_uniform angryh with dissolve
h "뭐? 너네 집??"
"응!"
h "ㅈ...잠만 난 아직 마음의 준비가!"
"가자!"
scene room_morning
hide school_front
show hone_uniform idleh with dissolve
h "ㅇ...여기가 [player_name]의 집..."
"자 공부하자!"
h "ㅇ...어어..."
show hone_uniform idle at right
show mom smile at left
m "어머 아들이 여친을 다 데려왔네? 반가워요^^"
show hone_uniform angryh
h "네?!?!?!??"

#hone4
menu:
    "이렇게 못생긴 애가 어떻게 내 여친이야!":
        show hone_uniform shadow with dissolve
        h "(빠직)"
        m "어머 이렇게 예쁜데 무슨 소리하는 거니?"
        m "상처받지 말아요 다 부끄러워서 저러는 거니깐요(속닥속닥)"
        h "아...네..."
        m "그럼 엄마는 이만 갈게 공부 열심히들 하렴~"
        hide mom smile with easeoutleft
        $player.minus(hone)
    "아 엄마! 아직 그런 사이는 아니야...":
        show hone_uniform idleh
        h "'아직...이라고 했다...'"
        m "호호 그러니? 엄마는 이만 가볼게 열심히 공부하렴~"
        hide mom smile with easeoutleft
        "그럼 이제 공부를 해볼..."
        "야 김혜원, 너 얼굴이 왜그렇게 빨개?"
        show hone_uniform shadowh with dissolve
        h "'아직....아직...그럼 나중에...?'"
        "야 김혜원!"
        show hone_uniform idleh
        h "ㅇ...어어!"
        "너 진짜 괜찮은 거 맞지?"
        h "ㄱ...그럼! 빨리 공부하자...///"
        "흐음..."
        $player.plus(hone)
hide hone_uniform
"[몇시간 후]"
stop music
show hone_uniform idle with dissolve
"야 김혜원! 나 이거 좀 알려줘"
h "뭔데?"
show hone_uniform question
h "야 이렇게 거꾸로 보여주면 어떻게 설명하라고;"
show hone_uniform idle
h "기다려봐"
play music "audio/heartbeat.mp3" loop
hide hone_uniform with dissolve
"김혜원이 주인공의 옆에 앉는다"
show hone_uniform bigside with dissolve
h "...이건 이렇게 하는거야."
show hone_uniform bigfront with dissolve
h "이해됐어?"
"고개를 돌린 그 순간 김혜원과 입김이 닿을 거리에서 눈이 마주친다."
#hone5
menu:
    "눈을 피한다":
        stop music
        "아ㅆ..."
        show hone_uniform shadow
        h "(빠직)"
        show hone_uniform angryh with vpunch
        play sound "audio/jap.mp3"
        h "야! 내가 열심히 가르쳐주는데 어?(퍽)"
        show hone_uniform angryh with vpunch
        play sound "audio/jap.mp3"
        h "고맙다고 말하지는 못할 망정(퍽)"
        show hone_uniform angryh with vpunch
        play sound "audio/jap.mp3"
        h "사람 기분 나쁘게 뭐? 씨??(퍽퍽)"
        "ㅁ...미안해! 잘못했어!!(쿨럭)"
        h "됐어! 이제 너한테 공부 안 가르쳐줘!"
        hide hone_uniform angry with easeoutleft
        "김혜원은 화를 내며 집을 나간다."
        "하...망했다..."
        $player.minus(hone)
    "지긋이 응시한다.":
        "..."
        h "///"
        "혜원아"
        h "[player_name]..."
        "서로의 얼굴이 가까워진다."
        "서로의 입술이..."
        hide hone_uniform
        show mom smile at left
        stop music
        m "애들아! 엄마가 과일 깎아왔..."
        "..."
        show hone_uniform shadow at right
        h "..."
        m "..."
        m "ㅇ...아 하던거 마저하렴ㅎㅎ 엄마는 이따가 올게...^^"
        hide mom with easeoutleft
        "ㅇ...엄마 그게 아니라!"
        show hone_uniform shadowh with dissolve
        h "///////"
        h "난 ㄱ...가볼게!"
        hide hone_uniform with easeoutright
        "ㅇ...어어"
        "하 씨..."
        "타이밍 진짜..."
        $player.plus(hone)
    "입술을 부딪힌다.":
        stop music
        show hone_uniform idle
        play sound "audio/kiss.mp3"
        h "!"
        show hone_uniform question
        h "ㄴ...너 지금 뭐한 거야???"
        "혜원아 ㄱ... 그게 아니라..."
        h "이 변태새끼!"
        play sound "audio/jjak.mp3"
        show hone_uniform angry with vpunch
        "(짝)"
        h "꺼져버려 늑대같은 놈!!!"
        hide hone_uniform with easeoutleft
        "아..."
        scene classroom
        hide room_morning
        "그렇게 김혜원에 의해 여자만 밝히는 늑대새끼로 학교에 소문이 나고..."
        show nana shadow at left with dissolve
        n "늑대새끼..."
        show ejoo_uniform at right with dissolve
        e "선배... 실망했어요..."
        "주위 사람들이 다 떠나가 남은 고등학교 생활을 아싸로 지내게 된다..."
        play music "audio/endingmusic.mp3" loop
        scene theend
        hide classroom
        "첫번째 엔딩"
        return
scene black
hide room_morning
"1주일 후 시험 결과는"
"당연히 망했다."
call screen lovePoint
play music "audio/normal.mp3" loop
scene computerroom
hide black
"[축제 전날]"
show dh scream with dissolve
dh "일단 우리들은 RC카를 이용해 게임을 만들건데"
dh " RC카 앞에 압정을 달고 뒤에는 작은 풍선을 붙여서 서로의 RC카 뒤에 있는\n풍선을 터뜨리면 이기는 게임을 만드려고 해"
dh "그러니 [player_name], 정이주는 RC카 조립을 좀 해줘"
"넵 알겠습니다"
e "ㄴ...네...!"
hide dh with dissolve
"[몇분 후]"
"휴 다 조립했다!"
"동아리선배1" "조립 다 했으면 우리 경기장 만드는 것 좀 도와주라!"
"넵 알겠습니다!"
"우드락을 이용해서 경기장을 만든다."
"동아리선배2" "[player_name]! RC카 나사가 헐거워!"
"앗 넵! 다시 하겠습니다!"
if ejoo.y_point==3:
    "어? 여기있던 드라이버가 어디갔지?"
    show ejoo_uniform balloon with dissolve
    "이주야, 여기 드라이버 못봤어?"
    show ejoo_uniform idle with dissolve
    e "네?? 전 지금 풍선 부는 거 도와주고 있어서 못봤어요..."
    show ejoo_uniform bingbing with dissolve
    e "으윽...어지러워..."
    "흠... 어디로 갔지...?"
hide ejoo_uniform
"[몇시간후 ]"
show dh scream with dissolve
dh "좋았어 모두들 수고했어! 내일 있을 축제 열심히 해보자!"
hide dh with dissolve
"동아리 부원들" "와아아아아아!"
"와아아아아!"
show ejoo_uniform idle
e "ㅇ... 와아!!"
scene black
"[축제 당일]"
scene computerroom
show ejoo_uniform idle with dissolve
e "조종은 이 휴대폰으로 조종하시면 되시고"
e "상대방의 RC카 뒤에 있는 풍선을 터뜨리시면 됩니다."
"이주야 부스운영 잘하고 있었어?"
if ejoo.y_point == 3:
    show ejoo_uniform idleh with dissolve
    e "ㄴ...넵!"
else:
    e "ㄴ...네"
e "아... 선배 혹시 이따가 공연 누구랑 보러 가세요?"
"아... 나도 부스 운영하느라 공연시작시간에 못가서"
"친구들이 날 다 버렸어..."
"그래서 같이 갈 사람이 없어서 안 갈려고..."
if ejoo.y_point == 3:
    show ejoo_uniform idleh with dissolve
    e "그럼 선배 저랑 보러가실래요?"
else:
    e "오 저돈데! 그럼 선배 저랑 보러가실래요?"

#ejoo4
menu:
    "그래!":
        show ejoo_uniform idleh with dissolve
        "ㅎㅎ 그럼 이따가 같이 가요!"
        $player.plus(ejoo)
        $ejoo.y_plus()
    "싫은데?":
        show ejoo_uniform sweat with dissolve
        e "아..ㅎㅎ"
        e "알겠습니다ㅎㅎ;"
        $player.minus(ejoo)
scene black
"[몇시간후]"
if ejoo.y_point == 4:
    scene sol
    show ejoo_uniform idleh
    e "선배 빨리 가요!"
    "그래그래"
else:
    "이제 공연이나 보러 가볼까...?"
    scene sol
if ejoo.y_point == 4:
    show ejoo_uniform smile with dissolve
    e "선배 너무 재밌어요!"
    "그러게! 다들 연습 엄청 했나봐!"
    hide ejoo_uniform
    jump selection1
    return
"오, 공연 되게 열심히 하네!"
"근데 혼자 보니까 좀..."
"외로운 걸...?"
"그냥 이주랑 같이 볼 걸..."
"하"
scene black
"그렇게 축제가 끝났고"
"방학이 시작되었다."
jump start2
return

label selection1:
"진행자" "공연은 재밌게 보셨나요?"
"네----!"
"진행자" "하하, 다행입니다."
"진행자" "아, 그리고 저희들이 공연을 보시는 분들을 위해\n작은 이벤트를 준비했습니다."
"진행자" "아까 공연장으로 들어오시기 전에 번호표 다 받으셨죠?"
"네----!"
"진행자" "저희가 번호추첨을 통해 당첨되신 분께 소정의 상품을 드릴 예정입니다!"
"상품...?"
"진행자" "자, 뽑아보겠습니다!"
"진행자" "..."
"진행자" "24번!"
"오! 나다!"
"진행자" "당첨되신 분은 이 위로 올라와 주세요!"
show ejoo_uniform idle with dissolve
e "선배 빨리 올라가보세요!"
"응, 알겠어!"
hide ejoo_uniform
"터벅터벅"
"진행자" "네 아주 잘생긴 분이 당첨되셨네요!"
"진행자" "성함이 어떻게 되시죠?"
"아... [player_name]입니다"
"진행자" "넵! [player_name]씨가 당첨되신 선물은 바로"
show bear with dissolve
"진행자" "이 곰인형입니다!"
hide bear
"진행자" "축하드립니다!"
show ejoo_uniform idle
e "선배 축하드려요!\n곰인형 너무 귀여운 것 같아요!"

#ejoo5
menu:
    "ㅎㅎ앙기모띠 너 절대 안 주지ㅋㅋ":
        e "좋아하시는 모습 보니까 저도 좋네요ㅎㅎ;"
        "ㅎㅎㅎㅎㅎ"
        $player.minus(ejoo)
    "이주야, 너 줄게.":
        show ejoo_uniform idleh
        e "네?"
        show ejoo_uniform shadowh with dissolve
        e "ㄱ... 감사합니다..."
        "ㅎㅎ"
        $player.plus(ejoo)
        $ejoo.y_plus()
scene black
stop music
"그렇게 축제는 끝이나고"
"방학이 시작되었다."
call screen lovePoint
jump start2
return

label start2:
scene room_morning
play music "audio/bored.mp3" loop
hide black with dissolve
"하암... 방학인데 지루하넴..."
show mom angry
m "[player_name]! 빨리 일어나!"
"아 왜요?"
m "오늘 할머니댁 가는 날이잖아!"
"아 그래요?"
"몰랐넹ㅎㅎ"
m "빨리 씻어!"
"네~"
scene black
hide room_morning with dissolve
"[몇시간 후]"
scene countryside
hide black with dissolve
"[할머니댁]"
"할머니 저 왔어요~~"
show grandmother smile with dissolve
g "호호 우리 손자 왔어~?"
g "호호 내새끼~"
"ㅎㅎㅎㅎ"
g "어여 들어와~"
"네~"
scene countrysideroom
hide countryside with dissolve
show grandmother smile with dissolve
g "이 할미가 손주를 위해서 특별히 선물을 준비했지"
"선물이요? ㅎㅎ뭘까"
hide grandmother
show pants with dissolve
g "자 어떠냐 이쁘지?"
hide pants
show grandmother smile with dissolve
g "할미가 예전부터 옷쪽에 감각이 좋아어~ 빨리 입어봐라!"
menu:
    "입어본다":
        "'뭐 마주칠 사람도 없으니까...'"
        "와 할머니 저한테 딱 맞아요~"
        g "호호 다행이네~"
        g "어우 우리 똥강아지 태가 사네 태가 살어!"
        "ㅎㅎ 할머니 감사합니다~"
        g "그려그려~"
        $player.m_minus()
        "[매력포인트가 감소하였습니다]"
    "거절한다":
        "아 할머니 이게 뭐예요;"
        show grandmother question with dissolve
        g "잉? 마음에 안 드냐?"
        "전 바지는 많아서 더이상 필요 없단 말이예요~"
        show grandmother angry
        g "예끼 이놈! 할머니가 주면 감사하다고 받지못할망정!"
        show grandmother smile
        g "이라고 말할 순 없지!"
        g "그럴 줄 알고 이 할미가 다른 선물도 준비했다!"
        "진짜요?"
        "뭔데요 뭔데요??"
        g "이 할미가 이 목걸이를 주마"
        hide grandmother
        show necklace with dissolve
        g "할아범이 가기 전에 매일 목에 걸던 건데 어떠냐?"
        "와 좋아요! 진짜 맘에 들어요!"
        "감사히 받겠습니다~"
        hide necklace
        show grandmother smile
        g "오냐~"
        $player.m_plus()
        "[매력포인트가 증가했습니다.]"
g "자, 그러면..."
"어머니~~"
show grandmother question
g "아이고 벌써 막내들이 도착했나 보다!"
scene black with dissolve
"친척들이 도착하고 서로 얘기를 하며 밤이 되어간다..."
scene countrysidedinner with dissolve
"친척들" "(왁자지껄)"
"'흠... 아이스크림이 먹고 싶은뎅...'"
"할머니! 여기 가까운 슈퍼가 어딨어요?"
show grandmother question with dissolve
g "잉? 슈퍼는 버스타고 30분은 가야되는디?"
"'흠...'"
"'아빠는 술마셔서 운전 못하시고...'"
"'나 혼자 버스타고 가야겠다'"
scene black with dissolve
"버스를 타고 슈퍼로 간다."
scene super with dissolve
"히히 아이스크림 뭐먹지?"
menu:
    "비비빅":
        "이거 먹어야겠다!"
        $player.m_minus()
        scene countryside_nightroad with dissolve
        "집으로 돌아가려고 버스정류장으로 가던 중..."
        "???" "히끅...히끅"
        "뭐지...? 저기서 누군가 우는데?"
        "???" "으아아아아앙ㅠㅠㅠㅠ"
        "저기요 괜찮으세요?"
        "앗!"
        "나나?"
        show nana_c2 crying with dissolve
        n "[player_name]군?ㅠㅠㅠ"
        "너 여기서 왜 울고 있어?"
        n "할머니댁에 놀러왔는데..."
        n "잠깐 수퍼가려고 하다가"
        n "길을 잃었어ㅠㅠㅠ"
        n "지갑도 잃어버리고"
        n "휴대폰도 꺼졌어ㅠㅠㅠㅠㅠ"
        "어우 저런..."
        jump selection3
        return
    "쌍쌍바":
        "이걸로 먹어야징"
        $player.m_plus()
        scene countryside_nightroad with dissolve
        "집으로 돌아가려고 버스정류장으로 가던 중..."
        "???" "히끅...히끅"
        "뭐지...? 저기서 누군가 우는데?"
        "???" "으아아아아앙ㅠㅠㅠㅠ"
        "저기요 괜찮으세요?"
        "앗!"
        "나나?"
        show nana_c2 crying with dissolve
        n "[player_name]군?ㅠㅠㅠ"
        "너 여기서 왜 울고 있어?"
        n "할머니댁에 놀러왔는데..."
        n "잠깐 수퍼가려고 하다가"
        n "길을 잃었어ㅠㅠㅠ"
        n "지갑도 잃어버리고"
        n "휴대폰도 꺼졌어ㅠㅠㅠㅠㅠ"
        "어우 저런..."
        jump selection4
        return

label selection3:
scene teeth with dissolve
"그때 나나는 [player_name]의 이 사이에 낀\n비비빅 팥을 발견한다."
scene countryside_nightroad with dissolve
show nana_c2 idle with dissolve
n "[player_name]군... 이에 팥 꼈어..."
"아, 그래?"
"쮸왑쮸왑 쩝쩝 쯉쯉"
"어때 이제 떼졌지?"
show nana_c2 disgusting with dissolve
n "ㅇ...응..."
"[매력포인트가 감소했습니다.]"
$player.minus(nana)
jump start3
return

label selection4:
"나나야 쌍쌍바 먹을래?"
"쌍쌍바 한 쪽을 나나에게 준다"
show nana_c2 idleh with dissolve
n "ㄱ... 고마워 [player_name]군...///"
"[매력포인트가 증가했습니다.]"
$player.plus(nana)
jump start3
return

label start3:
"흠..."
"그러면 일단 우리 할머니댁으로 갈래?"
"나도 잠깐 아이스크림 사러 나온 거라 휴대폰을 놓고 와서"
"가서 너네 부모님한테 연락해보자"
show nana_c2 idle
n "응! 알겠어!"
"어디보자... 버스가..."
"앗!"
n "왜그래 [player_name]군?"
"버스가"
"끊겼어"
scene black with dissolve
scene countryside_bridge
hide black with dissolve
"터벅터벅"
"'집에 얼마나 더 걸어야 도착하려나...'"
"그러고보니"
"나나는 할머니댁이 여기인 거 보면"
"나나는 어머니랑 아버지중 어느분이 한국분이셔?"
show nana_c2 idle
n "아빠가 한국사람!"
n "아빠가 일본여행가서 엄마 만났대!"
n "그때 한 눈에 반했대!"
"아아 그렇구나"
"오 여기 다리가 있네"
n "그러게! 꽤 높다! 저 밑에 물고기 있을까?"
show nana_c2 back with dissolve
"그때 나나의 머리 뒤에 벌레가 붙어있다"
menu:
    "잡아준다":
        show nana_c2 backclap with vpunch
        play sound "audio/jjak.mp3"
        "짝!"
        show nana_c2 idle
        n "히익! 갑자기 뭐야?"
        "아아 등 뒤에 벌레가 있어서..."
        show nana_c2 idleh
        n "!"
        n "ㄱ... 고마워 [player_name]군..."
        n "난 벌레 아무렇지 않게 잡는 남자가 멋지더라..."
        "아 ㄱ... 그래?ㅎㅎ"
        $player.plus(nana)
    "말해준다":
        "나나야 등 뒤에 벌레;"
        show nana_c2 idle with dissolve
        n "응?"
        show nana_c2 scream with vpunch
        stop music
        n "꺄아아아앍!"
        "어어!"
        "벌레를 보고 놀란 나나는 깜짝놀라 넘어져\n다리 밑으로 떨어질 뻔한 상황이다."
        play music "audio/sadmusic.mp3" loop
        scene nana_diving1 with dissolve
        "나나야!"
        n "[player_name]군..."
        n "나 무서워..."
        "아니야 기다려 내가 들어올려줄게!"
        "하지만 운동을 하지않고 집에서 게임만 한 나의 팔로\n나나를 들어올리기에는 역부족이였다."
        "으윽..."
        scene nana_diving2
        hide nana_diving1 with dissolve
        n "[player_name]군..."
        "말하지마! 들어올려줄게!"
        n "만난 지 얼마 안 됐지만"
        "그만! 으윽!"
        n "외국에서 온 나한테 친절히 대해줘서"
        scene nana_diving3
        hide nana_diving2 with dissolve
        n "고마웠어"
        "으윽! 왜 그런 말을 하는 거야! 들어올릴 수 있어 기다려!"
        n "[player_name]군 잘못이 아니야"
        "으아아아악!"
        n "잘지내"
        scene nana_diving4
        hide nana_diving3 with dissolve
        "나나는 밑으로 떨어졌다."
        "안 돼!!!"
        scene black
        "그렇게 나나는 그날 이후로"
        "볼 수 없었다."
        scene theend
        hide black with dissolve
        "두 번째 엔딩"
        return
scene countryside_night
"어, 나나야 다왔다 저기가 우리 할머니댁이야!"
show grandmother angry
g "우리 똥강아지 왜 이제 온 거여!"
show grandmother question
g "잉? 옆에 처자는 누구여?"
show grandmother question at right
show nana_c2 idle at left with dissolve
n "ㅇ... 안녕하세요!"
n "[player_name]군의 친구 야부키 나나입니다"
"할머니 이게 어떻게 된 거냐면..."
scene countryside_night with dissolve
"상황설명을 한다."
show grandmother smile at right with dissolve
g "호호 그래그래 일단 부모님께 전화하려무나"
show nana_c2 idleh at left with dissolve
n "네!"
hide nana_c2 with easeoutleft
"나나는 전화하러 간다."
g "그래서... 여자친구냐?"
"아 아니야 할머니! 그냥 같은 반 친구야"
show grandmother angry
g "예끼! 할멈을 속이려고 들어!"
show grandmother smile
g "잘해줘라 저런 처자 보기 힘들어!"
"아,, 알겠어"
show nana_c2 idleh at left with easeinleft
n "부모님이 이쪽으로 오신대!"
"오 잘됐다!"
scene countryside_night with dissolve
"그렇게 나나는 부모님의 차를 타고 갔다."
show nana_c2 idle with dissolve
n "[player_name]군! 학교에서 봐~!"
"그래그래"
stop music fadeout 2.0
scene black with dissolve
"이렇게 길고도 짧은 방학이 끝나고..."
"2학기가 시작되었다."
call screen lovePoint
play music "audio/normal.mp3" loop
scene computerroom with dissolve
show dh scream
dh "자, 이걸로 올해 동아리활동은 끝이야!"
hide dh scream with dissolve
"수고하셨습니다!"
show ejoo_uniform idle with dissolve
e "ㅅ... 수고하셨습니다!"
"이주야 동아리활동 수고많았어!"
show ejoo_uniform idleh with dissolve
e "ㄴ... 넵 선배도요...!"
show ejoo_uniform idle
e "아, 선배 혹시 이번주 주말에 뭐하세요...?"
"나?"
"음..."
"아무것도 안 하는데?"
show ejoo_uniform idleh
e "ㄱ... 그럼 저랑 영화보러 가실래요...?"
e "ㄱ... 같이 갈 친구가 없어서..."
menu:
    "하긴... 이주는 아싸니까 내가 가줘야겠다ㅋㅋ":
        show ejoo_uniform sweat
        e "아...ㅎㅎ 그럼 주말에 영화관에서 만나요"
        "그래~"
        $player.minus(ejoo)
    "흔쾌히 받들겠습니다 공주님":
        show ejoo_uniform idleh
        e "ㄱ... 공주님이라뇨...!"
        "ㅋㅋ그냥 농담해본 거야~"
        "공주님처럼 이쁜 것도 있긴 하고...ㅎ"
        e "!"
        show ejoo_uniform shadowh with dissolve
        e "ㄱ... 그러면 주말에 영화관에서 만나요..."
        "알겠어~"
        $player.plus(ejoo)
        $ejoo.y_plus()
scene black with dissolve
"[주말]"
scene cgv_roby with dissolve
"휴 늦을 뻔 했다..."
e "ㅅ... 선배~"
"어어 이주야!"
show ejoo_c1 idle with easeinleft
e "시간에 딱 맞게 오셨네요!"
"ㅎㅎ 사실 늦을 뻔 했어"
show ejoo_c1 smile
e "저도 오늘 늦을 뻔 했어요!ㅋㅋ"
show ejoo_c1 idle
e "그럼 들어가볼까요?"
"잠깐 팝콘 사고 들어가야지~"
show ejoo_c1 surprise
e "아 맞네요!"
scene cgv_popcorn with dissolve
"미소지기" "팝콘 여깄습니다~"
menu:
    "계산한다.":
        "카드를 꺼내며"
        "여기요."
        show ejoo_c1 idle with dissolve
        e "ㅅ... 선배 제가 낼게요!"
        "쉿."
        show ejoo_c1 idleh
        e "!"
        show ejoo_c1 shadowh with dissolve
        e "팝콘 ㄱ... 감사합니다..."
        "그래."
        $player.plus(ejoo)
        $ejoo.y_plus()
    "이주가 계산하게 한다.":
        "이주야 뭐해!"
        show ejoo_c1 idle
        e "ㄴ... 네?"
        "빨리 계산하라고!\n너가 영화보자고 했잖아!"
        show ejoo_c1 shadow with dissolve
        e "아...네..."
        $player.minus(ejoo)
scene cgv with dissolve
"와 재밌겠다"
"그치 이주야?"
show ejoo_c1 idle
e "ㄴ... 네!"
hide ejoo_c1 with dissolve
stop music fadeout 2.0
"영화가 시작되고"
"키스하는 장면이 나온다."
"'와...'"
"톡"
"응?"
scene cgv1 with dissolve
"이주와 손끝이 닿았다.\n어떻게 할까?"
menu:
    "꼬집는다.":
        scene cgv2
        "에잇!"
        e "악!"
        scene cgv
        show ejoo_c1 idle with dissolve
        "내 손에 니 더러운 손 닿지마!"
        show ejoo_c1 shadow with dissolve
        e "..."
        e "죄송합니다..."
        $player.minus(ejoo)
    "잡는다.":
        scene cgv3 with dissolve
        "스윽..."
        scene cgv with dissolve
        show ejoo_c1 idleh with dissolve
        e "...!"
        show ejoo_c1 shadowh
        "///"
        "영화관 안은 에어컨을 빵빵하게 틀어줬지만"
        "마치 밖에 나온 것마냥 더웠다."
        "이게..."
        "청춘인가...?"
        $player.plus(ejoo)
        $ejoo.y_plus()
scene black with dissolve
play music "audio/normal.mp3" loop
"영화가 끝나고..."
scene cgv_roby with dissolve
show ejoo_c1 idle with dissolve
e "선배 오늘 영화 재밌었어요!"
"그러게 재밌었다."
show ejoo_c1 idleh with dissolve
e "선배... 이제 밥 먹으러 가실래요...?"
"ㄱ... 그럴까?"
"ㅁ... 뭐먹지...?"
"앗!"
show ejoo_c1 idle
e "왜그러세요 선배?"
"미안해 이주야 나 먼저 가봐야될 것 같아!"
show ejoo_c1 surprise
e "ㅁ... 무슨 일이신데요...?"
"집에 가서 달팽이 밥줘야 돼!"
show ejoo_c1 shadow with dissolve
e "아..."
"그럼 나중에 보자!"
if ejoo.h_point >= 100:
    show ejoo_c1 idleh
    e "ㅈ... 잠시만요!"
    e "10월 10일에 우리 만나요!"
    "? ㅇ... 알겠어 그럼 나중에 보자!"
    e "ㄴ... 네!"
    show ejoo_c1 shadowh with dissolve
    e "얼마 안 남았어..."
else:
    show ejoo_c1 idle
    e "ㄴ...네...!"
scene black with dissolve
"[몇주후]"
call screen lovePoint
scene classroom with dissolve
"벌써 중간고사기간인가..."
show friend_uniform idle with easeinright
f "야 [player_name]! 이번엔 공부 안 하냐?"
"할 거야..."
"음..."
"야 너 독서실 다니냐?"
show friend_uniform question
f "뭔소리야; 내가 공부하는 애로 보이냐?"
hide friend_uniform with dissolve
"에휴 말을 말자..."
"독서실을 다니면 아무래도 집중이 잘 될 것 같은데..."
"아 맞다 걔가 있었지!"
show hone_uniform idle with dissolve
h "이번엔 또 뭐야?"
"야 너 독서실 다니지!"
h "응 왜?"
"독서실 어때? 집중 잘 돼?"
show hone_uniform question
h "당연한 걸 왜 묻고 있어?;"
"야야 나도 너 다니는 독서실 다닐래!"
show hone_uniform angryh with dissolve
h "ㅁ...뭐? ㅇ... 왜?"
menu:
    "중간고사 때문이지; 너 보러 가는 거 아니다;":
        show hone_uniform angry
        h "ㄴ... 누가 뭐래?"
        h "오든지 말든지 난 관심 없거든?"
        "뭐야... 갑자기 왜이래?"
        h "아 몰라! 너 저리가! 꼴보기 싫어!"
        "에휴..."
        $player.minus(hone)
    "너가 있어서.":
        h "!"
        show hone_uniform shadowh with dissolve
        h "뭐... 오면 나도 좋긴 하지...///"
        h "나 다니는 독서실 올 거면 빨리 와..."
        "알겠어 금방 갈게! 오늘 갈게!"
        $player.plus(hone)
scene black with dissolve
"[방과후]"
scene studyroom with dissolve
"여기가... 독서실..."
"공부 잘 되겠는 걸?"
"???" "쉿!"
"아... 죄송합니다..."
"좋았어! 공부해서 중간고사 박살내겠어!"
"[한시간 후]"
"내가 박살날 것 같다..."
"톡톡"
"응?"
show hone_uniform idle with dissolve
h "밖으로 나와(속닥속닥)"
scene studyroom_out with dissolve
show hone_uniform idle with dissolve
h "어때 독서실에서 하니까 공부는 할 만해?"
"똑같이 힘든데... 왜이러지?"
show hone_uniform bsmile
h "ㅋㅋㅋㅋㅋ독서실에서 공부한다고 돌머리가 갑자기\n집중이 되겠어?"
"아, 조용히 해;"
h "ㅋㅋㅋㅋㅋ 수고하고 난 다시 들어가서 공부한다~"
"그러든지..."
hide hone_uniform with easeoutleft
"하... 공부하기 싫다..."
scene vendingmachine with dissolve
"어? 자판기네?"
"흠... 김혜원한테 뭐라도 사다줄까...?"
menu:
    "사다준다.":
        "그래... 저번에 공부도 가르쳐줬으니까 이정도는 사줘야지"
        "근데 뭐를 사줘야되지..?"
        menu:
            "쌍화탕":
                "역시 김혜원은 쌍화탕이지!"
                $player.plus(hone)
                jump selection5
                return
            "ZICO":
                "걘 코코넛 좋아하니까 이걸로 사줘야겠다!"
                $player.minus(hone)
                jump selection6
                return
    "안 사준다.":
        "어우; 걘 뭐 사줄 가치조차 없어;"
        "내가 마실 커피나 뽑아가야겠다~"
        scene studyroom
        "저 멀리 김혜원이 보인다."
        "톡톡"
        show hone_uniform question with dissolve
        h "?"
        "옴뇸뇸~ 커피 개꿀맛~(속닥속닥)"
        show hone_uniform shadow
        h "(빠직)"
        stop music fadeout 2.0
        show hone_uniform bsmile with dissolve
        h "ㅎㅎ"
        "(뭐지... 왜 갑자기 기분나쁘게 웃지?)"
        h "죽어."
        play sound "audio/jap.mp3"
        show hone_uniform idle with vpunch
        scene black with dissolve
        "나의 고간에 매우 큰 충격이 가해졌고..."
        "이 날 이후로... 김혜원한테 깝치지 말기로 했다..."
        if hone.h_point >= 100:
            "깨어났을 때는 내 휴대폰으로 문자하나가 와있었다."
            h "10월 10일에 나와."
        jump start4
        return

label selection5:
scene studyroom with dissolve
"저 멀리 김혜원이 보인다..."
"톡톡"
show hone_uniform idle with dissolve
h "?"
"야, 먹어."
"쌍화탕을 건네준다."
h "뭔ㄷ..."
show hone_uniform idleh with dissolve
h "[player_name]...기억해줬구나..."
h "5살 때 멍청했던 난... 너가 준 쌍화탕을 먹고 엄친딸로 변할 수 있었어..."
h "나에겐 아주 의미가 깊은..."
h "[player_name]... 귀줘봐..."
scene hone_whisper1 with dissolve
h "10월 10일에 나와. 알겠지...?"
scene hone_whisper2 with dissolve
"ㅇ... 알겠어!"
scene studyroom
show hone_uniform idleh
h "ㅎㅎ"
stop music fadeout 2.0
jump start4
return

label selection6:
scene studyroom with dissolve
"저 멀리 김혜원이 보인다..."
"톡톡"
show hone_uniform idle with dissolve
h "?"
"야, 먹어."
"ZICO를 건네준다."
show hone_uniform question
h "야 너 장난하냐?"
"ㄴ...너 코코넛 좋아하잖아!"
h "코코넛젤리를 좋아하는 거지 누가 ZICO를 먹어!"
show hone_uniform shadow with dissolve
h "하... 너라면 쌍화탕 사다줄 거라고 생각했는데..."
"응? 뭐라고 했어?"
h "에휴 됐어..."
show hone_uniform angry
h "빨리 가서 공부나 해!"
"ㅇ... 알겠어..."
stop music fadeout 2.0
if hone.h_point >= 100:
    show hone_uniform idle with dissolve
    h "야 잠깐만"
    h "이리로 와봐."
    "왜?"
    h "너 10월 10일에 뭐해?"
    if ejoo.h_point >= 100:
        "그날에는 이주 만나기로 했는..."
    else:
        "아무일도 없는..."
    scene hone_whisper1 with dissolve
    h "그럼 그때 나랑 만나."
    scene hone_whisper2 with dissolve
    "ㅇ... 알겠어...!"
    scene studyroom
    show hone_uniform idleh
    h "ㅎㅎ"
    jump start4
    return
else:
    jump start4
    return

label start4:
scene black with dissolve
"2학기 중간고사가 다가왔고"
"결과는"
"당연히 망했다."
call screen lovePoint
scene classroom with dissolve
play music "audio/hongdaemusic.mp3" loop
"[다음날]"
"하암... 등교시간 좀 늦춰주면 안 되나...?"
show hone_uniform angry with dissolve
h "그런 생각하지말고 일찍 일어나면 되잖아!"
"아침부터 또 잔소리..."
h "뭐?"
"아무말도 안 했어ㅎㅎ"
"근데... 오늘은 뭔가 좀 조용한 거 같은 느낌이..."
"나나는?"
show hone_uniform question
h "그러게? 나나 원래 제일 일찍 오는데"
hide hone_uniform
show teacher scream
t "자, 다들 조용! 자리에 가서 앉아!"
"선생님~ 나나 왜 학교 안 왔어요?"
show teacher idle
t "나나는 오늘 아침에..."
t "교통사고를 당해서 병원에 입원했다."
"네?!"
hide teacher
show hone_uniform idle with dissolve
h "나나가 교통사고를 당했다니..."
h "야 [player_name], 나나 병문안 갈 거지?"
"당연히 가야지..."
h "그럼 내가 어디 병원인지 물어볼테니까\n학교 끝나고 가자."
"어어 알겠어."
scene black with dissolve
"병문안 가는 길"
scene bonjook with dissolve
"흠... 죽을 사갈까?"
menu:
    "사간다.":
        "그래, 죽정도는 당연히 사가야지."
        scene bonjook_inside with dissolve
        "와... 종류 엄청 많네?"
        "뭘 사가야되지?"
        menu:
            "쇠고기미역죽":
                "음! 무난하게 이걸로 사가야겠다!"
                "이걸로 주세요!"
                $player.minus(nana)
                jump selection7
                return
            "진품쇠고기육개장죽":
                "음! 역시 매콤한 게 낫지!"
                "이걸로 주세요!"
                $player.plus(nana)
                jump selection8
                return
    "안 사간다":
        "에이 돈 아깝게 뭔 죽이야~"
        "마음만 챙겨가면 되지!"
        $player.minus(nana)
        jump selection9
        return

label selection7:
show hospital_roby with dissolve
"헉헉..."
"나나의 병실이..."
"여기다!"
show hospital_morning with dissolve
"나나야!!!!!"
show nana_patient idle at right with dissolve
n "[player_name]군!"
show hone_uniform angry at left with dissolve
h "왜이제야 온 거야!"
"ㅎㅎ 미안미안"
"하지만 다 이유가 있었다고~"
show hone_uniform idle with dissolve
n "응? 이건 뭐야?"
"나나를 위해 특별히 죽을 준비해왔지~"
show nana_patient surprise with dissolve
n "정말?"
show nana_patient smile with dissolve
n "와아 나 오늘 한 끼도 못먹었는데!"
n "고마워 [player_name]군!"
"죽포장을 연다."
show nana_patient idle
n "쇠고기미역죽...?"
show nana_patient vomiting
n "우웁;"
hide nana_patient with easeoutleft
"나나는 자리를 박차고 일어나 화장실로 뛰어간다."
"ㅇ... 왜저러지?!"
show hone_uniform angry
h "[player_name] 이 바보야!"
h "나나 어렸을 때 미역먹고 토한 기억이 있어서"
h "미역만 보면 구역질이 올라온다고\n같이 밥 먹을 때마다 나나가 얘기했잖아!"
"앗... 그랬었어...?"
show nana_patient idle at right with easeinright
"나나가 다시 온다."
"나나야! 괜찮아?"
"미안해! 너가 미역 못먹는다는 걸 까먹고 있었어..."
show nana_patient smile with dissolve
n "ㅎㅎ 괜찮아 [player_name]군..."
h "에휴... [player_name]바보..."
jump start5
return

label selection8:
show hospital_roby with dissolve
"헉헉..."
"나나의 병실이..."
"여기다!"
show hospital_morning with dissolve
"나나야!!!!!"
show nana_patient idle at right with dissolve
n "[player_name]군!"
show hone_uniform angry at left with dissolve
h "왜이제야 온 거야!"
"ㅎㅎ 미안미안"
"하지만 다 이유가 있었다고~"
show hone_uniform idle with dissolve
n "응? 이건 뭐야?"
"나나를 위해 특별히 죽을 준비해왔지~"
show nana_patient surprise with dissolve
n "정말?"
show nana_patient smile with dissolve
n "와아 나 오늘 한 끼도 못먹었는데!"
n "고마워 [player_name]군!"
"죽포장을 연다."
show nana_patient idle with dissolve
n "아닛? 이 죽은?!"
show hone_uniform question with dissolve
h "왜? 무슨 죽인데?"
show nana_patient surprise
n "진품쇠고기육개장죽이잖아?!?!"
"(뿌듯)"
show nana_patient smile
n "병원밥만 먹다보면 얼큰한 게 먹고싶었는데"
n "역시 [player_name]군이야! 초다이스키!!"
"나나가 좋아하니까 나도 좋다ㅎㅎ"
jump start5
return

label selection9:
show hospital_roby with dissolve
"헉헉..."
"나나의 병실이..."
"여기다!"
show hospital_morning with dissolve
"나나야!!!!!"
show nana_patient idle at right with dissolve
n "[player_name]군!"
show hone_uniform angry at left with dissolve
h "왜이제야 온 거야!"
"ㅎㅎ 미안미안"
"하지만 다 이유가 있었다고~"
show hone_uniform idle
"김혜원, 나나" "무슨 이유?"
show nana_patient surprise with dissolve
n "앗 설마! 그 손에 든 것은...??"
"아ㅎㅎ"
"오늘 밥을 못먹어서ㅎㅎ\n나 먹을 삼각김밥 좀 갖고왔어ㅎㅎ"
show nana_patient shadow with dissolve
n "..."
show hone_uniform shadow with dissolve
h "[player_name]... 넌 진짜..."
show hone_uniform angry with vpunch
h "죽어!"
scene black
"그렇게 김혜원한테 죽을 듯이 맞았다..."
jump start5
return

label start5:
scene hospital_morning
show hone_uniform question at left with dissolve
show nana_patient idle at right with dissolve
h "나나야 그래서 어쩌다가 사고가 난 거야?"
n "그게..."
n "오늘 아침 버스를 타려고 기다리고 있었는데"
n "그날따라 유난히 사람이 많았어..."
n "근데 차가 지나가는 타이밍에"
n "누가 갑자기 나를 밀치는 바람에..."
show nana_patient smile
n "사고가 났지 모야ㅎㅎ"
show hone_uniform angry
h "뭐?? 완전 미친 거 아니야?"
h "경찰에 신고해야 되는거 아니야??"
"맞아 이건 경찰에 신고해야될 것 같은데??"
n "ㅎㅎ 아니야"
n "그날 사람이 많아서 사람들끼리 지나가다가 실수로 밀었나봐"
n "난 괜찮아ㅎㅎ"
show hone_uniform idle
h "정말... 나나는 사람이 너무 좋아서 탈이라니까..."
"인정!"
n "ㅎㅎ"
show nana_patient idle
n "이렇게 모였으니까 다들 게임이라도 할래?"
"오, 좋다! 어몽어스 ㄱ?"
show nana_patient smile
"나나, 김혜원" "ㄱㄱ!"
scene black with dissolve
"그렇게 저녁이 될 때까지 다같이 어몽어스를 했다..."
scene hospital_night
show hone_uniform idle at left with dissolve
h "그럼 이제 우리 가볼게!"
"나도 가봐야겠다"
show nana_patient smile at right with dissolve
n "그래 다들 조심히 가!"
scene hospital_desk with dissolve
show hone_uniform idle with dissolve
h "[player_name], 독서실 갈 거지?"
"응 가야지..."
"아!"
show hone_uniform question
h "왜그래?"
"나나 병실에 휴대폰 놓고 왔어!"
"잠깐만 기다려줘!"
show hone_uniform idle
h "에휴... 저 띨띨이..."
if hone.h_point >= 100:
    show hone_uniform shadowh with dissolve
    "그래서 좋은 거지만..."
show hone_uniform angry
h "빨리 갔다와!"
scene hospital_roby with dissolve
"빨리 가지고 나오..."
"응? 무슨 소리지?"
n "[player_name]군...ㅈㅇ..."
"내 이름이 들린 것 같은데?"
"귀를 문에 더 가까이 댄다."
stop music fadeout 2.0
scene hospital_night with dissolve
n "[player_name]군... 좋아해..."
n "처음 봤을 때부터... 잊을 수 없어..."
n "내 마음 한 칸을 차지하고 있는 걸..."
show nana_patient back with dissolve
n "10월 10일에... 꼭..."
"나나야?"
show nana_patient surpriseh
n "?! [player_name]군?!"
n "왜 다시..."
"아, 휴대폰을 놓고와서..."
show nana_patient shadow with dissolve
n "아..."
"..."
"그럼 이만 가볼게!"
"가려는 순간"
"나나가 나의 손을 잡는다."
"나나야?"
show nana_patient shadowh
n "저기..."
show nana_patient surpriseh with dissolve
n "10월 10일에 뭐해...?"
menu:
    "선약 있는데?":
        show nana_patient smile
        n "아...ㅎㅎ 알겠어..."
        "무슨 일인데?"
        n "아무것도 아니야ㅎㅎ"
        "그럼 만약에 그 날에 시간되면 연락할게"
        n "응 알겠어ㅎㅎ"
        n "잘 가 [player_name]군ㅎㅎ"
        "그래~"
        $player.minus(nana)
    "아무것도 안 해.":
        n "그러면 그 날에 나랑 만나자!"
        "ㅇ..어어 알겠어"
        show nana_patient smile
        n "ㅎㅎ 꼭이야!"
        n "잘 가~"
        "그래~"
        $player.plus(nana)
scene black with dissolve
"그렇게 시간이 흘러..."
"10월 10일이 되었다."
call screen lovePoint
scene room_morning with dissolve
"어떡하지..."
"얼떨결에 10월 10일에 이주, 김혜원, 나나한테 시간이 된다고 해버렸네..."
"하... 어떡하지..."
"긴 고민끝에..."
"정했다...!"
scene black
"[10월 10일]"

if ejoo.y_point == 8:
    jump ejoo_yending
    return
elif ejoo.h_point >= 100 and hone.h_point >= 100 and nana.h_point >= 100:
    jump multi_ending
    return
elif ejoo.h_point<100 and hone.h_point <100 and nana.h_point < 100:
    jump solo_ending
    return
elif ejoo.h_point >= 100:
    if ejoo.h_point >= hone.h_point:
        if ejoo.h_point >= nana.h_point:
            jump ejoo_ending
            return
        else:
            jump nana_ending
            return
    else:
        jump hone_ending
        return
elif hone.h_point >= 100:
    if hone.h_point >= nana.h_point:
        jump hone_ending
        return
    else:
        jump nana_ending
        return
elif nana.h_point >= 100:
    jump nana_ending
    return
else:
    jump solo_ending
    return

label ejoo_yending:
    scene ejooending with dissolve
    "아슬아슬하게 도착했다..."
    "앗 저기 보인다!"
    "여기야~"
    "???" "앗"
    play music "audio/horror.mp3" loop
    show ejoo_ending idle
    e "오셨어요 선배?"
    "어어 이주야"
    "오늘 왜부른 거야?"
    show ejoo_ending shadow with dissolve
    e "선배..."
    show ejoo_ending smile
    e "저희 처음 만났을 때 기억나요?"
    "당연히 기억나지!"
    "내가 그때 널 잡아줬잖아!"
    e "ㅎㅎ 맞아요"
    show ejoo_ending smileh with dissolve
    e "그때의 선배의 품... 따뜻했어요..."
    "하하 왜그래 갑자기ㅎㅎ"
    show ejoo_ending shadowh
    e "그날 이후로 제 머릿속이 이상해졌어요..."
    e "시도때도 없이 선배로 머릿속이 가득 차버렸죠..."
    e "그날 저는 느꼈어요..."
    show ejoo_ending 1
    e "갖고싶다."
    show ejoo_ending idle
    "이주야...?"
    show ejoo_ending smile
    e "선배! 급식실에서 제가 드렸던 베어브릭 잘 가지고 계시더라구요ㅎㅎ"
    "어어 그렇지..."
    show ejoo_ending y
    e "그때 선배가 저보고 다른 년들이랑"
    show ejoo_ending idle
    e "아..."
    show ejoo_ending smile
    e "죄송해요..."
    e "다른 선배들한테 그냥 동아리 후배라고 했을 때\n얼마나 상처받았는지 알아요?"
    "아 이주야 그게 아니..."
    "잠만..."
    "그 얘기는 널 만난 급식실 줄에서 한 게 아니고"
    "멀리 떨어진 자리에서 애들한테 말한 건데..."
    "너가 그 얘기를 어떻게 알아...?"
    show ejoo_ending idle
    e "아"
    show ejoo_ending smile
    e "베어브릭에 작은 도청기를 심어놨어요..."
    show ejoo_ending braveh
    e "좋아하는 사람이 멀리서도 하는 얘기를 듣고 싶어하는 건...\n당연하잖아요!"
    "뭐라고?"
    show ejoo_ending smileh
    e "아 그걸로 선배가 홍대가신다는 것도 알아서 따라갔어요!"
    show ejoo_ending idle with dissolve
    e "그런데..."
    show ejoo_ending 5
    e "다른 여자들이 선배한테 달라붙더라구요...?"
    show ejoo_ending idle
    "그럼... 그날 시선이 느껴졌던 건..."
    show ejoo_ending smileh
    e "네! 하루종일 멀리서 지켜봤어요...!"
    show ejoo_ending idleh with dissolve
    e "하지만 멀리서 바라보는 걸로는 성이 안 찼어요..."
    show ejoo_ending shadowh with dissolve
    e "더 큰... 선배의 한 부분을 갖고 싶었죠..."
    show ejoo_ending smileh
    e "때마침 동아리 축제준비때 선배가 드라이버를 쓰시고 계시더라구요!"
    show ejoo_ending 2
    e "선배의 땀이 잔뜩 묻은..."
    show ejoo_ending idle
    e "그래서"
    show ejoo_ending driver
    e "선배가 안 보는 사이에 훔쳤어요!"
    e "처음으로 선배를 가진 듯한 기분이였어요..."
    "이주야... 너..."
    show ejoo_ending smileh
    e "그런데 사람이란 게 욕심이 생기더라구요"
    show ejoo_ending 5
    e "더 큰..."
    show ejoo_ending idleh
    e "그래서 선배한테 만나자고 할려고 영화보러가자고 했는데"
    e "거기서 선배가 제 손을 잡았잖아요!"
    show ejoo_ending hand1 with dissolve
    e "이것봐요!"
    show ejoo_ending hand2
    e "그날 이후로 손 안 씻었어요!"
    e "매일 밤 이 손을 보며 선배를 떠올렸어요..."
    show ejoo_ending idle with dissolve
    e "그런데"
    show ejoo_ending y
    e "화장 떡칠한 갸루년이 선배한테 달라붙더라구요?"
    e "내 건데..."
    e "나만 가질 수 있는데..."
    show ejoo_ending idle
    e "그래서 아침에 사람이 많은 틈을 타"
    show ejoo_ending smileh
    e "밀어버렸어요."
    show ejoo_ending idle
    "정이주...넌 미쳤어..."
    show ejoo_ending smile
    e "죽일 각오로 밀친 건데 운이 좋게 안 죽었더라구요?"
    e "뭐 아쉽게 됐죠..."
    show ejoo_ending idle with dissolve
    e "선배... 이것 봐요..."
    e "전 선배한테 이렇게 진심을 다하고 있어요..."
    show ejoo_ending shadowh
    e "창피하지만..."
    show ejoo_ending braveh
    e "전 선배를 좋아해요!"
    show ejoo_ending surpriseh
    e "저랑 사귀실래요...?"
    menu:
        "넌 미쳤어.":
            show ejoo_ending smile
            e "하하"
    e "맞아요"
    e "전 선배한테 미쳤어요"
    show ejoo_ending idle
    e "살면서 이렇게 가지고 싶은 게 생긴 적... 처음이예요"
    show ejoo_ending braveh
    e "저랑 사귀게 되면 잘해줄게요!"
    e "매일 사랑해줄게요!"
    show ejoo_ending 1
    e "평생 나말고 다른 생각 안나게 해줄게!"
    show ejoo_ending idle
    e "아... 죄송해요..."
    show ejoo_ending shadowh with dissolve
    e "너무 흥분해서 저도 모르게 반말이..."
    show ejoo_ending idle
    e "그럼 선배 다시 말할 게요."
    show ejoo_ending smile
    e "저랑 함께 해줄래요?"
    menu:
        "싫어":
           ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
        "싫어":
            ""
    show ejoo_ending 7
    stop music
    e "왜요?"
    e "선배도 제가 싫어요?"
    e "싫은 거죠?"
    e "선배도 저 버리고 갈 거죠?"
    show ejoo_ending shadow with dissolve
    e "선배도 다른 사람이랑 똑같아."
    show ejoo_ending idle
    e "선배"
    hide ejoo_ending
    e ""
    e ""
    e ""
    show ejoo_ending y1
    play music "audio/scream.mp3"
    scene black
    scene theend with dissolve
    "여덟 번째 엔딩"
    return

label multi_ending:
    play music "audio/romantic.mp3" loop
    scene ending1 with dissolve
    "아슬아슬하게 도착했다..."
    "앗 저기 보인다!"
    "여기야~"
    "???" "앗"
    show hone_ending shadow at left with dissolve
    h "야 [player_name]... 이게 뭐하자는 거야?"
    show nana_ending shadow with dissolve
    n "[player_name]군... 왜..."
    show ejoo_ending at right with dissolve
    e "[player_name]선배... 왜 다른 사람까지..."
    show hone_ending idle
    show nana_ending idle
    show ejoo_ending idle
    "모두들 들어줘!"
    "난 사실 너네들이 날 왜 부른 지 알고있어"
    "나한테 고백하려고 했지?"
    show hone_ending surpriseh
    show nana_ending surpriseh
    show ejoo_ending surpriseh
    "김혜원,나나,정이주" "!"
    show hone_ending idle
    show nana_ending idle
    show ejoo_ending idle
    "나도 이런 짓을 한 게 잘못된 걸 알아..."
    "하지만!"
    "난 너네들이 다 소중해!"
    "너네들중에서 한 명을 고르다니..."
    "나머지 두 명한테는 너무 미안하다고!"
    "그래서 한 가지 방법을 떠올렸지..."
    "그건 바로..."
    "내가 너네들 전부와 사귀는 거야!"
    show hone_ending surpriseh
    show nana_ending surpriseh
    show ejoo_ending surpriseh
    "김혜원,나나,정이주" "뭣...!"
    "어때 이러면 모두가 행복해질 수 있어!"
    show hone_ending shadow
    h "[player_name]... 내가 너를 오랫동안 봐았지만..."
    h "이번 만큼은..."
    "(꿀꺽)"
    show hone_ending idle with dissolve
    h "ㄱ... 괜찮은 아이디어네...!"
    "!"
    show nana_ending braveh with dissolve
    n "나나도... [player_name]도 소중하지만\n다른 사람도 소중하니까..."
    show ejoo_ending shadowh with dissolve
    e "ㅈ...저는 [player_name]선배랑 사귈 수만 있다면..."
    "그럼 모두 동의한 거야?"
    show hone_ending smileh with dissolve
    h "그래"
    show nana_ending smileh with dissolve
    n "응!"
    show ejoo_ending smileh with dissolve
    e "네!"
    "모두들..."
    "사랑해!"
    scene black with dissolve
    "그렇게 나 [player_name]..."
    "세 명의 여친을 사귀게 된다..."
    scene theend with dissolve
    "일곱 번째 엔딩"
    return

label solo_ending:
    scene ending1 with dissolve
    "아슬아슬하게 도착했다..."
    "앗 저기 보인다!"
    "여기야~"
    "???" "앗"
    show friend_ending idle with dissolve
    f "야 너 또 아슬아슬했다?"
    "ㅎㅎ 미안~"
    "자 빨리 놀자!"
    scene black with dissolve
    "그렇다..."
    "나는 3명중 한 명을 택한다는 행동으로 인해"
    "선택받지 못한 두 명의 보복이 두려워"
    "아무도 만나지 않는다는 결정을 했다..."
    "이런 나의 행동이 이해되지 않는다면"
    "이 사실을 떠올리자"
    "나는 18년동안 모쏠이었다."
    "그 이유가 이것이다."
    play music "audio/endingmusic.mp3" loop
    scene theend with dissolve
    "여섯 번째 엔딩"
    return

label ejoo_ending:
    play music "audio/romantic.mp3" loop
    scene ending1 with dissolve
    "아슬아슬하게 도착했다..."
    "앗 저기 보인다!"
    "여기야~"
    "???" "앗"
    show ejoo_ending idle with dissolve
    e "ㅅ... 선배~!"
    "이주야 오늘 좀 이쁘네?"
    show ejoo_ending idleh with dissolve
    e "ㄱ... 감사합니다 선배..."
    "이주야 근데 오늘 왜 부른 거야?"
    show ejoo_ending shadow with dissolve
    e "그게요..."
    show ejoo_ending smile
    e "우선 좀 걸을까요...?"
    scene ending2 with dissolve
    show ejoo_ending idle with dissolve
    e "선배 저희 처음 만났을 때 기억나요?"
    e "그때 계단에서 안 넘어졌더라면 저희가 이렇게 같이 있을 수 없었겠죠..."
    "그렇지..."
    show ejoo_ending shadow with dissolve
    e "저는 예전부터 사람들이 무서웠어요"
    show ejoo_ending smile
    e "그런데 이상하게도 선배는 무섭지가 않았어요"
    e "선배랑 같이 동아리활동도 하고... 영화도 보러가고..."
    show ejoo_ending idle
    e "선배랑 같이 지내면서 한 가지 생각이 들었어요..."
    "무슨 생각...?"
    show ejoo_ending shadowh with dissolve
    e "이 사람을 놓치면 평생 후회하겠다..."
    show ejoo_ending idleh
    e "선배"
    e "저 선배 좋아해요"
    e "지금 이 말을 한 걸 후회할 수도 있겠지만"
    e "제 마음을 전하고 싶었어요"
    e "선배... 저랑 사귈래요...?"
    "이주야..."
    "나도 너랑 같이 지내면서 비슷한 생각을 했어..."
    "이런 나라도 괜찮다면..."
    "좋아!"
    show ejoo_ending surpriseh
    e "!"
    show ejoo_ending smileh with dissolve
    e "선배 좋아해요!"
    scene black with dissolve
    "그렇게 나는 18년의 모쏠인생을 끝내고"
    "여자친구를 사귀게 됐다."
    scene theend with dissolve
    "다섯 번째 엔딩"
    return

label hone_ending:
    play music "audio/romantic.mp3" loop
    "아슬아슬하게 도착했다..."
    "앗 저기 보인다!"
    "여기야~"
    "???" "앗"
    show hone_ending idle with dissolve
    h "[player_name]~!"
    "너 오늘 좀 예쁘네?"
    show hone_ending idleh
    h "ㅁ...뭐야..."
    show hone_ending shadowh with dissolve
    h "ㄱ...고마워"
    show hone_ending idle
    "근데 오늘 왜 부른 거야?"
    show hone_ending shadow with dissolve
    h "..."
    show hone_ending smile
    h "일단 좀 걸을까...?"
    scene ending2 with dissolve
    show hone_ending idle with dissolve
    h "우리가 언제부터 알았지?"
    "음..."
    "유치원때부터 알고 지냈으니까...\n한 다섯살...?"
    show hone_ending smile
    h "다섯살때부터 넌 언제나 변함없이 짜증났어"
    "하하..."
    show hone_ending idle with dissolve
    h "그런데 밉지는 않았어"
    h "언제나 알게모르게 너한테서 힘을 얻는 나였어"
    h "나에게 너는 그저 오래 알고지낸 소꿉친구였어."
    show hone_ending shadow with dissolve
    h "그때까지는..."
    "무슨 말이야?"
    show hone_ending idle
    h "올해 나나가 전학오고 동아리에서도 이주라는 후배가 생겼잖아?"
    show hone_ending shadowh with dissolve
    h "여자랑 어울리는 너를 보고 가슴 한편이 불편해지는 것을 느꼈어."
    h "처음에는 무슨 감정인지는 몰랐지만"
    h "이제는 확실하게 알 것 같아."
    h "[player_name]..."
    show hone_ending idle
    h "난 너를 좋아해!"
    h "나랑... 사겨줄래...?"
    "혜원아..."
    "이런 나라도 괜찮으면..."
    "사귀자!"
    show hone_ending surpriseh
    h "!"
    show hone_ending smileh
    h "그래!"
    scene black with dissolve
    "그렇게 나는 18년의 모쏠인생을 끝내고"
    "여자친구를 사귀게 됐다."
    scene theend with dissolve
    "네 번째 엔딩"
    return
    
label nana_ending:
    play music "audio/romantic.mp3" loop
    scene ending1 with dissolve
    "아슬아슬하게 도착했다..."
    "앗 저기 보인다!"
    "여기야~"
    "???" "앗"
    show nana_ending idle with dissolve
    n "[player_name]군~!"
    "ㅎㅎ 오늘 예쁘다"
    show nana_ending idleh with dissolve
    n "아ㅎㅎ 고마워...ㅎㅎ"
    "근데 오늘 왜 부른 거야?"
    show nana_ending shadow with dissolve
    n "그게..."
    show nana_ending smile
    n "우선 좀 걸을까...?"
    scene ending2 with dissolve
    show nana_ending idle with dissolve
    n "[player_name]군 우리 처음 만났을 때 기억나?"
    "아... 기억나지"
    "급하게 학교 가다가 일본인 교복을 입은 사람이랑 부딪힌 기억은\n쉽게 못잊지"
    show nana_ending smile
    n "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
    show nana_ending idle
    n "그땐 [player_name]군이 솔직히 좋은 인상은 아니였어"
    "아..."
    n "그런데 내가 전학오고나서 나를 엄청 챙겨줬잖아"
    n "그래서 처음엔 좋은 친구인 줄 알았어"
    show nana_ending shadow with dissolve
    n "그런데..."
    n "[player_name]군과 같이 지내는 시간이 지날수록..."
    show nana_ending shadowh
    n "조금씩 나의 마음을 눈치채기 시작했어..."
    n "애써 모른 척 했지만"
    n "이제는 인정하고 용기를 내볼려고..."
    "무슨 소리야 나나?"
    show nana_ending idleh with dissolve
    n "[player_name]군..."
    show nana_ending brave
    n "나 야부키나나는..."
    show nana_ending braveh with dissolve
    n "[player_name]군을 좋아합니다!"
    n "저랑 사귀어주세요!"
    "나나..."
    "이런 나라도 괜찮다면..."
    "제가 남친이 되어도 될까요?"
    show nana_ending surpriseh
    n "!"
    show nana_ending smileh with dissolve
    n "모찌롱!(물론!)"
    scene black with dissolve
    "그렇게 나는 18년의 모쏠인생을 끝내고"
    "여자친구를 사귀게 됐다."
    scene theend with dissolve
    "세 번째 엔딩"
    return
    
return
