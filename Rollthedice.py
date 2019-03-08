import random
d=0
p=0
while True:
	r=input("Press 'R' to roll and 'Q' to quit ")
	if r=='r':
		d=random.randint(1,6)
		print("You got :",d)
		if d==6:
			print("Congratulations, you can play now.")
			break
		else:
			print("Roll the dice again till you get 6.")
while True:
	r=input("Press 'R' to roll and 'Q' to quit ")
	if r=='r':
		d=random.randint(1,6)
		print("You got:",d)
		p=p+d
		print("Your position is:",p)
		if p>100:
			p=p-d
			print("Wait till you get ",100-p)
			print("Your new position is:",p)
		if p==100:
			print("You've Won!!!!")
			exit()
		if p==8:
			p=37
			print("Wow, a ladder, you reached:",p)
		if p==13:
			p=34
			print("Wow, a ladder, you reached:",p)
		if p==40:
			p=68
			print("Wow, a ladder, you reached:",p)
		if p==52:
			p=81
			print("Wow, a ladder, you reached:",p)
		if p==76:
			p=97
			print("Wow, a ladder, you reached:",p)
		if p==11:
			p=2
			print("Opps, a snake, you have to go down:",p)
		if p==25:
			p=4
			print("Opps, a snake, you have to go down:",p)
		if p==38:
			p=9
			print("Opps, a snake, you have to go down:",p)
		if p==65:
			p=46
			print("Opps, a snake, you have to go down:",p)
		if p==89:
			p=70
			print("Opps, a snake, you have to go down:",p)
		if p==93:
			p=64
			print("Opps, a snake, you have to go down:",p)
	elif r=='q':
		print("Thank You!")
		exit()