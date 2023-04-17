credentials = {
    "alice": "alice123", 
    "bob" : "bob123"
    }

username = input("enter your username:")
password = input("enter your password:")

if username in credentials:
    org_pass = credentials[username] 
    #org_pass = credentials["alice"]

    if password == org_pass:
        print("login successful")
    else:
        print("Unsuccessful")
else:
    print("no such user")
    


# if username ==  credentials ["alice"] and password == credentials["password"]:
#  print("login success")
# else:
#  print("login failed")
 
 