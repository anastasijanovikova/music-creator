import music21
import string

print("Enter your birth date")
day_in = int(input())
month_in = int(input())
year_in = int(input())
print("Enter your name")
name = raw_input()
name = name.lower()
name_num = list()
name = list(name)
fname = raw_input()
fname = fname.lower()
fname_num = list()
fname = list(fname)

n1 = len(name_num)
n2 = len(fname_num)

#generate list of notes for one voice
def generator(note_num):
    num = 0
    while num < note_num:
        note = "note" + str(num + 1)
        note = music21.note.Note
        noteList.append(note)
        print(noteList)
        num += 1

generator(6)

for note in noteList:
    note.pitch.ps = 70
    
