import pytest

import tinylm


def test_get_table_returns_transitions_for_simple_corpora() -> None:
    assert tinylm.get_table("xyxz") == {"x" : {"y":1, "z":1}, "y" : {"x":1}}
    assert tinylm.get_table("abab") == {"a" : {"b":2}, "b" : {"a":1}}


def test_predict_returns_only_possible_next_character() -> None:
    model = tinylm.Markov("abc")
    assert model.predict("a") == "b"
    assert model.predict("b") == "c"


def test_get_table_returns_multiple_possible_continuations() -> None:
    assert tinylm.get_table("abaca") == {'a': {'b': 1, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}}

def test_predict_raises_key_error_for_unknown_context() -> None:
    model = tinylm.Markov("abc")
    with pytest.raises(KeyError):
        model.predict("z")


def test_get_table_returns_empty_transitions_for_empty_corpus() -> None:
    assert tinylm.get_table("") == {}


def test_get_table_returns_empty_transtions_for_single_character_corpus() -> None:
    assert tinylm.get_table("a") == {}


def test_get_table_returns_empty_table_when_context_size_equals_context_length() -> None:
    assert tinylm.get_table("ab", size=2) == {}
