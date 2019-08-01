class SnakesLadders():
    def __init__(self):
        self.player_score = {1:0, 2:0}
        self.p1score = 0
        self.p2score = 0
        self.whose_turn = 1

    def assign_next_turn(self, die1, die2):
        if die1 == die2:
            return
        else:
            if self.whose_turn == 1:
                self.whose_turn = 2
            else:
                self.whose_turn = 1

    def position(self, current):
        snakesnladders = {2:38, 7:14, 8:31, 15:26, 16:6, 21:42, 28:84, 36:44, 46:25, 49:11, 51:67, 62:19, 64:60, 71:91, 74:53, 78:98, 87:94, 89:68, 92:88, 95:75, 99:80}
        if current in snakesnladders.keys():
            return snakesnladders[current]
        else:
            return current

    def rescore(self, die1, die2):
        score = 0
        score = self.player_score[self.whose_turn] + die1 + die2
        if score > 100:
            score = 200 - score
        score = self.position(score)
        return score

    def number_of_points(self, current_player):
        if self.player_score[current_player] < 100:
            return 'Player {number} is on square {score}'.format(number=current_player, score=self.player_score[current_player])
        elif self.player_score[current_player] == 100:
            return 'Player %d Wins!' % current_player


    def play(self, die1, die2):
        if self.player_score[1] == 100 or self.player_score[2] == 100:
            return 'Game over!'
        else:
            self.player_score[self.whose_turn] = self.rescore(die1,die2)
            x = self.number_of_points(self.whose_turn)
            self.assign_next_turn(die1, die2)
            return x
