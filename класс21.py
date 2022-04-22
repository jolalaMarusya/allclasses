class Dvij:
    def __init__ (self,g,h,j,k):
        self.g=g
        self.h=h
        self.j=j
        self.k=k

    def sm_v_m(self):
        return (self.g/100)

    def Speed(self):
        return (self.g/self.h)

    def Speed_nerav(self):
        return (self.j*self.h+self.k)

r1=Dvij(100,5,6,30)

print(r1.sm_v_m())
print(r1.Speed())
print(r1.Speed_nerav())
    
