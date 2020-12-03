import pytest

import map_solver.find_square as find_square
import map_utils


def test_wrong_char_map(bad_map_char, capsys):
    extracted_map = map_utils.extract_map(bad_map_char)
    assert find_square.MapSolver.check(extracted_map) == False
    captured = capsys.readouterr()
    assert captured.err == "map error\n"


def test_good_map(example_map, capsys):
    extracted_map = map_utils.extract_map(example_map)
    assert find_square.MapSolver.check(extracted_map) == True
    my_map = find_square.MapSolver(extracted_map)
    my_map.solve()
    captured = capsys.readouterr()
    assert (
        captured.out
        == ".....xxxxxxx...............\n....oxxxxxxx...............\n.....xxxxxxxo..............\n.....xxxxxxx...............\n....oxxxxxxx...............\n.....xxxxxxx...o...........\n.....xxxxxxx...............\n......o..............o.....\n..o.......o................\n"
    )


def test_wrong_map_size(capsys):
    extracted_map = map_utils.extract_map("0.ox")
    assert find_square.MapSolver.check(extracted_map) == False
    captured = capsys.readouterr()
    assert captured.err == "map error\n"