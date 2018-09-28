PROGRAM 2
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
		OUTPUT
enter r to roll a dicer
my position 1
your random value 1
enter r to roll a dicer
my position 2
your random value 1
enter r to roll a dicer
my position 7
your random value 5
enter r to roll a dicer
my position 9
your random value 2
enter r to roll a dicer
my position 14
your random value 5
enter r to roll a dicer
my position 17
your random value 3
enter r to roll a dicer
my position 21
your random value 4
enter r to roll a dicer
my position 27
your random value 6
enter r to roll a dicer
my position 28
your random value 1
enter r to roll a dicer
my position 29
your random value 1
enter r to roll a dicer
my position 33
your random value 4
enter r to roll a dicer
my position 37
your random value 4
enter r to roll a dicer
my position 40
your random value 3
wow ladder
enter r to roll a dicer
my position 71
your random value 3
enter r to roll a dicer
my position 75
your random value 4
enter r to roll a dicer
my position 77
your random value 2
enter r to roll a dicer
my position 79
your random value 2
enter r to roll a dicer
my position 84
your random value 5
enter r to roll a dicer
my position 89
your random value 5
sorry snake bite
enter r to roll a dicer
my position 72
your random value 2
enter r to roll a dicer
my position 78
your random value 6
enter r to roll a dicer
my position 81
your random value 3
enter r to roll a dicer
my position 85
your random value 4
enter r to roll a dicer
my position 91
your random value 6
enter r to roll a dicer
my position 97
your random value 6
enter r to roll a dicer
my position 99
your random value 2
enter r to roll a dicer
my position 103
your random value 4
you cant go beyound 100
enter r to roll a dicer
my position 102
your random value 3
you cant go beyound 100
enter r to roll a dicer
my position 104
your random value 5
you cant go beyound 100
enter r to roll a dicer
my position 100
your random value 1
congrats you won


