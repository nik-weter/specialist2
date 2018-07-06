class User:
    count = 0
    def __init__(self, n, l, p):
        self.__name = n
        self.__login = l
        self.__password = p
        User.count += 1

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n

    def get_login(self):
        return self.__login
    def set_login(self, n):
        print("You cant change lofin")
    login = property(get_login, set_login)
    def get_password(self):
        return '*******'
    def set_password(self, n):
        self.__password = n
    password = property(get_password, set_password)

    def show_info(self):
        return "{}: {}".format(self.name, self.login)

class SuperUser(User):
    count = 0

    def __init__(self, n, l, p, role):
        super().__init__( n, l, p)
        self.__role = role
        SuperUser.count += 1
        User.count -= 1
        #super(SuperUser, self).count -= 1

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, n):
        self.__role = n

user1 = User('John Lennon', 'lennon', '1234')
user2 = User('Ringo Star', 'star', '1234')
user3 = User('Pol MacCartny', 'pol', '1234')
admin = SuperUser('Test Test', 'test', '1234', 'administrator')
print(user1.show_info())
print(user2.login)
print(user3.password)
print(admin.role)
print(User.count)
print(SuperUser)
user3.login = 'asdqe'
admin.role = 'asdqwe'
print(admin.role)