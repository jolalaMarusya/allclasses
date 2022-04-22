class Book:
    def __init__(self,nazv,author,numbS,price):
        self.nazv=nazv
        self.author=author
        self.numbS=numbS
        self.price=price
    def Prog(self):
        if self.nazv.find("Програм") >= 0 or self.nazv.find("програм") >= 0 :
            return ("Двойная цена за книги по программированию",self.price * 2)
        else:
            return("Книга не по программированию")
    def Cr(self):
        return ("Редактирование одной страницы",self.numbS * 3)
    def Vivod(self):
        print(self.nazv," ", self.author," ",self.numbS," ",self.price)

#nazv1=input("Введите название книги")
#author=input("Автор")
#numbS=int(input("Количество страниц"))
#price=int(input("Цена"))
#ff2=Book(nazv1, author,numbS,price)
#ff2.Vivod()


for i in range(1):
    print("Номер книги",i)
    nazv1=input("Введите название книги")
    author1=input("Автор")
    numbS1=int(input("Колво стр"))
    price1=int(input("цена"))
    ff2=Book(nazv1, author1,numbS1,price1)
    ff2.Vivod()
    print(ff2.Cr())
    print(ff2.Prog())
