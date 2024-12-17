# Function_name(argument)
print("Hello, world!\n")

# Working with the print() function
# Sample Solution

print("Hello, Python!")
print("Hamza\n")
# print(Greg)
# print"Greg"
# print('Greg')
# print("Greg") print("Python")
# ...</sampleSolution>

# Instructions
print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.\n")

# Print empty space
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.\n")

# Python escape and newline characters
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.\n")

# Using multiple arguments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.\n")

# Positional arguments
print("My name is", "Python.")
print("Monty Python.\n")

# Keyword arguments
print("My name is", "Python.", end=" ")
print("Monty Python.\n")

print("My", "name", "is", "Monty", "Python.\n", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

# The print() function and its arguments
print("\nProgramming","Essentials","in", sep="***",end="...")
print("Python.\n")

# Formatting the output
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  ***** \n")

# Twice as large
print("         *")
print("       *   *")
print("     *       *")
print("   *           *")
print("  *              *")
print(" *****        *****")
print("     *        *")
print("     *        *")
print("     *        *")
print("     *        *")
print("     *        *")
print("     *        *")
print("     *        *") 
print("     **********")

# Duplicate string
print("\n")
print("         *          "*2)
print("       *   *        "*2)
print("     *       *      "*2)
print("   *           *    "*2)
print("  *              *  "*2)
print(" *****        ***** "*2)
print("     *        *     "*2)
print("     *        *     "*2)
print("     *        *     "*2)
print("     *        *     "*2)
print("     *        *     "*2)
print("     *        *     "*2)
print("     *        *     "*2) 
print("     **********     "*2)
print("\n")

# Correct Answer from Cisco
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

# 2.1.15 SECTION QUIZ
#Question 1: What is the output of the following program?
print("\n")
print("My\nname\nis\nBond.", end=" ")
print("James Bond.\n")

# Question 2: What is the output of the following program?
#print(sep="&", "fish", "chips")

# error message
#File "main.py", line 1
#    print(sep="&", "fish", "chips")
#                  ^
#SyntaxError: positional argument follows keyword argument
#Remember: Keyword arguments should be passed after any required positional arguments.

# Question 3: Which of the following print() function invocations will cause a SyntaxError?

#print('Greg\'s book.')
#print("'Greg's book.'")
#print('"Greg\'s book."')
#print("Greg\'s book.")
#print('"Greg's book."')

# Line 5 will raise SyntaxError, because the ' symbol in the Greg's book. string requires an escape character.


