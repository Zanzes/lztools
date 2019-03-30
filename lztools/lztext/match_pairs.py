from collections import namedtuple

MatchPair = namedtuple("MatchPair", ["open", "close"])
brace = MatchPair("{", "}")
bracket = MatchPair("[", "]")
parentheses = MatchPair("(", ")")
greater_and_less_than = MatchPair("<", ">")
double_quotes = MatchPair('"', '"')
quotes = MatchPair("'", "'")