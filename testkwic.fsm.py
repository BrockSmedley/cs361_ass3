#testkwic.fsm.py
#tests events from kwic
import eventspec

es = eventspec.EventSpec("kwic.fsm")

# we're gonna start in state: start
es.event("callConstructor")

es.event("callReset")
es.event("callAddText")

es.event("callAddText")
es.event("callIndex")
es.event("callAddText")
es.event("callIndex")
es.event("callListPairs")
es.event("callReset")

es.printLog()
