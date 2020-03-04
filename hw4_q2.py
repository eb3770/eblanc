# Author: Elayne Blancas
# Assignment / Part: HW4 - Q2
# Date due: 2020-03-06
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

pos_int=int(input("Please enter a positive integer: "))
top_stars_per_row=2*pos_int-1
top_spaces=0

for i in range (1,pos_int+1):
    print(top_spaces*" "+"*"*top_stars_per_row)
    top_stars_per_row-=2 
    top_spaces+=1

bottom_stars_per_row=3
bottom_spaces=top_spaces-2

for i in range (1,pos_int):
    print (bottom_spaces*" "+ "*"*bottom_stars_per_row)
    bottom_stars_per_row+=2
    bottom_spaces-=1 
    




