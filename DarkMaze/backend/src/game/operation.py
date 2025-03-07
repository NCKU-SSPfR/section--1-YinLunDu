from ..database.operation import save_game_state
from .judge import hit_obstacle, is_game_over, arrive_at_destination

def move_player(game_state, direction):
    if is_game_over(game_state["health"]):
        return game_state  # 遊戲已結束，直接返回

    x, y = game_state["current_position"]
    
    # 定義移動方向的映射表
    direction_map = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    if direction in direction_map:
        dx, dy = direction_map[direction]
        new_x, new_y = x + dx, y + dy
    else:
        return game_state  # 無效的方向，直接返回

    # 檢查是否超出邊界
    width, height = game_state["map_size"]
    if not (0 <= new_x < width and 0 <= new_y < height):
        return game_state  # 超出邊界，不更新位置

    next_position = [new_x, new_y]
    level_name = game_state["current_level_name"]

    if hit_obstacle(next_position, level_name):
        game_state["health"] -= 1  # 碰到障礙物扣血
    else:
        # 若沒碰到障礙物，更新玩家位置
        if next_position not in game_state["path"]:
            game_state["path"].append(next_position)
        game_state["current_position"] = next_position

    if arrive_at_destination(level_name, game_state["current_position"]):
        game_state["health"] = 666  # 玩家到達終點，設定特殊數值代表勝利

    # 更新遊戲狀態到資料庫
    save_game_state(
        game_state["username"], level_name, game_state["map_size"],
        game_state["health"], game_state["path"], game_state["current_position"]
    )

    return game_state
