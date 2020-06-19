import time 
from robot_sort import SortingRobot as robo1 
from random import seed, sample 

seed(5)

e_list = []
for i in range(100):
    e_list.append(sample(range(300), 100))

robot1 = 0 
for l in e_list:
    robot1 = robo1(l)

    time1 = robot1.sort()
    robot1_time += time1 


print("Time Complexity:", robot1_time)