# pylint: disable=missing-docstring

from enum import Enum


class PlayerChoice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class GameResult(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3


player1_object_map = {
    'A': PlayerChoice.ROCK,
    'B': PlayerChoice.PAPER,
    'C': PlayerChoice.SCISSOR
}

player2_object_map = {
    'X': PlayerChoice.ROCK,
    'Y': PlayerChoice.PAPER,
    'Z': PlayerChoice.SCISSOR
}


def game_result(player_choices):
    match player_choices:
        case (PlayerChoice.ROCK, PlayerChoice.ROCK):
            return GameResult.DRAW
        case (PlayerChoice.PAPER, PlayerChoice.PAPER):
            return GameResult.DRAW
        case (PlayerChoice.SCISSOR, PlayerChoice.SCISSOR):
            return GameResult.DRAW
        case (PlayerChoice.ROCK, PlayerChoice.SCISSOR):
            return GameResult.LOSE
        case (PlayerChoice.PAPER, PlayerChoice.ROCK):
            return GameResult.LOSE
        case (PlayerChoice.SCISSOR, PlayerChoice.PAPER):
            return GameResult.LOSE
        case (PlayerChoice.ROCK, PlayerChoice.PAPER):
            return GameResult.WIN
        case (PlayerChoice.PAPER, PlayerChoice.SCISSOR):
            return GameResult.WIN
        case (PlayerChoice.SCISSOR, PlayerChoice.ROCK):
            return GameResult.WIN


def map_game_strategy_line(game_strategy_line):
    game_strategy = game_strategy_line.split()
    player1_choice = player1_object_map[game_strategy[0]]
    player2_choice = player2_object_map[game_strategy[1]]
    return player1_choice, player2_choice


def get_strategy_list():
    game_strategy_list = list(map(
        map_game_strategy_line, open("input", encoding="utf-8").
            read().splitlines()
        ))
    return game_strategy_list


def get_total_score():
    total_score = 0
    for player_choices in get_strategy_list():
        result = game_result(player_choices)
        total_score = total_score + player_choices[1].value + result.value

    print(total_score)


if __name__ == '__main__':
    get_total_score()
