import random
import string


class Host:
    def __init__(self, duplicate=False, column=4, pool=6):
        print('duplicate: ', duplicate, '  column: ', column, '  pool: ', pool)
        balls = []
        if pool == 6:
            balls = ['B', 'R', 'Y', 'G', 'P', 'W']
        else:
            for i in range(pool): balls.append(string.ascii_uppercase[i])
        print(balls)
        if duplicate:
            selected_balls = []
            for i in range(column):
                selected_balls += random.sample(balls, 1)
        else:
            selected_balls = random.sample(balls, column)
        self._hidden_box = selected_balls

    def show_hidden_box(self):
        print(self._hidden_box)

    def guess_input(self):
        guess_balls = input("enter your guess: ")
        return self.guess(guess_balls)

    def guess(self, guess_balls):
        hit = 0
        blow = 0
        for i in range(4):
            if self._hidden_box[i] == guess_balls[i]:
                hit += 1
                blow += 1
            elif self._hidden_box[i] in guess_balls:
                blow += 1

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
