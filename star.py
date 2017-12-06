# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
# 学生类
class student(object):

    # __slots__ = ('__name')

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_student(self):
        print('%s:%s' % (self.__name, self.__score))


def show_time(self):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


student.show_time = show_time

s = student('star', 100)

s.score = 90
s.print_student()
print(time.time())
s.show_time()


# 教师类
class teacher(object):
    score = 0;
    student = 'None';

    def print_student(self):
        print('%s:%s' % (self.student, self.score))

    def get_score(self):
        return self.score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('分数必须为int型')
        if score < 0 or score > 100:
            raise ValueError('分数范围必须在0-100')
        self.score = score


s = teacher()
s.set_score(100)
s.print_student()
#测试枚举
from enum import Enum
MONTH = Enum('MONTH', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(MONTH.Jan)

#测试文件操作 读和写
# try:
#     f = open('E:\\test\\star.txt')
#     print(f.read())
# except IOError as e:
#     print(e)
# finally:
#     f.close()
#with 不需关闭文件，自动close

# with open('E:\\test\\star.txt', 'r') as f:
#     str = f.read()
#
# with open('E:\\test\\star.txt','w') as f:
#     f.write(str+'\n'+'hello world!')

#内存读写
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

import os
#windows内核没有fork函数，只能在linux或macos上运行
# pid = os.fork()
# if pid == 0:
#     print("这是子进程id=%s,我的父进程id = %s"% (os.getpid(),os.getppid()))
# else:
#     print("这是父进程，进程id = %s，我的子进程id = %s"% (os.getpid(),pid))







