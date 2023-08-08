class Person():
    ''' Human model'''
    def __init__(self, name, age):
        ''' inicalization of human atribute - name,age'''
        self.name = name
        self.age = age
        print("Human was created")

    def sing(self):
        ''' Sing '''
        print(self.name + " are sing")

    def dance(self):
        ''' Dance '''
        print(self.name + " are dancing")

man = Person("Alex", 27)
woman =Person("Valery", 19)

print(man.name)
woman.sing()
man.dance()
man.sing()