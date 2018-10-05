import random
d={1:'R',2:'P',3:'S'}
c=d[random.randint(1,3)]
while(True):
	p=input("enter'R','P','S'")
	if(c==p):
 		print("tie")
	elif(c=='R'and p=='S' or c=='P'and p=='R' or c=='S'and p=='P'):
		print("computer wins")
	else:
		print("player won")
		break
OUTPUT
enter'R','P','S'S
computer wins
enter'R','P','S'R
tie
enter'R','P','S'P
player won
