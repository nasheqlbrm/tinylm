import random

class Markov:
    def __init__(self, txt: str, size: int = 1) -> None:
        self.tables = [get_table(txt, size = i + 1) for i in range(size)]

    def predict(self, txt: str) -> str:
        """
        Given some text, predict the next character

	>>> m = Markov("abc")
        >>> m.predict("z") # doctest: +ELLIPSIS
        Traceback (most recent call last):
          ...
        KeyError: ...

        """
        table = self.tables[len(txt) - 1]
        next_counts = table.get(txt, {})
        if not next_counts:
            raise KeyError(f"{txt} not found")
        options: list[str] = []
        for next_char, count in next_counts.items():
            options.extend([next_char] * count)
        return random.choice(options)

def get_table(txt: str, size: int = 1) -> dict[str, dict[str, int]]:
    """
    Build a transition table form a training string
 
    >>> get_table("xyxz")
    {'x': {'y': 1, 'z': 1}, 'y': {'x': 1}}


    >>> get_table("abab") # doctest: +NORMALIZE_WHITESPACE
        {'a': {'b': 2}, 'b': {'a': 1}}
    """

    results: dict[str, dict[str, int]] = {}
    for i in range(len(txt)):
        chars = txt[i : i + size]
        try:
            out = txt[i + size]
        except IndexError:
            break

        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results

def main() -> None:
    print("Hello from tinylm!")
