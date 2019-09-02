"""
python 中 class 转 json 字符串的思路
"""
import json


class School(object):
    def __init__(self, name):
        self.name = name
        self.students = []

    def json_obj(self):
        obj = {'name': self.name,
               'students': []}
        for student in self.students:
            obj['students'].append(student.json_obj())
        return obj


class Student(object):
    def __init__(self, stu_num, name):
        self.stu_num = stu_num
        self.name = name

    def json_obj(self):
        obj = {'name': self.name,
               'stu_num': self.stu_num}
        return obj


stu1 = Student(name='stu1', stu_num=1001)
stu2 = Student(name='stu2', stu_num=1002)

school1 = School(name='test')
school1.students.append(stu1)
school1.students.append(stu2)

school2 = School(name=None)


print(json.dumps([school1.json_obj(), school2.json_obj()]))
