# class Batiment :

#     def init(self, adresse, etage):
#         self.adresse = adresse
#         self.etage = etage

#     def get_adresse(self):
#         return self.adresse

#     def get_etage(self):
#         return self.etage


# class Immeuble(Batiment):

#     def init(self, adresse, etage, balecon):
#         Batiment.init(self, adresse, etage)
#         self.balecon = balecon


#     def get_balecon(self):
#         return self.balecon


# class Supermarche(Batiment):

#     def init(self, adresse, etage, rayon):
#         Batiment.init(self, adresse, etage)
#         self.rayon = rayon

#     def get_rayon(self):
#         return self.rayon

# class Banque(Batiment):

#     def init(self, adresse, etage, nom, coffre):
#         Batiment.init(self, adresse, etage)
#         self.nom = nom
#         self.coffre = coffre

# def get_nom(self):
#     return self.nom

# def get_coffre(self):
#     return self.coffre

# immeuble1 = Immeuble("\nAdresse 1 rue 1", 2, 3)
# immeuble2 = Immeuble("Adresse 2 rue 2", 3, 5)
# immeuble3 = Immeuble("Adresse 3 rue 3", 4, 6)
# immeuble4 = Immeuble("Adresse 4 rue 4", 5, 7)

# supermarche1 = Supermarche("\nAdresse 5 rue 5", 1, 10)
# supermarche2 = Supermarche("Adresse 6 rue 6", 1, 11)

# banque = Banque("\nAdresse 7, rue 7", 1, "CIH", 30)

# print(">>>Immeuble numero 1 :",immeuble1.get_adresse(), "\nNombre d'etage : ",immeuble1.get_etage(), "\nNombre de balecons",immeuble1.get_balecon())
# print(">>>Super marché numero 1", supermarche1.get_adresse(), "\nNombre d'étage :", supermarche1.get_etage(), "\nNombre de rayons", supermarche1.get_rayon())
# print(">>>Banque", banque.get_adresse(), "\nNombre d'etage :", banque.get_etage(), "\nNom de la banque :", banque.get_nom(), "\nNombre de coffre :", banque.get_coffre())

class Batiment:

    def __init__(self, adresse, nb_etages):
        self.adresse = adresse
        self.nb_etages = nb_etages

    def get_adresse(self):
        return self.adresse

    def get_nb_etages(self):
        return self.nb_etages


class Immeuble(Batiment):

    def __init__(self, adresse, nb_etages, nb_balcons):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_balcons = nb_balcons

    def get_nb_balcons(self):
        return self.nb_balcons


class Supermarche(Batiment):

    def __init__(self, adresse, nb_etages, nb_rayons):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_rayons = nb_rayons

    def get_nb_rayons(self):
        return self.nb_rayons


class Banque(Batiment):

    def __init__(self, adresse, nb_etages, nb_coffres, nom):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_coffres = nb_coffres
        self.nom = nom

    def get_nb_coffres(self):
        return self.nb_coffres

    def get_nom(self):
        return self.nom


# 4 immeubles
immeuble1 = Immeuble("26 rue de la Gravenade", 3, 3)
immeuble2 = Immeuble("28 rue de la Grevande", 5, 6)
immeuble3 = Immeuble("53 rue elios mitterand", 2, 2)
immeuble5 = Immeuble("120 rue pleiades", 8, 4)

# 2 supermarché
supermarche1 = Supermarche("27 rue de la Gravenade", 1, 12)
supermarche2 = Supermarche("119 rue pleiades", 4, 25)

# 1 banque
banque = Banque("53 rue elios mitterand", 25, "Banque")