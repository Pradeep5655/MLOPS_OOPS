from oops_proj import chatbook

# user1 = chatbook()

# func vs mthd
# lst = [1,2,3]

# function
# a1 = len(lst)
# print(a1)

# method
user1 = chatbook()
print("uid of user1 : ", user1.id)

# using static method directly from class rather that obj
chatbook.set_id(10)


user2 = chatbook()
print("uid of user2 : ", user2.id)

user3 = chatbook()
print("uid of user3 : ", user3.id)
# print(user1._chatbook__name)

# getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

# user1.sendmsg() 
