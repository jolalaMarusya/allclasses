class Tovar:
    def __init__ (self,nazv=str(input("Название товара=")), st=int(input("Стоимость=")),kol=int(input("Количество=")),nom=int(input("Номер заказа="))):
        self.nazv = nazv
        self.st = st
        self.kol = kol
        self.nom = nom

    def stoi(self):
        print("Стоимость товара = ", self.st*self.kol)

    def Nazzv(self):
        print("Название товара = ", self.nazv)

class Zakaz(Tovar):
    def __init__(self,nazv=str(input("Название товара=")), st=int(input("Стоимость=")),kol=int(input("Количество=")),nom=int(input("Номер заказа=")),FIO=str(input("Фамилия имя отчество=")),PASD=str(input("Паспортные данные=")),adr=str(input("Адрес="))):
        self.FIO = FIO
        self.PASD = PASD
        self.adr = adr

        Tovar.__init__(self,nazv,st,kol,nom)

    def infa(self):
        print("Фамилия имя отчество = ",self.FIO,";", "Паспортные данные = ", self.PASD, ";", "Адрес", self.adr,";")
    def Fem(self):
        print("Фамилия имя отчество = ",self.FIO)

r1 = Zakaz ()
r1.infa()
r1.stoi()
r1.Nazzv()
r1.Fem()
