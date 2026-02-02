lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa"

#leia T-test abil, kas nende lausete sõnade keskmine pikkus erineb üldistatavalt

sõnad1=lause1.split()
print(sõnad1)
print(sõnad1[3])
print(len("tere"))
#kuva sõna nr3 tähtede arv
print(len(sõnad1[3]))
#sõnu lauses kokku
print(len(sõnad1))
#mitu tähte on sõnades
sonapikkused1=[len(sona) for sona in sõnad1]
print(sonapikkused1)

sõnad2=lause2.split()
print(sõnad2)
print(sõnad2[3])
#sõnu lauses kokku
print(len(sõnad2))
#mitu tähte on sõnades
sonapikkused2=[len(sona) for sona in sõnad2]
print(sonapikkused2)