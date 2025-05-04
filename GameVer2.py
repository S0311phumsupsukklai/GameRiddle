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

#function สำหรับรับคำขอและแสดงคำใบ้
def hint(secret_word,dic_words_hint,hint_list) :
    while True :
        input_player = input("อยากได้คำใบ้ไหม'\n อยากได้พิมพ์ 'อยาก' ไม่อยากได้พิมพ์ 'ไม่อยาก'\n")
        #ถ้าผู้เล่นพิมพ์ว่า อยาก และยังมีคำใบ้เหลืออยู่ สุ่มคำใบ้ที่เหลือ จากนั้นให้แสดงคำใบ้
        if (input_player == 'อยาก' or input_player == "'อยาก'") and len(hint_list) != 0:
            random.shuffle(hint_list) #สุ่มคำใบ้
            hint = hint_list.pop() #เอาคำใบ้ออกมา
            print('รับคำใบ้ไปเลยย\nคำใบ้คืออ ' + hint )
            break
        #ถ้าพิม์ว่า ไม่อยาก ให้แสดงผลลพธ์อีกแบบ
        elif input_player == "ไม่อยาก" or input_player == "'ไม่อยาก'" :
                print('ไม่อยากได้ก็ตามใจ เราไม่ง้อหรอก')
                break
        #กรณีพิมพ์ผิด
        elif len(hint_list) != 0 :
                print('เหมือนคุณจะพิมพ์ผิดนะ\nพิมพ์ใหม่อีกครั้งสิ')
        else :
             print('คำใบ้หมดแล้วล่ะ เสียใจด้วยนะ')    #บอกเมื่อไม่มีคำใบ้เหลืออยู่ในlist hint แล้ว
             break

    return hint_list #คืนค่า hint_list เพื่อ update hint ที่เหลืออยู๋นะปัจจุบัน

#เรียกใช้ key จาก dic_words_hint เพื่อเอามาสุ่มคำ
words = list(dic_words_hint.keys())

#ตราบใดที่คำยังไม่หมดและพลังชีวิตยังไม่เป็น 0 ใหัเล่นต่อได้
while len(words) > 0 and lives > 0 :

    random.shuffle(words)   #สุ่มคำในลิส words เพื่อให้คำไม่ซ้ากัน ในการเล่นแต่ครั้ง
    secret_word = words.pop()   #นำคำใน words ออกมา 1 คำ แทนค่าใน secret_words
    clue = list('?'*len(secret_word))   #กำหนดลิสของเบาะแสมาให้มีความยาวเท่ากับ secret_words

    #กำหนด list สำหรับคำใบ้ -> hint_list
    hint_list = dic_words_hint[secret_word]

    #รับตัวอักษรที่ผู้เล่นทายจากนั้น check ว่าตรงกับ secret_words หรือไม่
    while True :

        #ถ้าพลังชีวิตเป็น 1 ให้กดดันว่าเลือดเหลือ 1 แล้วนะะ
        if lives == 1 :
             print('เลือดเหลือ 1 แล้วนะะ') 

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
        elif lives > 0 :
            #ถ้าผิดให้เลือดลด กรณีพลังชีวิตยังมากกว่า 0 lives > 0 :
                lives = lives - 1
                print('lives : ' + str(lives))
            #ถ้าพลังชีวิตเป็น 0 ให้ผู้เล่นแพ้แล้ว ไปที่จบเกม
                if lives == 0 :
            #พลังชีวิตหมด คือแพ้แล้ว
                    print('หมดโอกาสแล้วล่ะ\nคุณแพ้แล้ว')
                    break
                else :
                    print('คุณตอบผิดนะ ลองใหม่อีกรอบนะ')
                    hint(secret_word,dic_words_hint,hint_list)#ตอบผิดแล้วสามารถขอคำใบ้ได้

#จบเกม 
#จบแบบชนะจะขึ้นไม่เหมือนกับตอนแพ้
if len(words) == 0 and lives == 3 :
    print('เก่งเกินนน ทายไม่ผิดสักตัวอักษรเลยย')
    print('คุณชนะแล้วล่ะ')
elif len(words) == 0 and lives > 0 :
        print('เก่งมากเลย ไม่เหลือคำให้คุณทายแล้วล่ะ')
        print('คุณชนะแล้ว')

print('Final score : ' + str(score))
print('END GAME!!')





