import os

from SetolNote import Note
from SetolNote import NoteBook

os.system('cls') #이전 결과가 terminal에 누적되는거 방지지

print("============")
my_notebook = NoteBook("세환 강의노트")
print(my_notebook)

print("============")
new_note = Note("수업하기싫다")
print(new_note)

print("============")
new_note2 = Note("파이썬강의")
print(new_note2)

print("============")
my_notebook.add_note(new_note)
my_notebook.add_note(new_note2, 100)

my_notebook.get_number_of_pages()

print("============")
print(my_notebook.notes[1])
