#เกมทายคำ vertion2 (เพิ่มให้มีหลายโหมดมากขึ้น เช่น โหมดสัตว์ โหมดพืช)

#นำเข้า function สุ่ม
import random

#กำหนดพลังชีวิตและคะแนน
lives = 3
score = 0

#กำหนด Dictionary โดยมี dictionary_category เป็น Keys 
        # ที่มี words เป็น Keys และมี hint เป็น value 
dic_words_hint_category = {
    'animals':{'panda':
                  ['สัตว์ที่มีวิถีชีวิตไม่ค่อยเอื้อต่อการอยู่รอด','สีตัวตัดกันแบบขาวดำ','มักเกี่ยวข้องกับไม้ไผ่'],

                'tiger':
                  ['สัตว์ในตระกูลเดียวกับแมว','พลังและความเร็ว','เจอได้ในเอเชีย'],

                'cat':
                  ['สัตว์เลี้ยงยอดนิยม','ชอบพื้นที่สูง','เดินเงียบมาก'],

                'ant':
                  ['เจอตัวเล็กๆ ในชีวิตประจำวัน','ทำงานหนักโดยไม่บ่น','โครงสร้างสังคมเป็นระเบียบมาก']
            },

    'plants':{'coconut':
                 ['มักพบในเขตร้อน','มีเปลือกแข็งและมีน้ำข้างใน','ผลของมันใช้ได้หลายอย่าง ทั้งกินและทำผลิตภัณฑ์ต่างๆ'],

              'sunflower':
                 ['ดอกมีสีเหลือง','หันตามทิศทางของแสงแดด','เมล็ดเป็นอาหารแฮมสเตอร์ได้'],

              'mango':
                 ['เป็นผลไม้ที่มีรสหวาน','ผลมันมีสีเหลืองส้มและเป็นที่นิยมในประเทศเอเชีย','เป็นผลไม้ที่มีรสชาติหวานอมเปรี้ยว']
            },

    'food':{'fried rice':
                ['เป็นอาหารที่ใช้ข้าวสวยเป็นหลัก','มักใส่เนื้อสัตว์ เช่น ไก่ หรือ กุ้ง','มีแตงกวาและมะนาว'],

            'cake':
                 ['วันเกิด','ของหวาน','เทียน'],

            'papaya salad':
                 ['มะละกอ','ครก','ภาคอีสาน']
            },

    'game':{'Minecraft':
                 ['บล็อก','ตัดไม้มือเปล่า','โหมดสร้างสรรค์ เอาชีวิตรอด'],
            'Arena of valor':
                 ['ป้อม','มี 5 ตำแหน่ง','5v5'],
            'Among Us':
                 ['ฆาตรกร','imposter','kill']
            }
        }

#function เลือก category
def secret_category_function(category_list) :
    print('หมวดหมู่คำ')
    for i in range(len(category_list)) :
        print(str(i+1) + '.' ,category_list[i])
    input_player = input('พิมพ์เลขของหมวดที่คุณต้องการเล่น\n')
    secret_category = category_list[int(input_player)-1]

    return secret_category #ส่ง category ไปเพื่อใช้ต่อ

#function เลือกเอา list ของ words ออกมา
def words_function(secret_category,dic_words_hint_category) :

    words = list(dic_words_hint_category[secret_category])
    random.shuffle(words) #สลับคำในlist

    return words #นำ words ออกมาใช้เล่นเกม




#function สำหรับรับคำขอและแสดงคำใบ้
def hint(secret_word,dic_words_hint_category,secret_category) :
    while True :
        input_player = input("อยากได้คำใบ้ไหม'\n อยากได้พิมพ์ 'อยาก' ไม่อยากได้พิมพ์ 'ไม่อยาก'\n")
        if input_player == 'อยาก' or input_player == "'อยาก'" :
            random.shuffle(dic_words_hint_category[secret_category][secret_word])
            hint = dic_words_hint_category[secret_category][secret_word].pop()
            print('รับคำใบ้ไปเลยย\nคำใบ้คืออ ' + hint )
            break
        else :
            if input_player == "ไม่อยาก" or input_player == "'ไม่อยาก'" :
                print('ไม่อยากได้ก็ตามใจ เราไม่ง้อหรอก')
                break
            else :
                print('เหมือนคุณจะพิมพ์ผิดนะ\nพิมพ์ใหม่อีกครั้งสิ')
    return dic_words_hint_category
while True :
    #list ของหมวดหมู่คำทาย
    category_list = list(dic_words_hint_category.keys())


    secret_category = secret_category_function(category_list)
    words = words_function(secret_category,dic_words_hint_category)

    #ตราบใดที่คำยังไม่หมดและพลังชีวิตยังไม่เป็น 0 ใหัเล่นต่อได้
    while len(words) > 0 and lives > 0 :

        random.shuffle(words)   #สุ่มคำในลิส words เพื่อให้คำไม่ซ้ากัน ในการเล่นแต่ครั้ง
        secret_word = words.pop()   #นำคำใน words ออกมา 1 คำ แทนค่าใน secret_words
        clue = list('?'*len(secret_word))   #กำหนดลิสของเบาะแสมาให้มีความยาวเท่ากับ secret_words

        #รับตัวอักษรที่ผู้เล่นทายจากนั้น check ว่าตรงกับ secret_words หรือไม่
        while True :

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
                        hint(secret_word,dic_words_hint_category,secret_category)#ตอบผิดแล้วสามารถขอคำใบ้ได้

    #จบเกม 
    #จบแบบชนะจะขึ้นไม่เหมือนกับตอนแพ้
    if len(words) == 0 and lives == 3 :
        print('เก่งเกินนน ไม่มีคำไหนที่คุณทายผิดเลยย!!')
        print('คุณชนะแล้วล่ะ')
    else :
        if len(words) == 0 and lives > 0 :
            print('เก่งมากเลย ไม่เหลือคำให้คุณทายแล้วล่ะ')
            print('คุณชนะแล้ว')

    print('Final score : ' + str(score))
    print('END GAME!!')





