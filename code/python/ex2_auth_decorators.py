from enum import Enum
from functools import wraps

class GameResult(Enum):
    CAT1_WON = "1"
    CAT2_WON = "0"
    DRAW = "0.5"

class Permissions(Enum):
    READ = "read"
    UPDATE = "update"

permissions = [Permissions.READ, Permissions.UPDATE]

def require_update_purrrmission(func):
    @wraps(func)
    
    def wrapper(*args, **kwargs):
        if not Permissions.UPDATE in permissions:
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper

class SensitiveFunctions:

    @require_update_purrrmission
    def update_score_board(cat1, cat2, game_result: GameResult):
        print("Winner is {0}".format(cat1))
        # Update score board

    def next_move_cat(cat, move):
        print("{0} plays the next move which is {1}".format(cat, move))
        play_move(cat, move)
        # Update game notes

SensitiveFunctions.next_move_cat("tabby", "Qxh6")
SensitiveFunctions.update_score_board("tabby", "simba", GameResult.CAT1_WON)