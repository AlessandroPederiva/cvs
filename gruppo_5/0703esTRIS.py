griglia=[["1","2","3"],["4","5","6"],["7","8","9"]]


def stampaGriglia(griglia_da_stampare):
    print(f"{griglia_da_stampare[0][0]} | {griglia[0][1]} | {griglia[0][2]}")
    print("-"*11)
    print(f"{griglia_da_stampare[1][0]} | {griglia[1][1]} | {griglia[1][2]}")
    print("-"*11)
    print(f"{griglia_da_stampare[2][0]} | {griglia[2][1]} | {griglia[2][2]}")

stampaGriglia(griglia)

#controllo_vittoria = funzione per vedere se vittoria
#modo 1 usando For

turno="X"

#while True:
stampaGriglia(griglia)
 