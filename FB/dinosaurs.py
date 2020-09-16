# Given two CSV data sets, first file contains stats about dinosaurs
# Second file has additional data
# Formula: speed = (speed = (STRIDE_LENGTH / LEG_LENGTH)-1) * SQRT(LEG_LENGTH * g)
# where g = 9.8m/s^2
# print out only the bipedal dinosaurs from fastest to slowest, thats it

import math
import heapq
import csv

def printBipedalDinosaursOrderBySpeed(DinoInfo, AdditionalInfo):
    bipedalDinosaurs = {}
    g = 9.8

    with open(AdditionalInfo, 'r') as f:
        line = f.readline()
        while line:
            line = f.readline().strip()
            print(line)
            if line:
                NAME, STRIDE_LENGTH, STANCE = line.split(',')
                if STANCE == "bipedal":
                    bipedalDinosaurs[NAME] = float(STRIDE_LENGTH)
    print(bipedalDinosaurs)

    with open(DinoInfo, 'r') as f:
        line = f.readline()
        while line:
            line = f.readline().strip()
            print(line)
            if line:
                NAME, LEG_LENGTH, DIET = line.split(',')
                if NAME in bipedalDinosaurs:
                    STRIDE_LENGTH, LEG_LENGTH = bipedalDinosaurs[NAME], float(LEG_LENGTH)
                    bipedalDinosaurs[NAME] = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)

    for key in sorted(bipedalDinosaurs, reverse=True):
        print(key)

printBipedalDinosaursOrderBySpeed('dataset1.csv', 'dataset2.csv')
