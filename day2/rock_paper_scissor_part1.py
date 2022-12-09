from enum import Enum


class GameObject(Enum):
    ROCK = 1,
    PAPER = 2,
    SCISSOR = 3


class GameResult(Enum):
    WIN = 6,
    LOSE = 0,
    DRAW = 3


player1_object_map = {
    'A': GameObject.ROCK,
    'B': GameObject.PAPER,
    'C': GameObject.SCISSOR
}

player2_object_map = {
    'X': GameObject.ROCK,
    'Y': GameObject.PAPER,
    'Z': GameObject.SCISSOR
}


def game_result(player_choices):
    match player_choices:
        case (GameObject.ROCK, GameObject.ROCK):
            return GameResult.DRAW
        case (GameObject.PAPER, GameObject.PAPER):
            return GameResult.DRAW
        case (GameObject.SCISSOR, GameObject.SCISSOR):
            return GameResult.DRAW
        case (GameObject.ROCK, GameObject.SCISSOR):
            return GameResult.WIN
        case (GameObject.PAPER, GameObject.ROCK):
            return GameResult.WIN
        case (GameObject.SCISSOR, GameObject.PAPER):
            return GameResult.WIN
        case (GameObject.ROCK, GameObject.PAPER):
            return GameResult.LOSE
        case (GameObject.PAPER, GameObject.SCISSOR):
            return GameResult.LOSE
        case (GameObject.SCISSOR, GameObject.ROCK):
            return GameResult.LOSE


def map_game_strategy_line(game_strategy_line):
    game_strategy = game_strategy_line.split()
    player1_choice = player1_object_map.get(game_strategy[0])
    player2_choice = player2_object_map.get(game_strategy[1])
    return player1_choice, player2_choice


def get_strategy_list():
    game_strategy_list = list(map(map_game_strategy_line, open("input").read().splitlines()))
    return game_strategy_list


def get_total_score():
    total_score = 0
    for player_choices in get_strategy_list():
        result = game_result(player_choices)
        total_score = total_score + player_choices[0].value + result.value

    print(total_score)


if __name__ == '__main__':
    get_total_score()
