#Part 1: printing inputed varables - Solved
"""
age = str(input("How old are you?"))
height = str(input("How tall are you?"))
weight = str(input("How much do you weigh?"))

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
"""
#-----------------------------------------------------------
#Part 2: dealing with writing texts in files - Solved, but not too good
filename = 'example.txt'

txt = open(filename)

print("Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#-----------------------------------------------------------
#Part 3: printing with tab and breaking lines - Solved
print("Let's practice everything.")
print("You'd need to know about escapes with \'that do:")
print("\n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print("--------------")
print(poem)
print("--------------")

#-----------------------------------------------------------
#Part 4: Some function with math operations and printing - Solved
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars + 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

#-----------------------------------------------------------
#Part 5: conditionals - Solved

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
elif people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")
elif people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
elif people <= dogs:
    print("People are less than or equal to dogs.")