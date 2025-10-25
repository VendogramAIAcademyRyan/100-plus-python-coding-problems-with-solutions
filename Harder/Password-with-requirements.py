import random
import string
 
def randomPassword(size):
	all_chars = string.ascii_letters + string.digits + string.punctuation
	password = ""
	password += random.choice(string.ascii_lowercase)
	password += random.choice(string.ascii_uppercase)
	password += random.choice(string.digits)
	password += random.choice(string.punctuation)
	
	for i in range(pass_len-4):
		password += random.choice(all_chars)
	return password
active =True
while active:
        
        try:
            pass_len = int(input("What would be the password length? "))
            if pass_len <= 3:
                print("this is too short")
            else:
                print ("First Random Password is:", randomPassword(pass_len))
                print ("Second Random Password is:", randomPassword(pass_len))
                print ("Third Random Password is:", randomPassword(pass_len))
                active =False
        except ValueError:
            print("ENTER AN INTEGER!!!!!!!")
