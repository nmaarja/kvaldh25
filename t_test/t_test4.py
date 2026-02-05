from scipy.stats import ttest_ind
lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud Arno roomas vargsi mööda klassitoa seinaäärt suure kapi juurde, kus õpetaja Laur maakaarte ja muid koolitarbeid hoidis ning puges kapi alla peitu"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa ei leia mina iial teal see suure laia ilma peal"

#lisa hümnile ja kevadele üks lause juurde
#võrrelge p-väärtusi ühe ja kahe lause puhul

sõnad1=lause1.split()
sonapikkused1=[len(sona) for sona in sõnad1]
sõnad2=lause2.split()
sonapikkused2=[len(sona) for sona in sõnad2]
print(ttest_ind(sonapikkused1, sonapikkused2))
print(sum(sonapikkused1)/len(sonapikkused1))