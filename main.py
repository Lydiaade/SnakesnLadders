class SnakesLadders():
    def __init__(self):
        self.players = int(input("How many players? "))
        i = 1
        self.player_score = {}
        self.player_names = {}
        while i <= self.players:
            self.player_score.update({i:0})
            self.player_names.update({i: input("Player %i name? " % i)})
            print(self.player_score)
            print(self.player_names)
            i += 1
        self.whose_turn = 1

    def assign_next_turn(self, die1, die2):
        if die1 == die2:
            return
        else:
            if self.whose_turn < self.players:
                self.whose_turn += 1
            else:
                self.whose_turn = 1

    def position(self, current):
        snakesnladders = {2:38, 7:14, 8:31, 15:26, 16:6, 21:42, 28:84, 36:44, 46:25, 49:11, 51:67, 62:19, 64:60, 71:91, 74:53, 78:98, 87:94, 89:68, 92:88, 95:75, 99:80}
        if current in snakesnladders.keys():
            return snakesnladders[current]
        else:
            return current

    def rescore1(self, die1, die2):
        score = 0
        score = self.player_score[self.whose_turn] + die1 + die2
        if score > 100:
            score = 200 - score
        score = self.position(score)
        return score

    def number_of_points(self, current_player):
        if self.player_score[current_player] < 100:
            return 'Player {number}, {name} is on square {score}'.format(number=current_player, name=self.player_names[current_player], score=self.player_score[current_player])
        elif self.player_score[current_player] == 100:
            return 'Player {number}, {name} Wins!'.format(number=current_player, name=self.player_names[current_player])


    def play(self, die1, die2):
        if 100 in self.player_score.values():
            return 'Game over!'
        else:
            self.player_score[self.whose_turn] = self.rescore1(die1,die2)
            x = self.number_of_points(self.whose_turn)
            self.assign_next_turn(die1, die2)
            return x