class Game:
    def __init__(self, title):
        self.title = title
        self.results = []

    def results(self):
        return self.results

    def players(self):
        return list(set(result.player for result in self.results))

    def average_score(self, player):
        scores = [result.score for result in self.results if result.player == player]
        if scores:
            return sum(scores) / len(scores)
        else:
            return 0

class Player:
    def __init__(self, username):
        self.username = username
        self.results = []

    def results(self):
        return self.results

    def games_played(self):
        return list(set(result.game for result in self.results))

    def played_game(self, game):
        return any(result.game == game for result in self.results)

    def num_times_played(self, game):
        return sum(1 for result in self.results if result.game == game)

class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        player.results.append(self)
        game.results.append(self)