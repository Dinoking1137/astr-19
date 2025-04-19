def floating_point_sum(a, b):

	c = a + b

	print("a + b: ", c)
	print("type(c)", type(c))
	print()

def integer_difference(a, b):

	c = a - b

	print("a - b: ", c)
	print("type(c)", type(c))
	print()

def floating_point_int_mult(a, b):

	c = a * b

	print("a * b: ", c)
	print("type(c)", type(c))
	print()

# This defines the main() function for our program
def main():

	#call stuffs
	print()
	floating_point_sum(1.0, 2.0)
	integer_difference(3, 1)
	floating_point_int_mult(3.1, 5)

# When we run the program, this executes first
if __name__=='__main__':

	main()