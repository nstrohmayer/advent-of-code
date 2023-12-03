import utilities
from GameInfo import GameInfo


def main():
    game_strings = utilities.read_file("Day 2.txt")

    # Cube limits
    red_limit = 12
    green_limit = 13
    blue_limit = 14

    # Generate list of GameInfo instances
    game_infos = []
    for game_string in game_strings:
        game_info = GameInfo.from_string(game_string)
        game_infos.append(game_info)

    # Validate games and add IDs of valid games
    valid_game_ids = []
    for game_info in game_infos:
        if game_info.is_possible(red_limit, green_limit, blue_limit):
            valid_game_ids.append(game_info.game_id)

    # Sum the IDs of valid games
    sum_valid_game_ids = sum(valid_game_ids)
    print(f"Sum of IDs of valid games: {sum_valid_game_ids}")


if __name__ == "__main__":
    main()
