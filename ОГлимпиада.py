class Olimp:
    def __init__(self,w,h,j):
        self.w = w
        self.h = h
        self.j = j

    def Score(self):
        if self.w > 10 or self.h > 10 or self.j > 10:
            return ("не по правилам,")
        else:
            return ("всё ок,")
    def Score2(self):
        if (self.w + self.h + self.j) > 30:
            return("нечестно")
        else:
            return("честно")
    def sum2(self):
        return (self.w + self.h + self.j)
    def avg2(self):
        return(self.w + self.h + self.j)//3


k = str(input())
r1 = Olimp(5,6,9)
print(k)
print("Проверка на очки:",r1.Score(),r1.Score2())
print("Сумма",r1.sum2())
print("Среднее кол-во баллов",r1.avg2())
