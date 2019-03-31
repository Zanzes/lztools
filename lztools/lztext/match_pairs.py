from collections import namedtuple

MatchPair = namedtuple("MatchPair", ["open", "close"])
brace_matcher = MatchPair("{", "}")
bracket_matcher = MatchPair("[", "]")
parentheses_matcher = MatchPair("(", ")")
greater_and_less_than_matcher = MatchPair("<", ">")
quotes_matcher = MatchPair('"', '"')
quote_matcher = MatchPair("'", "'")