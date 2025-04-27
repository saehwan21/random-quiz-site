class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self):
        return "Hi my name is %s and my back number is %d" %(self.name, self.back_number)
    
    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다. From %d to %d" %(self.back_number, new_number))
        self.back_number=new_number

choi = SoccerPlayer("choi","mf", 20)
print(choi)

choi.change_back_number(100)
print(choi)

