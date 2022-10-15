class Player:
    def __init__(self, name):
        self.name = name


class SnakesLadders:
    def __init__(self):
        self.num_of_players = int(input("How many players? "))
        self.players = []
        self.player_score = {}
        for i in range(self.num_of_players):
            name = input("Player %i name? " % (i + 1))
            player = Player(name)
            self.player_score.update({i + 1: 0})
            self.players.append(player)
        self.player_in_turn = self.players[0]
        print(self.player_score)

        # Using PlayerDetails
        self.whose_turn = 1

    def assign_next_turn(self, die1: int, die2: int) -> None:
        if die1 == die2:
            return
        else:
            if self.players.index(self.player_in_turn) + 1 < self.num_of_players:
                self.player_in_turn = self.players[self.players.index(self.player_in_turn) + 1]
                self.whose_turn = self.players.index(self.player_in_turn) + 1
            else:
                self.player_in_turn = self.players[0]
                self.whose_turn = self.players.index(self.player_in_turn) + 1

    def position(self, current: int) -> int:
        snakes = {16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}
        ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}
        if current in snakes.keys():
            print("Whoops, you seemed to have slipped on snake! Down you go!!")
            return snakes[current]
        elif current in ladders.keys():
            print("Yay! You've got a booster up a ladder!! Up, Up and Away!!")
            return ladders[current]
        else:
            return current

    def rescore(self, die1: int, die2: int) -> int:
        score = self.player_score[self.players.index(self.player_in_turn) + 1] + die1 + die2
        if score > 100:
            score = 200 - score
        score = self.position(score)
        return score

    def number_of_points(self, current_player: int) -> str:
        if self.player_score[current_player + 1] < 100:
            return f'Player {current_player + 1},' \
                   f' {self.players[current_player]} is on square {self.player_score[current_player + 1]}'
        elif self.player_score[current_player + 1] == 100:
            return f'Player {current_player + 1}, {self.players[current_player]} Wins!'

    def play(self, die1: int, die2: int) -> str:
        if 100 in self.player_score.values():
            return 'Game over!'
        else:
            self.player_in_turn.score = self.rescore(die1, die2)

            # Using PlayerDetails
            self.player_score[self.whose_turn] = self.rescore(die1, die2)
            print(self.players.index(self.player_in_turn))
            x = self.number_of_points(self.players.index(self.player_in_turn))
            self.assign_next_turn(die1, die2)
            return x
