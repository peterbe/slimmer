#-*- coding: utf-8 -*

CSS_1 = '''
/* Comment 1 */
div#main { 
  font-family: Verdana, "Courier New"      ;
}


h2 { 
  /* Comment 2 */
  font-size: 10px;
}
'''

expect_CSS_1 = '''
div#main{font-family:Verdana,"Courier New"}h2{font-size:10px}
'''


#----------------------------------------------------------------------------

CSS_2 = '''
<style type="text/css">
div#main { 
  font-family:  Verdana, "Courier New"      ;
}

h2 { 
  font-size: 10px;
}
</style>
'''

expect_CSS_2 = '''
<style type="text/css">
div#main{font-family:Verdana,"Courier New"}h2{font-size:10px}</style>
'''
#----------------------------------------------------------------------------
CSS_3 = r'''
#centercontent {
    border:1px solid #000000;
    voice-family: "\"}\"";
    voice-family: inherit;
    margin-left: 201px;
    }
'''    

expect_CSS_3 = r'''
#centercontent{border:1px solid #000;voice-family: "\"}\"";voice-family:inherit;margin-left:201px}
'''
#----------------------------------------------------------------------------

CSS_3b = unicode(CSS_3)

expect_CSS_3b = unicode(expect_CSS_3)


#----------------------------------------------------------------------------
CSS_3c = u'''
body {
    color:#000000;
    color:#ccFF99;
    \xa3
    }
'''    

expect_CSS_3c = u'''
body{color:#000;color:#cF9;\xa3}'''

#----------------------------------------------------------------------------
CSS_4 = r'''
p     {  color:#123456;   }


select {
	font-family: Verdana,Arial,Helvetica,sans-serif;
	font-size: 11px;
	color: #000000;
	/*
	background-color: #FFFFFF;
	*/
}
#myDiv { float: left; background: transparent; }
'''

expect_CSS_4 = r'''
p{color:#123456}select{font-family:Verdana,Arial,Helvetica,sans-serif;font-size:11px;color:#000}#myDiv{float:left;background:transparent}
'''

#----------------------------------------------------------------------------

CSS_5 = r'''
/* remove this comment */
#isnotMacIE5 { display: none;  }
#isMacIE5 { display: block; background-color: #060; color: #fff; }
/* commented backslash hack v2 \*/
#isnotMacIE5 { display: block; background-color: #060; color: #fff; }
#isMacIE5 { display: none; }
/* keep this comment */
#ismozilla { state: cool; }
/* safely remove this one too */
'''

expect_CSS_5 = r'''
#isnotMacIE5{display:none}#isMacIE5{display:block;background-color:#060;color:#fff}/* commented backslash hack v2 \*/
#isnotMacIE5{display:block;background-color:#060;color:#fff}#isMacIE5{display:none}/* keep this comment */
#ismozilla{state:cool}
'''

#----------------------------------------------------------------------------

CSS_6 = r'''
div   a {display:block;}
'''

expect_CSS_6 = r'''
div a{display:block}
'''

#----------------------------------------------------------------------------

CSS_7 = r'''
/* Holly hack to cure peek-a-boo IE 6 bug*/
/* Hides from IE5-mac \*/
* html #region-content {height: 1%;}
/* End hide from IE5-mac */
'''

expect_CSS_7 = r'''
/* Hides from IE5-mac \*/
* html #region-content{height:1%}/* End hide from IE5-mac */
'''

#----------------------------------------------------------------------------

HTML_1='''
<img src="a.gif" width="100" width="100" height='100' border=0>
<STYLE type="text/css">
div#main {
  font-family:Verdana,   "Courier New"      ;
}
</style>
<pre>
  Here
    width="100"
    
    
</pre>
'''
   
expect_HTML_1='''
<img src="a.gif" width="100" width="100" height='100' border=0><STYLE type="text/css">
div#main{font-family:Verdana,"Courier New"}</style><pre>
  Here
    width="100"
    
    
</pre>
'''


#----------------------------------------------------------------------------

HTML_2='''
<a   href="x"
 width="100%" border='0'>Pointless         extra
 
space</a>

<!-- one line comment -->
<!-- two line
comment -->

<script language="Javascript">
<!-- hide this
function foo() {
    alert("Hell");
}
//-->
</script>

'''
   
expect_HTML_2='''
<a href="x" width="100%" border='0'>Pointless         extra
 
space</a><!-- two line
comment --><script language="Javascript"><!--
function foo(){alert("Hell");}
//--></script>
'''


#----------------------------------------------------------------------------

