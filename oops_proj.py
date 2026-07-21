class chatbook:
  
  __user_id = 1
  
  def __init__(self):
    self.id = chatbook.__user_id
    chatbook.__user_id += 1
    self.__name= "Default user"
    self.username = ''
    self.passward = ''
    self.loggin = False
    # self.menu()
    
  
  @staticmethod 
  def get_id(self):
     return chatbook.__user_id
  
  @staticmethod
  def set_id(value):
    chatbook.__user_id = value  
    
  def get_name(self):
      return self.__name
    
  def set_name(self,value):
      self.__name = value
    
  def menu(self):
    user_ip = input("""Welcome to CHatbook !! How wold you like to proceed?
                    1. press 1 to signup
                    2. press 2 to signin
                    3. press 3 to write a post
                    4. press 4 to message a friend
                    5. press any other key to exit
                    
                    ->""")
    
    if user_ip == "1":
      self.siginup()
    elif user_ip =="2":
      self.siginin()
    elif user_ip == "3":
      self.my_post()
    elif user_ip == "4":
      self.sendmsg()
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
        self.loggin = True
        
      else:
        print("Please input correct credentials..")
    print("\n")
    self.menu()
    
  def my_post(self):
    if self.loggin == True:
      txt = input("Enter your msg here -> ")
      print(f"Following content has been posted -> {txt}")
    else:
      print("You need to signin first to post something..")
    print("\n")
    self.menu()
      
  def sendmsg(self):
    if self.loggin == True:
      txt = input("Enter your msg here -> ")
      frnd = input("Who to send the msg? -> ")
      print(f"Your msg has been sent to {frnd}")
    else:
      print("You need to signin first to post something..")
    print("\n")
    self.menu()
     