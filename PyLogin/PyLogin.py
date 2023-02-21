import time
import pwinput
import re
from replit import db


#checkPass
def checkPass(username, password):
  trials = 0
  if db[username] == password:
    print("SUCCESSFULL LOGIN...WELCOME :)")

  while password != db[username] and trials<3:
    print("Incorrect password...Try again")
    password = pwinput.pwinput(prompt="Re-enter password: ", mask="*")
    trials = trials + 1

    while password != db[username] and trials>=3:
      print("Incorrect password...Wait 60 seconds to try again")
      time.sleep(60)
      password = pwinput.pwinput(prompt="Re-enter password: ", mask="*")
      trials = trials + 1
    

    if db[username] == password:
      print("SUCCESSFULL LOGIN...WELCOME :)")

#passAuth

def passAuth(y,x):
    pass_pattern = "^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    pat = re.compile(pass_pattern)               
    mat = re.search(pat, x)
    if mat:
        print("Password is valid.")
        print("Welcome")
        conf_pass = pwinput.pwinput(prompt="Confirm password: ", mask="*")
        if conf_pass == x:
            print("Passwords match")
            print("Updating database with entered credentials")
            db.update({y:x})
        else:
            print("Passwords do not match")
            password = pwinput.pwinput(prompt="Create your password: ", mask="*")
            passAuth(y,password)
    else:
        print("Password invalid !!") 
        password = pwinput.pwinput(prompt="Create your password: ", mask="*")
        passAuth(y,password)

#main
def main():
    start = input("Type Login or Sign Up: ")

    if start.lower() == 'login':
        login()
    if start.lower() == 'sign up':
        signup()

#Login
def login():
    username = input("Enter username or type sign up: ")

    if username in db: 
        password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
        checkPass(username, password)
    elif username.lower() == 'sign up':
        signup()
    else:
        print("Incorrect username")
        login()

#Sign up
def signup():
    username = input("Create a username: ")
    if username in db:
        print('Username already taken...try another one')
        signup()
    else:
        print('Username accepted\n')
        print('''Password criteria:
        MUST contain at least 8 characters,
        MUST contain at least one uppercase letter,
        MUST contain at least one number,
        MUST contain at least one special character (!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~ )
        ''')
        
    
        password = pwinput.pwinput(prompt="Create your password: ", mask="*")
        passAuth(username,password)



main()