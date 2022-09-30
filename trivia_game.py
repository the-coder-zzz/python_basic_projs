print("-----------------------------------------\n")
print("-WELCOME TO MY TRIVIA GAME ABOUT PYTHON!-\n")
print("-----------------------------------------\n")
print("          Do you want to play?")

playing = input("> ")
if playing.lower() != "yes":
    quit()

print("\nOkay let's play! \n")
score = 0

print("1. Who created the Python programming language?")
answer = input("> ")
if answer.lower() == "guido van rossum":
    print("/Correct!")
    print("The Python programming language was created by Guido Van Rossum in 1991.\n")
    score += 1
else:
    print("Wrong!\n")

print("2. Which of these languages does Python resemble in its class syntax?")
answer = input("> ")
if answer.lower() == "c++":
    print("/Correct!")
    print("C++ uses the 'class' keyword for describing self contained entities called 'Objects' in the Object Oriented Programming jargon. Python has borrowed the 'class' keyword from C++ for describing objects.\n")
    score += 1
else:
    print("Wrong!\n")

print("3. What is the Java implementation of Python popularly known as ?")
answer = input("> ")
if answer.lower() == "jython":
    print("/Correct!")
    print("Python has two popular implementations, one that uses C and another that uses Java. The former is known as CPython (or just 'Python', since it is the most popular) and the latter is called as Jython or JPython.\n")
    score += 1
else:
    print("Wrong!\n")

print("4. Who composed a poem called ‘The Zen of Python’ about Python programming\n")
answer = input("> ")
if answer.lower() == "tim peters":
    print("/Correct!")
    print("Tim Peters, a major contributor to the Python community, wrote this poem to highlight the philosophies of Python.\n")
    score += 1
else:
    print("Wrong!\n")

print("5. The python is named about the popular British comedy troupe which is?")
answer = input("> ")
if answer.lower() == "monty python":
    print("/Correct!")
    print("The language’s name isn’t about snakes, but about the popular British comedy troupe Monty Python (from the 1970s).\n")
    score += 1
else:
    print("Wrong!\n")

print("Congratulations! You got " + str(score) + " question/s correct!")
print("You got " + str(score / 5 * 100) + "%")