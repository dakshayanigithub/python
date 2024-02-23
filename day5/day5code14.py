class college:
    def __init__(self,name):
        self.name=name
        self.ece1()
        self.ece2()
    def ece1(self):
        print("This is ECE-A",self.name)
    def ece2(self):
        print("This is ECE-B",self.name)
s=input()
obj=college(s)
