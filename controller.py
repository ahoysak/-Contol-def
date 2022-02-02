from user_functions import Functions
functionss = Functions




class Controller(Functions):
    def adduser(self):
        self.user_add()

    def get_users(self):
        self.get_all()

    def search_id(self):
        self.what_to_search = input('By Which Parametr you want to search: ')
        self.search_str = input('Search: ')
        self.search_by(self.search_str,self.what_to_search)

    def update_users(self):
        self.update_user()

    def menu_run(self):
        while True:
            print("1. Add New User\n"
                + "2. Get All Users\n"
                + "3. Search\n"
                + "4. Update User By Id"
                 )
            menu_flag = int(input("Type your choose: "))
            if menu_flag == 1:
                self.adduser()
            elif menu_flag == 2:
                self.get_users()
            elif menu_flag == 3:
                self.search_id()
            elif menu_flag == 4:
                self.update_users()