HTML_3='''
<input       value="    OK    "    >
<img   alt='    hej   '    title="  Bajs  "  width=32  >

<a href="x" width="100%"     border=0>Pointless         extra

space</a>
<img src='blank.gif'
  border='0' height='32'  alt='' width='32'>
'''
   
expect_HTML_3='''
<input value="    OK    "><img alt='    hej   ' title="  Bajs  " width=32 ><a href="x" width="100%" border=0>Pointless         extra

space</a><img src='blank.gif' border='0' height='32' alt='' width='32'>
'''

#----------------------------------------------------------------------------

HTML_4='''<script>
if (isMozi) {
   slides = slideml.doc.getElementsByTagNameNS("http://www.oscom.org/2003/SlideML/1.0/","slide");
}
else {
   slides = slideml.doc.getElementsByTagName("s:slide");
}
</script>'''

expect_HTML_4 = '''<script>if(isMozi){slides=slideml.doc.getElementsByTagNameNS("http://www.oscom.org/2003/SlideML/1.0/","slide");}else{slides=slideml.doc.getElementsByTagName("s:slide");}
</script>'''


#----------------------------------------------------------------------------

HTML_5='''<img src="/p_/sp" width="2" height="1" alt="" />'''

expect_HTML_5='''<img src="/p_/sp" width="2" height="1" alt="" />'''


#----------------------------------------------------------------------------

HTML_6='''
<style type="text/css"><!--
div.commentinline {
  font-family:Arial, Verdana, sans-serif;
  border-top:1px solid #cccccc;
  padding:3px 4px 4px 4px;
  margin-top:10px;
  margin-bottom:10px;
  margin-left:15px; 
}
//--></style>	    
'''

expect_HTML_6='''
<style type="text/css"><!--
div.commentinline{font-family:Arial,Verdana,sans-serif;border-top:1px solid #ccc;padding:3px 4px 4px 4px;margin-top:10px;margin-bottom:10px;margin-left:15px}
//--></style>'''


#----------------------------------------------------------------------------

HTML_7='''
<html>
  <!--#include virtual="/include/myinclude.asp"-->
  <body>
  </body>
</html>
'''

expect_HTML_7='''
<html><!--#include virtual="/include/myinclude.asp"--><body></body></html>
'''


#----------------------------------------------------------------------------

HTML_8=u'''
<html>
  <style>
  * { color:#000000; background-color:#ffcc99 ; }
  </style>
  <body>
    <div style="color:#CCCCCC; background-color: #ee99cc">Pay with \xa3</div>
  </body>
</html>
'''

expect_HTML_8=u'''
<html><style> *{color:#000;background-color:#fc9}</style><body><div style="color:#CCCCCC; background-color: #ee99cc">Pay with \xa3</div></body></html>
'''


#----------------------------------------------------------------------------

HTML_9=u'''
<html>
  <style>
  * { color:#000000; 
      background-color:#ffcc99 ;
    }
  </style>
  <body>
    <div style="color:#CCCCCC; background-color: #ee99cc">Pay with \xa3</div>
  </body>
</html>
'''

expect_HTML_9=u'''
<html><style> *{color:#000;background-color:#fc9}</style><body><div style="color:#CCCCCC; background-color: #ee99cc">Pay with \xa3</div></body></html>
'''


#----------------------------------------------------------------------------

JS_1='''
init = function() {
  foo();
  bar();
}
window.onload = init;
'''

expect_JS_1='''
init=function(){foo();bar();}
window.onload=init;
'''

#----------------------------------------------------------------------------

JS_2='''
function econvert(s) {
    s=s.replace(/%7E/g,'~');
    s=s.replace(/%28/g,'(');
    s=s.replace(/%29/g,')');
    s=s.replace(/%20/g,' ');
    s=s.replace(/_dot_| dot |_\._|\(\.\)/gi, '.');
    s=s.replace(/_at_|~at~/gi, '@');
    return s;
}
			
function AEHit() {
  var ss = document.getElementsByTagName("span");
  for (i=0; i< ss.length; i++) 
    if (ss[i].className=="aeh") 
      ss[i].innerHTML = econvert(ss[i].innerHTML);
}  
'''

expect_JS_2='''
function econvert(s){s=s.replace(/%7E/g,'~');s=s.replace(/%28/g,'(');
s=s.replace(/%29/g,')');s=s.replace(/%20/g,' ');s=s.replace(/_dot_| dot |_\._|\(\.\)/gi, '.');s=s.replace(/_at_|~at~/gi, '@');return s;}
function AEHit(){var ss=document.getElementsByTagName("span");for (i=0;i< ss.length;i++)if(ss[i].className=="aeh") 
ss[i].innerHTML=econvert(ss[i].innerHTML);}
'''


