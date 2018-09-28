import random
count=0
while(count<=100):
	n=input("enter r to roll a dice")
	if(n=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my position",count)
		print("your random value",a)
	if(count==8):
		count=37
		print("wow lader")
	elif(count==11):
		count=2
		print("sorry snake bite")
	elif(count==13):
		count=34
		print("wow ladder")
	elif(count==25):
		count=4
		print("sorry snake bite")
	elif(count==38):
		count=9
		print("sorry snake ladder")
	elif(count==40):
		count=68
		print("wow ladder")
	elif(count==52):
		count=81
		print("wow ladder")
	elif(count==65):
		count=46
		print("sorry snake bite")
	elif(count==76):
		count=97
		print("wow ladder")
	elif(count==89):
		count=70
		print("sorry snake bite")
	elif(count==93):
		count=64
		print("sorry snake bite")
	elif(count>100):
		count=count-a
		print("you cant go beyound 100")
	elif(count==100):
		print("congrats you won")
		break
