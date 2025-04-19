import numpy as np #import numpy to create arrays
from tabulate import tabulate #python built-in package to make tables

# This defines the main() function for our program
def main():

	#help(np.linspace)

	#Generate an array of x and y values
	x = np.linspace(0, 2 * np.pi, 1000) # generate 10 values from -2 to 2 regularly spaced

	sinx = np.sin(x) #compute y-values from x-values, where y = sin(x)

	#Tables using tabulate
	# Create a list of tuples of size 2 containing all x and y values
	table_data = [(a, b) for a, b in zip(sinx, x)]

	# Create the table
	table_header = ["sin(x)", "x"]
	python_table = tabulate(table_data, tablefmt = "grid", headers = table_header, floatfmt = ".3f")
	print(python_table)

# When we run the program, this executes first
if __name__=='__main__':

	main()