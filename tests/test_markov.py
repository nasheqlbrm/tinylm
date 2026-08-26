import pytest

import tinylm


def test_get_table() -> None:
    assert tinylm.get_table("xyxz") == {"x" : {"y":1, "z":1}, "y" : {"x":1}}
    assert tinylm.get_table("abab") == {"a" : {"b":2}, "b" : {"a":1}}


def test_predict_deterministic() -> None:
    model = tinylm.Markov("abc")
    assert model.predict("a") == "b"
    assert model.predict("b") == "c"


def test_get_table_nondeterministic() -> None:
    assert tinylm.get_table("abaca") == {'a': {'b': 1, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}}

def test_predict_unknown_raises() -> None:
    model = tinylm.Markov("abc")
    with pytest.raises(KeyError):
        model.predict("z")


def test_predict_unknown_matches_error_message() -> None:
    model = tinylm.Markov("abc")
    with pytest.raises(KeyError, match="not found"):
        model.predict("z")


def test_empty_corpus() -> None:
    assert tinylm.get_table("") == {}


def test_single_character_corpus() -> None:
    assert tinylm.get_table("a") == {}


def test_corpus_and_size_same() -> None:
    assert tinylm.get_table("ab", size=2) == {} 
