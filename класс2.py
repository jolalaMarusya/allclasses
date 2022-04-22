class yrav:
    def __init__(self,w,h,j):
        self.w = w
        self.h = h
        self.j = j
    def resh1(self):
        return(self.w-self.h)//self.j
r1 = yrav(10,5,1)
print("y(x)=",r1.resh1())
