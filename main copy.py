class Player:
    def __init__(self, name):
        self.name = name


class PlayerDetails():
    def __init__(self):
        PlayerDetails.player_score = {}
        PlayerDetails.player_names = {}

    def scores(self, object):
        i = 1
        while i <= object:
            PlayerDetails.player_score.update({i:0})
            i += 1
        return PlayerDetails.player_score
    
    def names(self, object):
        i = 1
        while i <= object:
            PlayerDetails.player_names.update({i: input("Player %i name? " % i)})
            i += 1
        return PlayerDetails.player_names


class SnakesLadders:
    def __init__(self, player_details):
        self.num_of_players = int(input("How many players? "))
        self.players = []
        for i in range(self.num_of_players):
            name = input("Player %i name? " % (i + 1))
            player = Player(name)
            self.players.append(player)
        self.player_in_turn = self.players[0]
        
        # Using PlayerDetails
        self.player_score = player_details.scores(self.num_of_players)
        self.player_names = player_details.names(self.num_of_players)
        self.whose_turn = 1

    def assign_next_turn(self, die1, die2):
        if die1 == die2:
            return
        else:
            if self.whose_turn < self.num_of_players:
                self.player_in_turn = self.players[self.players.index(self.player_in_turn) + 1]

                # Using PlayerDetails
                self.whose_turn += 1
            else:
                self.player_in_turn = self.players[0]

                # Using PlayerDetails
                self.whose_turn = 1

    def position(self, current):
        snakes = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}
        ladders = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}
        if current in snakes.keys():
            print("Whoops, you seemed to have slipped on snake! Down you go!!")
            return snakes[current]
        elif current in ladders.keys(): 
            print("Yay! You've got a booster up a ladder!! Up, Up and Away!!")
            return ladders[current]
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
            print('Player {number}, {name} is on square {score}'.format(number=current_player, name=self.players[current_player - 1], score=self.player_score[current_player]))
            return 'Player {number}, {name} is on square {score}'.format(number=current_player, name=self.player_names[current_player], score=self.player_score[current_player])
        elif self.player_score[current_player] == 100:
            return 'Player {number}, {name} Wins!'.format(number=current_player, name=self.player_names[current_player])


    def play(self, die1, die2):
        if 100 in self.player_score.values():
            return 'Game over!'
        else:
            self.player_in_turn.score = self.rescore(die1,die2)

            # Using PlayerDetails
            self.player_score[self.whose_turn] = self.rescore(die1,die2)
            x = self.number_of_points(self.whose_turn)
            self.assign_next_turn(die1, die2)
            return x
