from nau import Nau

def menu():
    print("w- Moure amunt")
    print("a- Moure equerre")
    print("d- Moure dreta")
    print("s- Moure avall")
    print("m- Mostra nau")
    print("0- Sortir")

def main():
    nau = Nau()
    sortir = False
    while not sortir:
        nau.mostrar()
        op = input("Entra una opció: ")
        if op=='d':
            nau.moure_dreta()
        elif op=='a':
            nau.moure_esquerre()
        elif op=='w':
            nau.moure_amunt()
        elif op=='s':
            nau.moure_avall()
        elif op=='m':
            nau.mostrar()
        elif op=='0':
            sortir=True
            print("Has sortit de l'avió")

if __name__ == "__main__":
                    sortir=True
                    print("Has sortit de l'avió")