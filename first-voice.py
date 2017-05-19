import music21
import string

print("Enter your name")
first_name = raw_input()
name = raw_input()

name = name.lower()
name = list(name)
name_num = list()
first_name = first_name.lower()
first_name = list(first_name)
first_name_num = list()

day = int(input())
month = int(input())
year = int(input())

noteList = []

def generator(note_num):
    num = 0
    while num < note_num:
        note = "note" + str(num + 1)
        note = music21.note.Note
        noteList.append(note)
        print(noteList)
        num += 1
        
def name_to_num(char_list, num_list, el, num):
    if el in char_list:
        time = 0
        times = char_list.count(el)
        while time < times:
            num_list.append(num)
            time +=1
            
            
def name_sum_def(num_list, num):
    num = 0
    for n in num_list:
        num += n
        
       
def name_mult_def(num_list, num):
    num = 1
    for n in num_list:
        num *= n

        
n1 = len(first_name)
n2 = len(name)

while n1 > 2:
    n1 -= 3
    
while n2 > 2:
    n2 -= 3
    
    
if n1 == 0:
    generator(20)
if n1 == 1:
    generator(30)
if n1 == 2:
    generator(40)
voice_1 = music21.stream.Stream()


for n in noteList:
    voice_1.append()
