import music21
import string

# input name 
print("Enter your name")
first_name = list(raw_input().lower())
name = list(raw_input().lower())

# create some empty lists
name_num = list()
first_name_num = list()

# input birthday
day = int(input())
month = int(input())
year = int(input())

## generate list of empty notes
# @param    note_num    number of notes to generate
# @return   noteList    generated list
def generator(note_num, noteList):
    noteList = []
    for i in xrange(note_num):
        noteList.append(music21.note.Note)
        print(noteList)
    return noteList
        
## idk what this does lol
# @param    char_list   
# @param    num_list    
# @param    el 
# @param    num    
# @return   num_list
def name_to_num(char_list, num_list, el, num):
    if el in char_list:
        times = char_list.count(el)
        for i in xrange(times):
            num_list.append(num)
    return num_list
            
## sum elements of a list ?
# @param    num_list    elements to sum
def name_sum_def(num_list):
    return sum(num_list)
        
## multiply all elements of list by const
# @param    num_list    list to multiply
# @param    num    const to multiply by
# @return   multiplied list
def name_mult_def(num_list, num):
    for i in xrange(len(num_list)):
        num_list[i] *= num
    return num_list

        
n1 = len(first_name)
n2 = len(name)

n1 = n1 % 4    
    
if n1 == 0:
    print("fugue 2")
if n1 == 1:
    print("fugue 8")
if n1 == 2:
    print("fugue 9")
if n1 == 3:
    print("fugue 19")


