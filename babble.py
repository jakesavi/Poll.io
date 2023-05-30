from itertools import count
import random
import csv
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','x','t','u','v','w','x','y','z']
def babbleExt():
    with open("dictionary.csv",'r+') as csvfile:
        reader = csv.reader(csvfile)
        desired = random.randrange(0,54555)
        count = 0
        for i in reader:
            if count == desired:
                return i
            else:
                count= count + 1 


def coinflip():
    flip = random.randrange(0,100)
    if flip >50:
        return True
    else:
        return False

def roll(numberOfDie, DieSides):
    DieResults = []
    for i in range(0,numberOfDie+1):
        DieResults.append(random.randrange(1,DieSides))
    return DieResults