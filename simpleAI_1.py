

class simpleAI_1:
    def __init__(self, gameHost, initial_guess='BRGY'):
        print('Initial guess is: ', initial_guess)
        self.__host = gameHost
        self.__hits = []
        self.__blows = []
        self.__guess_count = 0
        self.__certain = []
        self.__record = []
        for i in range(self.__host.__colum):
            self.__certain.append(self.__host.__balls)
        self.guess_input(initial_guess)

    def guess_input(self, input_guess):
        hb = self.__host.guess_for_AI(input_guess)
        self.__guess_count += 1
        self.__hits.append(hb[0])
        self.__blows.append(hb[1])
        self.__record.append(input_guess)

    def next_input(self):
        next = []
        return next

    def show_hits(self):
        print(self.__hits)

    def show_blows(self):
        print(self.__blows)

    def show_hb(self):
        print(self.__hits)
        print(self.__blows)

    def show_guess_count(self):
        print(self.__guess_count)
