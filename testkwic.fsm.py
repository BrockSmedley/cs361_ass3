#testkwic.fsm.py
#tests events from kwic
import eventspec
import kwic

es = eventspec.EventSpec("kwic.fsm")

print "testing..."
# we're gonna start in state: start
es.event("callConstructor")
es.event("callIndex")

es.event("callReset")
es.event("callAddText")

es.event("callAddText")
es.event("callIndex")
es.event("callAddText")
es.event("callIndex")
es.event("callListPairs")
es.event("callReset")

es.printLog()


print "\nreal shit..."
kk = kwic.Kwic(True)
kk.addText("this is some text I added\nthis is another line of text")
print "RESULT\n", kk.index()

kk.getFSMState()
