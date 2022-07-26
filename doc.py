import re
import docx
import random

document = docx.Document('./LANG1121.docx')

chinese_char = [[]]
pinyin = [[]]

def print_hanzi():
    for i in range(len(chinese_char)):
        print("Lesson ", i+1, ' ', chinese_char[i], end='\n')
        


def print_pinyin():
    for i in range(len(pinyin)):
        for j in range(len(pinyin[i])):
            print(j+1, pinyin[i][j], end='\t')
        print()

def read_data():
    index = 0
    for i in document.tables:
        for j in i.rows:
            for k in j.cells:
                a = k.text
            
                # a = ''.join([i for i in a if not i.isdigit()])
                pattern = r'[\u4e00-\u9fff]+(.+?)='
                match = re.search(pattern, a)
                if match:
                    chinese_char[index].append(match.group())
                # for n in re.findall(r'[\u4e00-\u9fff]+',a):
                #     print(n)

        for n in range(len(chinese_char[index])):
            temp = chinese_char[index][n].split()
            temp = temp[:-1]
            chinese_char[index][n] = ''.join(temp)
            
            the_pinyin = re.sub(r'[\u4e00-\u9fff]+', "", chinese_char[index][n])  
            pinyin[index].append(the_pinyin)

        for n in range(len(chinese_char[index])):
            match = re.search(r'[\u4e00-\u9fff]+', chinese_char[index][n])
            chinese_char[index][n] = match.group()  

        index += 1
        chinese_char.append([])
        pinyin.append([])

    chinese_char.pop()
    pinyin.pop()

read_data()

level = 1

print_hanzi()

print()


while len(chinese_char) != 0:
    # print_hanzi()
    print("Level ", level, " = ", end = "")
    random_lesson = random.randint(0,len(chinese_char)-1)
    random_char = random.randint(0,len(chinese_char[random_lesson])-1)
    the_pinyin = pinyin[random_lesson][random_char]
    hanzi = chinese_char[random_lesson][random_char]
    print(the_pinyin)

    input("Enter to show the answer = ")
    print(hanzi)

    chinese_char[random_lesson].remove(hanzi)
    pinyin[random_lesson].remove(the_pinyin)

    if (len(chinese_char[random_lesson]) == 0):
        chinese_char.remove([])
        pinyin.remove([])
    
    level += 1
    print()
    
print("Done Done Done!")
