"""def printtaa_summa(x, y):
    print(x + y)
    return
printtaa_summa(8, 12)


def summa(x, y):
    yht = x + y
    return
tulos = summa(8, 12)
print(tulos)
"""


def tietoja(nimi, ikä, harrastus):
    tervehdys = f'terve{nimi}. ikäsi on {ikä} ja harrastuksesi on {harrastus}'
    return tervehdys
henkilö = tietoja( nimi = ' Saeid', ikä = 30, harrastus = 'kuntosalilla käyminen.')
print(henkilö)

henkilö2 = tietoja(nimi = 'pekka', ikä = 35, harrastus = 'ohjelmointi')
print(henkilö2)

def tietoja2 (nimi, ikä, harrastus ='tenniksen pelaaminen'):
    tervehdys = f'terve {nimi}. ikäsi on {ikä}. Ja harrastuksesi on {harrastus}.'
    return tervehdys
henkilö3 = tietoja2(nimi = 'Mikko', ikä = 20)
print(henkilö3)