from typing import List, Dict


class GameInfo:
    def __init__(self, game_id: int, cubes_info: List[Dict[str, int]]):
        self.game_id: int = game_id
        self.cubes_info: List[Dict[str, int]] = cubes_info

    @classmethod
    def from_string(cls, game_string: str) -> 'GameInfo':
        game_data = game_string.split(': ')
        game_id = int(game_data[0].split()[1])
        cubes_info = []

        cubes_data = game_data[1].split('; ')
        for subset in cubes_data:
            cubes = subset.split(', ')
            cubes_info.append({cube.split()[1]: int(cube.split()[0]) for cube in cubes})

        return cls(game_id, cubes_info)

    def get_maximum_color_count(self):
        max_red = max_green = max_blue = 0

        for subset in self.cubes_info:
            for color, count in subset.items():
                if color == 'red':
                    max_red = max(max_red, count)
                elif color == 'green':
                    max_green = max(max_green, count)
                elif color == 'blue':
                    max_blue = max(max_blue, count)

        return max_blue, max_green, max_red

    def is_possible(self, red_limit: int, green_limit: int, blue_limit: int) -> bool:
        max_blue, max_green, max_red = self.get_maximum_color_count()

        return max_red <= red_limit and max_green <= green_limit and max_blue <= blue_limit

    def calculate_power(self) -> int:
        max_blue, max_green, max_red = self.get_maximum_color_count()

        return max_blue * max_green * max_red

    def __str__(self) -> str:
        cubes_str = ', '.join([f"{color}: {count}" for subset in self.cubes_info for color, count in subset.items()])
        return f"Game {self.game_id}: {cubes_str}"
