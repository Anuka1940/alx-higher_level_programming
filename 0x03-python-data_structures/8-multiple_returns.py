#!/usr/bin/python3
def multiple_returns(sentence):
        if len(sentence) > 0:
            length = len(sentence)
            return length, sentence[0]
        elif len(sentence) == 0:
            return len(sentence), None
