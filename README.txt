slimmer.py is a whitespace optimizer for CSS, HTML and XHTML output.
It's written by Peter Bengtsson, peter@fry-it.com in 2004-2005.

INSTALLATION::

 $ tar -zxvf slimmer-x.x.x.tgz
 $ cd slimmer/
 $ sudo python setup.py install
 
USAGE::

 >>> import slimmer
 >>> from slimmer import css_slimmer
 >>> css_slimmer("h1, h2 { font-family: 'Courier New', Courier; }")
 "h1,h2{font-family:'Courier New',Courier;border:1px solid black;}"
 >>> html_slimmer('<a  href="x" title="   foo  bar  "> one </a>  <br />')
 >>> from slimmer import html_slimmer, xhtml_slimmer
 >>> html_slimmer('''<a  href="x" title="   foo  bar  "
                   > one </a>  <br/>''')
 '<a href="x" title="   foo bar  "> one </a><br />'

 
UNITTESTS::

 $ cd slimmer/tests
 $ python testSlimmer.py
 
