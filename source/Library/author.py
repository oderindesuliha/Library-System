class Author:


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    # def __repr__(self):
    # return f"{self.first_name} {self.last_name}"


