from random import randint

count = 1

while count == 1:
	 for i in range (4):
		 x = randint (1, 100)
		 y = randint (1, 100)
		 
		 print("Question", i+1, ":", x, "*" ,y)
		 answer1 = int(input ("Enter your answer : "))
		 if answer1 == x*y:
			 print ("Correct !!")
		 else:
			 print("Wrong !!", "The correct answer is : " " ", x*y)
	 count = int(input ("Enter 1 to start the game : "))
else:
	print("Thanks for playing")

