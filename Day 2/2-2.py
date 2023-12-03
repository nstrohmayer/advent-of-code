import utilities
from GameInfo import GameInfo


def main():
    game_strings = utilities.read_file("Day 2.txt")

    game_infos = []
    for game_string in game_strings:
        game_info = GameInfo.from_string(game_string)
        game_infos.append(game_info)

    # Validate games and add IDs of valid games
    game_power_sum = 0
    for game_info in game_infos:
        game_power_sum += game_info.calculate_power()

    print(f"Sum of power of the cubes of games: {game_power_sum}")


if __name__ == "__main__":
    main()
