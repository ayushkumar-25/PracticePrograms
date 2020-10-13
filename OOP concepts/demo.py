class Computer:
    
    def __init__(self):
        print("init")
    
    def config(self):
        print("i5, 16GB, 1TB")


com1 = Computer()
com2 = Computer()
com3 = Computer()


com1.config()
com2.config()

# __init__ will be automatically called for each object created.
# Here 3 objects is created (com1, com2, com3) therefore __init__ will be called for 3 times.