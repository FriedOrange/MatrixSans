## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[1] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>10 different Font Family names were found:</p>
<ul>
<li>
<p>'Matrix Sans Raster SC' was found in:</p>
<ul>
<li>MatrixSansRasterSC-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans Screen SC' was found in:</p>
<ul>
<li>MatrixSansScreenSC-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans Video' was found in:</p>
<ul>
<li>MatrixSansVideo-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans Raster' was found in:</p>
<ul>
<li>MatrixSansRaster-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans Video SC' was found in:</p>
<ul>
<li>MatrixSansVideoSC-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans Screen' was found in:</p>
<ul>
<li>MatrixSansScreen-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans' was found in:</p>
<ul>
<li>MatrixSans-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans SC' was found in:</p>
<ul>
<li>MatrixSansSC-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans Print' was found in:</p>
<ul>
<li>MatrixSansPrint-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Matrix Sans Print SC' was found in:</p>
<ul>
<li>MatrixSansPrintSC-Regular.ttf (nameID 1)</li>
</ul>
</li>
</ul>
 [code: inconsistent-family-name]



</div>
</details>
</div>
</details>

<details><summary>[13] MatrixSansRasterSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: numbersign	Contours detected: 12	Expected: 2

- Glyph name: dollar	Contours detected: 9	Expected: 1, 3 or 5

- Glyph name: percent	Contours detected: 9	Expected: 4 or 5

- Glyph name: ampersand	Contours detected: 13	Expected: 1, 2 or 3

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 9	Expected: 1 or 4

- 1045 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ị̆ ị̇ ị̈ ị̉ ị̊ ị̋ ị̌ ị̒ ị̛̀ ị̛́ ị̛̂ ị̛̃ ị̛̄ ị̛̆ ị̛̇ ị̛̈ ị̛̉ ị̛̊ ị̛̋ ị̛̌</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* 7428 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[13] MatrixSansScreenSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: numbersign	Contours detected: 20	Expected: 2

- Glyph name: dollar	Contours detected: 17	Expected: 1, 3 or 5

- Glyph name: percent	Contours detected: 13	Expected: 4 or 5

- Glyph name: ampersand	Contours detected: 14	Expected: 1, 2 or 3

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 11	Expected: 1 or 4

- 1074 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ị̆ ị̇ ị̈ ị̉ ị̊ ị̋ ị̌ ị̒ ị̛̀ ị̛́ ị̛̂ ị̛̃ ị̛̄ ị̛̆ ị̛̇ ị̛̈ ị̛̉ ị̛̊ ị̛̋ ị̛̌</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* 10941 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[14] MatrixSansVideo-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: Gcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uogonek	Contours detected: 3	Expected: 1

- Glyph name: ohorn	Contours detected: 3	Expected: 2

- 50 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ĭ̛ i̛̇ i̛̊ i̛̋ i̛̒ ĭ̤ i̤̇ i̤̊ i̤̋ i̤̒ ĭ̦ i̦̇ i̦̊ i̦̋ i̦̒ ĭ̧ i̧̇ i̧̊ i̧̋ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* AE (U+00C6) has a counter-clockwise outer contour

* Aacute (U+00C1) has a counter-clockwise outer contour

* Aacute (U+00C1) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* 1290 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[13] MatrixSansRaster-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: numbersign	Contours detected: 12	Expected: 2

- Glyph name: dollar	Contours detected: 9	Expected: 1, 3 or 5

- Glyph name: percent	Contours detected: 9	Expected: 4 or 5

- Glyph name: ampersand	Contours detected: 13	Expected: 1, 2 or 3

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 9	Expected: 1 or 4

- 1045 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ĭ̛ i̛̇ i̛̊ i̛̋ i̛̒ ĭ̤ i̤̇ i̤̊ i̤̋ i̤̒ ĭ̦ i̦̇ i̦̊ i̦̋ i̦̒ ĭ̧ i̧̇ i̧̊ i̧̋ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* 7428 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[14] MatrixSansVideoSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: Gcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uogonek	Contours detected: 3	Expected: 1

- Glyph name: ohorn	Contours detected: 3	Expected: 2

- 50 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ị̆ ị̇ ị̈ ị̉ ị̊ ị̋ ị̌ ị̒ ị̛̀ ị̛́ ị̛̂ ị̛̃ ị̛̄ ị̛̆ ị̛̇ ị̛̈ ị̛̉ ị̛̊ ị̛̋ ị̛̌</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* AE (U+00C6) has a counter-clockwise outer contour

* Aacute (U+00C1) has a counter-clockwise outer contour

* Aacute (U+00C1) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* 1290 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[13] MatrixSansScreen-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: numbersign	Contours detected: 20	Expected: 2

- Glyph name: dollar	Contours detected: 17	Expected: 1, 3 or 5

