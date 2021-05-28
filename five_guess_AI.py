class five_guess_AI:
    def __init__(self, gameHost):
        self.__host = gameHost
        self.__hits = []
        self.__blows = []
        self.__guess_count = 0
        self.__certain = []
        self.__record = []
        pool = self.__host.get_pool()
        self.__S = []
        for ball_0 in pool:
            for ball_1 in pool:
                for ball_2 in pool:
                    for ball_3 in pool:
                        self.__S.append(ball_0+ball_1+ball_2+ball_3)

    def guess_input(self, input_guess):
        hb = self.__host.guess_for_AI(input_guess)
        self.__guess_count += 1
        self.__hits.append(hb[0])
        self.__blows.append(hb[1])
        self.__record.append(input_guess)
        self.trim_S()
        if hb[0] == self.__host.get_config()[1]:
            return True
        else:
            self.__S.remove(input_guess)
            return False

    def trim_S(self):
        for s in self.__S:
            hit = 0
            blow = 0
            for i in range(4):
                if s[i] == self.__record[-1][i]:
                    hit += 1
                    blow += 1
                elif s[i] in self.__record[-1]:
                    blow += 1
            if (self.__hits[-1], self.__blows[-1]) != (hit, blow):
                self.__S.remove(s)
        print('S count: ', len(self.__S))

    def next_input(self):
        return self.__S[0]

    def solve(self):
        self.guess_input('YYGG')
        self.show_guess_count()
        while True:
            next_input = self.next_input()
            print('input: ', next_input)
            if self.guess_input(next_input):
                self.show_hb()
                self.show_guess_count()
                break
            else:
                self.show_hb()
                self.show_guess_count()

    def show_hits(self):
        print('hits: ', self.__hits)

    def show_blows(self):
        print('blows: ', self.__blows)

    def show_hb(self):
        print('hits: ', self.__hits[-1])
        print('blows: ', self.__blows[-1])

    def show_guess_count(self):
        print('count: ', self.__guess_count)
