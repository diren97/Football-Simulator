import requests
import json

print("Veri dosyaları çekiliyor. Lütfen bekleyiniz.")
# Eğer out of range hatası veriyorsa, captcha limitine takıldınız.
user_agent = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' }

links= []
for i in range(10): # 10 sayfalık linki diziye iterasyonla ekliyoruz
    links.append("https://fmdataba.com/19/fm-2019-best-players/{}".format(i))

players = []
x = 1

for link in links: # dizideki linkleri koşturuyoruz
    data = requests.get(link,headers=user_agent).content.decode("utf-8")
    data2 = data.split('<th class="hidden-xs">{}</th>'.format(x))[1].split('<nav aria-label="Page navigation example">')[0]
    # x, kişi sayısıdır
    for player in data2.split("<strong>")[1:]:
        player_dict = {}
        #print(player.split('</strong></a><span')[0])
        player_name = player.split('</strong></a><span')[0] # isim okuma
        player_dict.update({"name":player_name})

        player_mevki = player.split('<span style="font-size:x-small; display: block;">')[1].split('</span>')[0] # mevki okuma
        player_dict.update({"mevki":player_mevki})
        #print(player_mevki)

        i = 1
        for value in player.split('style="font-size:small;">')[1:]:
            if i == 1: # Yaş
              #  print("Age: {}".format(value.split('</span>')[0]))
                yas_deger = value.split('</span>')[0]
                player_dict.update({"age":yas_deger})
            elif i == 2:
              #  print("Value: {}".format(value.split('</span>')[0]))
                value_deger = value.split('</span>')[0]
                player_dict.update({"value": value_deger})
            elif i == 3:
              #  print("Ove: {}".format(value.split('</span>')[0]))
                ove_deger = value.split('</span>')[0]
                player_dict.update({"ove": ove_deger})
            elif i == 4:
              #  print("Att: {}".format(value.split('</span>')[0]))
                att_deger = value.split('</span>')[0]
                player_dict.update({"att": att_deger})
            elif i == 5:
               # print("Def: {}".format(value.split('</span>')[0]))
                def_deger = value.split('</span>')[0]
                player_dict.update({"def": def_deger})
            elif i == 6:
               # print("Tec: {}".format(value.split('</span>')[0]))
                tec_deger = value.split('</span>')[0]
                player_dict.update({"tec": tec_deger})
            elif i == 7:
              #  print("Men: {}".format(value.split('</span>')[0]))
                men_deger = value.split('</span>')[0]
                player_dict.update({"men": men_deger})
            elif i == 8:
              #  print("Phy: {}".format(value.split('</span>')[0]))
                phy_deger = value.split('</span>')[0]
                player_dict.update({"phy": phy_deger})
            i += 1
        players.append(player_dict)
    x += 40 # her sayfada 40 kişi eklendiğinden 1. sayfada 1 ikinci sayfada 41'den başlamak üzeriyle ayarlanır


json.dump(players,open("json_yazma.txt","w"))
print(("İşlem tamamlandı"))

# for i in players:
#     print(i)