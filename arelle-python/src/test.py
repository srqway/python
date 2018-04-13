from arelle import Cntlr

xbrl = Cntlr.Cntlr(logFileName='/tmp/test.txt').modelManager.load('/home/hsiehpinghan/git/python/arelle-python/xbrl/tifrs-20130331/XBRL_TW_Entry_Points/FH/tifrs-fr0-m1-fh-cr-2888-2013Q1.xml')
#print(xbrl.modelObjects)
for fact in xbrl.facts:
   print(type(fact))