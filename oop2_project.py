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
        if user_input=='1':
            pass            
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()



ok=chatbook()