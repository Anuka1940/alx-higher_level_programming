#!/usr/bin/python3
def multiple_returns(sentence):
        if sentence:
            length = len(sentence)
            return length, sentence[0]
        return len(sentence), None
