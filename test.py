import random

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
category_list = list(dic_words_hint_category.keys())
for i in range(len(category_list)):
    print(str(i+1) + '.',category_list[i])
input('พิมพ์ตัวเลขหมวดที่ต้องการเล่นได้เลย!!')

secret_category = category_list.pop()
print(secret_category)
words = list(dic_words_hint_category[secret_category])
print(words)
random.shuffle(words)
secret_word = words.pop()
print(secret_word)
hint_list = list(dic_words_hint_category[secret_category][secret_word])
print(hint_list)
random.shuffle(hint_list)
hint = hint_list.pop()
print(hint)