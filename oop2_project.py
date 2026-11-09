# it is a dummy project for practice
# making a chatbook

class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.login=False
        self.menu()


    def menu(self):
        user_input=input("""Welcome to the Chatbook . How would you like to proeceed
                            1 -  press 1 to sign up
                            2 -  press 2 to login
                            3 -  press 3 to post message
                            4 -  press 4 to send message to a friend
                            5 -  press any number to exit
                            
                            ->""")
        if user_input == '1':
            self.signup()     
        elif user_input == '2':
            self.signin()            
        elif user_input == '3':
            self.mypost()
        elif user_input == '4':
            self.message()
        else:
            exit()


    def signup(self):
        email=input("enter email/username : ")
        pwd=input("enter password: ")
        self.username=email
        self.password=pwd
        print("you have sucessfully signed up")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print('please sign up first ')
        else:
            uname=input("enter username/email: ")
            pwd=input("enter password: ")
            if self.username==uname and self.password==pwd:
                print("you have successfully loged in ")
                self.login=True
            else:
                print("please input correct credential")
        self.menu()

    def mypost(self):
        if self.login==True:
            txt=input("enter message for your post: ")
            print(f"following content has been posted {txt}")
            print("\n")
        else:
            print("please signup first")
            print("\n")
        self.menu()

    def message(self):
        if self.login==True:
            txt=input("enter your message to send your friend : ")
            frnd=input("enter your friend name : ")
            print(f"your message has been sent to {frnd}")

        else:
            print("please signup first")
            print('\n')
            



ok=chatbook()