#dictionary demo
print("My first Python Dictionary Program \n")
dict = {}
temp=1
while temp==1:
	print("Enter 1 for adding new contact")
	print("Enter 2 for printing all contacts")
	print("Enter 3 for viewing specific contact")
	print("Enter 4 for deleting a specific contact")
	print("Enter 5 for editing a contact")
	print("Enter 6 for adding another number")
	print("Enter 7 for deleting a specific number of any contact")
	x=int(input())
	if x==1:
		print("Enter the name of new contact")
		key=input()
		print("Enter the number of ",key)
		value=input()
		dict[key]=[value]
		print("succesfully added")
	elif x==2:
		print(dict)
	elif x==3:
		print("Enter a name of contact to view it")
		key=input()
		print(dict[key])
	elif x==4:
		print("Enter a name of contact to delete it")
		key=input()
		del dict[key]
		print("Successfully deleted")
	elif x==5:
		print("Enter the name of the contact to be edited")
		key=input()
		print("Enter the new number for ",key)
		value=input()
		dict[key]=[value]
	elif x==6:
		print("Enter the name of the contact to which you want to add another number")
		key=input()
		print("Enter another number to be added to ",key)
		value=input()
		dict[key].append(value)
	elif x==7:
		print("Enter the name of the contact")
		key=input()
		print("Enter the number to be deleted")
		num=input()
		count=0
		for y in dict[key]:
			if num==y:
				dict[key].pop(count)
				count+=1
		print("Deleting succesful")
	else:
		print("bye bitch")
		break
