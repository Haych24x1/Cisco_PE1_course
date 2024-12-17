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

# Literals - the data in itself
print("2") # String
print(2) # Int

# Integers
print(0o123) # Octal Number Representation  - Only take numbers from 0-7 if 0o is in the number
print(0x123) # Hexadecimal Representation - It's a number with a decimal that value is equals to 291.
print("\n")
# You can tell the difference 0o is for Octal number. 0x is for Hexadecimal

# Floats
# Decimal point is essential for recognizing floating-point numbers within python
# Int vs Floats
print(int(4)) # Int
print(float(4.0), "\n") #Float

# Coding floats
print(0.0000000000000000000001, "\n")
# Python always chooses the more economical form of the number's presentation, 
# and you should take this into consideration when creating literals.

# Strings
print("I like \"Monty Python\", \n")

# Python can use an apostrophe instead of a quote. Either of these characters may delimit strings, but you must be consistent
print('I like "Monty Python"')

# Coding strings
print('I\'m Monty Python.\n')
print("I'm Monty Python.")
