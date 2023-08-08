class Animals():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Animal was created")

    def eat(self):
        '''eating animal'''
        print(self.name + " are eating")

    def sleep(self):
        '''sleeping animal'''
        print(self.name + " are sleeping")


lionAlex = Animals('Lion', "15")
print(lionAlex.name)
lionAlex.eat()
lionAlex.sleep()