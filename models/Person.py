from DBConnection import DBConnection

class Person:
    def __init__(self):
        print("new Person successfully created!")
        self.db = DBConnection()
        print(self.db)

    def create(self,  username, password, name, email, address='', photoUrl='https://image.flaticon.com/icons/svg/149/149071.svg'):
        print("Person.save()")
        print(self.db)

        if username is None or password is None or name is None or email is None:
            print("error was thrown...")
            raise ValueError('Person.create() called with improper parameter. Username, name, and email MUST NOT be null')
        
        else:
            print("inserting values")
            sql = "INSERT INTO `person` (`name`, `username`, `password`, `address`, `email`, `photo_url`)\
                     VALUES (%s, %s, %s, %s, %s, %s)" % (name, username, password, address, email, photoUrl) 
            self.db.executeSQL(sql)

    def delete(self):
        # TODO:
        print("Person.delete()")


p = Person()
p.create("dro248", "asdfjkl;", "OSTLER, David", "david.ostler001@gmail.com", None, None)

