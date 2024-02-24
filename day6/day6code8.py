class string:
    def length(self,s):
        print("length :",len(s))
class A:
    def characters(self,s):
        v,c=[],[]
        for i in s:
            if i.lower() in "aeiou":
                v.append(i)
        else:
            c.append(i)
        print("vowels",v,"\nconsonents:",c)
class B:
    def count(self,s):
        for i in s:
            print(i,"count:",s.count(i))
class C(string,A,B):
    def __init__(self,data):
        self.data=data
        self.length(data)
        self.characters(data)
        self.count(data)
        print("completed")
x=input()
obj=C(x)
