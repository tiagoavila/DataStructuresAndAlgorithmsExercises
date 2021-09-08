from Entities.Player import Player


def get_players_of_both_teams(players_team1, players_team2):
    dictionary_players_team1 = {}
    players_who_play_in_both_teams = []

    for player in players_team1:
        key = player.first_name + " " + player.last_name
        dictionary_players_team1[key] = True

    for player in players_team2:
        key = player.first_name + " " + player.last_name
        if key in dictionary_players_team1:
            players_who_play_in_both_teams.append(key)

    return players_who_play_in_both_teams


def main():
    basketball_players = [Player("Jill", "Huang"), Player("Janko", "Barton"), Player("Wanda", "Vakulskas"),
                          Player("Jill", "Moloney"), Player("Luuk", "Watkins")]
    football_players = [Player("Hanzla", "Radosti"), Player("Tina", "Watkins"), Player("Alex", "Patel"),
                        Player("Jill", "Huang"), Player("Wanda", "Vakulskas")]

    print("Players who play in both teams:", get_players_of_both_teams(basketball_players, football_players))


if __name__ == "__main__":
    main()
