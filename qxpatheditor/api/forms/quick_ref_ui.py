# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Dev\QXPathEditor\forms/quick_ref.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from qxpatheditor.qt import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Quick Reference")
        Form.resize(608, 353)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.textEditQuickRef = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditQuickRef.sizePolicy().hasHeightForWidth())
        self.textEditQuickRef.setSizePolicy(sizePolicy)
        self.textEditQuickRef.setReadOnly(True)
        self.textEditQuickRef.setObjectName("textEditQuickRef")
        self.gridLayout.addWidget(self.textEditQuickRef, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Quick Reference", "Quick Reference"))
        self.textEditQuickRef.setHtml(_translate("Form", """
<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">
<h3 id="browser-console">Browser console</h3>
<pre><code class="lang-js">$x(<span class="hljs-string">"//div"</span>)
</code></pre>
<p>Works in Firefox and Chrome.</p>
<h2 id="selectors">Selectors</h2>
<h3 id="descendant-selectors">Descendant selectors</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>CSS</th>
<th>Xpath</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>h1</code></td>
<td><code>//h1</code></td>
</tr>
<tr>
<td><code>div p</code></td>
<td><code>//div//p</code></td>
</tr>
<tr>
<td><code>ul &gt; li</code></td>
<td><code>//ul/li</code></td>
</tr>
<tr>
<td><code>ul &gt; li &gt; a</code></td>
<td><code>//ul/li/a</code></td>
</tr>
<tr>
<td><code>div &gt; *</code></td>
<td><code>//div/*</code></td>
</tr>
<tr>
<td>----</td>
<td>----</td>
</tr>
<tr>
<td><code>:root</code></td>
<td><code>/</code></td>
</tr>
<tr>
<td><code>:root &gt; body</code></td>
<td><code>/body</code></td>
</tr>
</tbody>
</table>
<p>{: .xp}</p>
<h3 id="attribute-selectors">Attribute selectors</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>CSS</th>
<th>Xpath</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>#id</code></td>
<td><code>//*[@id=&quot;id&quot;]</code></td>
</tr>
<tr>
<td><code>.class</code></td>
<td><code>//*[@class=&quot;class&quot;]</code></td>
</tr>
<tr>
<td><code>input[type=&quot;submit&quot;]</code></td>
<td><code>//input[@type=&quot;submit&quot;]</code></td>
</tr>
<tr>
<td><code>a#abc[for=&quot;xyz&quot;]</code></td>
<td><code>//a[@id=&quot;abc&quot;][@for=&quot;xyz&quot;]</code></td>
</tr>
<tr>
<td><code>a[rel]</code></td>
<td><code>//a[@rel]</code></td>
</tr>
<tr>
<td>----</td>
<td>----</td>
</tr>
<tr>
<td><code>a[href^=&#39;/&#39;]</code></td>
<td><code>//a[starts-with(@href, &#39;/&#39;)]</code></td>
</tr>
<tr>
<td><code>a[href$=&#39;pdf&#39;]</code></td>
<td><code>//a[ends-with(@href, &#39;.pdf&#39;)]</code></td>
</tr>
<tr>
<td><code>a[href*=&#39;://&#39;]</code></td>
<td><code>//a[contains(@href, &#39;://&#39;)]</code></td>
</tr>
<tr>
<td><code>a[rel~=&#39;help&#39;]</code></td>
<td><code>//a[contains(@rel, &#39;help&#39;)]</code></td>
</tr>
</tbody>
</table>
<p>{: .xp}</p>
<h3 id="order-selectors">Order selectors</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>CSS</th>
<th>Xpath</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ul &gt; li:first-child</code></td>
<td><code>//ul/li[1]</code></td>
</tr>
<tr>
<td><code>ul &gt; li:nth-child(2)</code></td>
<td><code>//ul/li[2]</code></td>
</tr>
<tr>
<td><code>ul &gt; li:last-child</code></td>
<td><code>//ul/li[last()]</code></td>
</tr>
<tr>
<td><code>li#id:first-child</code></td>
<td><code>//li[@id=&quot;id&quot;][1]</code></td>
</tr>
<tr>
<td><code>a:first-child</code></td>
<td><code>//a[1]</code></td>
</tr>
<tr>
<td><code>a:last-child</code></td>
<td><code>//a[last()]</code></td>
</tr>
</tbody>
</table>
<p>{: .xp}</p>
<h3 id="siblings">Siblings</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>CSS</th>
<th>Xpath</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>h1 ~ ul</code></td>
<td><code>//h1/following-sibling::ul</code></td>
</tr>
<tr>
<td><code>h1 + ul</code></td>
<td><code>//h1/following-sibling::ul[1]</code></td>
</tr>
<tr>
<td><code>h1 ~ #id</code></td>
<td><code>//h1/following-sibling::[@id=&quot;id&quot;]</code></td>
</tr>
</tbody>
</table>
<p>{: .xp}</p>
<h3 id="jquery">jQuery</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>CSS</th>
<th>Xpath</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>$(&#39;ul &gt; li&#39;).parent()</code></td>
<td><code>//ul/li/..</code></td>
</tr>
<tr>
<td><code>$(&#39;li&#39;).closest(&#39;section&#39;)</code></td>
<td><code>//li/ancestor-or-self::section</code></td>
</tr>
<tr>
<td><code>$(&#39;a&#39;).attr(&#39;href&#39;)</code></td>
<td><code>//a/@href</code></td>
</tr>
<tr>
<td><code>$(&#39;span&#39;).text()</code></td>
<td><code>//span/text()</code></td>
</tr>
</tbody>
</table>
<p>{: .xp}</p>
<h3 id="other-things">Other things</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>CSS</th>
<th>Xpath</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>h1:not([id])</code></td>
<td><code>//h1[not(@id)]</code></td>
</tr>
<tr>
<td>Text match</td>
<td><code>//button[text()=&quot;Submit&quot;]</code></td>
</tr>
<tr>
<td>Text match (substring)</td>
<td><code>//button[contains(text(),&quot;Go&quot;)]</code></td>
</tr>
<tr>
<td>Arithmetic</td>
<td><code>//product[@price &gt; 2.50]</code></td>
</tr>
<tr>
<td>Has children</td>
<td><code>//ul[*]</code></td>
</tr>
<tr>
<td>Has children (specific)</td>
<td><code>//ul[li]</code></td>
</tr>
<tr>
<td>Or logic</td>
<td><code>//a[@name or @href]</code></td>
</tr>
<tr>
<td>Union (joins results)</td>
<td>`//a</td>
<td>//div`</td>
</tr>
</tbody>
</table>
<p>{: .xp}</p>
<style>
/* ensure tables align */
table.xp {table-layout: fixed;}
table.xp tr>:nth-child(1) {width: 35%;}
table.xp tr>:nth-child(2) {width: auto;}
table.xp tr>:nth-child(3) {width: 10%; text-align:right;}
</style>

<h3 id="class-check">Class check</h3>
<pre><code class="lang-bash">//<span class="hljs-keyword">div</span>[<span class="hljs-keyword">contains</span>(concat(<span class="hljs-string">' '</span>,normalize-<span class="hljs-literal">space</span>(@class),<span class="hljs-string">' '</span>),<span class="hljs-string">' foobar '</span>)]
</code></pre>
<p>Xpath doesn&#39;t have the &quot;check if part of space-separated list&quot; operator, so this is the workaround (<a href="http://pivotallabs.com/xpath-css-class-matching/">source</a>).</p>
<h2 id="expressions">Expressions</h2>
<h3 id="steps-and-axes">Steps and axes</h3>
<p>| <code>//</code> | <code>ul</code> | <code>/</code>  | <code>a[@id=&#39;link&#39;]</code> |
| Axis | Step | Axis | Step            |
{: .-css-breakdown}</p>
<h3 id="prefixes">Prefixes</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>Prefix</th>
<th>Example</th>
<th>What</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>//</code></td>
<td><code>//hr[@class=&#39;edge&#39;]</code></td>
<td>Anywhere</td>
</tr>
<tr>
<td><code>./</code></td>
<td><code>./a</code></td>
<td>Relative</td>
</tr>
<tr>
<td><code>/</code></td>
<td><code>/html/body/div</code></td>
<td>Root</td>
</tr>
</tbody>
</table>
<p>{: .-headers}</p>
<p>Begin your expression with any of these.</p>
<h3 id="axes">Axes</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>Axis</th>
<th>Example</th>
<th>What</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/</code></td>
<td><code>//ul/li/a</code></td>
<td>Child</td>
</tr>
<tr>
<td><code>//</code></td>
<td><code>//[@id=&quot;list&quot;]//a</code></td>
<td>Descendant</td>
</tr>
</tbody>
</table>
<p>{: .-headers}</p>
<p>Separate your steps with <code>/</code>. Use two (<code>//</code>) if you don&#39;t want to select direct children.</p>
<h3 id="steps">Steps</h3>
<pre><code class="lang-bash"><span class="hljs-regexp">//</span>div
<span class="hljs-regexp">//</span>div[@name=<span class="hljs-string">'box'</span>]
<span class="hljs-regexp">//</span>[@id=<span class="hljs-string">'link'</span>]
</code></pre>
<p>A step may have an element name (<code>div</code>) and <a href="#predicate">predicates</a> (<code>[...]</code>). Both are optional.
They can also be these other things:</p>
<pre><code class="lang-bash">/<span class="hljs-regexp">/a/text</span>()     <span class="hljs-comment">#=&gt; "Go home"</span>
/<span class="hljs-regexp">/a/</span><span class="hljs-variable">@href</span>      <span class="hljs-comment">#=&gt; "index.html"</span>
/<span class="hljs-regexp">/a/</span>*          <span class="hljs-comment">#=&gt; All a's child elements</span>
</code></pre>
<h2 id="predicates">Predicates</h2>
<h3 id="predicates">Predicates</h3>
<pre><code class="lang-bash">//div[true()]
//div[@class="head"]
//div[<span class="hljs-string">@class="head"</span>][<span class="hljs-symbol">@id="top"</span>]
</code></pre>
<p>Restricts a nodeset only if some condition is true. They can be chained.</p>
<h3 id="operators">Operators</h3>
<pre><code class="lang-bash"><span class="hljs-meta"># Comparison</span>
<span class="hljs-comment">//a[@id = "xyz"]</span>
<span class="hljs-comment">//a[@id != "xyz"]</span>
<span class="hljs-comment">//a[@price &gt; 25]</span>
</code></pre>
<pre><code class="lang-bash"># Logic (<span class="hljs-keyword">and</span>/<span class="hljs-keyword">or</span>)
//<span class="hljs-keyword">div</span>[@id=<span class="hljs-string">"head"</span> <span class="hljs-keyword">and</span> position()=<span class="hljs-number">2</span>]
//<span class="hljs-keyword">div</span>[(x <span class="hljs-keyword">and</span> y) <span class="hljs-keyword">or</span> <span class="hljs-keyword">not</span>(z)]
</code></pre>
<p>Use comparison and logic operators to make conditionals.</p>
<h3 id="using-nodes">Using nodes</h3>
<pre><code class="lang-bash"><span class="hljs-comment"># Use them inside functions</span>
<span class="hljs-regexp">//u</span>l[count(li) &gt; <span class="hljs-number">2</span>]
<span class="hljs-regexp">//u</span>l[count(li[@class=<span class="hljs-string">'hide'</span>]) &gt; <span class="hljs-number">0</span>]
</code></pre>
<pre><code class="lang-bash"># This returns `&lt;ul&gt;` that has a `&lt;li&gt;` child
<span class="hljs-comment">//ul[li]</span>
</code></pre>
<p>You can use nodes inside predicates.</p>
<h3 id="indexing">Indexing</h3>
<pre><code class="lang-bash">//a[<span class="hljs-number">1</span>]                  # <span class="hljs-built_in">first</span> &lt;a&gt;
//a[<span class="hljs-built_in">last</span>()]             # <span class="hljs-built_in">last</span> &lt;a&gt;
//ol/<span class="hljs-built_in">li</span>[<span class="hljs-number">2</span>]              # <span class="hljs-built_in">second</span> &lt;<span class="hljs-built_in">li</span>&gt;
//ol/<span class="hljs-built_in">li</span>[<span class="hljs-built_in">position</span>()=<span class="hljs-number">2</span>]   # same as above
//ol/<span class="hljs-built_in">li</span>[<span class="hljs-built_in">position</span>()&gt;<span class="hljs-number">1</span>]   # :<span class="hljs-keyword">not</span>(:<span class="hljs-built_in">first</span>-child)
</code></pre>
<p>Use <code>[]</code> with a number, or <code>last()</code> or <code>position()</code>.</p>
<h3 id="chaining-order">Chaining order</h3>
<pre><code class="lang-bash">a[<span class="hljs-string">1</span>][<span class="hljs-symbol">@href='/'</span>]
a[<span class="hljs-string">@href='/'</span>][<span class="hljs-symbol">1</span>]
</code></pre>
<p>Order is significant, these two are different.</p>
<h3 id="nesting-predicates">Nesting predicates</h3>
<pre><code><span class="hljs-regexp">//</span>section[<span class="hljs-regexp">//</span>h1[@id=<span class="hljs-string">'hi'</span>]]
</code></pre><p>This returns <code>&lt;section&gt;</code> if it has an <code>&lt;h1&gt;</code> descendant with <code>id=&#39;hi&#39;</code>.</p>
<h2 id="functions">Functions</h2>
<h3 id="node-functions">Node functions</h3>
<pre><code class="lang-bash">name()                     <span class="hljs-meta"># <span class="hljs-comment">//[starts-with(name(), 'h')]</span></span>
text()                     <span class="hljs-meta"># <span class="hljs-comment">//button[text()="Submit"]</span></span>
                           <span class="hljs-meta"># <span class="hljs-comment">//button/text()</span></span>
lang(<span class="hljs-keyword">str</span>)
namespace-uri()
</code></pre>
<pre><code class="lang-bash">count()                    # <span class="hljs-comment">//table[count(tr)=1]</span>
position()                 # <span class="hljs-comment">//ol/li[position()=2]</span>
</code></pre>
<h3 id="boolean-functions">Boolean functions</h3>
<pre><code class="lang-bash"><span class="hljs-keyword">not</span>(expr)                  # button[<span class="hljs-keyword">not</span>(starts-<span class="hljs-keyword">with</span>(<span class="hljs-literal">text</span>(),<span class="hljs-string">"Submit"</span>))]
</code></pre>
<h3 id="string-functions">String functions</h3>
<pre><code class="lang-bash">contains()                 # font[contains(@<span class="hljs-keyword">class</span>,<span class="hljs-string">"head"</span>)]
starts-<span class="hljs-keyword">with</span>()              # font[starts-<span class="hljs-keyword">with</span>(@<span class="hljs-keyword">class</span>,<span class="hljs-string">"head"</span>)]
ends-<span class="hljs-keyword">with</span>()                # font[ends-<span class="hljs-keyword">with</span>(@<span class="hljs-keyword">class</span>,<span class="hljs-string">"head"</span>)]
</code></pre>
<pre><code class="lang-bash"><span class="hljs-function"><span class="hljs-title">concat</span><span class="hljs-params">(x,y)</span></span>
<span class="hljs-function"><span class="hljs-title">substring</span><span class="hljs-params">(str, start, len)</span></span>
<span class="hljs-function"><span class="hljs-title">substring-before</span><span class="hljs-params">(<span class="hljs-string">"01/02"</span>, <span class="hljs-string">"/"</span>)</span></span>  #=&gt; <span class="hljs-number">01</span>
<span class="hljs-function"><span class="hljs-title">substring-after</span><span class="hljs-params">(<span class="hljs-string">"01/02"</span>, <span class="hljs-string">"/"</span>)</span></span>   #=&gt; <span class="hljs-number">02</span>
<span class="hljs-function"><span class="hljs-title">translate</span><span class="hljs-params">()</span></span>
<span class="hljs-function"><span class="hljs-title">normalize-space</span><span class="hljs-params">()</span></span>
<span class="hljs-function"><span class="hljs-title">string-length</span><span class="hljs-params">()</span></span>
</code></pre>
<h3 id="type-conversion">Type conversion</h3>
<pre><code class="lang-bash"><span class="hljs-function"><span class="hljs-title">string</span><span class="hljs-params">()</span></span>
<span class="hljs-function"><span class="hljs-title">number</span><span class="hljs-params">()</span></span>
<span class="hljs-function"><span class="hljs-title">boolean</span><span class="hljs-params">()</span></span>
</code></pre>
<h2 id="axes">Axes</h2>
<h3 id="using-axes">Using axes</h3>
<pre><code class="lang-bash">/<span class="hljs-regexp">/ul/li</span>                       <span class="hljs-comment"># ul &gt; li</span>
/<span class="hljs-regexp">/ul/child</span><span class="hljs-symbol">:</span><span class="hljs-symbol">:li</span>                <span class="hljs-comment"># ul &gt; li (same)</span>
/<span class="hljs-regexp">/ul/following</span>-<span class="hljs-symbol">sibling:</span><span class="hljs-symbol">:li</span>    <span class="hljs-comment"># ul ~ li</span>
/<span class="hljs-regexp">/ul/descendant</span>-<span class="hljs-keyword">or</span>-<span class="hljs-symbol">self:</span><span class="hljs-symbol">:li</span>   <span class="hljs-comment"># ul li</span>
/<span class="hljs-regexp">/ul/ancestor</span>-<span class="hljs-keyword">or</span>-<span class="hljs-symbol">self:</span><span class="hljs-symbol">:li</span>     <span class="hljs-comment"># $('ul').closest('li')</span>
</code></pre>
<p>Steps of an expression are separated by <code>/</code>, usually used to pick child nodes. That&#39;s not always true: you can specify a different &quot;axis&quot; with <code>::</code>.</p>
<p>| <code>//</code> | <code>ul</code> | <code>/child::</code> | <code>li</code> |
| Axis | Step | Axis       | Step |
{: .-css-breakdown}</p>
<h3 id="child-axis">Child axis</h3>
<pre><code class="lang-bash"><span class="hljs-comment"># both the same</span>
<span class="hljs-regexp">//u</span>l<span class="hljs-regexp">/li/</span>a
<span class="hljs-regexp">//</span>child::ul<span class="hljs-regexp">/child::li/</span>child::a
</code></pre>
<p><code>child::</code> is the default axis. This makes <code>//a/b/c</code> work.</p>
<pre><code class="lang-bash"><span class="hljs-comment"># both the same</span>
<span class="hljs-comment"># this works because `child::li` is truthy, so the predicate succeeds</span>
<span class="hljs-regexp">//u</span>l[li]
<span class="hljs-regexp">//u</span>l[child::li]
</code></pre>
<pre><code class="lang-bash"><span class="hljs-comment"># both the same</span>
<span class="hljs-regexp">//u</span>l[count(li) &gt; <span class="hljs-number">2</span>]
<span class="hljs-regexp">//u</span>l[count(child::li) &gt; <span class="hljs-number">2</span>]
</code></pre>
<h3 id="descendant-or-self-axis">Descendant-or-self axis</h3>
<pre><code class="lang-bash"><span class="hljs-comment"># both the same</span>
<span class="hljs-regexp">//</span>div<span class="hljs-regexp">//</span>h4
<span class="hljs-regexp">//</span>div<span class="hljs-regexp">/descendant-or-self::h4</span>
</code></pre>
<p><code>//</code> is short for the <code>descendant-or-self::</code> axis.</p>
<pre><code class="lang-bash"><span class="hljs-comment"># both the same</span>
<span class="hljs-regexp">//u</span>l<span class="hljs-regexp">//</span>[last()]
<span class="hljs-regexp">//u</span>l<span class="hljs-regexp">/descendant-or-self::[last()]</span>
</code></pre>
<h3 id="other-axes">Other axes</h3>
<table cellspacing="10" border="1">
<thead>
<tr>
<th>Axis</th>
<th>Abbrev</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ancestor</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>ancestor-or-self</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td><code>attribute</code></td>
<td><code>@</code></td>
<td><code>@href</code> is short for <code>attribute::href</code></td>
</tr>
<tr>
<td><code>child</code></td>
<td></td>
<td><code>div</code> is short for <code>child::div</code></td>
</tr>
<tr>
<td><code>descendant</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>descendant-or-self</code></td>
<td><code>//</code></td>
<td><code>//</code> is short for <code>/descendant-or-self::node()/</code></td>
</tr>
<tr>
<td><code>namespace</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td><code>self</code></td>
<td><code>.</code></td>
<td><code>.</code> is short for <code>self::node()</code></td>
</tr>
<tr>
<td><code>parent</code></td>
<td><code>..</code></td>
<td><code>..</code> is short for <code>parent::node()</code></td>
</tr>
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td><code>following</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>following-sibling</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>preceding</code></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>preceding-sibling</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>{: .-headers}</p>
<p>There are other axes you can use.</p>
<h3 id="unions">Unions</h3>
<pre><code class="lang-bash"><span class="hljs-comment">//a | //span</span>
</code></pre>
<p>Use <code>|</code> to join two expressions.</p>
<h2 id="more-examples">More examples</h2>
<h3 id="examples">Examples</h3>
<pre><code class="lang-bash"><span class="hljs-comment">//*                 # all elements</span>
count(<span class="hljs-comment">//*)          # count all elements</span>
(<span class="hljs-comment">//h1)[1]/text()    # text of the first h1 heading</span>
<span class="hljs-comment">//li[span]          # find a &lt;li&gt; with an &lt;span&gt; inside it</span>
                    # ...expands to <span class="hljs-comment">//li[child::span]</span>
<span class="hljs-comment">//ul/li/..          # use .. to select a parent</span>
</code></pre>
<h3 id="find-a-parent">Find a parent</h3>
<pre><code class="lang-bash">//section[h1[@id=<span class="hljs-string">'section-name'</span>]]
</code></pre>
<p>Finds a <code>&lt;section&gt;</code> that directly contains <code>h1#section-name</code></p>
<pre><code class="lang-bash"><span class="hljs-regexp">//</span>section[<span class="hljs-regexp">//</span>h1[@id=<span class="hljs-string">'section-name'</span>]]
</code></pre>
<p>Finds a <code>&lt;section&gt;</code> that contains <code>h1#section-name</code>.
(Same as above, but uses descendant-or-self instead of child)</p>
<h3 id="closest">Closest</h3>
<pre><code class="lang-bash">./ancestor-<span class="hljs-keyword">or</span>-self::[@class=<span class="hljs-string">"box"</span>]
</code></pre>
<p>Works like jQuery&#39;s <code>$().closest(&#39;.box&#39;)</code>.</p>
<h3 id="attributes">Attributes</h3>
<pre><code class="lang-bash">//item[<span class="hljs-symbol">@price</span> &gt; <span class="hljs-number">2</span>*<span class="hljs-symbol">@discount]</span>
</code></pre>
<p>Finds <code>&lt;item&gt;</code> and check its attributes</p>
<h2 id="references">References</h2>
<p>{: .-one-column}</p>
<ul>
<li><a href="http://www.whitebeam.org/library/guide/TechNotes/xpathtestbed.rhtm">Xpath test bed</a> <em>(whitebeam.org)</em></li>
</ul>
"""))