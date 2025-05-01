#เกมทายคำ vertion1 (แบบอย่างง่าย)

#นำเข้า function สุ่ม
import random

#กำหนดพลังชีวิตและคะแนน
lives = 3
score = 0

#กำหนดลิสของคำทีจะให้ผู้เล่นทาย
words = ['panda','tiger','cat','ant']

#function if lives equal one 
# ตอนที่พลังชีวิตเหลือเท่ากับ 1 ให้บอกว่านี่โอกาสสุดท้ายแล้วนะ
def lives_1(lives) :
    if lives == 1 :
        print('โอกาสสุดท้ายแล้วนะ')
        lives = lives - 1 
        return lives

#ตราบใดที่คำยังไม่หมดและพลังชีวิตยังไม่เป็น 0 ใหัเล่นต่อได้
while len(words) > 0 and lives > 0 :

    random.shuffle(words)   #สุ่มคำในลิส words เพื่อให้คำไม่ซ้ากัน ในการเล่นแต่ครั้ง
    secret_word = words.pop()   #นำคำใน words ออกมา 1 คำ แทนค่าใน secret_words
    clue = list('?'*len(secret_word))   #กำหนดลิสของเบาะแสมาให้มีความยาวเท่ากับ secret_words

    #รับตัวอักษรที่ผู้เล่นทายจากนั้น check ว่าตรงกับ secret_words หรือไม่
    while True :

        lives_1(lives)
        print(clue)    #แสดงลิสของเบาะแส เช่น ['?','?','?']

        #นำ input ของผู้เล่นมาตรจสอบ
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
                    break
                else :
                    print('คุณตอบผิดนะ ลองใหม่อีกรอบนะ')

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





