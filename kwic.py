#kwic.py
#implements kwic as a class

import eventspec
DEBUG = False

es = eventspec.EventSpec("kwic.fsm")

class Kwic:
    def __init__(self, periodsToBreaks = False, ignoreWords = []):
        es.event("callConstructor")
        self.periodsToBreaks = periodsToBreaks
        self.ignoreWords = ignoreWords
        self.text= ""

    def addText(self, text):
        es.event("callAddText")
        self.text += text

    def listPairs(self):
        es.event("callListPairs")
        lines = splitBreaks(self.text, self.periodsToBreaks)
        splitLines = splitTheLines(lines)
        return getPairs(splitLines)

    def index(self):
        es.event("callIndex")
        return kwic(self.text, self.ignoreWords, False, self.periodsToBreaks)

    def reset(self):
        ev.event("callReset")
        self.text = ""
        self.idx = 0

    def getFSMState(self):
        es.printLog()


# OG kwic functions
def shift(line):
    return [line[i:] + line[:i] for i in xrange(0,len(line))]

def cleanWord(word):
    return filter (lambda c: c not in [".",",","?","!",":"], word.lower())

def ignorable(word,ignoreWords):
    return cleanWord(word) in map(lambda w: w.lower(), ignoreWords)

def splitBreaks(string, periodsToBreaks):
    es.event("callSplitBreaks")
    if not periodsToBreaks:
        return string.split("\n")
    else:
        line = ""
        lines = []
        lastChar1 = None
        lastChar2 = None
        breakChars = map(chr, xrange(ord('a'),ord('z')+1))
        for c in string:
            if (c == " ") and (lastChar1 == ".") and (lastChar2 in breakChars):
                lines.append(line)
                line = ""
            line += c
            lastChar2 = lastChar1
            lastChar1 = c
        lines.append(line)
        return lines

def splitTheLines(lines):
    es.event("callSplitTheLines")
    return map(lambda l: l.split(), lines)

def kwic(string, ignoreWords=[], listPairs=False, periodsToBreaks=False):
    lines = splitBreaks(string, periodsToBreaks)
    splitLines = splitTheLines(lines)
    if listPairs:
        pairs = getPairs(splitLines)
    es.event("shiftLines")
    shiftedLines = [map(lambda x:(x,i), shift(splitLines[i])) for i in xrange(0,len(splitLines))]
    es.event("flattenLines")
    flattenedLines = [l for subList in shiftedLines for l in subList]
    es.event("filterLines")
    filteredLines = filter(lambda l: not ignorable(l[0][0], ignoreWords), flattenedLines)
    es.event("sortResult")
    if not listPairs:
        res = sorted(filteredLines, key = lambda l: (map(cleanWord, l[0]),l[1]))
    else:
        res = (sorted(filteredLines, key = lambda l: (map(lambda w:w.lower(), l[0]),l[1])),
                map(lambda wp: (wp, pairs[wp]), sorted(filter(lambda wp: pairs[wp] > 1, pairs.keys()))))
    if DEBUG:
        print "==============Original result=================================="
        print res
    return res

def getPairs(splitLines):
    es.event("callGetPairs")
    pairs = {}
    for l in splitLines:
        seen = set([])
        for wu1 in l:
            wc1 = cleanWord(wu1)
            if len(wc1) == 0:
                continue
            for wu2 in l:
                wc2 = cleanWord(wu2)
                if wc1 < wc2:
                    if (wc1,wc2) in seen:
                        continue
                    seen.add((wc1,wc2))
                    if (wc1, wc2) in pairs:
                        pairs[(wc1,wc2)] += 1
                    else:
                        pairs[(wc1,wc2)] = 1
    return pairs
