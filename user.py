class User:

    def __init__(self, id, username, email, password, role):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__password = password
        self.__role = role

    def __int__(self):
        pass

    def view(self):
        print(self.__id, self.__username, self.__email, self.__password, self.__role)
        return f"{self.__id} {self.__username} {self.__email} {self.__password} {self.__role}"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role