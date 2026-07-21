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
      self.siginup()
    elif user_ip =="2":
      self.siginin()
    elif user_ip == "3":
      pass
    elif user_ip == "4":
      pass
    else:
      exit()
      
  def siginup(self):
    email = input("Enter your mail here -> ")
    pwd = input("Enter your passward here ->")
    self.username = email
    self.passward = pwd      
    print("You have signed up succesfully !!")
    print("\n")
    self.menu()
    
  def siginin(self):
    if self.username=='' and self.passward=='':
      print("Please signup first by pressing 1 in the main menu")
    else:
      uname = input("Enter your mail/username here -> ")
      pwd = input("Enter your passward here -> ")
      if self.username==uname and self.passward==pwd:
        print("You have signed in successfully !!")
        self.loggin == True
        
      else:
        print("Please input correct credentials..")
    print("\n")
    self.menu()
     
     
obj = chatbook()
    