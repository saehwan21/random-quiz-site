class Note(object):
    def __init__(self, content=None):
        self.content = content
    def write_content(self, content):
        self.content=content
    def remove_all(self):
        self.content=""
    def __str__(self):
        return "노트에 적힌 내용입니다. : {0}".format(self.content)
    

class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page=-1):
        if self.page_number<301:
            if page == -1:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes[page] = note
        else:
            print("page가 모두 채워졌습니다")
    
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당페이지는 존재하지않습니다.")
    
    def get_number_of_pages(self):
        print(len(self.notes.keys()))

