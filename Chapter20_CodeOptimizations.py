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


def get_missing_number_from_array(array_numbers):
    dictionary_numbers = dict.fromkeys(array_numbers, True)
    missing_number = None

    for number in range(len(array_numbers)):
        if number not in dictionary_numbers:
            missing_number = number
            break

    return missing_number


def get_missing_number_from_array_using_sum_approach(array_numbers):
    full_sum = 0
    actual_sum = 0

    for number in range(1, len(array_numbers) + 1):
        full_sum += number

    for number in array_numbers:
        actual_sum += number

    return full_sum - actual_sum


def calculate_greatest_profit_from_single_buy_followed_by_single_sell(stock_prices_array):
    current_buy = stock_prices_array[0]
    current_sell = stock_prices_array[1]
    current_sell_index = 1
    array_length = len(stock_prices_array)

    for index in range(1, array_length - 1):
        sell_index = index + 1

        if stock_prices_array[sell_index] > current_sell:
            current_sell = stock_prices_array[sell_index]
            current_sell_index = sell_index

        if stock_prices_array[index] < current_buy and index < current_sell_index:
            current_buy = stock_prices_array[index]

    return int(current_sell) - int(current_buy)


def main():
    basketball_players = [Player("Jill", "Huang"), Player("Janko", "Barton"), Player("Wanda", "Vakulskas"),
                          Player("Jill", "Moloney"), Player("Luuk", "Watkins")]
    football_players = [Player("Hanzla", "Radosti"), Player("Tina", "Watkins"), Player("Alex", "Patel"),
                        Player("Jill", "Huang"), Player("Wanda", "Vakulskas")]

    print("Players who play in both teams:", get_players_of_both_teams(basketball_players, football_players))

    print("Missing Number from array is:", get_missing_number_from_array([2, 3, 0, 6, 1, 5]))
    print("Missing Number from array is:", get_missing_number_from_array([8, 2, 3, 9, 4, 7, 5, 0, 6]))

    print("Missing Number from array is:", get_missing_number_from_array_using_sum_approach([2, 3, 0, 6, 1, 5]))
    print("Missing Number from array is:",
          get_missing_number_from_array_using_sum_approach([8, 2, 3, 9, 4, 7, 5, 0, 6]))

    print("Greatest profit is:",
          calculate_greatest_profit_from_single_buy_followed_by_single_sell([10, 7, 5, 8, 11, 2, 6]))


if __name__ == "__main__":
    main()
