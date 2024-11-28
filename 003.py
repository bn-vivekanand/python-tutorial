#ERROR HANDLING
def dividefun(num):
	try:
		return 42 / num
	except ZeroDivisionError:
		print("Error: You tried to divide by Zero")
print(dividefun(2))
print(dividefun(0))