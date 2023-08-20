from threading import Thread, active_count, current_thread
from time import sleep
import random, string
# import expressions

#hw: questions 1-3 on multithreading 

# def print_double(num):
#     print('The double of {} is {} '.format(num, num*2))
# double_maker = Thread(target = print_double, args = (10,))
# double_maker.start()
# print('Thread ended')

# def get_squares(start, end):
#     for num in range(start, end+1, 1):
#         print('The square of {} is {} '.format(num, num*num))
# square_thread = Thread(target = get_squares, args = (10,20))
# square_thread.start()
# square_thread.join()
# print('Message 1')
# print('Message 2')
# print('Message 3')

# def prime_checker(num):
#     prime = True
#     for d in range(2, int(num**0.5) +1, 1):
#         print('{} checked with {}'.format(num,d))
#         if num % d == 0:
#             prime = False
#         if prime == True: 
#             print('{} is a prime number'.format(num))
#         else:
#             print('{} is not a prime number'.format(num))

# def primes(numbers):
#     for num in numbers:
#         t = Thread(target = prime_checker, args = (num,))
#         t.start()
#         t.join()
#         print('Completed task for {}!'.format(num))

# prime_thread = Thread(target = primes, args = ([4483,4493,],))
# prime_thread.start()
# prime_thread.join()
# print('The program ended')

##################
##question 1 and 2
################## 

# letters = ['A', 'B', 'C', 'D']
# def func():
#     for letter in letters:
#         print(letter)
#         sleep(2)
# thread = Thread(target = func)
# thread.start()
# print('E')

# explain every picture in introduction slides next class
# insert code for all alogorithms
# explain singleton design pattern 

# def number_printer1():
#     sleep(1)
#     for number in range(0,10,1):
#         print('num_printer1 - {}'.format(number))
#         sleep(1)
#     print('numberprinter1 finished')

# def number_printer2():
#     sleep(4)
#     for number in range(0,5,1):
#         print('num_printer2 - {}'.format(number))
#         sleep(1)
#     print('numberprinter2 finished')
# thread1, thread2 = Thread(target = number_printer1), Thread(target = number_printer2)
# thread1.start()
# thread2.start()
# print('threads started')
# thread1.join()
# thread2.join()
# print('threads finished')



###########
#question 3
###########
#create an empty 2d list with 5 subsets
# import random

# # create an empty 2D list
# #generate 5 random integers for the 5 subsets 
# my_list = [[random.randint(1,10) for j in range(5)] for i in range(5)]
# print(my_list)
# def row_product(row):
#     product = 1
#     for num in row:
#         product *= num
#     print("Product of row", my_list.index(row), "is", product)
# #create a thread for each row
# threads = [Thread(target = row_product, args = (row,)) for row in my_list]

# #start each thread
# for thread in threads:
#     thread.start()

###########
#question 4
###########
expression_list = []
answers_list = []

def count_lines(filename, data_list):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print('numbers of lines in {} '.format(filename), len(lines))
        for line in lines:
            data_list.append(line)
thread1 = Thread(target = count_lines, args=('expressions.txt', expression_list))
thread2 = Thread(target = count_lines, args=('answers.txt', answers_list))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print('finished counting lines!')
print('Expressions: ')
print(expression_list)
print('Answers: ')
print(answers_list)

def readExpressions():
    with open('expressions.txt', 'r') as file:
        x = len(file.readlines())
        print('The total number of lines in expressions.txt ', x)


#################################################
# the is_alive method checks the state of a thread
# before calling start(), threads are not alive 
#################################################

# def user_input():
#     while True:
#         number = int(input('Please enter a non-zero number: '))
#         if number == 0: #similar to base case
#             print('you entered a 0 :(')
#             break
#         print(number*2)
#         print('thread is still alive')
# def checker_function():
#     while user_input_thread.is_alive():
#         pass #as long as while loop does not break, thread is alive
#     print('the thread is not alive')
# user_input_thread = Thread(target = user_input)
# checker_thread = Thread(target = checker_function)
# user_input_thread.start()
# checker_thread.start()


############
# question 5
############

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
 

 #################################  
 # question 6
 # show which thread finishes first
 #################################
# import time

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


# while t1.is_alive():
#     pass
# print('done with t1')

# while t2.is_alive():
#     pass
# print('done with t2')

# print('letters list 1: ', letters_list1)
# print('letters list 2: ', letters_list2)



