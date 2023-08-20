import threading, time, random, string
from threading import Thread, active_count, current_thread


################################################
# hw: repeat previous exercises with inheritance
################################################

# class Hello(threading.Thread):
#     def __init__(self, min, max):
#         self.min, self.max = 1,3
#         threading.Thread.__init__(self, min, max)

        # time.sleep(self.max)
        # for i in range(1000):
        #     print(random.choice(range(self.min, self.max)))
#This creates the thread objects, but they don't do anything yet.
# h = Hello(1,3)
# k = Hello(0,3)

#This causes each thread to do its work
# h.start()
# k.start()

#example 1
class MyThread(threading.Thread):
    def run(self):
        print('run function')

if __name__ == '__main__':
    for i in range(3):
        t = MyThread()
        t.start()

###########
# problem 1
###########

# letters = ['A', 'B', 'C', 'D']
# def func():
#     for letter in letters:
#         print(letter)
#         sleep(2)
# thread = Thread(target = func)
# thread.start()
# print('E')

##################
# with inheritance
##################

from time import sleep

class MyThread(threading.Thread):
    def run(self):
        self.letters= ['A', 'B', 'C', 'D']
        for letter in self.letters:
            print(letter)
            sleep(2)
        print('E')
    
if __name__ == '__main__':
    t = MyThread()
    t.start()
    
###########
# problem 2
###########
# from threading import Thread

# def number_printer():
#     for number in range(1,6,1):
#         print(number)
#         time.sleep(1)
    
# thread = Thread(target = number_printer)
# thread.start()
# print('A')
# thread.join()
# print('B')

##################
# with inheritance
##################

class MyThread(Thread):
    def number_printer(self):
        print('in number_printer')
        for number in range(1,6,1):
            if number == 1:
                print('A')
            print(number)
            time.sleep(1)
        print('B')
    def run(self):
        self.number_printer()

if __name__ == '__main__':
    thread = MyThread()
    thread.start()
    thread.join()



###########
# problem 3
###########

import random

# create an empty 2D list
#generate 5 random integers for the 5 subsets 
# my_list = [[random.randint(1,10) for j in range(5)] for i in range(5)]
# print(my_list)
# def row_product(row):
#     product = 1
#     for num in row:
#         product *= num
#     print("Product of row", my_list.index(row), "is \n", product)
# #create a thread for each row
# threads = [Thread(target = row_product, args = (row,)) for row in my_list]

# #start each thread
# for thread in threads:
#     thread.start()
#     thread.join()

##################
# with inheritance
##################

class MyThread(Thread):
    def __init__(self, row):
        Thread.__init__(self)
        self.row = row
    def run(self):
        product = 1
        for num in self.row:
            product *= num
        print('Product of row', my_list.index(self.row), 'is \n', product)

my_list = [[random.randint(1,10) for j in range(5)] for i in range(5)]
print(my_list)
if __name__ == '__main__':
    threads = [MyThread(row,) for row in my_list]
    for thread in threads:
        thread.start()
        thread.join()

###########
# problem 4- skipped
###########

# expression_list = []
# answers_list = []

# def count_lines(filename, data_list):
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#         print('numbers of lines in {} '.format(filename), len(lines))
#         for line in lines:
#             data_list.append(line)
# thread1 = Thread(target = count_lines, args=('expressions.txt', expression_list))
# thread2 = Thread(target = count_lines, args=('answers.txt', answers_list))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()
# print('finished counting lines!')
# print('Expressions: ')
# print(expression_list)
# print('Answers: ')
# print(answers_list)

################## 
# with inheritance
##################

class MyThread(Thread):
    def __init__(self, filename, datalist):
        Thread.__init__(self)
        self.filename = filename
        self.datalist = datalist
    def count_lines(self, filename, datalist):
        with open(filename, 'r') as f:
            lines = f.readlines()
            print('numbers of lines in {} '.format(filename), len(lines))
            for line in lines:
                datalist.append(line)

expression_list = []
answers_list = []
if __name__ == '__main__':
    t1 = MyThread('expressions.txt', expression_list,)
    t2 = MyThread('answers.txt', answers_list,)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
print('Expressions: ', expression_list)
print('Answers: ', answers_list)
    
########### 
# problem 5
###########

# def generate_nums():
#     for i in range(0,101):
#         print(random.randint(0,100))
#     print('thread has finished execution')
# # def checker_function():
        
# nums_thread = Thread(target = generate_nums)
# nums_thread.start()

# while nums_thread.is_alive():
#     pass
# print('done with program')

################## 
# with inheritance
##################

class MyThread(Thread):
    def generate_nums(self):
        for i in range(0,101):
            print(random.randint(0,100))
        print('the thread has finished execution')
    def run(self):
        self.generate_nums()
if __name__ == '__main__':
    nums_thread = MyThread()
    nums_thread.start()

    while nums_thread.is_alive():
        pass
    print('DONE with program')

###########
# problem 6
###########

import time

# letters_list1 = []
# letters_list2 = []
# letters_list3 = []
# letters_list4 = []
# letters_list5 = []

# def generate_list_thread(thread_list, name):
#     for i in range(10):
#         letter = random.choice(string.ascii_lowercase)
#         thread_list.append(letter)
#         # time.sleep(1)
#         print('{}: '.format(name), '\n',thread_list)
#     while current_thread().is_alive():
#         if not active_count()>5:
#             print('{} generated {}'.format(current_thread().name, thread_list))
#             print('completed with {}'.format(current_thread().name))
#             break
# #create 5 threads
# t1 = Thread(target= generate_list_thread, name = 'Thread 1', args = (letters_list1,'Thread1',))
# t2 = Thread(target = generate_list_thread, name = 'Thread 2' , args= (letters_list2, 'Thread 2',))
# t3 = Thread(target = generate_list_thread, name = 'Thread 3' , args= (letters_list3, 'Thread 3',))
# t4 = Thread(target = generate_list_thread, name = 'Thread 4' , args= (letters_list4, 'Thread 4',))
# t5 = Thread(target = generate_list_thread, name = 'Thread 5' , args= (letters_list5, 'Thread 5',))

# time.sleep(2)
# t1.start()
# t1.join()

# t2.start()
# t2.join()

# t3.start()
# t3.join()

# t4.start()
# t4.join()

# t5.start()
# t5.join()

################## 
# with inheritance
##################
letters_list1 = []
letters_list2 = []
letters_list3 = []
letters_list4 = []
letters_list5 = []

class MyThread(Thread):
    def __init__(self, thread_list, name):
        Thread.__init__(self)
        self.thread_list = thread_list
        self.name = name
    def generate_list_thread(self):
        for i in range(10):
            letter = random.choice(string.ascii_lowercase)
            self.thread_list.append(letter)
            # time.sleep(1)
            print('{}: '.format(self.name), '\n',self.thread_list)   
        while current_thread().is_alive():
            if not active_count()>5:
                print('{} generated {}'.format(current_thread().name, self.thread_list))
                print('completed with {}'.format(current_thread().name))
                break
    def run(self):
        self.generate_list_thread()

if __name__ =='__main__':
    t1 = MyThread(letters_list1, 'Thread1')
    t2 = MyThread(letters_list2, 'Thread2')
    t3 = MyThread(letters_list3, 'Thread3')
    t4 = MyThread(letters_list4, 'Thread4')
    t5 = MyThread(letters_list5, 'Thread5')

    time.sleep(2)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    t4.start()
    t4.join()
    t5.start()
    t5.join()













