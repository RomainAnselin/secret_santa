import random
import numpy as np
import sys
import time
from termcolor import colored

srcf = open("engineers", "r")
srclist = srcf.read().splitlines()
srcf.close()

dstf = open(".gifted","r")
dstlist = dstf.read().splitlines()
dstf.close()

giverf = open(".gifter","r")
hasvoted = giverf.read().splitlines()
giverf.close()


remain = np.setdiff1d(srclist,dstlist)
hasntplayed = np.setdiff1d(srclist,hasvoted)

wasremoved = 0
waitt = 0.10

# print("Hasn't played:", hasntplayed)

print(colored(""" 
 #####                                        #####                             
#     # ######  ####  #####  ###### #####    #     #   ##   #    # #####   ##   
#       #      #    # #    # #        #      #        #  #  ##   #   #    #  #  
 #####  #####  #      #    # #####    #   """, 'green'), colored("""   #####  #    # # #  #   #   #    # 
      # #      #      #####  #        #            # ###### #  # #   #   ###### 
#     # #      #    # #   #  #        #      #     # #    # #   ##   #   #    # 
 #####  ######  ####  #    # ######   #       #####  #    # #    #   #   #    # 
""", 'red'))
#print()

def printtype(my_str, wait):
    for char in my_str:
        print(char, end='', flush=True)

        time.sleep(wait)

#print("\nHO, HO, HO! Dear Little Elf, please enter your first name as defined in this list below:\n", srclist, "\n")
strintro = "\nHO, HO, HO! My Dear Little Elf, please enter your first name below:\n"
printtype (strintro, waitt)
giver = input("Dear Santa, my name is: ")

# print("Remain to give:", remain)
if giver in remain:
    giveridx = np.where(remain == giver)[0]
    # print("giver index:", giveridx, "for", giver)
    remain = np.delete(remain, giveridx)
    wasremoved=1
    # print("Remain to give after removal:", remain)
#remain.delete(giver)
# Consider removing the giver from the remain ballot before starting.
# Would avoid deadlock management altogether but require readding them to the remain list if that was done

# print("Giver list", hasvoted)
if giver in hasvoted:
    time.sleep(2)
    print ("\nHmm. Thanks", giver, ". Let me think...")
    time.sleep(5)
    print ("\nIt's not much in the spirit of Christmas to try and have a second roll. Coal for you this Christmas...\n")
    time.sleep(3)
    sys.exit()

if giver not in srclist:
    print ("\n I'm not quite sure I got that name right. Can you check for a typo or contact Santa's Support team in case of an oversight?")
    sys.exit()

def roulette():
    gift = str(random.choice(remain))
    # print(gift)
    # Random wont cut it on the last 2 in case 1 giver remain to receive a gift (A and B to give and A and C to receive. )
    # Need to account for that and "make the choice" to avoid deadlock on last round
    if len(remain) == 2:
        notsorandom = np.intersect1d(remain,hasntplayed)
        lasttwo = np.setdiff1d(remain,hasntplayed)
        # Case where both players remaining have to be distributed to each other
        if len(notsorandom) == 1:
            #print ("NR:", notsorandom, "LT: ", lasttwo)
            if giver in remain:
                gift = str(lasttwo[0])
            else:
                gift = str(notsorandom[0])

    if giver == gift:
        print ("Oops, we have made a mistake and were about to ask you to get your own present. Not very christmasy now is it? Let's try again")
        roulette()
    else:
        time.sleep(1)
        #print ("\nWe have picked someone for you", giver)
        str1 = "\nWe are picking someone for you " + giver 
        strwait = ".....\n\n"
        str2 = "But you have to be patient :)\n\n"
        str3 = "Have you been a good person this year?\n\n"
        str4 = "Are you sure?\n\n"
        str5 = "OK I believe you, let's get rolling, I know you have hard work to do\n\n"
        printtype(str1, waitt)
        printtype(strwait, 1)
        #printtype(giver, waitt)
        time.sleep(3)
        printtype(str2, waitt)
        time.sleep(3)
        printtype(str3, waitt)
        time.sleep(5)
        printtype(str4, waitt)
        time.sleep(4)
        printtype(str5, waitt)
        time.sleep(3)
        # print ("\nBut you have to be patient :)\n")
        # time.sleep(3)
        # print ("Have you been a good person this year?\n")
        # time.sleep(5)
        # print ("Are you sure?\n")
        # time.sleep(4)
        # print ("OK I believe you, let's get rolling, I know you have hard work to do")
        # time.sleep(3)
    return gift

# print("Already gifted", dstlist)

## Time to make gifts !
gifted = roulette()

if wasremoved == 1:
    np.append(remain, giver)

dstlist.append(gifted)
hasvoted.append(giver)

random.shuffle(dstlist)
random.shuffle(hasvoted)

#print (str(dstlist))

# Rewrite the lists in files after shuffling
dstf = open(".gifted","w")
for i in dstlist:
    dstf.write(i + '\n')
dstf.close()

giverf = open(".gifter","w")
for y in hasvoted:
    giverf.write(y + '\n')
giverf.close()

strfinal = "HO, HO, HO! So, my dear helper " + colored(giver, 'red') + ". As one of Santa's elves, could you please make a nice surprise for " + colored(gifted, 'green') + ".\nBut dont tell anyone, it's a secret between us two !!!\n\n"
printtype(strfinal, waitt)
#print ("\nSo my dear helper", giver, "! As one of Santa's elves, could you please make a nice surprise for", gifted, "\nBut dont tell anyone, it's a secret between us two !!!")
