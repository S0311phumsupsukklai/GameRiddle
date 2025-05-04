import random
dic_words_hint = {'panda':
                  ['สัตว์ที่มีวิถีชีวิตไม่ค่อยเอื้อต่อการอยู่รอด','สีตัวตัดกันแบบขาวดำ','มักเกี่ยวข้องกับไม้ไผ่'],

                  'tiger':
                  ['สัตว์ในตระกูลเดียวกับแมว','พลังและความเร็ว','เจอได้ในเอเชีย'],

                  'cat':
                  ['สัตว์เลี้ยงยอดนิยม','ชอบพื้นที่สูง','เดินเงียบมาก'],

                  'ant':
                  ['เจอตัวเล็กๆ ในชีวิตประจำวัน','ทำงานหนักโดยไม่บ่น','โครงสร้างสังคมเป็นระเบียบมาก']}
words = list(dic_words_hint.keys())
random.shuffle(words)   #สุ่มคำในลิส words เพื่อให้คำไม่ซ้ากัน ในการเล่นแต่ครั้ง
secret_word = words.pop()   #นำคำใน words ออกมา 1 คำ แทนค่าใน secret_words
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