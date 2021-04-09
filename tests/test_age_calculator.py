#!/usr/bin/env python

"""Tests for `age_calculator` package."""
from datetime import datetime

import pytest


from age_calculator import age_calculator
from age_calculator.age_calculator import age_in_days, age_in_hours


@pytest.mark.parametrize(
    "date_of_birth, date_of_death, expected_days",
    [
        (datetime(1941, 1, 8), datetime(1989, 10, 4), 17_801),
        (datetime(1939, 10, 27), None, 29_750),
        (datetime(1940, 11, 22), None, 29_358),
        (datetime(1943, 3, 29), None, 28_501),
        (datetime(1942, 2, 1), datetime(2020, 1, 21), 28_478),
        (datetime(1943, 5, 5), None, 28_464),
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
    assert age_in_days(date_of_birth, date_of_death) >= expected_days


@pytest.mark.parametrize(
    "date_of_birth, date_of_death, expected_hours",
    [
        (datetime(1941, 1, 8), datetime(1989, 10, 4), 427_224),
        (datetime(1939, 10, 27), None, 714_000),
        (datetime(1940, 11, 22), None, 704_592),
        (datetime(1943, 3, 29), None, 684_024),
        (datetime(1942, 2, 1), datetime(2020, 1, 21), 683_472),
        (datetime(1943, 5, 5), None, 683_136),
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
