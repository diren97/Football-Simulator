from random import randint
import time
import sys

class mac_algoritmasi:
    aksiyon_sayisi = 0
    guclu_takim = 0
    aksiyon_dakikalari = []

    def mac_ani(self,t,takim1,takim2,skor1=0,skor2=0):
        while t > 0:
            sys.stdout.write('\r{}  {} -- {} -- {}  {}'.format(takim1.get("takim_adi"),skor1,t,skor2,takim2.get("takim_adi")))
            t -=1
            sys.stdout.flush()
            time.sleep(1)
            for i in self.aksiyon_dakikalari:
                ""

    def aks_sayi_takim_gucu(self, takim1, takim2, takim1_mevkiler, takim2_mevkiler):
        oyuncu_sayilari = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        takim1_toplam_att = 0
        takim1_toplam_def = 0
        takim1_toplam_tec = 0
        takim2_toplam_att = 0
        takim2_toplam_def = 0
        takim2_toplam_tec = 0

        temp = 0
        takim1_kaleci_sayisi = 1
        for mevki in takim1_mevkiler:
            if temp == 0:
                takim1_defans_sayisi = mevki
            elif temp == 1:
                takim1_orta_sayisi = mevki
            elif temp == 2:
                takim1_forvet_sayisi = mevki
            temp += 1
        temp = 0
        for mevki in takim2_mevkiler:
            if temp == 0:
                takim2_defans_sayisi = mevki
            elif temp == 1:
                takim2_orta_sayisi = mevki
            elif temp == 2:
                takim2_forvet_sayisi = mevki
            temp += 1
        temp = 0
        for i in takim1:
            if temp == 0:
                takim1_toplam_tec += int(i.get("tec")) * 5
                takim1_toplam_att += int(i.get("att")) * 0.5
                takim1_toplam_def += int(i.get("def")) * 3
            if temp in oyuncu_sayilari[1:takim1_defans_sayisi]:
                takim1_toplam_tec += int(i.get("tec"))
                takim1_toplam_att += int(i.get("att")) * 0.5
                takim1_toplam_def += int(i.get("def")) * 5
            elif temp in oyuncu_sayilari[takim1_defans_sayisi:takim1_defans_sayisi + takim1_orta_sayisi]:
                takim1_toplam_tec += int(i.get("tec")) * 5
                takim1_toplam_att += int(i.get("att")) * 2
                takim1_toplam_def += int(i.get("def")) * 2
            elif temp in oyuncu_sayilari[takim1_orta_sayisi + takim1_defans_sayisi:]:
                takim1_toplam_tec += int(i.get("tec")) * 5
                takim1_toplam_att += int(i.get("att")) * 5
                takim1_toplam_def += int(i.get("def"))
            temp += 1
        temp = 0
        for i in takim2:
            if temp == 0:
                takim2_toplam_tec += int(i.get("tec")) * 5
                takim2_toplam_att += int(i.get("att")) * 0.5
                takim2_toplam_def += int(i.get("def")) * 3
            if temp in oyuncu_sayilari[1:takim1_defans_sayisi]:
                takim2_toplam_tec += int(i.get("tec"))
                takim2_toplam_att += int(i.get("att")) * 0.5
                takim2_toplam_def += int(i.get("def")) * 5
            elif temp in oyuncu_sayilari[takim1_defans_sayisi:takim1_defans_sayisi + takim1_orta_sayisi]:
                takim2_toplam_tec += int(i.get("tec")) * 5
                takim2_toplam_att += int(i.get("att")) * 2
                takim2_toplam_def += int(i.get("def")) * 2
            elif temp in oyuncu_sayilari[takim1_orta_sayisi + takim1_defans_sayisi:]:
                takim2_toplam_tec += int(i.get("tec")) * 5
                takim2_toplam_att += int(i.get("att")) * 5
                takim2_toplam_def += int(i.get("def"))
            temp += 1

        takim1_tec_ort = float(takim1_toplam_tec / 11)
        takim1_def_ort = float(takim1_toplam_def / 11)
        takim1_att_ort = float(takim1_toplam_att / 11)
        takim2_tec_ort = float(takim2_toplam_tec / 11)
        takim2_def_ort = float(takim2_toplam_def / 11)
        takim2_att_ort = float(takim2_toplam_att / 11)

        a = takim1_att_ort - takim2_def_ort
        b = takim2_att_ort - takim1_def_ort
        c = takim1_tec_ort - takim2_tec_ort
        att_def_farki = a - b

        if att_def_farki > 0:  # 1. takim diğer takima göre daha avantajli
            if c > 0:  # 1. takimin tekniği diğer takima göre daha avantajli
                att_def_farki += 2 * c
                self.guclu_takim = 1
            else:
                att_def_farki -= 2 * c
                if att_def_farki < 0:
                    self.guclu_takim = 2
                    abs(att_def_farki)
                else:
                    self.guclu_takim = 1
        else:
            if c > 0:
                att_def_farki -= 2 * c
                if att_def_farki < 0:
                    self.guclu_takim = 2
                    abs(att_def_farki)
                else:
                    self.guclu_takim = 1
            else:
                att_def_farki += 2 * c
                self.guclu_takim = 2

        if att_def_farki / 3 < 5:
            self.aksiyon_dakikalari = 5
        else:
            self.aksiyon_dakikalari = att_def_farki / 3

    def aksiyon_dakikalari(self, aksiyon_sayisi):
        self.aksiyon_dakikalari = []
        for i in aksiyon_sayisi:
            x = randint(0, 90)
            self.aksiyon_dakikalari.append(x)

    def sari_kart(self, takim_mevki):
        if randint(0, 1):
            a = randint(1, 100)
            if a < 31:
                defans = takim_mevki[0]
                takim1_kart = randint(1, defans)
                return takim1_kart
            elif a < 81:
                orta_saha = takim_mevki[1]
                takim1_kart = randint[1, orta_saha]
                return takim1_kart + int(takim_mevki[0])
            else:
                forvet = takim_mevki[2]
                takim1_kart = randint[1, forvet]
                return takim1_kart + int(takim_mevki[0] + takim_mevki[1])

    def kirmizi_kart(self, takim1_mevki, takim2_mevki):
        if randint(0, 1):
            a = randint(1, 100)
            if a < 51:
                defans = takim1_mevki[0]
                takim1_kart = randint(1, defans)
                return takim1_kart
            elif a < 91:
                orta_saha = takim1_mevki[1]
                takim1_kart = randint[1, orta_saha]
                return takim1_kart + int(takim1_mevki[0])
            else:
                forvet = takim1_mevki[2]
                takim1_kart = randint[1, forvet]
                return takim1_kart + int(takim1_mevki[0] + takim1_mevki[1])
        else:
            a = randint(1, 100)
            if a < 51:
                defans = takim2_mevki[0]
                takim2_kart = randint(1, defans)
                return takim2_kart
            elif a < 91:
                orta_saha = takim2_mevki[1]
                takim2_kart = randint[1, orta_saha]
                return takim2_kart + int(takim2_mevki[0])
            else:
                forvet = takim2_mevki[2]
                takim2_kart = randint[1, forvet]
                return takim2_kart + int(takim2_mevki[0] + takim2_mevki[1])

    def gol(self, takim1_mevki, takim2_mevki, guclu_takim_no=1):
        if guclu_takim_no == 1:
            guc = randint(1, 10)
            if guc < 8:
                a = randint(1, 100)
                if a < 21:
                    defans = takim1_mevki[0]
                    takim1_gol = randint(1, defans)
                    return takim1_gol
                elif a < 61:
                    orta_saha = takim1_mevki[1]
                    takim1_gol = randint[1, orta_saha]
                    return takim1_gol + int(takim1_mevki[0])
                else:
                    forvet = takim1_mevki[2]
                    takim1_gol = randint[1, forvet]
                    return takim1_gol + int(takim1_mevki[0] + takim1_mevki[1])
            else:
                a = randint(1, 100)
                if a < 21:
                    defans = takim2_mevki[0]
                    takim2_gol = randint(1, defans)
                    return takim2_gol
                elif a < 61:
                    orta_saha = takim2_mevki[1]
                    takim2_gol = randint[1, orta_saha]
                    return takim2_gol + int(takim2_mevki[0])
                else:
                    forvet = takim2_mevki[2]
                    takim2_gol = randint[1, forvet]
                    return takim2_gol + int(takim2_mevki[0] + takim2_mevki[1])
        else:
            temp = takim1_mevki
            takim1_mevki = takim2_mevki
            takim2_mevki = temp
            guc = randint(1, 10)
            if guc < 8:
                a = randint(1, 100)
                if a < 21:
                    defans = takim1_mevki[0]
                    takim1_gol = randint(1, defans)
                    return takim1_gol
                elif a < 61:
                    orta_saha = takim1_mevki[1]
                    takim1_gol = randint[1, orta_saha]
                    return takim1_gol + int(takim1_mevki[0])
                else:
                    forvet = takim1_mevki[2]
                    takim1_gol = randint[1, forvet]
                    return takim1_gol + int(takim1_mevki[0] + takim1_mevki[1])
            else:
                a = randint(1, 100)
                if a < 21:
                    defans = takim2_mevki[0]
                    takim2_gol = randint(1, defans)
                    return takim2_gol
                elif a < 61:
                    orta_saha = takim2_mevki[1]
                    takim2_gol = randint[1, orta_saha]
                    return takim2_gol + int(takim2_mevki[0])
                else:
                    forvet = takim2_mevki[2]
                    takim2_gol = randint[1, forvet]
                    return takim2_gol + int(takim2_mevki[0] + takim2_mevki[1])
    def mac_esnasi(self):
        ""