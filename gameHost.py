import random
import string


class Host:
    def __init__(self, duplicate=False, column=4, pool=6):
        print('duplicate: ', duplicate, '  column: ', column, '  pool: ', pool)
        self.__balls = []
        if pool == 6:
            __balls = ['B', 'R', 'Y', 'G', 'P', 'W']
        else:
            for i in range(pool): self.__balls.append(string.ascii_uppercase[i])
        print(self.__balls)
        if duplicate:
            selected_balls = []
            for i in range(column):
                selected_balls += random.sample(self.__balls, 1)
        else:
            selected_balls = random.sample(self.__balls, column)
        self.__hidden_box = selected_balls

    def show_hidden_box(self):
        print(self.__hidden_box)

    def get_pool(self):
        return self.__balls

    def get_hidden_box(self):
        return self.__hidden_box

    def guess_input(self):
        guess_balls = input("enter your guess: ")
        return self.guess(guess_balls)

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

    def guess_for_AI(self, guess_balls):
        hit = 0
        blow = 0
        for i in range(4):
            if self.__hidden_box[i] == guess_balls[i]:
                hit += 1
                blow += 1
            elif self.__hidden_box[i] in guess_balls:
                blow += 1

        return hit, blow
