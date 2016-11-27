#kwic.py
#implements kwic as a class

from mykwic import *
from mykwic import kwic as kwicit

class Kwic:
    def __init__(self, periodsToBreaks = False, ignoreWords = []):
        self.periodsToBreaks = periodsToBreaks
        self.ignoreWords = ignoreWords
        self.idx = 0
        self.text= ""

    def addText(self, text):
        self.text += text
        sb = splitBreaks(text, self.periodsToBreaks)
        self.idx +=win len(sb) - 1

    def getText(self):
        return self.text

    def listPairs(self):
        lines = splitBreaks(self.text, self.periodsToBreaks)
        splitLines = splitTheLines(lines)
        return getPairs(splitLines)

    def index(self):
        return self.idx

    def reset(self):
        self.text = ""
        self.idx = 0

    def kwic(self):
        return kwicit(self.text, self.ignoreWords, False, self.periodsToBreaks)
