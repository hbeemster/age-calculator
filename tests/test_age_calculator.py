#!/usr/bin/env python

"""Tests for `age_calculator` package.


Now using FreezeGun!
FreezeGun is a library that allows your Python tests to travel through time by mocking the datetime module.

We can now exactly test the expected values, so this is independent of the current date.


https://pypi.org/project/freezegun/
https://pypi.org/project/pytest-freezegun/
"""
from datetime import datetime

import pytest

from age_calculator.age_calculator import age_in_days, age_in_hours, date_diff

# Test on this date
TEST_DATE = "2021-01-21"

# ------------------------------------------------------------------------
@pytest.mark.freeze_time(TEST_DATE)
@pytest.mark.parametrize(
    "date_of_birth, date_of_death, expected_days",
    [
        (datetime(1941, 1, 8), datetime(1989, 10, 4), 17_801),
        (datetime(1939, 10, 27), None, 29_672),
        (datetime(1940, 11, 22), None, 29_280),
        (datetime(1943, 3, 29), None, 28_423),
        (datetime(1942, 2, 1), datetime(2020, 1, 21), 28_478),
        (datetime(1943, 5, 5), None, 28_386),
    ],
    ids=[
        "Graham Chapman",
        "John Cleese",
        "Terry Gilliam",
        "Eric Idle",
        "Terry Jones",
        "Michael Palin",
    ],
)
def test_age_in_days(date_of_birth, date_of_death, expected_days):
    assert age_in_days(date_of_birth, date_of_death) == expected_days


# ------------------------------------------------------------------------
@pytest.mark.freeze_time(TEST_DATE)
@pytest.mark.parametrize(
    "date_of_birth, date_of_death, expected_hours",
    [
        (datetime(1941, 1, 8), datetime(1989, 10, 4), 427_224),
        (datetime(1939, 10, 27), None, 712_128),
        (datetime(1940, 11, 22), None, 702_720),
        (datetime(1943, 3, 29), None, 682_152),
        (datetime(1942, 2, 1), datetime(2020, 1, 21), 683_472),
        (datetime(1943, 5, 5), None, 68_1264),
    ],
    ids=[
        "Graham Chapman",
        "John Cleese",
        "Terry Gilliam",
        "Eric Idle",
        "Terry Jones",
        "Michael Palin",
    ],
)
def test_age_in_hours(date_of_birth, date_of_death, expected_hours):
    assert age_in_hours(date_of_birth, date_of_death) >= expected_hours


# ------------------------------------------------------------------------
@pytest.mark.freeze_time(TEST_DATE)
@pytest.mark.parametrize(
    "date_from, date_to, expected_days",
    [
        (datetime(2021, 1, 1), datetime(2021, 1, 2), 1),
        (datetime(2021, 1, 1), datetime(2021, 1, 3), 2),
        (datetime(2021, 1, 1), None, 20),
    ],
)
def test_date_diff(date_from, date_to, expected_days):
    """"""
    assert date_diff(date_from, date_to) == expected_days
