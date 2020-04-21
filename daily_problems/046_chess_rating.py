'''
This problem was asked by Facebook.

In chess, the Elo rating system is used to calculate
 strengths based on game results.

A simplified description of the Elo system is as follows.
Every player begins at the same score. For each subsequent
game, the loser transfers some points to the winner, where
the amount of points transferred depends on how unlikely the
 win is. For example, a 1200-ranked player should gain much
 more points for beating a 2000-ranked player than for beating a
 1300-ranked player.

Implement this system.
'''

class Elo:

    def __init__(self):
        self.ratings = {}
        self.d = 1000 # default rating when joined
        self.k = 32 # rate of change in score

    def add_player(self, name):
        self.ratings[name] = self.d

    def expected(self, r1, r2):
        # L(x) = 1 / (1 + e(u - x)/s))
        return 1/(1+10**((r2-r1)/ 400))

    def update(self, p1, p2, outcome):
        e1 = self.expected(self.ratings[p1], self.ratings[p2])
        e2 = self.expected(self.ratings[p2], self.ratings[p1])
        print(e1)
        print(e2)

        if outcome == p1:
            o1,o2, = 1,0
        elif outcome == p2:
            o1,o2 = 0,1
        else:
            o1 = o2 = .5

        # new_rating = rating + 32(score-expected score)
        self.ratings[p1] += self.k * (o1-e1)
        self.ratings[p2] += self.k * (o2-e2)
        print(self.ratings)
year_2020 = Elo()
year_2020.add_player('Estelle')
year_2020.add_player('Lauren')
year_2020.update('Estelle', 'Lauren', 'Estelle')