#----------------------------------------------------------------------------

JS_3='''
var x = " ";
x +="nothing";
x+= "something";
x+="anything";
y  =  10;
y +=1;
y+= 1;
y+=1;

y +=15;
y+= 15;
y+=15;
'''

expect_JS_3='''
var x=" ";x+="nothing";x+="something";x+="anything";
y=10;y+=1;y+=1;y+=1;
y+=15;y+=15;y+=15;
'''

#----------------------------------------------------------------------------

JS_4 ='''
this.onLoad = true;
this.onLoaded = false;
var x = true;
'''

expect_JS_4 ='''
this.onLoad=true;this.onLoaded=false;var x=true;
'''

#----------------------------------------------------------------------------

JS_5 ='''
if (document.getElementById("someting")) {
  cool();
} else if (document.getElementById("elsething")) {
  wicked();
} else {
  poor();
}
'''

expect_JS_5 ='''
if(document.getElementById("someting")){cool();}else if(document.getElementById("elsething")){wicked();}else{poor();}
'''

#----------------------------------------------------------------------------

# function foo() { alert( "foo" ); }
JS_6 ='''
bar = function () { alert( "bar" ); }
bar2 = function() { alert( "bar2" ); }
'''

# function foo(){alert( "foo" );}
expect_JS_6 ='''
bar=function(){alert( "bar" );}
bar2=function(){alert( "bar2" );}
'''

#----------------------------------------------------------------------------

# testing local variables inside functions
JS_7 ='''
function foobar(x,y) {
  var element1 = document.getElementById('something');
  alert(element1);
}
'''

# function foo(){alert( "foo" );}
expect_JS_7 ='''
function foobar(x,y) {
  var e = document.getElementById('something');
  alert(e);
}  
'''

#----------------------------------------------------------------------------

# comments within the code
JS_8 ='''
function foobar(x,y) {
  var element1 = document.getElementById('something'); // alert(element1);
  alert(element1); // this can be removed
} // end of function;
'''

expect_JS_8 ='''
function foobar(x,y){var element1=document.getElementById('something');alert(element1);}
'''


#----------------------------------------------------------------------------

# 
JS_9 ='''
function nodeContained(innernode, outernode){
    // check if innernode is contained in outernode
    var node = innernode.parentNode;
    while (node != document) {
        if (node == outernode) {
            return true; 
        }
        node=node.parentNode;
    }
    return false;
};
'''

expect_JS_9 ='''
function nodeContained(innernode,outernode){var node=innernode.parentNode;while(node!=document){if(node==outernode) {return true;}
node=node.parentNode;}
return false;};

'''

#----------------------------------------------------------------------------

# 
JS_10 ='''
                        // Insert P element
                        if (tinyMCE.isGecko && tinyMCE.settings['force_p_newlines'] && e.keyCode == 13 && !e.shiftKey) {
                                // Insert P element instead of BR
                                if (tinyMCE.selectedInstance._insertPara(e)) {
                                        // Cancel event
                                        tinyMCE.execCommand("mceAddUndoLevel");
                                        tinyMCE.cancelEvent(e);
                                        return false;
                                }
                        }
'''

expect_JS_10 ='''
if(tinyMCE.isGecko && tinyMCE.settings['force_p_newlines'] && e.keyCode == 13 && !e.shiftKey){if(tinyMCE.selectedInstance._insertPara(e)) {tinyMCE.execCommand("mceAddUndoLevel");tinyMCE.cancelEvent(e);
return false;}}
'''

JS_11 = '''
ajax = Class.create();
ajax.prototype = {
	initialize: function(url, options){
		this.transport = this.getTransport();
		this.postBody = options.postBody || '';
		this.method = options.method || 'post';
		this.onComplete = options.onComplete || null;
		this.update = $(options.update) || null;
		this.request(url);
	},

	request: function(url){
		this.transport.open(this.method, url, true);
		this.transport.onreadystatechange = this.onStateChange.bind(this);
		if (this.method == 'post') {
			this.transport.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
			if (this.transport.overrideMimeType) this.transport.setRequestHeader('Connection', 'close');
		}
		this.transport.send(this.postBody);
	},

	onStateChange: function(){
		if (this.transport.readyState == 4 && this.transport.status == 200) {
			if (this.onComplete) 
				setTimeout(function(){this.onComplete(this.transport);}.bind(this), 10);
			if (this.update)
				setTimeout(function(){this.update.innerHTML = this.transport.responseText;}.bind(this), 10);
			this.transport.onreadystatechange = function(){};
		}
	},

	getTransport: function() {
		if (window.ActiveXObject) return new ActiveXObject('Microsoft.XMLHTTP');
		else if (window.XMLHttpRequest) return new XMLHttpRequest();
		else return false;
	}
};
'''

