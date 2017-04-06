#  File: CalculatePI.py

#  Description: calculates the probability of winning the prize by switching doors in the lets make a deal game

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 56865

#  Date Created: 03/04

#  Date Last Modified: 03/04

import random
def main():

    num_plays = eval(input("Enter number of times you want to play: "))

    num = 0
    view = 1
    newguess = 1
    wins = 0
    prob_switch = 0
    prob_notswith = 0
    
    print(' ')
    print('  Prize','Guess','View','New Guess', sep = '     ')

    while num <= num_plays :

        num += 1
        prize = random.randint(1,3)
        guess = random.randint(1,3)

        while (view == prize) or (view == guess) :

            view = random.randint(1,3)

        while (newguess == view) or (newguess == guess):

            newguess = random.randint(1,3)

        if newguess == prize:

            wins += 1
                
        print("    " + str(prize), end = "         ")
        print(str(guess),str(view),str(newguess), sep = '         ')



    prob_switch = round((wins/num),2)

    prob_notswitch = 1-prob_switch
    
    print(" ")
    print("Probability of winning if you switch = " + str(prob_switch))
    print("Probability of winning if you do not switch = " + str(prob_notswitch))

            
main()

                

        
