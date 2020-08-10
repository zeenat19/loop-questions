day = input("enter your day")
post = input("enter your post")
if day == "monday":
	if post == "disco":
		print(post,"will be elected")
		print(post,"incharge of the girls are punchual or not")
if day == "tuesday":
	if post == "T&P":
		print(post,"will be elected")
		print(post,"incharge of studies")
if day == "wednesday":
	if post == "food & hygine":
		print(post,"will be elected")
		print(post,"incharge of kichen")
if day == "thrusday":
	if post == "FM":
		print(post,"will be elected")
		print(post,"incharge of facility of campus")
if day == "friday":
	if post == "IT":
		print(post,"will be elected")
		print(post,"incharge of laptops")
elif day == "saturday":
	if post == "health coodinator":
		print(post,"will be elected")
		print(post,"incharge of girls health in campus")
	else:
		print(post,"incharge of council members")
else:
	print("no other day have to be elected")
	vote = input("enter your name")
	vote1 = input("enter your name1")
	vote2 = input("enter your name2")
	vote3 = input("enter your name3")
	if vote > vote1 and vote1 > vote2 and vote2>vote3:
		print(vote,"she selected for disco post")
	elif vote1 > vote2 and vote3 > vote2 and vote2>vote:
		print(vote1,"have been selected for T&P post")
	elif vote2>vote1 and vote3>vote2  and vote1>vote:
		print(vote2,"have been selected for food & hygini")
	elif vote3>vote2 and vote2>vote1 and vote1>vote2:
		print(vote3,"have been selected")
	else:
		print("no one selected")
	i = i + 1
