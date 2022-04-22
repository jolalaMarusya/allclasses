class int2:
    def __init__(self,w):
        self.w=w

    def chet_nechet(self):
        if self.w % 2 ==0:
            print("Чёт")
            self.w = self.w **2
            print(self.w)
        else:
            print("Нечёт")
            self.w=self.w **2
            print(self.w)
r1 = int2 (11)
r1.chet_nechet()
