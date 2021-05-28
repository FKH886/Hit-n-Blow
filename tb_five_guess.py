from gameHost import Host
from five_guess_AI import five_guess_AI

if __name__ == '__main__':
    gameHost = Host(duplicate=True)
    gameHost.show_hidden_box()
    gameAI = five_guess_AI(gameHost)
    gameAI.solve()