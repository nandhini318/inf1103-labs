print("============================")
print("Welcome here")
print("My first post!")
print("============================")
username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)
followers = 100

followers += 50
print("Followers after first increase:", followers)

followers += 20
print("Followers after second increase:", followers)

followers -= 10
print("Followers after decrease:", followers)
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print()
print("Instagram Profile")
print("====================")
print("Username:", username)
print("Age:", age)
print("Category:", category)
if age > 40 and category == "fun":
    print("You are old what is fun for you??")