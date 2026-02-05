#täishäälikud

from scipy.stats import ttest_ind
lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud Arno roomas vargsi mööda klassitoa seinaäärt suure kapi juurde, kus õpetaja Laur maakaarte ja muid koolitarbeid hoidis ning puges kapi alla peitu"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa ei leia mina iial teal see suure laia ilma peal"

th="aeiouõäöü"
print(lause1.lower()) #teeb kõik tähed väikseks
print([t for t in "koolimajja" if t in th]) #leiab täishäälikud sõnas "koolimajja"
print(len([t for t in "koolimajja" if t in th])) #leiab selle sõna täishäälikute arvu

def t_arv(sona):
    return len ([t for t in sona if t in th])

print(t_arv("kalamaja"))

arvud1=[t_arv(sona) for sona in lause1.lower().split()]
print(arvud1)

#kuva ka teise teksti iga sõna täishäälikute arv, kontrolli pisteliselt

th="aeiouõäöü"
print(lause2.lower()) #teeb kõik tähed väikseks

def t_arv(sona):
    return len ([t for t in sona if t in th])


arvud2=[t_arv(sona) for sona in lause2.lower().split()]
print(arvud2)

#võrdle nende arvude aritmeetilisi keskmisi t-testiga
print(ttest_ind(arvud1, arvud2))

#kuva kummagi arvujada aritmeetilise keskmine välja
def keskmine(m):
    return sum(m)/len(m)

print(keskmine(arvud1), keskmine(arvud2))

#täishäälikute osakaal kevades
def t_osa(sona):
    return len ([t for t in sona if t in th])/len(sona)

osakaalud1=[t_osa(sona) for sona in lause1.lower().split()]
print (osakaalud1)
print(keskmine(osakaalud1))

#leidke täishäälikute osakaalud ja nende keskmine hümni tekstis
def t_osa(sona):
    return len ([t for t in sona if t in th])/len(sona)

osakaalud2=[t_osa(sona) for sona in lause2.lower().split()]
print (osakaalud2)
print(keskmine(osakaalud2))

#võrrelge t-testiga kahe teksti täishäälikute osakaale
print(ttest_ind(osakaalud1, osakaalud2))

#usaldusvahemik
import statsmodels.stats.api as sms
cm = sms.CompareMeans(sms.DescrStatsW(osakaalud1), sms.DescrStatsW(osakaalud2))
print(cm.tconfint_diff(usevar='unequal'))