expect_JS_11 ='''
ajax=Class.create();ajax.prototype = {initialize: function(url,options){this.transport=this.getTransport();this.postBody=options.postBody || '';this.method=options.method || 'post';this.onComplete=options.onComplete || null;this.update = $(options.update) || null;this.request(url);},
request: function(url){this.transport.open(this.method, url, true);this.transport.onreadystatechange=this.onStateChange.bind(this);if(this.method=='post'){this.transport.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');if(this.transport.overrideMimeType) this.transport.setRequestHeader('Connection', 'close');}
this.transport.send(this.postBody);},
onStateChange: function(){if(this.transport.readyState == 4 && this.transport.status == 200) {if(this.onComplete) 
setTimeout(function(){this.onComplete(this.transport);}.bind(this),10);if(this.update)
setTimeout(function(){this.update.innerHTML=this.transport.responseText;}.bind(this),10);this.transport.onreadystatechange=function(){};}},
getTransport: function(){if(window.ActiveXObject) return new ActiveXObject('Microsoft.XMLHTTP');else if(window.XMLHttpRequest) return new XMLHttpRequest();else return false;}};
'''
expect_JS_11_hardcore ='''
ajax=Class.create();ajax.prototype = {initialize: function(_0,_1){this.transport=this.getTransport();this.postBody=_1.postBody || '';this.method=_1.method || 'post';this.onComplete=_1.onComplete || null;this.update = $(_1.update) || null;this.request(_0);},
request: function(_0){this.transport.open(this.method, _0, true);this.transport.onreadystatechange=this.onStateChange.bind(this);if(this.method=='post'){this.transport.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');if(this.transport.overrideMimeType) this.transport.setRequestHeader('Connection', 'close');}
this.transport.send(this.postBody);},
onStateChange: function(){if(this.transport.readyState == 4 && this.transport.status == 200) {if(this.onComplete) 
setTimeout(function(){this.onComplete(this.transport);}.bind(this),10);if(this.update)
setTimeout(function(){this.update.innerHTML=this.transport.responseText;}.bind(this),10);this.transport.onreadystatechange=function(){};}},
getTransport: function(){if(window.ActiveXObject) return new ActiveXObject('Microsoft.XMLHTTP');else if(window.XMLHttpRequest) return new XMLHttpRequest();else return false;}};
'''

#----------------------------------------------------------------------------

JS_12='''
function foo(documentnode, nodevalue) {
    return documentnode + nodevalue;
}
'''

expect_JS_12='''
function foo(documentnode,nodevalue){return documentnode + nodevalue;}
'''
expect_JS_12_hardcore='''
function foo(_0,_1){return _0 + _1;}
'''

#----------------------------------------------------------------------------
JS_13 = '''
addEvent(window, 'load', function(){
   var editlinks = getElementsByClass("edit", document, "img");
   for (var e in editlinks) {
      foo();
   }
});
'''

expect_JS_13 = '''
addEvent(window, 'load', function(){var editlinks=getElementsByClass("edit", document, "img");for(var e in editlinks){foo();}});
'''

#----------------------------------------------------------------------------
JS_14 = '''
function (variable1, variable2) {
  if (variable1 == variable2) {
    return true;
  } else { 
    return false; 
  }
}'''

expect_JS_14 = '''
function (variable1,variable2) {if(variable1==variable2){return true;}else{return false;}}
'''
expect_JS_14_hardcore = '''
function (_0,_1) {if(_0==_1){return true;}else{return false;}}
'''


#----------------------------------------------------------------------------
JS_15 = '''
var x =1
if (x==1) {
  x=2;
}'''

expect_JS_15 = '''
var x=1if(x==1){x=2;}
'''


#----------------------------------------------------------------------------
JS_16 = '''
var uk_counties = ['a', 'b', 'c'];
var uk__9123 = ['a', 'b', 'c'];
var uk = ['a', 'b', 'c'];
var uk_counties = ["a", "b", "c"];
var uk__9123 = ["a", "b", "c"];
var uk = ["a", "b", "c"];
'''

expect_JS_16 = '''
var uk_counties=['a', 'b', 'c'];var uk__9123=['a', 'b', 'c'];var uk=['a', 'b', 'c'];var uk_counties=["a", "b", "c"];var uk__9123=["a", "b", "c"];var uk=["a", "b", "c"];
'''
