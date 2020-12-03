#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re


def extract_map(given_map: str) -> list:
    """
    Simple function to read the map file or the pure string map

    :param given_map: str, given map
    :return: list, splitted map
    """
    if check_desired_arg_format(given_map):
        if os.path.exists(given_map):
            with open(given_map, "r", encoding="utf-8") as map_txt:
                given_map = map_txt.read()
        given_map = given_map.split("\n")
        if len(given_map) > 1 and given_map[-1] == "":
            given_map.pop()
        return given_map
    return []


def check_desired_arg_format(given_map) -> bool:
    """
    Take the given argument at the instantiation of the object and check if it's the expected type

    :param given_map: passed arg to class
    :return: bool, True if it's an str
    """
    return type(given_map) == str


def parse_map_param(param_line: str) -> tuple:
    """
    Parse the parameters of the map

    :param param_line: str, first line map
    :return: tuple, (line_count, empty_char, barrier_char, solid_char)
    """
    if len(param_line) >= 4:
        solid_char = param_line[-1]
        barrier_char = param_line[-2]
        empty_char = param_line[-3]
        if not param_line[:-3].isdigit():
            return ()
        line_count = int(param_line[:-3])
        return line_count, empty_char, barrier_char, solid_char
    return ()


def is_map_length_equal(param_length: int, computed_length: int) -> bool:
    """
    Check if the length of the map is equal to the given length in parameters line

    :param param_length: int, length from parameters
    :param computed_length: int, length of the file
    :return: bool, True if length are equal
    """
    return computed_length - 1 == param_length


def is_char_param_different(
    empty_char: str, barrier_char: str, solid_char: str
) -> bool:
    """
    Check is char given in parameters are different

    :param empty_char: str, given empty character
    :param barrier_char: str, given barrier character
    :param solid_char: str, given solid character
    :return: bool, True if all different
    """
    return (
        empty_char != barrier_char
        and empty_char != solid_char
        and barrier_char != solid_char
    )


def check_min_map_length(given_map: list) -> bool:
    """
    Check the minimum required length of the map

    :param given_map: list, splitted given map
    :return: bool, True if map has the minimum length required
    """
    return not (len(given_map) < 2 or len(given_map[1]) < 1)


def is_map_only_contain_param_chars(
    given_map: list, empty_char: str, barrier_char: str
) -> bool:
    """
    Check if the map contains only the given characters

    :param given_map: list, splitted given map
    :param empty_char: str, given empty character
    :param barrier_char: str, given barrier character
    :return: bool, True if map only contains the given characters
    """
    regex_char = "([%c%c]+)" % (empty_char, barrier_char)
    line_length = len(given_map[1])
    for line in given_map[1:]:
        if len(re.search(regex_char, line).group()) != line_length:
            return False
    return True
