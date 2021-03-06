# Python program to illustrate the concept 
# of threading 
# importing the threading module 

from threading import Thread
from time import sleep

def print_cube(num): 
    
    sleep(5)
    print("Cube: {}".format(num * num * num)) 
    name=input('Please enter your name: ')
    sleep(2)
    print(name)

def print_square(num): 
    sleep(7)
    print("Square: {}".format(num * num))
    

if __name__ == "__main__": 
	# creating thread 
	t1 = Thread(target=print_square, args=(10,)) 
	t2 = Thread(target=print_cube, args=(10,)) 

	# starting thread 1 
	t1.start() 
	# starting thread 2 
	t2.start() 

	# wait until thread 1 is completely executed 
	t1.join() 
	# wait until thread 2 is completely executed 
	t2.join() 

	# both threads completely executed 
	print("Done!") 

