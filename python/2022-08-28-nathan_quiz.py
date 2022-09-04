import getpass, sys

# Print question and return user input
def question_with_response(num, prompt):
    if num > 0: 
        print("Question " + str(num) + ": " + prompt)
    else:
        print("Question: " + prompt)
    msg = input()
    return msg

# Number of questions
questions = 7 

# Correct answer counter
correct = 0

# Intro
print('Hello everyone!, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
rsp = question_with_response(0, "Let's see how smart you are! Ready to take a quiz?")
if rsp == "no":
    print("Sorry, you must take it!")
    correct += 1  
else:
    print("Okay!")

# Start questions
rsp = question_with_response(1, "What command is used to include other functions that are developed?")
if rsp == "import":
    print(rsp + " is correct!")
    correct += 1  
else:
    print(rsp + " is incorrect!")

rsp = question_with_response(2, "What command in this example is used to evaluate a response?")
if rsp == "if":
    print(rsp + " is correct!")
    correct += 1  
else:
    print(rsp + " is incorrect!")

rsp = question_with_response(3, "Each 'if' command contains an '_________' to determine a true or false condition?")
if rsp == "expression":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response(4, "What is two or more lines of code called?")
if rsp == "sequence":
    print(rsp + " is correct!")
    correct += 1  
else:
    print(rsp + " is incorrect!")

rsp = question_with_response(5, "What is the dynamic result of the input command?")
if rsp == "msg":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response(6, "What is a keyword in Python that defines a function?")
if rsp == "def":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response(7, "What is it called when you group a sequence of commands (often repeatedly)")
if rsp == "procedural abstraction":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

# Calculate percentage
q_percent = 100 * correct / questions
formatted_q_percent = "{:.0f}".format(q_percent)  # Rounding

# Results
print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions) + " or " + str(formatted_q_percent) + "%")