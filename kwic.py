#kwic.py
#implements kwic as a class

from mykwic import *
from mykwic import kwic as kwicit

class Kwic:
    def __init__(self, periodsToBreaks = False, ignoreWords = []):
        #event: initialize data
        self.periodsToBreaks = periodsToBreaks
        self.ignoreWords = ignoreWords
        self.idx = 0
        self.text= ""

    def addText(self, text):
        #event: add text
        self.text += text
        sb = splitBreaks(text, self.periodsToBreaks)
        incrementIndex(self, len(sb) - 1)

    def incrementIndex(self, increment):
        #event: increment index
        self.idx += increment

    def getText(self):
        #event: get text
        return self.text

    def listPairs(self):
        #event: list pairs
        lines = splitBreaks(self.text, self.periodsToBreaks)
        splitLines = splitTheLines(lines)
        return getPairs(splitLines)

    def index(self):
        #event: get index
        return self.idx

    def reset(self):
        #event: reset data
        self.text = ""
        self.idx = 0

    def kwic(self):
        #event: run kwic
        return kwicit(self.text, self.ignoreWords, False, self.periodsToBreaks)
