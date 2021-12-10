import unittest

from python.src.y2021.dec10 import Dec10, NavLine


class TestDec10(unittest.TestCase):

    def test_syntax_error_score(self):
        data = [
            "[({(<(())[]>[[{[]{<()<>>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{[]{()[[[]",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]"
        ]
        self.assertEqual(26397,
                         Dec10(instructions=data).part_1())

    def test_complete_lines(self):
        data = [
            ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
            ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
            ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
            ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
            ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>")
        ]

        for line, expected in data:
            self.assertEqual(expected,
                             NavLine(line).complete)

        self.assertEqual(
            288957,
            Dec10(instructions=[d[0] for d in data]).part_2()
        )
