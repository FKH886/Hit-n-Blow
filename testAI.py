from gameHost import Host
from simpleAI_1 import simpleAI_1

if __name__ == '__main__':
    gameHost = Host()
    gameAI = simpleAI_1(gameHost)
    gameAI.show_hb()
    gameAI.show_guess_count()
    gameAI.guess_input('YGBW')
    gameAI.show_hb()
    gameAI.show_guess_count()
