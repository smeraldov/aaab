class Tabiat:
    def __init__(self,nom,rang):
        self.nom=nom
        self.rang=rang
    def __str__(self):
        return f'nomi : {self.nom} , rangi {self.rang}'
tabiat1=Tabiat('savanna','sariq')



class Gul(Tabiat):
    def __init__(self,nom,rang,tur):
        super().__init__(nom,rang)
        self.tur=tur
    def __str__(self):
        return f'nomi : {self.nom} , rangi : {self.rang} , turi :{self.tur}'
gul1=Gul('qutb','siyohrang','gunafsha')


class Havo(Tabiat):
    def __init__(self,nom,rang,harorat):
        super().__init__(nom,rang)
        self.harorat=harorat
    def __str__(self):
        return f'nomi : {self.nom} , rangi : {self.rang} , harorati :{self.harorat}'
havo1=Havo('qutb','oq','sovuq')


class Hayvon(Tabiat):
    def __init__(self,nom,rang,tur):
        super().__init__(nom,rang)
        self.tur=tur
    def __str__(self):
        return f'nomi : {self.nom} , rangi : {self.rang} , turi :{self.tur}'
hayvon1=Hayvon('qutb','oq','oqayiq')


class Mintaqa(Tabiat):
    def __init__(self,nom,rang,harorat):
        super().__init__(nom,rang)
        self.harorat=harorat
    def __str__(self):
        return f'nomi : {self.nom} , rangi : {self.rang} , harorati :{self.harorat}'
mintaqa1=Mintaqa('mo\'tadil','yashil','iliq')


class Iqlim(Tabiat):
    def __init__(self,nom,rang,harorat):
        super().__init__(nom,rang)
        self.harorat=harorat
    def __str__(self):
        return f'nomi : {self.nom} , rangi : {self.rang} , harorati :{self.harorat}'
iqlim1=Iqlim('tropik','sariq','issiq')




print(tabiat1)
print(gul1)
print(hayvon1)
print(havo1)
print(mintaqa1)
print(iqlim1)
