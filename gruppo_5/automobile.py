class Automobile:
    def __init__(self,BENZ,GPL):
        self.BENZ = BENZ
        self.GPL = GPL
        self.statoGpl = True

    def cambia_in_benzina(self):
        self.statoGpl = False
        # TODO: Cambia lo stato a benzina

    def cambia_in_gpl(self):
        self.statoGpl = True
        # TODO: Cambia lo stato a GPL
    
    def accendiMotore(self):
        if self.StatoGpl and self.BENZ>=1:   
            self.BENZ -= 1 

    def accelera(self):
        if self.statoGpl:
            if self.GPL >=3:
                self.GPL -=3
            else:
                self.GPL =0
                self.statoGpl = False
                self.BENZ -= 10
        elif self.BENZ >= 10:
            self.BENZ -= 10
        else:
            self.BENZ =0
        # TODO: Logica per consumare carburante e GPL durante l'accelerazione
        pass

    def stato(self):
        print(f"BENZINA: {self.BENZ} - GPL: {self.GPL}")  # Mostra lo stato attuale

# Codice principale
benz = int(input("Quanta benzina hai >> "))
gpl = int(input("Quanto gpl hai >> "))

automobile = Automobile(benz,gpl)  # Creazione dell'oggetto

automobile.stato()  # Stato iniziale
scelta = ' '
while scelta != 'X':
    print("X esci | B benzina | G GPL | A accelera | On Accendi Motore >> ", end="")
    scelta = input().title()
    if scelta == 'B':
        automobile.cambia_in_benzina()
    elif scelta == 'G':
        automobile.cambia_in_gpl()
    elif scelta == 'A':
        automobile.accelera()
        automobile.stato()
    elif scelta == "On":
        automobile.accendiMotore()
        automobile.stato()
