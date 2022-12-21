#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    ave = 0
    summ = 0
    for tup in my_list:
        ave += (tup[0] * tup[1])
        summ += (tup[1])
    return (ave) / (summ)
