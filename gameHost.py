import random
import string


class Host:
    def __init__(self, duplicate=False, column=4, pool=6):
        self.__duplicate = duplicate
        self.__column = column
        self.__pool_num = pool
        print('duplicate: ', duplicate, '  column: ', column, '  pool: ', pool)
        self.__pool = []
        if pool == 6:
            self.__pool = ['B', 'R', 'Y', 'G', 'P', 'W']
        else:
            for i in range(pool): self.__pool.append(string.ascii_uppercase[i])
        print(self.__pool)
        if duplicate:
            selected_balls = []
            for i in range(column):
                selected_balls += random.sample(self.__pool, 1)
        else:
            selected_balls = random.sample(self.__pool, column)
        self.__hidden_box = selected_balls

    def show_hidden_box(self):
        print(self.__hidden_box)

    def get_pool(self):
        return self.__pool

    def get_hidden_box(self):
        return self.__hidden_box

    def get_config(self):
        return self.__duplicate, self.__column, self.__pool_num

    def guess(self, guess_balls):
        hit = 0
        blow = 0
        temp_guess = list(guess_balls)
        for i in range(4):
            if self.__hidden_box[i] == guess_balls[i]:
                hit += 1
                temp_guess.remove(self.__hidden_box[i])
            elif self.__hidden_box[i] in temp_guess:
                blow += 1
                temp_guess.remove(self.__hidden_box[i])

        if hit > 1:
            print(hit, "Hits, ", end='')
        else:
            print(hit, "Hit, ", end='')
        if blow > 1:
            print(blow, "Blows, ")
        else:
            print(blow, "Blow, ")
        if hit == 4:
            return True
        else:
            return False

    def guess_input(self):
        guess_balls = input("enter your guess: ")
        return self.guess(guess_balls)

    def guess_for_AI(self, guess_balls):
        hit = 0
        blow = 0
        temp_b = self.__hidden_box
        for i in range(self.__column):
            if guess_balls[i] == self.__hidden_box[i]:
                hit += 1
                temp_b.remove(guess_balls[i])
            elif guess_balls[i] in temp_b:
                blow += 1
                temp_b.remove(guess_balls[i])
        return hit, blow

    def trim_for_AI(self, a, b):
        hit = 0
        blow = 0
        temp_b = b
        for i in range(self.__column):
            if a[i] == b[i]:
                hit += 1
                temp_b.remove(a[i])
            elif a[i] in temp_b:
                blow += 1
                temp_b.remove(a[i])
        return hit, blow

    def guess_for_AI_input(self, guess_balls):
        guess_balls = input("enter your guess: ")
        return self.guess_for_AI(guess_balls)
