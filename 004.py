print("Please enter your age")
num = input()
try:
	if int(num) > -1:
		print("Your age is", num)
	else:
		print("Age cannot be less then Zero")
except ValueError:
	print("Value Error: Please provide numeric value")