class Igryshka:
    def __init__(self,nazv,date,cost,vozrast):
        self.nazv=nazv
        self.date = date
        self.cost = cost
        self.vozrast = vozrast
    def Vivod_infa(self):
        print("Название игрушки",self.nazv,"Год сборки",self.date,"Цена",self.cost,"Возрастное ограничение",self.vozrast)
    def opred_vozrast(self):
        if self.vozrast <= 0:
            return "Для новорождённых"
        elif self.vozrast > 0 and self.vozrast <= 6:
            return "Для ребёнка"
        elif self.vozrast >6 and self.vozrast <= 12:
            return "Для дошколят"
        elif self.vozrast >12 and self.vozrast <18:
            return "Для подростков"
        elif self.vozrast >=18:
            return "Для взрослых"

    def plysh(self):
        if self.nazv.find("мягк") >= 0 or self.nazv.find("Мягк") >= 0 :
            return "Это плюшевая игрушка"
        else:
            return "Это не плюшевая игрушка"

nazv1 = input("Введите название игрушки")
date1 = int(input("Введите год сборки"))
cost1 = int(input("Введите цену игрушки"))
vozrast1 = int(input("Введите возраст игрушки"))
igr22=Igryshka(nazv1,date1,cost1,vozrast1)
igr22.Vivod_infa()
print(igr22.opred_vozrast())
print(igr22.plysh())
