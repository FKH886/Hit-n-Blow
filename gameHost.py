import random
import string
import copy


class Host:
    def __init__(self, duplicate=False, column=4, pool=6, print_log=False):
        self.__duplicate = duplicate
        self.__column = column
        self.__pool_num = pool
        if print_log:
            print('duplicate: ', duplicate, '  column: ', column, '  pool: ', pool)
        self.__pool = []
        if pool == 6:
            self.__pool = ['B', 'R', 'Y', 'G', 'P', 'W']
        else:
            for i in range(pool): self.__pool.append(string.ascii_uppercase[i])
        if print_log:
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

    def set_hidden_box(self, box):
        self.__hidden_box = box

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
            print(blow, "Blows")
        else:
            print(blow, "Blow", end='')
        if hit == 4:
            print('!')
            return True
        else:
            print('.')
            return False

    def guess_input(self):
        guess_balls = input("enter your guess: ")
        return self.guess(guess_balls)

    def guess_for_AI(self, guess_balls):
        hit = 0
        blow = 0
        temp_a = [char for char in guess_balls]
        temp_b = copy.deepcopy(self.__hidden_box)
        for i in range(self.__column):
            if guess_balls[i] == self.__hidden_box[i]:
                hit += 1
                temp_a.remove(guess_balls[i])
                temp_b.remove(guess_balls[i])
        for i in range(len(temp_a)):
            if temp_a[i] in temp_b:
                blow += 1
                temp_b.remove(temp_a[i])
        return hit, blow

    def guess_for_AI_input(self, guess_balls):
        guess_balls = input("enter your guess: ")
        return self.guess_for_AI(guess_balls)
