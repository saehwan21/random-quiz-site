class Person(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return "저의 이름은 {0}입니다. 나이는 {1}입니다.".format(self.name, self.age)


class Korean(Person):
    pass



first_korean = Korean("setol", 35)
print(first_korean)
