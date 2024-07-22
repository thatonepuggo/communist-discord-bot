import re
from re import RegexFlag
import util

REGEX_FLAGS = RegexFlag.IGNORECASE | RegexFlag.MULTILINE | RegexFlag.UNICODE

class Phrase:
    def __init__(self, regex: str, credits: int):
        self.regex = regex
        self.credits = credits

    def replace_vars(self, regex: str):
        return util.format_var(regex, {
            "articles": r"(the|a|an)",
            "communism": r"(ccp|communism|communist|china|the party)",
            "capitalism": r"(america|capitalism|burgers|imperialism|the west)",
            "bad": r"(bad|horrible|shit|idiot)",
            "good": r"(good|cool|sigma|epic|epik|awesome)",
        })

    def matches(self, string: str) -> list:
        replaced = self.replace_vars(self.regex)
        return re.findall(replaced, string, REGEX_FLAGS)

phrases = [
    Phrase(r"%articles%? ?%communism% is %bad%", -100),
    Phrase(r"%articles%? ?%communism% is %good%", 100),

    Phrase(r"i (love|like) %articles%? ?ccp", 100),
    Phrase(r"i (hate|dislike) %articles%? ?ccp", -100),

    Phrase(r"france", -500),
    Phrase(r"oak", -500),

    Phrase(r"taiwan is not %articles%? ?country", 10000),
    Phrase(r"taiwan is %articles%? ?country", -10000),

    Phrase(r"bing chilling", 10),
    Phrase(r"ching chong", 10),

    Phrase(r"glory to %articles%? ?%communism%", 500),
    Phrase(r"glory to %articles%? ?%capitalism%", -1000),

    Phrase(r"winnie the pooh", -1000000000),

    Phrase(r"remove all enemies of %articles%? state", 900),

    Phrase(r"tiananmen square", -10000),
    Phrase(r"1989", -10000),
    Phrase(r"1984", -1000),

]

def get_msg_credit(string: str) -> int:
    ret = 0
    for phrase in phrases:
        ret += len(phrase.matches(string)) * phrase.credits
    return ret