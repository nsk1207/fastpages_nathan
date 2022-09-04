import getpass, sys

SubjectList = ["Math", "History"]

QandA = []

# math
QandA.append({
    "What is 10 times 14?": "140", 
    "What is 3 times 8?": "24", 
    "What is 10 divided by 2?": "5",
    "What is 20 times 6?": "120",
    "What is 4 times 15?": "60"
    })

# history
QandA.append({
    "When did the Civil War start?": "1861", 
    "Who was the first president?": "George Washington"
    })

# Number of questions
#questions = len(QandA)

# Print question and return user input
def question_with_response(prompt):
    print("Question " + ": " + prompt)
    msg = input()
    return msg

scores = [0 , 0]

# Intro
print('Hello everyone!, ' + getpass.getuser() + " running " + sys.executable)
print("Let's see how smart you are! Ready to take a quiz?")

# Start questions
def for_loop_index():    
    # subject index
    s = 0    
    for subject in QandA:
        print("\nSubject: " + SubjectList[s])
        for ques, ans in subject.items():        
            #print(ques, ans)
            rsp = question_with_response(ques)
            if rsp == ans:
                print(rsp + " is correct!")
                scores[s] += 1 
            else:
                print(rsp + " is incorrect!")
        # subject index increase
        s += 1
    
    print()
    print("Correct answers in " + SubjectList[0] + ": " + str(scores[0]) + " out of " + str(len(QandA[0])))
    print("Correct answers in " + SubjectList[1] + ": " + str(scores[1]) + " out of " + str(len(QandA[1])))
    return

#for_loop_index()

# add a new math question with input
print("Please add a questions in Math")
newq = input()
print("Please add corresponding answer")
newa = input()

#add new question and answer
temp_dict = {newq: newa}
QandA[0].update(temp_dict)


for_loop_index()