class Favorite_Animal:

	def __init__(self, arm_length, leg_length, number_of_eyes, tail, is_it_furry):

		#Length in feet

		self.arm_length = arm_length
		self.leg_length = leg_length
		self.number_of_eyes = number_of_eyes
		self.tail = tail
		self.is_it_furry = is_it_furry

	def __str__(self):

		output = "Arm length: " + str(self.arm_length)
		output += "\nLeg Length: " + str(self.leg_length)
		output += "\nNumber of Eyes: " + str(self.number_of_eyes)
		output += "\nHas tail?: " + str(self.tail)
		output += "\nIs furry?: " + str(self.is_it_furry) + "\n"
		return output

def main():

	#call stuffs
	print()

	animal_1 = Favorite_Animal(2.0, 6.6, 2, True, False)
	print(animal_1)


# When we run the program, this executes first
if __name__ == '__main__':

	main()