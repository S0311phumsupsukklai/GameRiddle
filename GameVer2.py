#เกมทายคำ vertion2 (เพิ่มคำใบ้)

#นำเข้า function สุ่ม
import random

#กำหนดพลังชีวิตและคะแนน
lives = 3
score = 0

#กำหนด Dictionary โดยมีคำที่ผู้เล่นทายเป็น Keys และคำใบ้เป็น value
dic_words_hint = {'panda':
                  ['สัตว์ที่มีวิถีชีวิตไม่ค่อยเอื้อต่อการอยู่รอด','สีตัวตัดกันแบบขาวดำ','มักเกี่ยวข้องกับไม้ไผ่'],

                  'tiger':
                  ['สัตว์ในตระกูลเดียวกับแมว','พลังและความเร็ว','เจอได้ในเอเชีย'],

                  'cat':
                  ['สัตว์เลี้ยงยอดนิยม','ชอบพื้นที่สูง','เดินเงียบมาก'],

                  'ant':
                  ['เจอตัวเล็กๆ ในชีวิตประจำวัน','ทำงานหนักโดยไม่บ่น','โครงสร้างสังคมเป็นระเบียบมาก']}

#function if lives equal one 
# ตอนที่พลังชีวิตเหลือเท่ากับ 1 ให้บอกว่านี่โอกาสสุดท้ายแล้วนะ
def lives_1(lives) :
    if lives == 1 :
        print('เลือดเหลือ 1 แล้วนะะ')
        lives = lives - 1 
        return lives

#function สำหรับรับคำขอและแสดงคำใบ้
def hint(secret_word,dic_words_hint) :
    while True :
        input_player = input("อยากได้คำใบ้ไหม'\n อยากได้พิมพ์ 'อยาก' ไม่อยากได้พิมพ์ 'ไม่อยาก'\n")
        if input_player == 'อยาก' or input_player == "'อยาก'" :
            random.shuffle(dic_words_hint[secret_word])
            hint = dic_words_hint[secret_word].pop()
            print('รับคำใบ้ไปเลยย\nคำใบ้คืออ ' + hint )
            break
        else :
            if input_player == "ไม่อยาก" or input_player == "'ไม่อยาก'" :
                print('ไม่อยากได้ก็ตามใจ เราไม่ง้อหรอก')
                break
            else :
                print('เหมือนคุณจะพิมพ์ผิดนะ\nพิมพ์ใหม่อีกครั้งสิ')

#เรียกใช้ key จาก dic_words_hint เพื่อเอามาสุ่มคำ
words = list(dic_words_hint.keys())

#ตราบใดที่คำยังไม่หมดและพลังชีวิตยังไม่เป็น 0 ใหัเล่นต่อได้
while len(words) > 0 and lives > 0 :

    random.shuffle(words)   #สุ่มคำในลิส words เพื่อให้คำไม่ซ้ากัน ในการเล่นแต่ครั้ง
    secret_word = words.pop()   #นำคำใน words ออกมา 1 คำ แทนค่าใน secret_words
    clue = list('?'*len(secret_word))   #กำหนดลิสของเบาะแสมาให้มีความยาวเท่ากับ secret_words

    #รับตัวอักษรที่ผู้เล่นทายจากนั้น check ว่าตรงกับ secret_words หรือไม่
    while True :

        lives_1(lives)
        print(clue)    #แสดงลิสของเบาะแส เช่น ['?','?','?']

        #นำ input ของผู้เล่นมาตรวจสอบ
        guess = input('ทายตัวอักษรมาสิ : ')
        for i in range(len(secret_word)):
            if guess == secret_word[i] :
               clue[i] = guess  #ถ้าตรวจสอบแล้วตรงให้แทนค่าลงไปในลิสเบาะแส

        #check ว่าทายคำนี้เสร็จแล้วหรือยัง
        finish = ''.join(clue) == secret_word

        #ถ้าทายเสร็จแล้วให้เพิ่มคะแนนแล้ว break เพื่อไปคำถัดไป
        if guess in secret_word :
            if finish :
                print('เก่งมาก คำนั้นคือคำว่า ' + secret_word)
                score = score + 1
                print('score : ' + str(score))
                break
        else :
            #ถ้าผิดให้เลือดลด แต่พลังชีวิตยังมากกว่า 0
            if lives > 0 :
                lives = lives - 1
                print('lives : ' + str(lives))
            #ถ้าพลังชีวิตเป็น 0 ให้ผู้เล่นแพ้แล้ว ไปที่จบเกม
                if lives == 0 :
                    #พลังชีวิตหมด คือแพ้แล้ว
                    print('หมดโอกาสแล้วล่ะ')
                    hint(secret_word,dic_words_hint)#ตอบผิดแล้วสามารถขอคำใบ้ได้
                    break
                else :
                    print('คุณตอบผิดนะ ลองใหม่อีกรอบนะ')
                    hint(secret_word,dic_words_hint)#ตอบผิดแล้วสามารถขอคำใบ้ได้

#จบเกม 
#จบแบบชนะจะขึ้นไม่เหมือนกับตอนแพ้
if len(words) == 0 and lives == 3 :
    print('เก่งเกินนน ทายไม่ผิดสักตัวอักษรเลยย')
    print('คุณชนะแล้วล่ะ')
else :
    if len(words) == 0 and lives > 0 :
        print('เก่งมากเลย ไม่เหลือคำให้คุณทายแล้วล่ะ')
        print('คุณชนะแล้ว')

print('Final score : ' + str(score))
print('END GAME!!')





