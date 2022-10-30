# juego de black-jack
import random
import maso 

cart = maso.cart;

def nombreJugador():
    nombre = input("Ingrese su nombre: ")
    return print(f'Bienvenido al juego de Black-Jack {nombre}');
nombreJugador()

comenzar= input("¿Desea comenzar a jugar? (s/n)")
print(comenzar)

if comenzar == "s":
# que de el maso de cartas retorne solo el valor de la misma y que muestre la carta tambien 
    def getCard():
        randomCart=  random.choice(cart)
        valorCarta = randomCart["value"]
        print(f'Carta: {randomCart["name"]}, Valor: {valorCarta}')
        return valorCarta 
    
    contador = 0;

    while contador <= 21:
        continuar = input('desea una carta? (s/n) ')
        while continuar == "s":
                contador += getCard()
                print(f'Total de puntos: {contador}')
                continuar = input('desea una carta? (s/n) ')
                if contador > 21:
                    print('Perdiste')
                    break;
                elif contador == 21:
                    print('Ganaste')
                    break;
                elif continuar == "n":
                    print('Gracias por jugar')
                    break;
        # if contador > 21:
        #     print('Perdiste')
        #     break

        # elif contador <= 21:
        #     contador += getCard();
        #     print(f'tu puntuacion es de {contador}');
            
        #     if contador == 21:
        #             print('Ganaste')
        #             break;

        # continuar = input('desea otra carta? (s/n) ')
        # if continuar == 'n':
        #     print('Gracias por jugar')
        #     break;


elif comenzar == "n":
    print('Gracias por jugar')  
else:
    print('No es una opción valida')