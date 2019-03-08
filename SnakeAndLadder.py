import random
p=0
d=0
snl={8:37,38:9,11:2,13:34,40:68,65:46,52:81,76:97,93:64,89:70}
def rolldice():
	return random.randint(1,6)
#get 1 to 6 on the dice to enter the game
while True:
	r=input("Press r to roll the dice, q to quit: ")
	if r=='r':
		d=rolldice()
		print("You got...",d)
		if d==6 or d==1:
			print("Congratulations, you are in the game now!")
			break
		else:
			print("You need to get 6 to play the game, keep rolling")
	elif r =='q':
		exit()
while True:
	r=input("Press r to roll the dice, q to quit:")
	if r=='r':
		d=rolldice()
		print("You got",d)
		p=p+d
		if p==100:
			print("Hurray! you've won!!")
			exit()
		if p>100:
			p=p-d
			print("You need to get,",100-p,"to reach home.")
			print("Your new position is",p)
		if p in snl:
			if p<snl[p]:
				print("Oops, a snake!!")
			if p>snl[p]:
				print("Its a ladder!!")
			p=snl[p]
			print("Move to",p)
	elif r=='q':
			exit()


