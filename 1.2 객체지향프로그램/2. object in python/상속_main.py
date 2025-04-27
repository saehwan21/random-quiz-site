from 상속2 import Person
from 상속2 import Employee

myPerson=Person("박세환", 35, "Male")

myEmployee = Employee("세톨", 36, "Male", 300000, "2011/01/02")

myPerson.about_me()
myEmployee.about_me()  # 이걸하면 부모클래스의 about_me까지 출력됨

