
class Player:
    def __init__(self, player_name, player_position):
        self.player_name = player_name
        self.player_position = player_position


class NFLTeam:
    def __init__(self, team_name, players):
        self.team_name = team_name
        self.players = players

    def display_team(self):
        print("Team Name:", self.team_name)
        print("Players:")

        for player in self.players:
            print(player.player_name, "-", player.player_position)



player1 = Player("Joe Montana", "Quarterback")
player2 = Player("Barry Sanders", "Running Back")
player3 = Player("Jerry Rice", "Wide Receiver")
player4 = Player("Graham Gano", "Kicker")


player_list = [player1, player2, player3, player4]


team = NFLTeam("San Francisco 49ers", player_list)


team.display_team()
