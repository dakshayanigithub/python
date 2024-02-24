class training:
    def __init__(self):
        print("This is class training")
class ece1(training):
    def __init__(self):
        super().__init__()
        print("This is class ece1")
class ece2:
    def __init__(self):
        print("This is class ece2")

class ece3(ece2):
    def __init__(self):
        super().__init__()
        print("This is class ece3")
class ece4:
    def __init__(self):
        print("This is class ece4")
a=ece1()
b=ece3()
c=ece4()