- Glyph name: percent	Contours detected: 13	Expected: 4 or 5

- Glyph name: ampersand	Contours detected: 14	Expected: 1, 2 or 3

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 11	Expected: 1 or 4

- 1074 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ĭ̛ i̛̇ i̛̊ i̛̋ i̛̒ ĭ̤ i̤̇ i̤̊ i̤̋ i̤̒ ĭ̦ i̦̇ i̦̊ i̦̋ i̦̒ ĭ̧ i̧̇ i̧̊ i̧̋ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* 10941 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[14] MatrixSans-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: Gcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: ohorn	Contours detected: 3	Expected: 2

- 50 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ĭ̛ i̛̇ i̛̊ i̛̋ i̛̒ ĭ̤ i̤̇ i̤̊ i̤̋ i̤̒ ĭ̦ i̦̇ i̦̊ i̦̋ i̦̒ ĭ̧ i̧̇ i̧̊ i̧̋ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* AE (U+00C6) has a counter-clockwise outer contour

* Aacute (U+00C1) has a counter-clockwise outer contour

* Aacute (U+00C1) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* 1293 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[14] MatrixSansSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: Gcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: ohorn	Contours detected: 3	Expected: 2

- 50 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ị̆ ị̇ ị̈ ị̉ ị̊ ị̋ ị̌ ị̒ ị̛̀ ị̛́ ị̛̂ ị̛̃ ị̛̄ ị̛̆ ị̛̇ ị̛̈ ị̛̉ ị̛̊ ị̛̋ ị̛̌</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* AE (U+00C6) has a counter-clockwise outer contour

* Aacute (U+00C1) has a counter-clockwise outer contour

* Aacute (U+00C1) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* Abreveacute (U+1EAE) has a counter-clockwise outer contour

* 1293 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[13] MatrixSansPrint-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: numbersign	Contours detected: 20	Expected: 2

- Glyph name: dollar	Contours detected: 17	Expected: 1, 3 or 5

- Glyph name: percent	Contours detected: 13	Expected: 4 or 5

- Glyph name: ampersand	Contours detected: 14	Expected: 1, 2 or 3

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 11	Expected: 1 or 4

- 1074 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ĭ̛ i̛̇ i̛̊ i̛̋ i̛̒ ĭ̤ i̤̇ i̤̊ i̤̋ i̤̒ ĭ̦ i̦̇ i̦̊ i̦̋ i̦̒ ĭ̧ i̧̇ i̧̊ i̧̋ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* 10941 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>

<details><summary>[13] MatrixSansPrintSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 300, but got 200 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309), uni0324 (U+0324) and uni032E (U+032E)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: numbersign	Contours detected: 20	Expected: 2

- Glyph name: dollar	Contours detected: 17	Expected: 1, 3 or 5

- Glyph name: percent	Contours detected: 13	Expected: 4 or 5

- Glyph name: ampersand	Contours detected: 14	Expected: 1, 2 or 3

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 11	Expected: 1 or 4

- 1074 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
lessequal, greaterequal, greater, less</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Glyph 0x00A0 is called &quot;nbspace&quot;: Change to &quot;uni00A0&quot;</p>
 [code: not-recommended-00a0]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, tai-le, tifinagh, syriac, hebrew, coptic, duployan, canadian-aboriginal, malayalam, old-permic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
106 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ị̆ ị̇ ị̈ ị̉ ị̊ ị̋ ị̌ ị̒ ị̛̀ ị̛́ ị̛̂ ị̛̃ ị̛̄ ị̛̆ ị̛̇ ị̛̈ ị̛̉ ị̛̊ ị̛̋ ị̛̌</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Zapotec (Latn, 490,000 speakers), South Central Banda (Latn, 244,000 speakers), Dii (Latn, 71,000 speakers), Vute (Latn, 21,000 speakers), Fur (Latn, 1,230,163 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Avokaya (Latn, 100,000 speakers), Ejagham (Latn, 120,000 speakers), Basaa (Latn, 332,940 speakers), Mango (Latn, 77,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Han (Latn, 6 speakers), Yala (Latn, 200,000 speakers), Heiltsuk (Latn, 300 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Navajo (Latn, 166,319 speakers), Teke-Ebo (Latn, 260,000 speakers), Igbo (Latn, 27,823,640 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Southern Kisi (Latn, 360,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Kom (Latn, 360,685 speakers), Ekpeye (Latn, 226,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Kaska (Latn, 125 speakers), Bafut (Latn, 158,146 speakers), Ngbaka (Latn, 1,020,000 speakers), Aghem (Latn, 38,843 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Nateni (Latn, 100,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* A (U+0041) has a counter-clockwise outer contour

* 10941 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID is 'PfEd', a font editor default. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: bad]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 11 | 124 | 1153 | 71 | 989 | 0 | 
| 0% | 0% | 0% | 5% | 49% | 3% | 42% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
