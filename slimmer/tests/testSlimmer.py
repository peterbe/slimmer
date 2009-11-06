import os
from time import time
import unittest
import codecs

import sys
sys.path.insert(0,'../')
import slimmer

VERBOSE = False

from codechunks import *

class SlimmerTestCase(unittest.TestCase):
    
    def _assert(self, str1, str2, name=''):
        """ special kind of assertEqual that strips """
        if not str1.strip() == str2.strip():
            print '\n'+"-"*70
            print "DIFFERENCES %s"%name
            print "----Result|"+"-"*50
            #print repr(str1.strip())
            print str1.strip()
            print "----Expect|"+"-"*50
            #print repr(str2.strip())
            print str2.strip()
            print "-"*70
            x = str1.strip()
            y = str2.strip()
            print x
            arrow = ''
            for i, e in enumerate(list(x)):
                if e==y[i]:
                    arrow += "-"
                else:
                    arrow += "^"
                    break
            print arrow            
        self.assertEqual(str1.strip(), str2.strip())
        #assert str1.strip() == str2.strip()
        #return self.assertEqual(str1.strip(), str2.strip())
    
    def timer(self, name, timeittook, size1, size2):
        record = {'name':name, 'time':timeittook,
                  'size1':size1, 'size2':size2}
        records = self.timed_records
        records.append(record)
        self.time_records = records

    
    def setUp(self):
        self.timed_records=[]
        
    def tearDown(self):
        for record in self.timed_records:

            if VERBOSE:
                print "-- %s --:"%record['name']
                print "%s seconds"%round(record['time'], 6)
                print "Was: %s\tNow: %s"%(record['size1'], record['size2'])
                percent = round(100*record['size2']/float(record['size1']), 5)
                percent = "%s%%"%percent
                difference = record['size1'] - record['size2']
                print "Difference: %s (%s)"%(difference, percent)
                print 
            

    def atest(self, str1, str2, name, func, printresult=VERBOSE, *args, **kw):
        """ standard type of test """
        before = str1
        expect = str2
        
        t0=time()
        args = [before]+list(args)
        result = apply(func, args, kw)
        if printresult:
            print result
        T = time()-t0
        
        self.timer(name,time()-t0, len(before), len(result))
        
        self._assert(result, expect, name)

        
        
    #--- Start the madness! ----------------------------------------------
    
    def testGuessSyntax(self):
        for var, value in globals().items():
            syntax = None
            if var.find('CSS')> -1:
                syntax = slimmer.guessSyntax(value)
                self.assertEqual(syntax, 'css')
            elif var.find('JS')> -1:
                syntax = slimmer.guessSyntax(value)
                self.assertEqual(syntax, 'js')
            elif var.find('HTML')> -1:
                syntax = slimmer.guessSyntax(value)
                self.assertTrue(syntax in ('html','xhtml'))
                
            else:
                continue
            
    def testGuessHTMLorXHTML(self):
        code = """<ul>
        <li>One</li>
        <li>Two</li>
        </ul>"""
        self.assertEqual(slimmer.guessSyntax(code), 'html')
        
        code = """
        <a href="foo.html"><img src="foo.jpg" /></a>
        """
        self.assertEqual(slimmer.guessSyntax(code), 'xhtml')
            
    
    def testCSS1(self):
        before = CSS_1
        expect = expect_CSS_1
        self.atest(before, expect, "CSS1", slimmer.css_slimmer)
        
    def testCSS2(self):
        before = CSS_2
        expect = expect_CSS_2
        self.atest(before, expect, "CSS2", slimmer.css_slimmer)

    def testCSS3(self):
        before = CSS_3
        expect = expect_CSS_3
        self.atest(before, expect, "CSS3", slimmer.css_slimmer)
        
    def testCSS3b(self):
        before = CSS_3b
        expect = expect_CSS_3b
        self.atest(before, expect, "CSS3b", slimmer.css_slimmer)        

    def testCSS3c(self):
        before = CSS_3c
        expect = expect_CSS_3c
        self.atest(before, expect, "CSS3c", slimmer.css_slimmer)
        
    def testCSS4(self):
        before = CSS_4
        expect = expect_CSS_4
        self.atest(before, expect, "CSS4", slimmer.css_slimmer)        

    def testCSS5(self):
        before = CSS_5
        expect = expect_CSS_5
        self.atest(before, expect, "CSS5", slimmer.css_slimmer)
        
    def testCSS6(self):
        before = CSS_6
        expect = expect_CSS_6
        self.atest(before, expect, "CSS6", slimmer.css_slimmer)
    
    def testCSS7(self):
        before = CSS_7
        expect = expect_CSS_7
        self.atest(before, expect, "CSS6", slimmer.css_slimmer)    

    def testHTML1(self):
        before = HTML_1
        expect = expect_HTML_1
        self.atest(before, expect, "HTML1", slimmer.html_slimmer)

    def testHTML2(self):
        before = HTML_2
        expect = expect_HTML_2
        self.atest(before, expect, "HTML2", slimmer.html_slimmer)
        
    def testHTML3(self):
        before = HTML_3
        expect = expect_HTML_3
        self.atest(before, expect, "HTML3", slimmer.html_slimmer)        
        
    def testHTML4(self):
        before = HTML_4
        expect = expect_HTML_4
        self.atest(before, expect, "HTML4", slimmer.html_slimmer)        
        
    def testHTML5(self):
        before = HTML_5
        expect = expect_HTML_5
        self.atest(before, expect, "HTML5", slimmer.html_slimmer)
        
    def testHTML6(self):
        before = HTML_6
        expect = expect_HTML_6
        self.atest(before, expect, "HTML6", slimmer.html_slimmer)
        
    def testHTML7(self):
        before = HTML_7
        expect = expect_HTML_7
        self.atest(before, expect, "HTML7", slimmer.html_slimmer)
        
    def testHTML8(self):
        before = HTML_8
        expect = expect_HTML_8
        self.atest(before, expect, "HTML8", slimmer.html_slimmer)
        
    def testHTML9(self):
        """ UTF-8 characters in the HTML """
        before = HTML_9
        expect = expect_HTML_9
        self.atest(before, expect, "HTML9", slimmer.html_slimmer)        
        
    def testJS1(self):
        before = JS_1
        expect = expect_JS_1
        self.atest(before, expect, "JS1", slimmer.js_slimmer)
        
    def testJS2(self):
        before = JS_2
        expect = expect_JS_2
        self.atest(before, expect, "JS2", slimmer.js_slimmer)        
        
    def testJS3(self):
        before = JS_3
        expect = expect_JS_3
        self.atest(before, expect, "JS3", slimmer.js_slimmer)                

    def testJS4(self):
        before = JS_4
        expect = expect_JS_4
        self.atest(before, expect, "JS4", slimmer.js_slimmer)
        
    def testJS5(self):
        before = JS_5
        expect = expect_JS_5
        self.atest(before, expect, "JS5", slimmer.js_slimmer)
        
    def testJS6(self):
        before = JS_6
        expect = expect_JS_6
        self.atest(before, expect, "JS6", slimmer.js_slimmer)
        
    def testJS8(self):
        before = JS_8
        expect = expect_JS_8
        self.atest(before, expect, "JS8", slimmer.js_slimmer)        

    def testJS9(self):
        before = JS_9
        expect = expect_JS_9
        self.atest(before, expect, "JS9", slimmer.js_slimmer)

    def testJS10(self):
        before = JS_10
        expect = expect_JS_10
        self.atest(before, expect, "JS10", slimmer.js_slimmer)

    def testJS11a(self):
        before = JS_11
        expect = expect_JS_11
        self.atest(before, expect, "JS11", slimmer.js_slimmer)

    def testJS11b(self):
        before = JS_11
        expect = expect_JS_11_hardcore
        self.atest(before, expect, "JS11", slimmer.js_slimmer, 
                   hardcore=True)

    def testJS12a(self):
        before = JS_12
        expect = expect_JS_12
        self.atest(before, expect, "JS12", slimmer.js_slimmer)

    def testJS12b(self):
        before = JS_12
        expect = expect_JS_12_hardcore
        self.atest(before, expect, "JS12", slimmer.js_slimmer,
                   hardcore=True)
                   
    def testJS13(self):
        before = JS_13
        expect = expect_JS_13
        self.atest(before, expect, "JS13", slimmer.js_slimmer)                   
        
    def testJS14a(self):
        before = JS_14
        expect = expect_JS_14
        self.atest(before, expect, "JS14a", slimmer.js_slimmer)        

    def testJS14b(self):
        before = JS_14
        expect = expect_JS_14_hardcore
        self.atest(before, expect, "JS14b", slimmer.js_slimmer,
                   hardcore=True)        
        
    def testJS15(self):
        before = JS_15
        expect = expect_JS_15
        self.atest(before, expect, "JS15", slimmer.js_slimmer)
        
    def testJS16(self):
        before = JS_16
        expect = expect_JS_16
        self.atest(before, expect, "JS16", slimmer.js_slimmer)
        
        
    def testUnicodeHTML1(self):
        here = os.path.dirname(__file__)
        before = codecs.open(os.path.join(here, 'euc-jp.html'),
                             'r','euc-jp').read()
        assert isinstance(before, unicode)
        after = slimmer.html_slimmer(before)
        assert isinstance(after, unicode)
        
    def testUnicodeHTML2(self):
        here = os.path.dirname(__file__)
        before = codecs.open(os.path.join(here, 'utf-8.html'),
                             'r','utf-8').read()
        assert isinstance(before, unicode)
        after = slimmer.html_slimmer(before)
        assert isinstance(after, unicode)
        expect = u'<html><p>\u0e2a\u0e27\u0e31\u0e2a\u0e14\u0e35\u0e04\u0e23\u0e31\u0e1a</p></html>'
        assert after == expect
        

def suite():
    return unittest.makeSuite(SlimmerTestCase)
        
        
if __name__ == '__main__':
    if '-v' in sys.argv[1:] or '--verbose' in sys.argv[1:]:
        VERBOSE = True
    unittest.main()
        

