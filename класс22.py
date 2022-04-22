from math import sqrt
class yravn:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def disk(self):
        self.d=self.b**2 - 4 *self.a * self.c
        return self.d

#    def proverka(self):
 #       if self.d == 0:
  #          return "Один корень"
   #     elif self.d >0:
    #        return "Два корня"
     #   elif self.d < 0:
      #      return "Нету решения"

    def korn12(self):
        if self.d == 0:
            return (-self.b/2*self.a)
        elif self.d > 0:
            return(("x1",(-self.b+(sqrt(self.d)))/(2*self.a)),("x2",(-self.b-(sqrt(self.d)))/(2*self.a)))
        elif self.d < 0:
            return "Нету решения"



r1=yravn(3,-14,-5,0)


print(r1.disk())
print(r1.korn12())
