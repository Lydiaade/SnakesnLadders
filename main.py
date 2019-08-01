

class SnakesLadders():
    def __init__(self):
        self.p1score = 0
        self.p2score = 0
        self.whose_turn = 1

    def assign_next_turn(self, die1, die2):
        if die1 == die2:
            return
        else:
            if self.whose_turn == 1:
                self.whose_turn = 2
            self.whose_turn = 1

    def position(self, current):
        snakesnladders = {2:38, 7:14, 8:31, 15:26, 16:6, 21:42, 28:84, 36:44, 46:25, 49:11, 51:67, 62:19, 64:60, 71:91, 74:53, 78:98, 87:94, 89:68, 92:88, 95:75, 99:80}
        if current in snakesnladders.keys():
            return snakesnladders[current]
        else:
            return current
        
    def rescore(self, pscore, die1, die2):
        score = 0
        score = pscore + die1 + die2
        if score > 100:
            score = 200 - score
        score = self.position(score)
        return score

    def play(self, die1, die2):
        if self.p1score == 100 or self.p2score == 100:
            return 'Game over!'
        elif self.whose_turn == 1:
            self.p1score = self.rescore(self.p1score, die1, die2)
            self.assign_next_turn(die1, die2)
            if self.p1score < 100:
                return 'Player 1 is on square %d' % self.p1score
            elif self.p1score == 100:
                return 'Player 1 Wins!'
        elif self.whose_turn == 2:
            self.p2score = self.rescore(self.p2score, die1, die2)
            self.assign_next_turn(die1, die2)
            if self.p2score < 100:
                return 'Player 2 is on square %d' % self.p2score
            elif self.p2score == 100:
                return 'Player 2 Wins!'