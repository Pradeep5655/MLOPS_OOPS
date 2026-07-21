class chatbook:
  def __init__(self):
    self.username = ' '
    self.passward = ''
    self.loggin = False
    self.menu()
    
  def menu(self):
    user_ip = input("""Welcome to CHatbook !! How wold you like to proceed?
                    1. press 1 to signup
                    2. press 2 to signin
                    3. press 3 to write a post
                    4. press 4 to message a friend
                    5. press any other key to exit""")
    if user_ip == "1":
      pass
    elif user_ip =="2":
      pass
    elif user_ip == "3":
      pass
    elif user_ip == "4":
      pass
    else:
      exit()
      
obj = chatbook()
    