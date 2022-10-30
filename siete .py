# juego de black-jack
import random

def nombreJugador():
    nombre = input("Ingrese su nombre: ")
    return print(f'Bienvenido al juego de Black-Jack {nombre}');
nombreJugador()

comenzar= input("¿Desea comenzar a jugar? (s/n)")
print(comenzar)

if comenzar == "s":
        
    cart = [
        {"name": "A ♠️", "value": 1 or 11},
        {"name": "2 ♠️", "value": 2},
        {"name": "3 ♠️", "value": 3},
        {"name": "4 ♠️", "value": 4},
        {"name": "5 ♠️", "value": 5},
        {"name": "6 ♠️", "value": 6},
        {"name": "7 ♠️", "value": 7},
        {"name": "8 ♠️", "value": 8},
        {"name": "9 ♠️", "value": 9},
        {"name": "10 ♠️", "value": 10},
        {"name": "J ♠️", "value": 10},
        {"name": "Q ♠️", "value": 10},
        {"name": "K ♠️", "value": 10},

        {"name": "A ♣️", "value": 1 or 11},
        {"name": "2 ♣️", "value": 2},
        {"name": "3 ♣️", "value": 3},
        {"name": "4 ♣️", "value": 4},
        {"name": "5 ♣️", "value": 5},
        {"name": "6 ♣️", "value": 6},
        {"name": "7 ♣️", "value": 7},
        {"name": "8 ♣️", "value": 8},
        {"name": "9 ♣️", "value": 9},
        {"name": "10 ♣️", "value": 10},
        {"name": "J ♣️", "value": 10},
        {"name": "Q ♣️", "value": 10},
        {"name": "K ♣️", "value": 10},

        {"name": "A ♥️", "value": 1 or 11},
        {"name": "2 ♥️", "value": 2},
        {"name": "3 ♥️", "value": 3},
        {"name": "4 ♥️", "value": 4},
        {"name": "5 ♥️", "value": 5},
        {"name": "6 ♥️", "value": 6},
        {"name": "7 ♥️", "value": 7},
        {"name": "8 ♥️", "value": 8},
        {"name": "9 ♥️", "value": 9},
        {"name": "10 ♥️", "value": 10},
        {"name": "J ♥️", "value": 10},
        {"name": "Q ♥️", "value": 10},
        {"name": "K ♥️", "value": 10},

        {"name": "A ♦️", "value": 1 or 11},
        {"name": "2 ♦️", "value": 2},
        {"name": "3 ♦️", "value": 3},
        {"name": "4 ♦️", "value": 4},
        {"name": "5 ♦️", "value": 5},
        {"name": "6 ♦️", "value": 6},
        {"name": "7 ♦️", "value": 7},
        {"name": "8 ♦️", "value": 8},
        {"name": "9 ♦️", "value": 9},
        {"name": "10 ♦️", "value": 10},
        {"name": "J ♦️", "value": 10},
        {"name": "Q ♦️", "value": 10},
        {"name": "K ♦️", "value": 10},
    ]


# que de el maso de cartas retorne solo el valor de la misma y que muestre la carta tambien 
    def getCard():
        randomCart=  random.choice(cart)
        valorCarta = randomCart["value"]
        print(f'Carta: {randomCart["name"]}, Valor: {valorCarta}')
        return valorCarta 
        # print()
    

#    si el usuario desea otra carta
    continuar = input('desea una carta? (s/n) ')

    contador = 0;
    while continuar == 's':

        if contador < 21:
            contador += getCard();
            print(f'tu puntuacion es de {contador}');
            continuar = input('desea otra carta? (s/n) ')

        elif contador == 21:
            print('ganaste')
            break;
        else:
            print('perdiste')
            break;

        if continuar == 'n':
            print('Gracias por jugar')
            break;


elif comenzar == "n":
    print('Gracias por jugar')  
else:
    print('No es una opción valida')