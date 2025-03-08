from judge_code import is_game_over

def test_game_over_0():
    assert is_game_over(0) == True

def test_game_over_666():
    assert is_game_over(666) == True

def test_game_over_other():
    assert is_game_over(87) == False
