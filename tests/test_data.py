from pathlib import Path

import pandas as pd
import pytest

from tennisage.data import _clean_matches, _parse_career_js, _url_name


DATA = Path(__file__).parent / "data"
female = _parse_career_js((DATA / "FemalePlayerCareer.js").read_text())
male = _parse_career_js((DATA / "MalePlayerCareer.js").read_text())


def test_parse():
    assert female.shape == (3, 8)
    assert list(female["opponent"]) == ["Anne Miller", "Alexia Dechaume Balleret", "Magui Serna"]
    assert list(male["result"]) == ["L", "L", "W"]


def test_ages_female():
    serena = _clean_matches(female, pd.Timestamp("1981-09-26"))
    # same as the first row of serena.csv in hw2
    assert serena["age_player"][0] == pytest.approx(14.0917, abs=1e-4)
    assert serena["age_opponent"][0] == pytest.approx(18.7762, abs=1e-4)
    assert serena["age_gap"][0] == pytest.approx(-4.6845, abs=1e-4)


def test_ages_male():
    rafa = _clean_matches(male, pd.Timestamp("1986-06-03"))
    # the men's file already has the opponent's age
    assert list(rafa["age_opponent"]) == [22.264202601, 24.2902121834, 18.7597535934]
    assert rafa["age_player"][0] == pytest.approx(15.27, abs=0.01)


def test_url_name():
    assert _url_name("serena williams") == "SerenaWilliams"
    assert _url_name("Serena Williams") == "SerenaWilliams"
    assert _url_name("SerenaWilliams") == "SerenaWilliams"
