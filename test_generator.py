import random
import unittest

from generator import (
    CIRCLE,
    DIAMOND,
    EMPTY,
    INFILTRATOR,
    format_card,
    generate_card,
)


class GeneratorTests(unittest.TestCase):
    def test_card_has_correct_counts(self) -> None:
        rng = random.Random(123)
        card = generate_card(rng)
        flat = [cell for row in card for cell in row]

        self.assertEqual(len(flat), 25)
        self.assertEqual(flat.count(DIAMOND), 6)
        self.assertEqual(flat.count(CIRCLE), 5)
        self.assertEqual(flat.count(INFILTRATOR), 1)
        self.assertEqual(flat.count(EMPTY), 13)

    def test_formatting_is_deterministic_with_seed(self) -> None:
        rng = random.Random(42)
        card = generate_card(rng)
        rendered = format_card(card)

        expected = (
            "- - O - -\n"
            "O ♦ O - -\n"
            "X - ♦ - -\n"
            "- ♦ - ♦ -\n"
            "O O ♦ ♦ -"
        )
        self.assertEqual(rendered, expected)


if __name__ == "__main__":
    unittest.main()
