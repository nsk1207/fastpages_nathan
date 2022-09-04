InfoDb = []

# InfoDB is a data structure with expected Keys and Values

# Append to List a Dictionary of key/values related to a person and cars
InfoDb.append({
    "FirstName": "Nathan",
    "LastName": "Kim",
    "DOB": "December 7",
    "Residence": "San Diego",
    "Email": "nathank51687@stu.powayusd.com",
    "Hobbies": ["Grinding SAT", "Listening to Music", "Watching TV"]
})

# Append to List a 2nd Dictionary of key/values
InfoDb.append({
    "FirstName": "Max",
    "LastName": "Wu",
    "DOB": "January 12",
    "Residence": "San Diego",
    "Email": "mwu@powayusd.com",
    "Hobbies": ["Watching TV", "Listening to Music", "Skating"]
})

# Append to List a 3rd Dictionary of key/values
InfoDb.append({
    "FirstName": "Bob",
    "LastName": "Bobby",
    "DOB": "January 10",
    "Residence": "San Diego",
    "Email": "bbobby@powayusd.com",
    "Hobbies": ["Biking", "Eating", "Walking"]
})

# Append to List a 3rd Dictionary of key/values
InfoDb.append({
    "FirstName": "Robert",
    "LastName": "Lee",
    "DOB": "February 11",
    "Residence": "San Diego",
    "Email": "asmith@powayusd.com",
    "Hobbies": ["Biking", "Eating", "Walking"]
})

# Print the data structure
#print(InfoDb)

# print function: given a dictionary of InfoDb content
def print_data(d_rec):
    print(d_rec["FirstName"], d_rec["LastName"])  # using comma puts space between values
    print("\t", "Residence:", d_rec["Residence"]) # \t is a tab indent
    print("\t", "Birth Day:", d_rec["DOB"])
    print("\t", "Hobbies: ", end="")  # end="" make sure no return occurs
    print(", ".join(d_rec["Hobbies"]))  # join allows printing a string list with separator
    print()


# for loop algorithm iterates on length of InfoDb
def for_loop():
    print("For loop output\n")
    for record in InfoDb:
        print_data(record)

#for_loop()

# while loop algorithm contains an initial n and an index incrementing statement (n += 1)
def while_loop():
    print("While loop output\n")
    i = 0
    while i < len(InfoDb):
        record = InfoDb[i]
        print_data(record)
        i += 1
    return

#while_loop()

# for loop with index
def for_loop_index():
    print("For loop with index output\n")
    for i in range(0, len(InfoDb), 1):
        record = InfoDb[i]
        print_data(record)
    return

#for_loop_index()

# reverse order
def for_loop_index_reverse():
    print("Reverse order\n")
    for i in range(len(InfoDb)-1, -1, -1):
        record = InfoDb[i]
        print_data(record)
    return

for_loop_index_reverse()