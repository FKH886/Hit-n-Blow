from gameHost import Host
from five_guess_AI import five_guess_AI

if __name__ == '__main__':
    gameHost = Host(duplicate=True)
    gameHost.show_hidden_box()
    gameAI = five_guess_AI(gameHost)
    gameAI.solve()
    counts = [0]*500
    for i in range(500):
        gameHost = Host(duplicate=True)
        gameAI = five_guess_AI(gameHost)
        counts[i] = gameAI.solve()
    print(sum(counts)/500)
