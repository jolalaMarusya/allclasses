class treyg:
    def __init__(self,w,h,j):
        self.w = w
        self.h = h
        self.j = j

    def sych(self):
        if (self.w + self.h > self.j) and (self.w+self.j>self.h) and (self.j+self.h>self.w):
            return ("Да")
        else:
            return ("Нету")
    def perimetr(self):
        return (self.w + self.h + self.j)
    def plosh(self):
        pp=(self.w + self.h + self.j)//2
        return (pp*(pp-self.w)*(pp-self.h)*(pp-self.j))**(1./2)
r1 = treyg(4,5,7)
print(r1.sych())
print("Периметр=",r1.perimetr())
print("Площадь=",r1.plosh())
