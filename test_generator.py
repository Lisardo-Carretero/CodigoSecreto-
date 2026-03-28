import random
import unittest

from generator import (
    BLUE_DIAMOND,
    RED_SQUARE,
    EMPTY,
    INFILTRATOR,
    format_card,
    generate_card,
)


class GeneratorTests(unittest.TestCase):
    def test_card_has_correct_counts_when_blue_starts(self) -> None:
        rng = random.Random(123)
        card = generate_card(rng, active_team="blue")
        flat = [cell for row in card for cell in row]

        self.assertEqual(len(flat), 25)
        self.assertEqual(flat.count(BLUE_DIAMOND), 6)
        self.assertEqual(flat.count(RED_SQUARE), 5)
        self.assertEqual(flat.count(INFILTRATOR), 1)
        self.assertEqual(flat.count(EMPTY), 13)

    def test_card_has_correct_counts_when_red_starts(self) -> None:
        rng = random.Random(123)
        card = generate_card(rng, active_team="red")
        flat = [cell for row in card for cell in row]

        self.assertEqual(flat.count(BLUE_DIAMOND), 5)
        self.assertEqual(flat.count(RED_SQUARE), 6)
        self.assertEqual(flat.count(INFILTRATOR), 1)
        self.assertEqual(flat.count(EMPTY), 13)

    def test_formatting_is_deterministic_with_seed(self) -> None:
        rng = random.Random(42)
        card = generate_card(rng, active_team="blue")
        rendered = format_card(card)

        expected = (
            "- - ■ - -\n"
            "■ ◆ ■ - -\n"
            "X - ◆ - -\n"
            "- ◆ - ◆ -\n"
            "■ ■ ◆ ◆ -"
        )
        self.assertEqual(rendered, expected)


if __name__ == "__main__":
    unittest.main()
