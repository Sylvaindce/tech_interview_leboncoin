#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

import map_utils


class MapError(Exception):
    """
    Class for map error exceptions
    """

    pass


class MapSolver:
    """
    This class take as argument a path of map file or directly the map str
    Once the map validated ( public method: check() ), you can run the solver ( public method: solve() )
    You can save the result to a file if the argument 'save_to_file=True' is provided to solve method
    """

    # Optimization: set class attributes
    __slots__ = [
        "__filename",
        "__given_map",
        "__line_count",
        "__empty_char",
        "__barrier_char",
        "__solid_char",
        "__result",
    ]

    def __init__(self, given_map: str):
        self.__filename = ""
        self.__given_map = ""
        self.__line_count = 0
        self.__empty_char = None
        self.__barrier_char = None
        self.__solid_char = None
        self.__result = [0, 0, 0]
        self.given_map = given_map

    @property
    def given_map(self):
        """
        Given map getter
        Mandatory to declare the setter below
        """
        return self.__given_map

    @given_map.setter
    def given_map(self, given_map: str):
        """
        Set the given map to the scope of the class (self.__given_map)
        Also start the validity check of the given map
        """
        self.__filename = given_map[0]
        self.__given_map = given_map
        (
            self.__line_count,
            self.__empty_char,
            self.__barrier_char,
            self.__solid_char,
        ) = map_utils.parse_map_param(given_map[0])

    @staticmethod
    def check(given_map) -> bool:
        """
        Run the batch of tests to validate the map
        """
        try:
            if not MapSolver.__is_valid(given_map):
                raise MapError()
        except MapError:
            print("map error", file=sys.stderr)
            return False
        return True

    @staticmethod
    def __is_valid(given_map) -> bool:
        """
        Function to test if the map is valid
        1. Test the minimum lenght of the map
        2. Parse the first line parameters to get parameters (int char char char)
        3. Test if the three char parameters are different
        4. Test if the map have the right amount of line
        5. Test map contains only the provided three characters
        :return: bool, True if it's valid
        """
        if not map_utils.check_min_map_length(given_map):
            return False
        parsed_param = map_utils.parse_map_param(given_map[0])
        if not parsed_param:
            return False
        (
            line_count,
            empty_char,
            barrier_char,
            solid_char,
        ) = parsed_param
        if not map_utils.is_char_param_different(empty_char, barrier_char, solid_char):
            return False
        if not map_utils.is_map_length_equal(line_count, len(given_map)):
            return False
        if not map_utils.is_map_only_contain_param_chars(
            given_map, empty_char, barrier_char
        ):
            return False
        return True

    def solve(self, save_to_file=False):
        """
        Run the solver and print out the result
        """
        self.__find_max_square()
        self.__print_map()
        if save_to_file:
            self.dump_map()

    def __find_max_square(self):
        """
        Create Mask of the given map with the square size at this position

                x1 x2
            -----
        y1 | 6  6
        y2 | 6  ?

        if VAL[y2][x2] is an obstacle square size is 0

        else VAL[y2][x2] = 1 + min( VAL[y2][x1], VAL[y1][x2], VAL[y1][x1] )

         a----b
         |    |
         |    |
         c----d

        Then at at the position [y2][x2] we can fit a square of size 7 and the known position of it
        is the right bottom corner (d).

        Save the position of the position and the maximum square size in self.__result = [y, x, square_size]
        """
        line_length = len(self.__given_map[1])
        mask_tab = [[0 for _ in range(line_length)] for _ in range(self.__line_count)]

        for y, line in enumerate(self.__given_map[1:]):
            for x, row in enumerate(line):
                if row != self.__barrier_char:
                    try:
                        square_size = 1 + min(
                            mask_tab[y][x - 1],
                            mask_tab[y - 1][x],
                            mask_tab[y - 1][x - 1],
                        )
                    except IndexError:
                        square_size = 1
                    mask_tab[y][x] = square_size
                    if square_size > self.__result[2]:
                        self.__result = [y, x, square_size]

    def __print_map(self):
        """
        Simple function to print the obtained result
        """
        for i in range(self.__result[2]):
            line = list(self.__given_map[self.__result[0] - i + 1])
            for j in range(self.__result[2]):
                line[self.__result[1] - j] = self.__solid_char
            self.__given_map[self.__result[0] - i + 1] = "".join(line)
        print("\n".join(self.__given_map[1:]))

    def dump_map(self):
        """
        Simple function to dump map into file
        """
        output_filename = self.__filename + "_solved.txt"
        with open(output_filename, "w", encoding="utf-8") as output_fd:
            for line in self.__given_map:
                output_fd.write(line)
                output_fd.write("\n")


def run(args):
    for arg in args[1:]:
        given_map = map_utils.extract_map(arg)
        if MapSolver.check(given_map):
            map_solver = MapSolver(given_map)
            map_solver.solve(save_to_file=True)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv)
    else:
        """
        If no map provided, generate a random map
        Following import are only used for the map generator
        """
        import io
        import random

        try:
            proj_base_path = os.path.realpath(
                os.path.join(os.path.dirname(__file__), "..", "..", "materials")
            )
            sys.path.append(proj_base_path)
            import map_gen
        except ModuleNotFoundError:
            proj_base_path = os.path.realpath(
                os.path.join(os.path.dirname(__file__), "materials")
            )
            sys.path.append(proj_base_path)
            import map_gen

        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        map_gen.map_gen(
            random.randint(0, 20), random.randint(0, 20), random.randint(1, 5)
        )

        output = new_stdout.getvalue()
        sys.stdout = old_stdout

        print("##### GENERATED MAP #####")
        print(output)
        print("##### GENERATED MAP #####")
        given_map = map_utils.extract_map(output)
        if MapSolver.check(given_map):
            map_solver = MapSolver(given_map)
            map_solver.solve(save_to_file=False)