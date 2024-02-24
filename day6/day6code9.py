class A:
    def __init__(self,data1):
        self.data1=data1
        print("Data :",data1)
class B(A):
    def __init__(self,data1,data2):
        super().__init__(self.data1)
        self.data2=data2
        print("Data :",data2)
class C(B):
    def __init__(self,data1,data2,data3):
        self.data1=data1
        self.data2=data2
        super().__init__(data1,data2)
        self.data3=data3
        print("Data :",data3)
a,b,c=map(str,input().split())
obj=C(a,b,c)
