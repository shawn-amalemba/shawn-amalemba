# Netflix type system demo - FakeFlix
import csv
import sys
import string  # for use in the secure password and other parts of the program


def main():
    menu()


def menu():
    print("************Welcome to KEMSA regional depot**************")
    print()

    choice = input("""
                      A: Please Register
                      B: Login
                      Q: Quit

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        register()
    elif choice == "B" or choice == "b":
        login()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

#where you define how your password should look like and what it should contain
def long_enough(pw):
    'Password must be at least 6 characters'
    return len(pw) >= 6


def short_enough(pw):
    'Password cannot be more than 12 characters'
    return len(pw) <= 12


def has_lowercase(pw):
    'Password must contain a lowercase letter'
    return len(set(string.ascii_lowercase).intersection(pw)) > 0


def has_uppercase(pw):
    'Password must contain an uppercase letter'
    return len(set(string.ascii_uppercase).intersection(pw)) > 0


def has_numeric(pw):
    'Password must contain a digit'
    return len(set(string.digits).intersection(pw)) > 0


def has_special(pw):
    'Password must contain a special character'
    return len(set(string.punctuation).intersection(pw)) > 0


def test_password(pw, tests=[long_enough, short_enough, has_lowercase, has_uppercase, has_numeric, has_special]):
    for test in tests:
        if not test(pw):
            print(test.__doc__)
            return False
    return True


def register():
    # user is prompted to input all the required fields
    print(" Enter first name")
    global firstname
    firstname = input()
    print(" Enter surname")
    global surname
    surname = input()
    print(" Enter Date of Birth Format: dd/mm/yy")
    global dob
    dob = input()
    print(" Enter Gender")
    global gender
    gender = input()
    print(" Enter main genre of interest")
    global interest
    interest = input()
    print(" Enter email address")
    global email
    email = input()
    substring = dob[-4:]
    print(substring)
    print(" Your unique username is", firstname + surname + substring)
    global username
    username = firstname + surname + substring
    # secure password checker
    passwordchecker()

#confirms the password the user puts according to how it has been defined above.
def passwordchecker():
    password = input("Please enter a password - must be secure and meet our format requirements")
    if test_password(password):
        with open('kemsa.txt', 'a') as kemsa:
            kemsaWriter = csv.writer(kemsa)
            kemsaWriter.writerow(
                [username, password, firstname, surname, dob, gender, interest, email])
            print("Record has been written to file")
            kemsa.close()
            menu()
    else:
        passwordchecker()
#log in code... to enable the user to login after registering above
#it will pull information from the saved text file.
def login():
    print("***************PLEASE LOGIN***************")

    #we have now to pull the data from the txt file we saved when the user registerd
    #we use the code below
    with open("kemsa.txt", 'r') as kemsa:
    #prompt the user to key in his details to enable him or her to log in
        username=input("put in your username: ")
        password=input("put in your password: ")
    #calling the reader to read our saved file
        kemsaReader=csv.reader(kemsa)
        for row in kemsaReader:
            for field in row:

                if field==username and row[1]==password:
                    print("access granted")
                    displayfilms()
                    notloggedin="false"
#here we display what the user will see after logging in
def displayfilms():
    print("*****PLEASE PLACE YOUR ORDER*****")

# the program is initiated, so to speak, here
main()