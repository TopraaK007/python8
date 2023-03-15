# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import sqlite3


class Shoesdatabase():
    def __init__(self, name):
        self.name = name
        self.status = True
        self.dataBaseconnet()

    def run(self):
        self.menu()
        choice = self.choice()
        if choice == 1:
            self.add()
        if choice == 2:
            self.delete()
        if choice == 3:
            self.update()
        if choice == 4:
            while True:
                try:
                    select = int(input(
                        "1)Hepsini Göster\n2)Markaya Göre Göster\n3)Modele Göre Göster\n4)Renge Göre Göster\n5)Numaraya Göre Göster\n6)Adede Göre Göster\n7)Fiyata Göre Göster\nSeç:"))
                    if select < 1 or select > 7:
                        print("(1-7) arasında seçim yapınız")
                        continue
                    break
                except ValueError:
                    print("Lütfen (1-7) arasında seçim yapınız!")

            return self.showshoes(select)

        if choice == 5:
            self.exit()

    def menu(self):
        print("""
    *** HOŞGELDİNİZ ***

    1)VERİ EKLE
    2)VERİ SİL
    3)VERİ GÜNCELLE
    4)VERİ GÖSTER
    5)ÇIKIŞ""")

    def choice(self):
        while True:
            try:
                choice = int(input("Yapmak İstediğini Seçimi Giriniz:"))
                if choice < 1 or choice > 5:
                    print("(1-5) arasında seçim yapınız!!!")
                    continue
                break
            except ValueError:
                print("Lütfen (1-5) arasında değer giriniz!!!")
        return choice

    def add(self):
        marka = input("Marka giriniz:").lower().capitalize()
        cinsiyet = input("Cinsiyet Giriniz:").lower().capitalize()
        model = input("Model giriniz:").lower().capitalize()
        renk = input("Renk giriniz:").lower().capitalize()

        while True:
            try:
                numara = int(input("Numara giriniz:"))
                if numara < 10 or numara > 48:
                    print("Böyle bir numara yok!!!")
                    continue
                break
            except ValueError:
                print("Lütfen (10-48) arasında numara giriniz!!!")
        while True:
            try:
                adet = int(input("Adet giriniz:"))
                break
            except ValueError:
                print("Lütfen adet sayısını giriniz!")
        while True:
            try:
                fiyat = int(input("Fiyat giriniz:"))
                break
            except ValueError:
                print("Lütfen ürün fiyatını  giriniz!")
        self.cursor.execute(
            "INSERT INTO shoes VALUES('{}','{}','{}','{}',{},{},{})".format(marka, model, renk, cinsiyet, numara, adet,
                                                                            fiyat))
        self.connect.commit()
        print("{}-{}  kaydedildi.".format(marka, model))

    def delete(self):
        self.cursor.execute("SELECT * FROM shoes")
        allshoes = self.cursor.fetchall()

        convertall = lambda x: [str(y) for y in x]

        for sayi, shoes in enumerate(allshoes, 1):
            print("{})".format(sayi), "-".join(convertall(shoes)))

        while True:
            try:
                choice = int(input("Silmek istediğiniz ürün id giriniz:"))
                break
            except ValueError:
                print("Silmek istediğiniz ürün id giriniz!!!")

        self.cursor.execute("DELETE FROM shoes where rowid={}".format(choice))
        self.connect.commit()
        print("İşlem Başarılı.")

    def update(self):
        self.cursor.execute("SELECT * FROM shoes")
        allshoes = self.cursor.fetchall()

        convertall = lambda x: [str(y) for y in x]

        for sayi, shoes in enumerate(allshoes, 1):
            print("{})".format(sayi), "-".join(convertall(shoes)))

        while True:
            try:
                choice = int(input("Güncellemek istediğiniz ürün id giriniz:"))
                break
            except ValueError:
                print("Hata tekrar dene!")

        while True:
            try:
                updateselect = int(input("1)Marka\n2)Cinsiyet\n3)Model\n4)Renk\n5)Numara\n6)Adet7)Fiyat\nSeç:"))
                if updateselect < 1 or updateselect > 7:
                    print("Lütfen (1-7) arasında seçim yapınız!")
                    continue
                break
            except ValueError:
                print("Lütfen (1-7) arasında seçim yapınız!")
        operations = ["marka", "cinsiyet", "model", "renk", "numara", "adet", "fiyat"]

        if updateselect == 5:
            while True:
                try:
                    newvalue = int(input("Numara giriniz:"))
                    if newvalue < 10 or newvalue > 48:
                        print("Böyle bir numara yok!!!")
                        continue
                    break
                except ValueError:
                    print("Lütfen (10-48) arasında numara giriniz!!!")
            self.cursor.execute("UPDATE shoes set numara={} where rowid={}".format(newvalue, choice))
        if updateselect == 6:
            while True:
                try:
                    adet = int(input("Adet giriniz:"))
                    break
                except ValueError:
                    print("Lütfen adet sayısını giriniz!")
            self.cursor.execute("UPDATE shoes set adet={} where rowid={}".format(adet, choice))
            self.connect.commit()
        if updateselect == 7:
            while True:
                try:
                    fiyat = int(input("fiyat giriniz:"))
                    break
                except ValueError:
                    print("Lütfen ürün fiyatını giriniz!")
            self.cursor.execute("UPDATE shoes set fiyat={} where rowid={}".format(fiyat, choice))
        self.connect.commit()
        if updateselect not in (5, 6, 7):
            new = input("Yeni değeri giriniz:").lower().capitalize()
            self.cursor.execute(
                "UPDATE shoes set {}='{}' where rowid={}".format(operations[updateselect - 1], new, choice))
            print("Değerler güncellendi.")
            self.connect.commit()

    def showshoes(self, select):
        if select == 1:
            self.cursor.execute("SELECT * FROM shoes")
            all = self.cursor.fetchall()

            convertall = lambda x: [str(y) for y in x]

            for sayi, shoes in enumerate(all, 1):
                print("{})".format(sayi), "-".join(convertall(shoes)))

            self.connect.commit()

        if select == 2:
            self.cursor.execute("SELECT marka FROM shoes")

            marka = list(enumerate(list(self.cursor.fetchall()), 1))

            for sayi, shoes in marka:
                print("{}){}".format(sayi, shoes[0]))

            while True:
                try:
                    select = int(input("İstediğiniz markanın numarasını giriniz:"))
                    if select < 1 or select > sayi:
                        print("Böyle bir numara yok")
                        continue
                    break
                except ValueError:
                    print("Lütfen numara seçiniz!!")

            self.cursor.execute("SELECT * FROM shoes WHERE marka='{}'".format(marka[select - 1][1][0]))

            all = self.cursor.fetchall()

            convertall = lambda x: [str(y) for y in x]

            for sayi, shoes in enumerate(all, 1):
                print("{}){}".format(sayi, shoes[0]))

            self.connect.commit()

        if select == 3:
            self.cursor.execute("SELECT model FROM shoes")

            model = list(enumerate(list(self.cursor.fetchall()), 1))

            for sayi, a in model:
                print("{}){}".format(sayi, a[0]))

            while True:
                try:
                    select = int(input("Model numarasını seçiniz:"))
                    if select < 1 or select > sayi:
                        print("Böyle bir ürün bulunmamaktadır!")
                        continue
                    break
                except ValueError:
                    print("Lütfen numara giriniz!!!")

            self.cursor.execute("SELECT * FROM shoes WHERE model='{}'".format(model[select - 1][1][0]))

            all = self.cursor.fetchall()

            convertall = lambda x: [str(y) for y in x]

            for sayi, shoes in enumerate(all, 1):
                print("{})".format(sayi), "-".join(convertall(shoes)))

            self.connect.commit()
        if select == 4:
            self.cursor.execute("SELECT renk FROM shoes")

            renk = list(enumerate(list(self.cursor.fetchall()), 1))

            for sayi, a in renk:
                print("{}){}".format(sayi, a[0]))

            while True:
                try:
                    select = int(input("renk numarasını seçiniz:"))
                    if select < 1 or select > sayi:
                        print("Böyle bir ürün bulunmamaktadır!")
                        continue
                    break
                except ValueError:
                    print("Lütfen numara giriniz!!!")

            self.cursor.execute("SELECT * FROM shoes WHERE renk='{}'".format(renk[select - 1][1][0]))

            all = self.cursor.fetchall()

            convertall = lambda x: [str(y) for y in x]

            for sayi, shoes in enumerate(all, 1):
                print("{})".format(sayi), "-".join(convertall(shoes)))

            self.connect.commit()
        if select == 5:
            self.cursor.execute("SELECT numara FROM shoes")

            numara = list(enumerate(list(self.cursor.fetchall()), 1))

            for sayi, a in numara:
                print("{}){}".format(sayi, a[0]))

            while True:
                try:
                    select = int(input("Ürün numarasını seçiniz:"))
                    if select < 1 or select > sayi:
                        print("Böyle bir ürün bulunmamaktadır!")
                        continue
                    break
                except ValueError:
                    print("Lütfen numara giriniz!!!")

            self.cursor.execute("SELECT * FROM shoes WHERE numara={}".format(numara[select - 1][1][0]))

            all = self.cursor.fetchall()

            if select == 6:
                self.cursor.execute("SELECT adet FROM shoes")

                adet = list(enumerate(list(self.cursor.fetchall()), 1))

                for sayi, a in adet:
                    print("{}){}".format(sayi, a[0]))

                while True:
                    try:
                        select = int(input("Ürün numarasını seçiniz:"))
                        if select < 1 or select > sayi:
                            print("Böyle bir ürün bulunmamaktadır!")
                            continue
                        break
                    except ValueError:
                        print("Lütfen numara giriniz!!!")

                self.cursor.execute("SELECT * FROM shoes WHERE adet={}".format(adet[select - 1][1][0]))

                all = self.cursor.fetchall()

            convertall = lambda x: [str(y) for y in x]

            for sayi, shoes in enumerate(all, 1):
                print("{})".format(sayi), "-".join(convertall(shoes)))

            self.connect.commit()

        if select == 7:
            self.cursor.execute("SELECT fiyat FROM shoes")

            fiyat = list(enumerate(list(self.cursor.fetchall()), 1))

            for sayi, a in fiyat:
                print("{}){}".format(sayi, a[0]))

            while True:
                try:
                    select = int(input("Ürün numarasını seçiniz:"))
                    if select < 1 or select > sayi:
                        print("Böyle bir ürün bulunmamaktadır!")
                        continue
                    break
                except ValueError:
                    print("Lütfen numara giriniz!!!")

            self.cursor.execute("SELECT * FROM shoes WHERE fiyat={}".format(fiyat[select - 1][1][0]))

            all = self.cursor.fetchall()

        convertall = lambda x: [str(y) for y in x]

        for sayi, shoes in enumerate(all, 1):
            print("{})".format(sayi), "-".join(convertall(shoes)))

        self.connect.commit()

    def dataBaseconnet(self):
        self.connect = sqlite3.connect("FL01.dbo")
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS shoes(marka TEXT,renk TEXT,model TEXT,cinsiyet TEXT,numara INT,adet INT,fiyat INT)")
        self.connect.commit()

    def exit(self):
        self.status = False


shoes = Shoesdatabase("DataBase")
while shoes.status:
    shoes.run()

