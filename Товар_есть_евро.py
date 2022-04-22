class Tovar:
    def __init__(self,nazv,cost,date,aa):
        self.nazv=nazv
        self.cost=cost
        self.date=date
        self.aa=aa
    def skolko_let(self):
        if self.date == 2020:
            return("Товар 2020 года", aa1 + self.cost)
        else:
            return "Товар не 2020 года"
    def rubl_in_euro(self):
        return("В евро",self.cost * 93.54)

#a = (self.cost * 20)/ 100

nazv1 = input("Введите название товара")
cost1 = int(input("цена"))
date1 = int(input("год выпуска"))
aa1 = (cost1 * 20)/100
ff2=Tovar(nazv1, cost1,date1,aa1)
print(ff2.skolko_let())
print(ff2.rubl_in_euro())
        
