import json


class ana_menu:
    defans_liste = []
    forvet_liste = []
    orta_saha_liste = []
    kaleci_liste = []
    takimlar = []
    def Listeleme(self):
        kaleci_id=1
        defans_id=1
        orta_saha_id=1
        forvet_id=1


        oyuncular= self.veriCek()
        for i in oyuncular:
                if i.get('kesin_mevki') == "kaleci":
                    self.kaleci_liste.append(i)
                    kaleci_id+=1
                elif i.get('kesin_mevki') == "defans":
                    self.defans_liste.append(i)
                    defans_id+=1
                elif i.get('kesin_mevki') == "orta_saha":
                    self.orta_saha_liste.append(i)
                    orta_saha_id+=1
                elif i.get('kesin_mevki') == "forvet":
                    self.forvet_liste.append(i)
                    forvet_id+=1


    def Menu(self):
        print('Yapmak istediginiz islemi seciniz.')
        print('1-Oyunculari Listele')
        print('2-Takim Kur')
        print('3-Mac Yap')
        print('4-Cikis')


    def veriCek(self):
        api_Data = json.load(open("json_yazma.txt"))
        return api_Data


    def listele(self):
        oyuncular = self.veriCek()

        mevki_secim = int(input('1-Kaleci \n 2-Defans \n 3-Orta Saha \n 4-Forvet \n Oyuncu Mevkisi Secin: '))

        if mevki_secim == 1:
            print ("Kaleci")
            for i in oyuncular:
                if i.get('kesin_mevki') == "kaleci":
                    print (i)
        if mevki_secim == 2:
            print ("Defans")
            for i in oyuncular:
                if i.get('kesin_mevki') == "defans":
                    print (i)
        if mevki_secim == 3:
            print ("OrtaSaha")
            for i in oyuncular:
                if i.get('kesin_mevki') == "orta_saha":
                    print (i)
        if mevki_secim == 4:
            print ("Forvet")
            for i in oyuncular:
                if i.get('kesin_mevki') == "forvet":
                    print (i)


    def takimKur(self):
        oyuncular = self.veriCek()
        takim1 = []
        defansSecim = int(input('Kac tane Defans secmek istiyorsun?: '))
        ortasahaSecim =int(input('Kac tane Orta Saha secmek istiyorsun?: '))
        forvetSecim = int(input('Kac tane Forvet secmek istiyorsun?: '))
        for i in range(11):
            oyuncu_id = 1
            for i in self.kaleci_liste:
                print("{}. {}".format(oyuncu_id, i))
                oyuncu_id += 1
            kaleci = int(input("kaleci secin:"))
            takim1.append(self.kaleci_liste[kaleci - 1])
            self.kaleci_liste.pop(kaleci - 1)


            for a in range(defansSecim):
                oyuncu_id = 1
                print("Defans")
                for i in self.defans_liste:
                    print("{}. {}".format(oyuncu_id, i))
                    oyuncu_id += 1
                defans = int(input("defans secin:"))
                takim1.append(self.defans_liste[defans - 1])
                self.defans_liste.pop(defans - 1)

            for a in range(ortasahaSecim):
                oyuncu_id = 1
                print("Orta Saha")
                for i in self.orta_saha_liste:
                    print("{}. {}".format(oyuncu_id, i))
                    oyuncu_id += 1
                orta_saha = int(input("Orta Saha secin:"))
                takim1.append(self.orta_saha_liste[orta_saha - 1])
                self.orta_saha_liste.pop(orta_saha - 1)

            for a in range(forvetSecim):
                oyuncu_id = 1
                print("Forvet")
                for i in self.forvet_liste:
                    print("{}. {}".format(oyuncu_id, i))
                    oyuncu_id += 1
                forvet = int(input("forvet secin:"))
                takim1.append(self.forvet_liste[forvet-1])
                self.forvet_liste.pop(forvet-1)
            self.takimlar.append(takim1)
            break
menu = ana_menu()
while True:
    menu.Listeleme()
    menu.Menu()
    islem = input('Secim:')
    islem = int(islem)

    if islem == 1:
        menu.listele()

    if islem == 2:
        menu.takimKur()
    if islem == 3:
        pass
    if islem == 4:
        exit()