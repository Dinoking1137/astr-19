def f(x):

	output = x**3
	output += 8

	print("f(x): ", output)

	if(output>27):
		print("YAY!\n")

# This defines the main() function for our program
def main():

	#call stuffs
	print()
	f(9)


# When we run the program, this executes first
if __name__=='__main__':

	main()