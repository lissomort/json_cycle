#!/usr/bin/python3

from unittest.mock import patch
from data import is_correct_cycle
from algo import find_cycles


def test_data_is_correct_cycle_backedge():
    assert is_correct_cycle(["one", "one"], []) is False


def test_data_is_correct_cycle_already_added():
    assert is_correct_cycle(["one", "two", "one"], [["one", "two", "one"]]) is False


def test_data_is_correct_cycle_not_minimum_cycle():
    assert is_correct_cycle(["one", "two", "three", "two"], []) is False


@patch("algo.util_rec_function")
def test_algo_find_cycles_no_cycles(mock_util_func):
    mock_util_func.return_value = True
    result = find_cycles({"one": ["two", "three"], "two": "four", "four": "one"})
    assert result == []
