import pytest

import map_solver.map_utils as map_utils


@pytest.mark.parametrize(
    "scenario", [("9.ox", True), ([], False), ("", True), (None, False), ((0,), False)]
)
def test_check_desired_arg_format(scenario):
    input_map, expected_result = scenario
    assert map_utils.check_desired_arg_format(input_map) == expected_result


@pytest.mark.parametrize(
    "scenario",
    [
        ("", ()),
        ("9.ox", (9, ".", "o", "x")),
        ("229.ox", (229, ".", "o", "x")),
        ("ooox", ()),
        ("9ooox", ()),
    ],
)
def test_parse_map_param(scenario):
    param_line, expected_result = scenario
    assert map_utils.parse_map_param(param_line) == expected_result


@pytest.mark.parametrize("scenario", [(5, 6, True), (5, 0, False)])
def test_map_length(scenario):
    param_length, computed_length, expected_result = scenario
    assert (
        map_utils.is_map_length_equal(param_length, computed_length) == expected_result
    )


@pytest.mark.parametrize(
    "scenario",
    [
        ("a", "b", "c", True),
        ("b", "b", "c", False),
        ("b", "b", "b", False),
        ("a", "b", "b", False),
    ],
)
def test_is_char_param_different(scenario):
    char_1, char_2, char_3, expected_result = scenario
    assert map_utils.is_char_param_different(char_1, char_2, char_3) == expected_result


@pytest.mark.parametrize(
    "scenario", [(["", "1"], True), ([], False), (["", ""], False)]
)
def test_check_min_map_length(scenario):
    splitted_map, expected_result = scenario
    assert map_utils.check_min_map_length(splitted_map) == expected_result


def test_wrong_char_in_map(bad_map_char):
    parsed_map = bad_map_char.split("\n")[:-1]
    params = map_utils.parse_map_param(parsed_map[0])
    assert (
        map_utils.is_map_only_contain_param_chars(parsed_map, params[1], params[2])
        == False
    )


def test_valid_char_in_map(example_map):
    parsed_map = example_map.split("\n")[:-1]
    params = map_utils.parse_map_param(parsed_map[0])
    assert (
        map_utils.is_map_only_contain_param_chars(parsed_map, params[1], params[2])
        == True
    )
