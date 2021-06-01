import copy
from math import factorial
from itertools import permutations


class five_guess_AI:
    def __init__(self, gameHost):
        self.__host = gameHost
        self.__hits = []
        self.__blows = []
        self.__guess_count = 0
        self.__certain = []
        self.__record = []
        pool = self.__host.get_pool()
        self.__S = ['']
        self.initialize_S()

    def initialize_S(self):
        duplicate, column_num, pool_num = self.__host.get_config()
        pool = self.__host.get_pool()
        if duplicate:
            self.__S = [''] * (pool_num ** column_num)
            for i in range(column_num - 1, -1, -1):
                ball = 0
                itj = 0
                for j in range(len(self.__S)):
                    if j - itj >= pool_num ** i:
                        itj = j
                        if ball + 1 == pool_num:
                            ball = 0
                        else:
                            ball += 1
                    self.__S[j] += pool[ball]
        else:
            self.__S = [list(i) for i in list(permutations(pool, column_num))]

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
            return False

    def trim_for_AI(self, a, b):
        hit = 0
        blow = 0
        temp_a = [char for char in a]
        temp_b = [char for char in b]
        for i in range(self.__host.get_config()[1]):
            if a[i] == b[i]:
                hit += 1
                temp_a.remove(a[i])
                temp_b.remove(a[i])
        for i in range(len(temp_a)):
            if temp_a[i] in temp_b:
                blow += 1
                temp_b.remove(temp_a[i])
        return hit, blow

    def trim_S(self):
        for s in copy.deepcopy(self.__S):
            if (self.__hits[-1], self.__blows[-1]) != self.trim_for_AI(s, self.__record[-1]):
                self.__S.remove(s)

    def next_input(self):
        return self.__S[0]

    def solve(self, print_log=False):
        pool = self.__host.get_pool()
        initial_input = [pool[0], pool[1], pool[0], pool[1]]
        self.guess_input(initial_input)
        if print_log:
            print('input: ', initial_input)
            self.show_hb()
            self.show_guess_count()
        while True:
            next_input = self.next_input()
            solved = self.guess_input(next_input)
            if print_log:
                print('input: ', next_input)
                self.show_hb()
                self.show_guess_count()
            if solved:
                break
        return self.__guess_count

    def show_hits(self):
        print('hits: ', self.__hits)

    def show_blows(self):
        print('blows: ', self.__blows)

    def show_hb(self):
        print('hits: ', self.__hits[-1])
        print('blows: ', self.__blows[-1])

    def show_guess_count(self):
        print('count: ', self.__guess_count)