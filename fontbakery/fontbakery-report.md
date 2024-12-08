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

<details><summary>[9] MatrixSansRasterSC-Regular.ttf</summary>
<div>
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

- Glyph name: plus	Contours detected: 5	Expected: 1

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: zero	Contours detected: 13	Expected: 2 or 3

- Glyph name: one	Contours detected: 7	Expected: 1

- Glyph name: two	Contours detected: 8	Expected: 1

- Glyph name: three	Contours detected: 9	Expected: 1

- Glyph name: four	Contours detected: 9	Expected: 1 or 2

- Glyph name: five	Contours detected: 8	Expected: 1

- Glyph name: six	Contours detected: 9	Expected: 1 or 2

- Glyph name: seven	Contours detected: 7	Expected: 1

- Glyph name: eight	Contours detected: 11	Expected: 3

- Glyph name: nine	Contours detected: 9	Expected: 1 or 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: question	Contours detected: 7	Expected: 2

- Glyph name: at	Contours detected: 12	Expected: 2

- Glyph name: A	Contours detected: 12	Expected: 2

- Glyph name: B	Contours detected: 11	Expected: 2 or 3

- Glyph name: C	Contours detected: 9	Expected: 1

- Glyph name: D	Contours detected: 12	Expected: 2

- Glyph name: E	Contours detected: 7	Expected: 1

- Glyph name: F	Contours detected: 7	Expected: 1

- Glyph name: G	Contours detected: 11	Expected: 1

- Glyph name: H	Contours detected: 13	Expected: 1

- Glyph name: I	Contours detected: 7	Expected: 1

- Glyph name: J	Contours detected: 8	Expected: 1

- Glyph name: K	Contours detected: 13	Expected: 1 or 2

- Glyph name: L	Contours detected: 7	Expected: 1

- Glyph name: M	Contours detected: 16	Expected: 1

- Glyph name: N	Contours detected: 15	Expected: 1

- Glyph name: O	Contours detected: 12	Expected: 2

- Glyph name: P	Contours detected: 9	Expected: 1 or 2

- Glyph name: Q	Contours detected: 14	Expected: 2

- Glyph name: R	Contours detected: 12	Expected: 1 or 2

- Glyph name: S	Contours detected: 9	Expected: 1

- Glyph name: T	Contours detected: 7	Expected: 1

- Glyph name: U	Contours detected: 13	Expected: 1

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Z	Contours detected: 7	Expected: 1

- Glyph name: bracketleft	Contours detected: 7	Expected: 1

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bracketright	Contours detected: 7	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 6	Expected: 2

- Glyph name: b	Contours detected: 12	Expected: 2

- Glyph name: c	Contours detected: 7	Expected: 1

- Glyph name: d	Contours detected: 12	Expected: 2

- Glyph name: e	Contours detected: 6	Expected: 2

- Glyph name: f	Contours detected: 8	Expected: 1

- Glyph name: g	Contours detected: 12	Expected: 2 or 3

- Glyph name: h	Contours detected: 12	Expected: 1

- Glyph name: i	Contours detected: 6	Expected: 2

- Glyph name: j	Contours detected: 9	Expected: 2

- Glyph name: k	Contours detected: 11	Expected: 1 or 2

- Glyph name: l	Contours detected: 7	Expected: 1

- Glyph name: m	Contours detected: 13	Expected: 1

- Glyph name: n	Contours detected: 10	Expected: 1

- Glyph name: o	Contours detected: 8	Expected: 2

- Glyph name: p	Contours detected: 12	Expected: 2

- Glyph name: q	Contours detected: 12	Expected: 2

- Glyph name: r	Contours detected: 7	Expected: 1

- Glyph name: s	Contours detected: 5	Expected: 1

- Glyph name: t	Contours detected: 8	Expected: 1

- Glyph name: u	Contours detected: 10	Expected: 1

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 12	Expected: 1

- Glyph name: z	Contours detected: 5	Expected: 1

- Glyph name: braceleft	Contours detected: 7	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceright	Contours detected: 7	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: cent	Contours detected: 12	Expected: 1 or 2

- Glyph name: sterling	Contours detected: 8	Expected: 1 or 2

- Glyph name: currency	Contours detected: 8	Expected: 2

- Glyph name: yen	Contours detected: 9	Expected: 1 or 2

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: section	Contours detected: 12	Expected: 2

- Glyph name: copyright	Contours detected: 18	Expected: 3

- Glyph name: ordfeminine	Contours detected: 7	Expected: 2 or 3

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: logicalnot	Contours detected: 3	Expected: 1

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 20	Expected: 3 or 4

- Glyph name: degree	Contours detected: 6	Expected: 2

- Glyph name: plusminus	Contours detected: 6	Expected: 1 or 2

- Glyph name: twosuperior	Contours detected: 5	Expected: 1

- Glyph name: threesuperior	Contours detected: 5	Expected: 1

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: micro	Contours detected: 12	Expected: 1

- Glyph name: paragraph	Contours detected: 19	Expected: 1, 2 or 3

- Glyph name: cedilla	Contours detected: 2	Expected: 1

- Glyph name: onesuperior	Contours detected: 5	Expected: 1

- Glyph name: ordmasculine	Contours detected: 7	Expected: 2 or 3

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: onequarter	Contours detected: 11	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 10	Expected: 3

- Glyph name: threequarters	Contours detected: 11	Expected: 3 or 4

- Glyph name: questiondown	Contours detected: 7	Expected: 2

- Glyph name: Agrave	Contours detected: 14	Expected: 3

- Glyph name: Aacute	Contours detected: 14	Expected: 3

- Glyph name: Acircumflex	Contours detected: 15	Expected: 3

- Glyph name: Atilde	Contours detected: 16	Expected: 3

- Glyph name: Adieresis	Contours detected: 14	Expected: 4

- Glyph name: Aring	Contours detected: 16	Expected: 3 or 4

- Glyph name: AE	Contours detected: 12	Expected: 2

- Glyph name: Ccedilla	Contours detected: 11	Expected: 1 or 2

- Glyph name: Egrave	Contours detected: 9	Expected: 2

- Glyph name: Eacute	Contours detected: 9	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 10	Expected: 2

- Glyph name: Edieresis	Contours detected: 9	Expected: 3

- Glyph name: Igrave	Contours detected: 9	Expected: 2

- Glyph name: Iacute	Contours detected: 9	Expected: 2

- Glyph name: Icircumflex	Contours detected: 10	Expected: 2

- Glyph name: Idieresis	Contours detected: 9	Expected: 3

- Glyph name: Eth	Contours detected: 12	Expected: 2

- Glyph name: Ntilde	Contours detected: 19	Expected: 2

- Glyph name: Ograve	Contours detected: 14	Expected: 3

- Glyph name: Oacute	Contours detected: 14	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: Otilde	Contours detected: 16	Expected: 3

- Glyph name: Odieresis	Contours detected: 14	Expected: 4

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: Oslash	Contours detected: 13	Expected: 2 or 3

- Glyph name: Ugrave	Contours detected: 15	Expected: 2

- Glyph name: Uacute	Contours detected: 15	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 16	Expected: 2

- Glyph name: Udieresis	Contours detected: 15	Expected: 3

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Thorn	Contours detected: 10	Expected: 1 or 2

- Glyph name: germandbls	Contours detected: 13	Expected: 1

- Glyph name: agrave	Contours detected: 8	Expected: 3

- Glyph name: aacute	Contours detected: 8	Expected: 3

- Glyph name: acircumflex	Contours detected: 9	Expected: 3

- Glyph name: atilde	Contours detected: 10	Expected: 3

- Glyph name: adieresis	Contours detected: 8	Expected: 4

- Glyph name: aring	Contours detected: 10	Expected: 4

- Glyph name: ae	Contours detected: 9	Expected: 3

- Glyph name: ccedilla	Contours detected: 9	Expected: 1 or 2

- Glyph name: egrave	Contours detected: 8	Expected: 3

- Glyph name: eacute	Contours detected: 8	Expected: 3

- Glyph name: ecircumflex	Contours detected: 9	Expected: 3

- Glyph name: edieresis	Contours detected: 8	Expected: 4

- Glyph name: igrave	Contours detected: 7	Expected: 2

- Glyph name: iacute	Contours detected: 7	Expected: 2

- Glyph name: icircumflex	Contours detected: 8	Expected: 2

- Glyph name: idieresis	Contours detected: 7	Expected: 3

- Glyph name: eth	Contours detected: 10	Expected: 2

- Glyph name: ntilde	Contours detected: 14	Expected: 2

- Glyph name: ograve	Contours detected: 10	Expected: 3

- Glyph name: oacute	Contours detected: 10	Expected: 3

- Glyph name: ocircumflex	Contours detected: 11	Expected: 3

- Glyph name: otilde	Contours detected: 12	Expected: 3

- Glyph name: odieresis	Contours detected: 10	Expected: 4

- Glyph name: oslash	Contours detected: 11	Expected: 3

- Glyph name: ugrave	Contours detected: 12	Expected: 2

- Glyph name: uacute	Contours detected: 12	Expected: 2

- Glyph name: ucircumflex	Contours detected: 13	Expected: 2

- Glyph name: udieresis	Contours detected: 12	Expected: 3

- Glyph name: yacute	Contours detected: 14	Expected: 2

- Glyph name: thorn	Contours detected: 14	Expected: 2

- Glyph name: ydieresis	Contours detected: 14	Expected: 3

- Glyph name: Amacron	Contours detected: 13	Expected: 3

- Glyph name: amacron	Contours detected: 7	Expected: 3

- Glyph name: Abreve	Contours detected: 15	Expected: 3

- Glyph name: abreve	Contours detected: 9	Expected: 3

- Glyph name: Aogonek	Contours detected: 14	Expected: 2 or 3

- Glyph name: aogonek	Contours detected: 8	Expected: 2

- Glyph name: Cacute	Contours detected: 11	Expected: 2

- Glyph name: cacute	Contours detected: 9	Expected: 2

- Glyph name: Ccircumflex	Contours detected: 12	Expected: 2

- Glyph name: ccircumflex	Contours detected: 10	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 10	Expected: 2

- Glyph name: cdotaccent	Contours detected: 8	Expected: 2

- Glyph name: Ccaron	Contours detected: 12	Expected: 2

- Glyph name: ccaron	Contours detected: 10	Expected: 2

- Glyph name: Dcaron	Contours detected: 15	Expected: 3

- Glyph name: dcaron	Contours detected: 14	Expected: 3

- Glyph name: Dcroat	Contours detected: 12	Expected: 2

- Glyph name: dcroat	Contours detected: 11	Expected: 2

- Glyph name: Emacron	Contours detected: 8	Expected: 2

- Glyph name: emacron	Contours detected: 7	Expected: 3

- Glyph name: Ebreve	Contours detected: 10	Expected: 2

- Glyph name: ebreve	Contours detected: 9	Expected: 3

- Glyph name: Edotaccent	Contours detected: 8	Expected: 2

- Glyph name: edotaccent	Contours detected: 7	Expected: 3

- Glyph name: Eogonek	Contours detected: 9	Expected: 1 or 2

- Glyph name: eogonek	Contours detected: 8	Expected: 2

- Glyph name: Ecaron	Contours detected: 10	Expected: 2

- Glyph name: ecaron	Contours detected: 9	Expected: 3

- Glyph name: Gcircumflex	Contours detected: 14	Expected: 2

- Glyph name: gcircumflex	Contours detected: 15	Expected: 3 or 4

- Glyph name: Gbreve	Contours detected: 14	Expected: 2

- Glyph name: gbreve	Contours detected: 15	Expected: 3 or 4

- Glyph name: Gdotaccent	Contours detected: 12	Expected: 2

- Glyph name: gdotaccent	Contours detected: 13	Expected: 3 or 4

- Glyph name: Gcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: gcommaaccent	Contours detected: 14	Expected: 3 or 4

- Glyph name: Hcircumflex	Contours detected: 16	Expected: 2

- Glyph name: hcircumflex	Contours detected: 15	Expected: 2

- Glyph name: Hbar	Contours detected: 12	Expected: 2

- Glyph name: hbar	Contours detected: 11	Expected: 1

- Glyph name: Itilde	Contours detected: 11	Expected: 2

- Glyph name: itilde	Contours detected: 9	Expected: 2

- Glyph name: Imacron	Contours detected: 8	Expected: 2

- Glyph name: imacron	Contours detected: 6	Expected: 2

- Glyph name: Iogonek	Contours detected: 9	Expected: 1 or 2

- Glyph name: iogonek	Contours detected: 8	Expected: 2 or 3

- Glyph name: Idotaccent	Contours detected: 8	Expected: 2

- Glyph name: dotlessi	Contours detected: 5	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: ij	Contours detected: 14	Expected: 3 or 4

- Glyph name: Jcircumflex	Contours detected: 11	Expected: 2

- Glyph name: jcircumflex	Contours detected: 11	Expected: 2

- Glyph name: Kcommaaccent	Contours detected: 15	Expected: 2 or 3

- Glyph name: kcommaaccent	Contours detected: 13	Expected: 2 or 3

- Glyph name: kgreenlandic	Contours detected: 9	Expected: 1 or 2

- Glyph name: Lacute	Contours detected: 9	Expected: 2

- Glyph name: lacute	Contours detected: 9	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: Lcaron	Contours detected: 9	Expected: 2

- Glyph name: lcaron	Contours detected: 9	Expected: 2

- Glyph name: Ldot	Contours detected: 8	Expected: 2

- Glyph name: ldot	Contours detected: 8	Expected: 2

- Glyph name: Lslash	Contours detected: 8	Expected: 1

- Glyph name: lslash	Contours detected: 7	Expected: 1

- Glyph name: Nacute	Contours detected: 17	Expected: 2

- Glyph name: nacute	Contours detected: 12	Expected: 2

- Glyph name: Ncommaaccent	Contours detected: 17	Expected: 2

- Glyph name: ncommaaccent	Contours detected: 12	Expected: 2

- Glyph name: Ncaron	Contours detected: 18	Expected: 2

- Glyph name: ncaron	Contours detected: 13	Expected: 2

- Glyph name: napostrophe	Contours detected: 13	Expected: 2

- Glyph name: Eng	Contours detected: 16	Expected: 1

- Glyph name: eng	Contours detected: 12	Expected: 1

- Glyph name: Omacron	Contours detected: 13	Expected: 3

- Glyph name: omacron	Contours detected: 9	Expected: 3

- Glyph name: Ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: ohungarumlaut	Contours detected: 12	Expected: 4

- Glyph name: OE	Contours detected: 12	Expected: 2

- Glyph name: oe	Contours detected: 11	Expected: 3

- Glyph name: Racute	Contours detected: 14	Expected: 3

- Glyph name: racute	Contours detected: 9	Expected: 2

- Glyph name: Rcommaaccent	Contours detected: 14	Expected: 3

- Glyph name: rcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: Rcaron	Contours detected: 15	Expected: 3

- Glyph name: rcaron	Contours detected: 10	Expected: 2

- Glyph name: Sacute	Contours detected: 11	Expected: 2

- Glyph name: sacute	Contours detected: 7	Expected: 2

- Glyph name: Scircumflex	Contours detected: 12	Expected: 2

- Glyph name: scircumflex	Contours detected: 8	Expected: 2

- Glyph name: Scedilla	Contours detected: 11	Expected: 1 or 2

- Glyph name: scedilla	Contours detected: 7	Expected: 1 or 2

- Glyph name: Scaron	Contours detected: 12	Expected: 2

- Glyph name: scaron	Contours detected: 8	Expected: 2

- Glyph name: uni0162	Contours detected: 9	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 10	Expected: 1 or 2

- Glyph name: Tcaron	Contours detected: 10	Expected: 2

- Glyph name: tcaron	Contours detected: 10	Expected: 2

- Glyph name: Utilde	Contours detected: 17	Expected: 2

- Glyph name: utilde	Contours detected: 14	Expected: 2

- Glyph name: Umacron	Contours detected: 14	Expected: 2

- Glyph name: umacron	Contours detected: 11	Expected: 2

- Glyph name: Ubreve	Contours detected: 16	Expected: 2

- Glyph name: ubreve	Contours detected: 13	Expected: 2

- Glyph name: Uring	Contours detected: 17	Expected: 3

- Glyph name: uring	Contours detected: 14	Expected: 3

- Glyph name: Uhungarumlaut	Contours detected: 17	Expected: 3

- Glyph name: uhungarumlaut	Contours detected: 14	Expected: 3

- Glyph name: Uogonek	Contours detected: 15	Expected: 1

- Glyph name: uogonek	Contours detected: 12	Expected: 1

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: ycircumflex	Contours detected: 15	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Zacute	Contours detected: 9	Expected: 2

- Glyph name: zacute	Contours detected: 7	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 8	Expected: 2

- Glyph name: zdotaccent	Contours detected: 6	Expected: 2

- Glyph name: Zcaron	Contours detected: 10	Expected: 2

- Glyph name: zcaron	Contours detected: 8	Expected: 2

- Glyph name: uni018F	Contours detected: 10	Expected: 2

- Glyph name: florin	Contours detected: 9	Expected: 1

- Glyph name: Ohorn	Contours detected: 15	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 11	Expected: 2

- Glyph name: Uhorn	Contours detected: 16	Expected: 1

- Glyph name: uhorn	Contours detected: 13	Expected: 1

- Glyph name: uni01CD	Contours detected: 15	Expected: 3

- Glyph name: uni01CE	Contours detected: 9	Expected: 3

- Glyph name: uni01CF	Contours detected: 10	Expected: 2

- Glyph name: uni01D0	Contours detected: 8	Expected: 2

- Glyph name: uni01D1	Contours detected: 15	Expected: 3

- Glyph name: uni01D2	Contours detected: 11	Expected: 3

- Glyph name: uni01D3	Contours detected: 16	Expected: 2

- Glyph name: uni01D4	Contours detected: 13	Expected: 2

- Glyph name: uni01D5	Contours detected: 14	Expected: 4

- Glyph name: uni01D6	Contours detected: 13	Expected: 4

- Glyph name: uni01D7	Contours detected: 13	Expected: 4

- Glyph name: uni01D8	Contours detected: 14	Expected: 4

- Glyph name: uni01D9	Contours detected: 14	Expected: 4

- Glyph name: uni01DA	Contours detected: 15	Expected: 4

- Glyph name: uni01DB	Contours detected: 13	Expected: 4

- Glyph name: uni01DC	Contours detected: 14	Expected: 4

- Glyph name: Gcaron	Contours detected: 14	Expected: 2

- Glyph name: gcaron	Contours detected: 15	Expected: 3 or 4

- Glyph name: Scommaaccent	Contours detected: 11	Expected: 2

- Glyph name: scommaaccent	Contours detected: 7	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 10	Expected: 2

- Glyph name: jdotless	Contours detected: 8	Expected: 1

- Glyph name: uni0251	Contours detected: 10	Expected: 2

- Glyph name: uni0259	Contours detected: 6	Expected: 2

- Glyph name: uni0261	Contours detected: 12	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: breve	Contours detected: 3	Expected: 1

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: ogonek	Contours detected: 2	Expected: 1

- Glyph name: tilde	Contours detected: 4	Expected: 1

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: gravecomb	Contours detected: 2	Expected: 1

- Glyph name: acutecomb	Contours detected: 2	Expected: 1

- Glyph name: circumflexcomb	Contours detected: 3	Expected: 1

- Glyph name: tildecomb	Contours detected: 4	Expected: 1

- Glyph name: brevecomb	Contours detected: 3	Expected: 1

- Glyph name: hookabovecomb	Contours detected: 3	Expected: 1

- Glyph name: ringcomb	Contours detected: 4	Expected: 2

- Glyph name: hungarumlautcomb	Contours detected: 4	Expected: 2

- Glyph name: caroncomb	Contours detected: 3	Expected: 1

- Glyph name: commaturnedabovecomb	Contours detected: 2	Expected: 1

- Glyph name: horncomb	Contours detected: 3	Expected: 1

- Glyph name: commaaccentcomb	Contours detected: 2	Expected: 1

- Glyph name: cedillacomb	Contours detected: 2	Expected: 1

- Glyph name: ogonekcomb	Contours detected: 2	Expected: 1

- Glyph name: uni032E	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 11	Expected: 2

- Glyph name: uni03A9	Contours detected: 13	Expected: 1

- Glyph name: uni03BC	Contours detected: 12	Expected: 1

- Glyph name: pi	Contours detected: 9	Expected: 1

- Glyph name: baht	Contours detected: 11	Expected: 3 or 5

- Glyph name: uni1E0C	Contours detected: 13	Expected: 3

- Glyph name: uni1E0D	Contours detected: 13	Expected: 3

- Glyph name: uni1E0E	Contours detected: 13	Expected: 3

- Glyph name: uni1E0F	Contours detected: 13	Expected: 3

- Glyph name: uni1E20	Contours detected: 12	Expected: 2

- Glyph name: uni1E21	Contours detected: 13	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 14	Expected: 2

- Glyph name: uni1E25	Contours detected: 13	Expected: 2

- Glyph name: uni1E2A	Contours detected: 14	Expected: 2

- Glyph name: uni1E2B	Contours detected: 13	Expected: 2

- Glyph name: uni1E36	Contours detected: 8	Expected: 2

- Glyph name: uni1E37	Contours detected: 8	Expected: 2

- Glyph name: uni1E38	Contours detected: 9	Expected: 3

- Glyph name: uni1E39	Contours detected: 9	Expected: 3

- Glyph name: uni1E3A	Contours detected: 8	Expected: 2

- Glyph name: uni1E3B	Contours detected: 8	Expected: 2

- Glyph name: uni1E42	Contours detected: 17	Expected: 2

- Glyph name: uni1E43	Contours detected: 14	Expected: 2

- Glyph name: uni1E44	Contours detected: 16	Expected: 2

- Glyph name: uni1E45	Contours detected: 11	Expected: 2

- Glyph name: uni1E46	Contours detected: 16	Expected: 2

- Glyph name: uni1E47	Contours detected: 11	Expected: 2

- Glyph name: uni1E48	Contours detected: 16	Expected: 2

- Glyph name: uni1E49	Contours detected: 11	Expected: 2

- Glyph name: uni1E5A	Contours detected: 13	Expected: 3

- Glyph name: uni1E5B	Contours detected: 8	Expected: 2

- Glyph name: uni1E5C	Contours detected: 14	Expected: 4

- Glyph name: uni1E5D	Contours detected: 9	Expected: 3

- Glyph name: uni1E5E	Contours detected: 13	Expected: 3

- Glyph name: uni1E5F	Contours detected: 8	Expected: 2

- Glyph name: uni1E60	Contours detected: 10	Expected: 2

- Glyph name: uni1E61	Contours detected: 6	Expected: 2

- Glyph name: uni1E62	Contours detected: 10	Expected: 2

- Glyph name: uni1E63	Contours detected: 6	Expected: 2

- Glyph name: uni1E6C	Contours detected: 8	Expected: 2

- Glyph name: uni1E6D	Contours detected: 9	Expected: 2

- Glyph name: uni1E6E	Contours detected: 8	Expected: 2

- Glyph name: uni1E6F	Contours detected: 9	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 13	Expected: 2

- Glyph name: uni1E92	Contours detected: 8	Expected: 2

- Glyph name: uni1E93	Contours detected: 6	Expected: 2

- Glyph name: uni1E97	Contours detected: 10	Expected: 3

- Glyph name: Germandbls	Contours detected: 13	Expected: 1

- Glyph name: Adotbelow	Contours detected: 13	Expected: 3

- Glyph name: adotbelow	Contours detected: 7	Expected: 3

- Glyph name: Ahookabove	Contours detected: 15	Expected: 3

- Glyph name: ahookabove	Contours detected: 9	Expected: 3

- Glyph name: Acircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: acircumflexacute	Contours detected: 11	Expected: 4

- Glyph name: Acircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: acircumflexgrave	Contours detected: 11	Expected: 4

- Glyph name: Acircumflexhookabove	Contours detected: 14	Expected: 4

- Glyph name: acircumflexhookabove	Contours detected: 12	Expected: 4

- Glyph name: Acircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: acircumflextilde	Contours detected: 13	Expected: 4

- Glyph name: Acircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: acircumflexdotbelow	Contours detected: 10	Expected: 4

- Glyph name: Abreveacute	Contours detected: 13	Expected: 4

- Glyph name: abreveacute	Contours detected: 11	Expected: 4

- Glyph name: Abrevegrave	Contours detected: 13	Expected: 4

- Glyph name: abrevegrave	Contours detected: 11	Expected: 4

- Glyph name: Abrevehookabove	Contours detected: 14	Expected: 4

- Glyph name: abrevehookabove	Contours detected: 12	Expected: 4

- Glyph name: Abrevetilde	Contours detected: 15	Expected: 4

- Glyph name: abrevetilde	Contours detected: 13	Expected: 4

- Glyph name: Abrevedotbelow	Contours detected: 16	Expected: 4

- Glyph name: abrevedotbelow	Contours detected: 10	Expected: 4

- Glyph name: Edotbelow	Contours detected: 8	Expected: 2

- Glyph name: edotbelow	Contours detected: 7	Expected: 3

- Glyph name: Ehookabove	Contours detected: 10	Expected: 2

- Glyph name: ehookabove	Contours detected: 9	Expected: 3

- Glyph name: Etilde	Contours detected: 11	Expected: 2

- Glyph name: etilde	Contours detected: 10	Expected: 3

- Glyph name: Ecircumflexacute	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexacute	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflexgrave	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexgrave	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflexhookabove	Contours detected: 11	Expected: 3

- Glyph name: ecircumflexhookabove	Contours detected: 12	Expected: 4

- Glyph name: Ecircumflextilde	Contours detected: 12	Expected: 3

- Glyph name: ecircumflextilde	Contours detected: 13	Expected: 4

- Glyph name: Ecircumflexdotbelow	Contours detected: 11	Expected: 3

- Glyph name: ecircumflexdotbelow	Contours detected: 10	Expected: 4

- Glyph name: Ihookabove	Contours detected: 10	Expected: 2

- Glyph name: ihookabove	Contours detected: 8	Expected: 2

- Glyph name: Idotbelow	Contours detected: 8	Expected: 2

- Glyph name: idotbelow	Contours detected: 7	Expected: 3

- Glyph name: Odotbelow	Contours detected: 13	Expected: 3

- Glyph name: odotbelow	Contours detected: 9	Expected: 3

- Glyph name: Ohookabove	Contours detected: 15	Expected: 3

- Glyph name: ohookabove	Contours detected: 11	Expected: 3

- Glyph name: Ocircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflexhookabove	Contours detected: 14	Expected: 4

- Glyph name: ocircumflexhookabove	Contours detected: 14	Expected: 4

- Glyph name: Ocircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: ocircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: Ocircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: ocircumflexdotbelow	Contours detected: 12	Expected: 4

- Glyph name: Ohornacute	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohornacute	Contours detected: 13	Expected: 3

- Glyph name: Ohorngrave	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohorngrave	Contours detected: 13	Expected: 3

- Glyph name: Ohornhookabove	Contours detected: 18	Expected: 3 or 4

- Glyph name: ohornhookabove	Contours detected: 14	Expected: 3

- Glyph name: Ohorntilde	Contours detected: 19	Expected: 3 or 4

- Glyph name: ohorntilde	Contours detected: 15	Expected: 3

- Glyph name: Ohorndotbelow	Contours detected: 16	Expected: 3 or 4

- Glyph name: ohorndotbelow	Contours detected: 12	Expected: 3

- Glyph name: Udotbelow	Contours detected: 14	Expected: 2

- Glyph name: udotbelow	Contours detected: 11	Expected: 2

- Glyph name: Uhookabove	Contours detected: 16	Expected: 2

- Glyph name: uhookabove	Contours detected: 13	Expected: 2

- Glyph name: Uhornacute	Contours detected: 18	Expected: 2

- Glyph name: uhornacute	Contours detected: 15	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 18	Expected: 2

- Glyph name: uhorngrave	Contours detected: 15	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 19	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 16	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 20	Expected: 2

- Glyph name: uhorntilde	Contours detected: 17	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 17	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 14	Expected: 2

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: ygrave	Contours detected: 14	Expected: 2

- Glyph name: Ydotbelow	Contours detected: 11	Expected: 2

- Glyph name: ydotbelow	Contours detected: 8	Expected: 2

- Glyph name: Yhookabove	Contours detected: 13	Expected: 2

- Glyph name: yhookabove	Contours detected: 15	Expected: 2

- Glyph name: Ytilde	Contours detected: 14	Expected: 2

- Glyph name: ytilde	Contours detected: 16	Expected: 2

- Glyph name: dblverticalbar	Contours detected: 14	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: dagger	Contours detected: 9	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 9	Expected: 1 or 3

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: perthousand	Contours detected: 11	Expected: 6 or 7

- Glyph name: minute	Contours detected: 3	Expected: 1

- Glyph name: second	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: uni2070	Contours detected: 8	Expected: 2 or 3

- Glyph name: foursuperior	Contours detected: 6	Expected: 1 or 2

- Glyph name: fivesuperior	Contours detected: 5	Expected: 1

- Glyph name: sixsuperior	Contours detected: 6	Expected: 2

- Glyph name: sevensuperior	Contours detected: 5	Expected: 1

- Glyph name: eightsuperior	Contours detected: 7	Expected: 3

- Glyph name: ninesuperior	Contours detected: 6	Expected: 2

- Glyph name: uni207D	Contours detected: 5	Expected: 1

- Glyph name: uni207E	Contours detected: 5	Expected: 1

- Glyph name: uni207F	Contours detected: 7	Expected: 1

- Glyph name: uni2080	Contours detected: 8	Expected: 2 or 3

- Glyph name: oneinferior	Contours detected: 5	Expected: 1

- Glyph name: twoinferior	Contours detected: 5	Expected: 1

- Glyph name: threeinferior	Contours detected: 5	Expected: 1

- Glyph name: fourinferior	Contours detected: 6	Expected: 1 or 2

- Glyph name: fiveinferior	Contours detected: 5	Expected: 1

- Glyph name: sixinferior	Contours detected: 6	Expected: 2

- Glyph name: seveninferior	Contours detected: 5	Expected: 1

- Glyph name: eightinferior	Contours detected: 7	Expected: 3

- Glyph name: nineinferior	Contours detected: 6	Expected: 2

- Glyph name: uni208D	Contours detected: 5	Expected: 1

- Glyph name: uni208E	Contours detected: 5	Expected: 1

- Glyph name: colonmonetary	Contours detected: 12	Expected: 1 or 3

- Glyph name: lira	Contours detected: 8	Expected: 1

- Glyph name: naira	Contours detected: 12	Expected: 1, 3 or 5

- Glyph name: peseta	Contours detected: 19	Expected: 2, 3 or 4

- Glyph name: rupee	Contours detected: 17	Expected: 3

- Glyph name: won	Contours detected: 14	Expected: 1, 3, 4 or 7

- Glyph name: sheqel	Contours detected: 18	Expected: 2

- Glyph name: dong	Contours detected: 12	Expected: 3 or 4

- Glyph name: Euro	Contours detected: 9	Expected: 1 or 2

- Glyph name: kip	Contours detected: 11	Expected: 1

- Glyph name: tugrik	Contours detected: 7	Expected: 1

- Glyph name: peso	Contours detected: 9	Expected: 1, 2 or 4

- Glyph name: guarani	Contours detected: 11	Expected: 1, 2 or 3

- Glyph name: hryvnia	Contours detected: 7	Expected: 1 or 2

- Glyph name: cedi	Contours detected: 12	Expected: 1 or 2

- Glyph name: tenge	Contours detected: 6	Expected: 2

- Glyph name: rupeeIndian	Contours detected: 7	Expected: 1

- Glyph name: liraTurkish	Contours detected: 9	Expected: 1

- Glyph name: manat	Contours detected: 15	Expected: 1

- Glyph name: ruble	Contours detected: 9	Expected: 2

- Glyph name: bitcoin	Contours detected: 11	Expected: 3

- Glyph name: literSign	Contours detected: 10	Expected: 2

- Glyph name: numero	Contours detected: 22	Expected: 3 or 4

- Glyph name: uni2117	Contours detected: 19	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 15	Expected: 2

- Glyph name: trademark	Contours detected: 16	Expected: 2

- Glyph name: Ohm	Contours detected: 13	Expected: 1

- Glyph name: onethird	Contours detected: 10	Expected: 3

- Glyph name: twothirds	Contours detected: 10	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 12	Expected: 5

- Glyph name: threeeighths	Contours detected: 12	Expected: 5

- Glyph name: fiveeighths	Contours detected: 12	Expected: 5

- Glyph name: seveneighths	Contours detected: 12	Expected: 5

- Glyph name: arrowleft	Contours detected: 5	Expected: 1

- Glyph name: arrowup	Contours detected: 9	Expected: 1

- Glyph name: arrowright	Contours detected: 5	Expected: 1

- Glyph name: arrowdown	Contours detected: 9	Expected: 1

- Glyph name: arrowboth	Contours detected: 9	Expected: 1

- Glyph name: arrowupdn	Contours detected: 11	Expected: 1

- Glyph name: northWestArrow	Contours detected: 8	Expected: 1

- Glyph name: northEastArrow	Contours detected: 8	Expected: 1

- Glyph name: southEastArrow	Contours detected: 8	Expected: 1

- Glyph name: southWestArrow	Contours detected: 8	Expected: 1

- Glyph name: partialdiff	Contours detected: 9	Expected: 2

- Glyph name: emptyset	Contours detected: 17	Expected: 3

- Glyph name: increment	Contours detected: 11	Expected: 2

- Glyph name: product	Contours detected: 17	Expected: 1

- Glyph name: summation	Contours detected: 9	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 8	Expected: 1

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: approxequal	Contours detected: 8	Expected: 2

- Glyph name: notequal	Contours detected: 7	Expected: 1

- Glyph name: lessequal	Contours detected: 6	Expected: 2

- Glyph name: greaterequal	Contours detected: 6	Expected: 2

- Glyph name: filledbox	Contours detected: 7	Expected: 1

- Glyph name: whiteSquare	Contours detected: 12	Expected: 2

- Glyph name: blackSmallSquare	Contours detected: 3	Expected: 1

- Glyph name: whiteSmallSquare	Contours detected: 4	Expected: 2

- Glyph name: triagup	Contours detected: 7	Expected: 1

- Glyph name: upWhiteTriangle	Contours detected: 12	Expected: 2

- Glyph name: rightBlackTriangle	Contours detected: 7	Expected: 1

- Glyph name: rightWhiteTriangle	Contours detected: 12	Expected: 2

- Glyph name: triagdn	Contours detected: 7	Expected: 1

- Glyph name: downWhiteTriangle	Contours detected: 12	Expected: 2

- Glyph name: leftBlackTriangle	Contours detected: 7	Expected: 1

- Glyph name: leftWhiteTriangle	Contours detected: 12	Expected: 2

- Glyph name: blackDiamond	Contours detected: 7	Expected: 1

- Glyph name: whiteDiamond	Contours detected: 12	Expected: 2

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: circle	Contours detected: 12	Expected: 2

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: blackCircle	Contours detected: 7	Expected: 1

- Glyph name: leftanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: rightanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: uniFB01	Contours detected: 11	Expected: 1, 2 or 3

- Glyph name: uniFB02	Contours detected: 13	Expected: 1 or 2

- Glyph name: A	Contours detected: 12	Expected: 2

- Glyph name: AE	Contours detected: 12	Expected: 2

- Glyph name: Aacute	Contours detected: 14	Expected: 3

- Glyph name: Abreve	Contours detected: 15	Expected: 3

- Glyph name: Acircumflex	Contours detected: 15	Expected: 3

- Glyph name: Adieresis	Contours detected: 14	Expected: 4

- Glyph name: Agrave	Contours detected: 14	Expected: 3

- Glyph name: Amacron	Contours detected: 13	Expected: 3

- Glyph name: Aogonek	Contours detected: 14	Expected: 2 or 3

- Glyph name: Aring	Contours detected: 16	Expected: 3 or 4

- Glyph name: Atilde	Contours detected: 16	Expected: 3

- Glyph name: B	Contours detected: 11	Expected: 2 or 3

- Glyph name: C	Contours detected: 9	Expected: 1

- Glyph name: Cacute	Contours detected: 11	Expected: 2

- Glyph name: Ccaron	Contours detected: 12	Expected: 2

- Glyph name: Ccedilla	Contours detected: 11	Expected: 1 or 2

- Glyph name: Ccircumflex	Contours detected: 12	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 10	Expected: 2

- Glyph name: D	Contours detected: 12	Expected: 2

- Glyph name: Dcaron	Contours detected: 15	Expected: 3

- Glyph name: Dcroat	Contours detected: 12	Expected: 2

- Glyph name: E	Contours detected: 7	Expected: 1

- Glyph name: Eacute	Contours detected: 9	Expected: 2

- Glyph name: Ebreve	Contours detected: 10	Expected: 2

- Glyph name: Ecaron	Contours detected: 10	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 10	Expected: 2

- Glyph name: Edieresis	Contours detected: 9	Expected: 3

- Glyph name: Edotaccent	Contours detected: 8	Expected: 2

- Glyph name: Egrave	Contours detected: 9	Expected: 2

- Glyph name: Emacron	Contours detected: 8	Expected: 2

- Glyph name: Eng	Contours detected: 16	Expected: 1

- Glyph name: Eogonek	Contours detected: 9	Expected: 1 or 2

- Glyph name: Eth	Contours detected: 12	Expected: 2

- Glyph name: Euro	Contours detected: 9	Expected: 1 or 2

- Glyph name: F	Contours detected: 7	Expected: 1

- Glyph name: G	Contours detected: 11	Expected: 1

- Glyph name: Gbreve	Contours detected: 14	Expected: 2

- Glyph name: Gcaron	Contours detected: 14	Expected: 2

- Glyph name: Gcircumflex	Contours detected: 14	Expected: 2

- Glyph name: Gdotaccent	Contours detected: 12	Expected: 2

- Glyph name: H	Contours detected: 13	Expected: 1

- Glyph name: Hbar	Contours detected: 12	Expected: 2

- Glyph name: Hcircumflex	Contours detected: 16	Expected: 2

- Glyph name: I	Contours detected: 7	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: Iacute	Contours detected: 9	Expected: 2

- Glyph name: Icircumflex	Contours detected: 10	Expected: 2

- Glyph name: Idieresis	Contours detected: 9	Expected: 3

- Glyph name: Idotaccent	Contours detected: 8	Expected: 2

- Glyph name: Igrave	Contours detected: 9	Expected: 2

- Glyph name: Imacron	Contours detected: 8	Expected: 2

- Glyph name: Iogonek	Contours detected: 9	Expected: 1 or 2

- Glyph name: Itilde	Contours detected: 11	Expected: 2

- Glyph name: J	Contours detected: 8	Expected: 1

- Glyph name: Jcircumflex	Contours detected: 11	Expected: 2

- Glyph name: K	Contours detected: 13	Expected: 1 or 2

- Glyph name: L	Contours detected: 7	Expected: 1

- Glyph name: Lacute	Contours detected: 9	Expected: 2

- Glyph name: Lcaron	Contours detected: 9	Expected: 2

- Glyph name: Ldot	Contours detected: 8	Expected: 2

- Glyph name: Lslash	Contours detected: 8	Expected: 1

- Glyph name: M	Contours detected: 16	Expected: 1

- Glyph name: N	Contours detected: 15	Expected: 1

- Glyph name: Nacute	Contours detected: 17	Expected: 2

- Glyph name: Ncaron	Contours detected: 18	Expected: 2

- Glyph name: Ntilde	Contours detected: 19	Expected: 2

- Glyph name: O	Contours detected: 12	Expected: 2

- Glyph name: OE	Contours detected: 12	Expected: 2

- Glyph name: Oacute	Contours detected: 14	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: Odieresis	Contours detected: 14	Expected: 4

- Glyph name: Ograve	Contours detected: 14	Expected: 3

- Glyph name: Ohorn	Contours detected: 15	Expected: 2 or 3

- Glyph name: Ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: Omacron	Contours detected: 13	Expected: 3

- Glyph name: Oslash	Contours detected: 13	Expected: 2 or 3

- Glyph name: Otilde	Contours detected: 16	Expected: 3

- Glyph name: P	Contours detected: 9	Expected: 1 or 2

- Glyph name: Q	Contours detected: 14	Expected: 2

- Glyph name: R	Contours detected: 12	Expected: 1 or 2

- Glyph name: Racute	Contours detected: 14	Expected: 3

- Glyph name: Rcaron	Contours detected: 15	Expected: 3

- Glyph name: S	Contours detected: 9	Expected: 1

- Glyph name: Sacute	Contours detected: 11	Expected: 2

- Glyph name: Scaron	Contours detected: 12	Expected: 2

- Glyph name: Scircumflex	Contours detected: 12	Expected: 2

- Glyph name: T	Contours detected: 7	Expected: 1

- Glyph name: Tcaron	Contours detected: 10	Expected: 2

- Glyph name: Thorn	Contours detected: 10	Expected: 1 or 2

- Glyph name: U	Contours detected: 13	Expected: 1

- Glyph name: Uacute	Contours detected: 15	Expected: 2

- Glyph name: Ubreve	Contours detected: 16	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 16	Expected: 2

- Glyph name: Udieresis	Contours detected: 15	Expected: 3

- Glyph name: Ugrave	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 16	Expected: 1

- Glyph name: Uhungarumlaut	Contours detected: 17	Expected: 3

- Glyph name: Umacron	Contours detected: 14	Expected: 2

- Glyph name: Uogonek	Contours detected: 15	Expected: 1

- Glyph name: Uring	Contours detected: 17	Expected: 3

- Glyph name: Utilde	Contours detected: 17	Expected: 2

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: Z	Contours detected: 7	Expected: 1

- Glyph name: Zacute	Contours detected: 9	Expected: 2

- Glyph name: Zcaron	Contours detected: 10	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 8	Expected: 2

- Glyph name: a	Contours detected: 6	Expected: 2

- Glyph name: aacute	Contours detected: 8	Expected: 3

- Glyph name: abreve	Contours detected: 9	Expected: 3

- Glyph name: acircumflex	Contours detected: 9	Expected: 3

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: adieresis	Contours detected: 8	Expected: 4

- Glyph name: ae	Contours detected: 9	Expected: 3

- Glyph name: agrave	Contours detected: 8	Expected: 3

- Glyph name: amacron	Contours detected: 7	Expected: 3

- Glyph name: ampersand	Contours detected: 13	Expected: 1, 2 or 3

- Glyph name: aogonek	Contours detected: 8	Expected: 2

- Glyph name: approxequal	Contours detected: 8	Expected: 2

- Glyph name: aring	Contours detected: 10	Expected: 4

- Glyph name: arrowboth	Contours detected: 9	Expected: 1

- Glyph name: arrowdown	Contours detected: 9	Expected: 1

- Glyph name: arrowup	Contours detected: 9	Expected: 1

- Glyph name: arrowupdn	Contours detected: 11	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 9	Expected: 1 or 4

- Glyph name: at	Contours detected: 12	Expected: 2

- Glyph name: atilde	Contours detected: 10	Expected: 3

- Glyph name: b	Contours detected: 12	Expected: 2

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceleft	Contours detected: 7	Expected: 1

- Glyph name: braceright	Contours detected: 7	Expected: 1

- Glyph name: bracketleft	Contours detected: 7	Expected: 1

- Glyph name: bracketright	Contours detected: 7	Expected: 1

- Glyph name: breve	Contours detected: 3	Expected: 1

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: c	Contours detected: 7	Expected: 1

- Glyph name: cacute	Contours detected: 9	Expected: 2

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: ccaron	Contours detected: 10	Expected: 2

- Glyph name: ccedilla	Contours detected: 9	Expected: 1 or 2

- Glyph name: ccircumflex	Contours detected: 10	Expected: 2

- Glyph name: cdotaccent	Contours detected: 8	Expected: 2

- Glyph name: cedilla	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 12	Expected: 1 or 2

- Glyph name: circle	Contours detected: 12	Expected: 2

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: colonmonetary	Contours detected: 12	Expected: 1 or 3

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: copyright	Contours detected: 18	Expected: 3

- Glyph name: currency	Contours detected: 8	Expected: 2

- Glyph name: d	Contours detected: 12	Expected: 2

- Glyph name: dagger	Contours detected: 9	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 9	Expected: 1 or 3

- Glyph name: dcaron	Contours detected: 14	Expected: 3

- Glyph name: dcroat	Contours detected: 11	Expected: 2

- Glyph name: degree	Contours detected: 6	Expected: 2

- Glyph name: dollar	Contours detected: 9	Expected: 1, 3 or 5

- Glyph name: dong	Contours detected: 12	Expected: 3 or 4

- Glyph name: dotlessi	Contours detected: 5	Expected: 1

- Glyph name: e	Contours detected: 6	Expected: 2

- Glyph name: eacute	Contours detected: 8	Expected: 3

- Glyph name: ebreve	Contours detected: 9	Expected: 3

- Glyph name: ecaron	Contours detected: 9	Expected: 3

- Glyph name: ecircumflex	Contours detected: 9	Expected: 3

- Glyph name: edieresis	Contours detected: 8	Expected: 4

- Glyph name: edotaccent	Contours detected: 7	Expected: 3

- Glyph name: egrave	Contours detected: 8	Expected: 3

- Glyph name: eight	Contours detected: 11	Expected: 3

- Glyph name: emacron	Contours detected: 7	Expected: 3

- Glyph name: emptyset	Contours detected: 17	Expected: 3

- Glyph name: eng	Contours detected: 12	Expected: 1

- Glyph name: eogonek	Contours detected: 8	Expected: 2

- Glyph name: eth	Contours detected: 10	Expected: 2

- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: f	Contours detected: 8	Expected: 1

- Glyph name: five	Contours detected: 8	Expected: 1

- Glyph name: fiveeighths	Contours detected: 12	Expected: 5

- Glyph name: four	Contours detected: 9	Expected: 1 or 2

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: g	Contours detected: 12	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 15	Expected: 3 or 4

- Glyph name: gcaron	Contours detected: 15	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 15	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 13	Expected: 3 or 4

- Glyph name: germandbls	Contours detected: 13	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: greaterequal	Contours detected: 6	Expected: 2

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: h	Contours detected: 12	Expected: 1

- Glyph name: hbar	Contours detected: 11	Expected: 1

- Glyph name: hcircumflex	Contours detected: 15	Expected: 2

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: i	Contours detected: 6	Expected: 2

- Glyph name: iacute	Contours detected: 7	Expected: 2

- Glyph name: icircumflex	Contours detected: 8	Expected: 2

- Glyph name: idieresis	Contours detected: 7	Expected: 3

- Glyph name: igrave	Contours detected: 7	Expected: 2

- Glyph name: ij	Contours detected: 14	Expected: 3 or 4

- Glyph name: imacron	Contours detected: 6	Expected: 2

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: iogonek	Contours detected: 8	Expected: 2 or 3

- Glyph name: itilde	Contours detected: 9	Expected: 2

- Glyph name: j	Contours detected: 9	Expected: 2

- Glyph name: jcircumflex	Contours detected: 11	Expected: 2

- Glyph name: k	Contours detected: 11	Expected: 1 or 2

- Glyph name: kgreenlandic	Contours detected: 9	Expected: 1 or 2

- Glyph name: l	Contours detected: 7	Expected: 1

- Glyph name: lacute	Contours detected: 9	Expected: 2

- Glyph name: lcaron	Contours detected: 9	Expected: 2

- Glyph name: ldot	Contours detected: 8	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: lessequal	Contours detected: 6	Expected: 2

- Glyph name: lira	Contours detected: 8	Expected: 1

- Glyph name: logicalnot	Contours detected: 3	Expected: 1

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: lslash	Contours detected: 7	Expected: 1

- Glyph name: m	Contours detected: 13	Expected: 1

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: n	Contours detected: 10	Expected: 1

- Glyph name: nacute	Contours detected: 12	Expected: 2

- Glyph name: napostrophe	Contours detected: 13	Expected: 2

- Glyph name: ncaron	Contours detected: 13	Expected: 2

- Glyph name: nine	Contours detected: 9	Expected: 1 or 2

- Glyph name: notequal	Contours detected: 7	Expected: 1

- Glyph name: ntilde	Contours detected: 14	Expected: 2

- Glyph name: numbersign	Contours detected: 12	Expected: 2

- Glyph name: o	Contours detected: 8	Expected: 2

- Glyph name: oacute	Contours detected: 10	Expected: 3

- Glyph name: ocircumflex	Contours detected: 11	Expected: 3

- Glyph name: odieresis	Contours detected: 10	Expected: 4

- Glyph name: oe	Contours detected: 11	Expected: 3

- Glyph name: ogonek	Contours detected: 2	Expected: 1

- Glyph name: ograve	Contours detected: 10	Expected: 3

- Glyph name: ohorn	Contours detected: 11	Expected: 2

- Glyph name: ohungarumlaut	Contours detected: 12	Expected: 4

- Glyph name: omacron	Contours detected: 9	Expected: 3

- Glyph name: one	Contours detected: 7	Expected: 1

- Glyph name: oneeighth	Contours detected: 12	Expected: 5

- Glyph name: onehalf	Contours detected: 10	Expected: 3

- Glyph name: onequarter	Contours detected: 11	Expected: 3 or 4

- Glyph name: onethird	Contours detected: 10	Expected: 3

- Glyph name: ordfeminine	Contours detected: 7	Expected: 2 or 3

- Glyph name: ordmasculine	Contours detected: 7	Expected: 2 or 3

- Glyph name: oslash	Contours detected: 11	Expected: 3

- Glyph name: otilde	Contours detected: 12	Expected: 3

- Glyph name: p	Contours detected: 12	Expected: 2

- Glyph name: paragraph	Contours detected: 19	Expected: 1, 2 or 3

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: partialdiff	Contours detected: 9	Expected: 2

- Glyph name: percent	Contours detected: 9	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 11	Expected: 6 or 7

- Glyph name: peseta	Contours detected: 19	Expected: 2, 3 or 4

- Glyph name: pi	Contours detected: 9	Expected: 1

- Glyph name: plus	Contours detected: 5	Expected: 1

- Glyph name: plusminus	Contours detected: 6	Expected: 1 or 2

- Glyph name: product	Contours detected: 17	Expected: 1

- Glyph name: q	Contours detected: 12	Expected: 2

- Glyph name: question	Contours detected: 7	Expected: 2

- Glyph name: questiondown	Contours detected: 7	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: r	Contours detected: 7	Expected: 1

- Glyph name: racute	Contours detected: 9	Expected: 2

- Glyph name: radical	Contours detected: 8	Expected: 1

- Glyph name: rcaron	Contours detected: 10	Expected: 2

- Glyph name: registered	Contours detected: 20	Expected: 3 or 4

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: rupee	Contours detected: 17	Expected: 3

- Glyph name: s	Contours detected: 5	Expected: 1

- Glyph name: sacute	Contours detected: 7	Expected: 2

- Glyph name: scaron	Contours detected: 8	Expected: 2

- Glyph name: scircumflex	Contours detected: 8	Expected: 2

- Glyph name: section	Contours detected: 12	Expected: 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: seven	Contours detected: 7	Expected: 1

- Glyph name: seveneighths	Contours detected: 12	Expected: 5

- Glyph name: six	Contours detected: 9	Expected: 1 or 2

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: sterling	Contours detected: 8	Expected: 1 or 2

- Glyph name: summation	Contours detected: 9	Expected: 1

- Glyph name: t	Contours detected: 8	Expected: 1

- Glyph name: tcaron	Contours detected: 10	Expected: 2

- Glyph name: thorn	Contours detected: 14	Expected: 2

- Glyph name: three	Contours detected: 9	Expected: 1

- Glyph name: threeeighths	Contours detected: 12	Expected: 5

- Glyph name: threequarters	Contours detected: 11	Expected: 3 or 4

- Glyph name: tilde	Contours detected: 4	Expected: 1

- Glyph name: trademark	Contours detected: 16	Expected: 2

- Glyph name: triagdn	Contours detected: 7	Expected: 1

- Glyph name: triagup	Contours detected: 7	Expected: 1

- Glyph name: two	Contours detected: 8	Expected: 1

- Glyph name: twothirds	Contours detected: 10	Expected: 1 or 3

- Glyph name: u	Contours detected: 10	Expected: 1

- Glyph name: uacute	Contours detected: 12	Expected: 2

- Glyph name: ubreve	Contours detected: 13	Expected: 2

- Glyph name: ucircumflex	Contours detected: 13	Expected: 2

- Glyph name: udieresis	Contours detected: 12	Expected: 3

- Glyph name: ugrave	Contours detected: 12	Expected: 2

- Glyph name: uhorn	Contours detected: 13	Expected: 1

- Glyph name: uhungarumlaut	Contours detected: 14	Expected: 3

- Glyph name: umacron	Contours detected: 11	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni0162	Contours detected: 9	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 10	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 10	Expected: 2

- Glyph name: uni01CD	Contours detected: 15	Expected: 3

- Glyph name: uni01CE	Contours detected: 9	Expected: 3

- Glyph name: uni01CF	Contours detected: 10	Expected: 2

- Glyph name: uni01D0	Contours detected: 8	Expected: 2

- Glyph name: uni01D1	Contours detected: 15	Expected: 3

- Glyph name: uni01D2	Contours detected: 11	Expected: 3

- Glyph name: uni01D3	Contours detected: 16	Expected: 2

- Glyph name: uni01D4	Contours detected: 13	Expected: 2

- Glyph name: uni01D5	Contours detected: 14	Expected: 4

- Glyph name: uni01D6	Contours detected: 13	Expected: 4

- Glyph name: uni01D7	Contours detected: 13	Expected: 4

- Glyph name: uni01D8	Contours detected: 14	Expected: 4

- Glyph name: uni01D9	Contours detected: 14	Expected: 4

- Glyph name: uni01DA	Contours detected: 15	Expected: 4

- Glyph name: uni01DB	Contours detected: 13	Expected: 4

- Glyph name: uni01DC	Contours detected: 14	Expected: 4

- Glyph name: uni0251	Contours detected: 10	Expected: 2

- Glyph name: uni0259	Contours detected: 6	Expected: 2

- Glyph name: uni0261	Contours detected: 12	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni032E	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 11	Expected: 2

- Glyph name: uni03A9	Contours detected: 13	Expected: 1

- Glyph name: uni03BC	Contours detected: 12	Expected: 1

- Glyph name: uni1E0C	Contours detected: 13	Expected: 3

- Glyph name: uni1E0D	Contours detected: 13	Expected: 3

- Glyph name: uni1E0E	Contours detected: 13	Expected: 3

- Glyph name: uni1E0F	Contours detected: 13	Expected: 3

- Glyph name: uni1E20	Contours detected: 12	Expected: 2

- Glyph name: uni1E21	Contours detected: 13	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 14	Expected: 2

- Glyph name: uni1E25	Contours detected: 13	Expected: 2

- Glyph name: uni1E2A	Contours detected: 14	Expected: 2

- Glyph name: uni1E2B	Contours detected: 13	Expected: 2

- Glyph name: uni1E36	Contours detected: 8	Expected: 2

- Glyph name: uni1E37	Contours detected: 8	Expected: 2

- Glyph name: uni1E38	Contours detected: 9	Expected: 3

- Glyph name: uni1E39	Contours detected: 9	Expected: 3

- Glyph name: uni1E3A	Contours detected: 8	Expected: 2

- Glyph name: uni1E3B	Contours detected: 8	Expected: 2

- Glyph name: uni1E42	Contours detected: 17	Expected: 2

- Glyph name: uni1E43	Contours detected: 14	Expected: 2

- Glyph name: uni1E44	Contours detected: 16	Expected: 2

- Glyph name: uni1E45	Contours detected: 11	Expected: 2

- Glyph name: uni1E46	Contours detected: 16	Expected: 2

- Glyph name: uni1E47	Contours detected: 11	Expected: 2

- Glyph name: uni1E48	Contours detected: 16	Expected: 2

- Glyph name: uni1E49	Contours detected: 11	Expected: 2

- Glyph name: uni1E5A	Contours detected: 13	Expected: 3

- Glyph name: uni1E5B	Contours detected: 8	Expected: 2

- Glyph name: uni1E5C	Contours detected: 14	Expected: 4

- Glyph name: uni1E5D	Contours detected: 9	Expected: 3

- Glyph name: uni1E5E	Contours detected: 13	Expected: 3

- Glyph name: uni1E5F	Contours detected: 8	Expected: 2

- Glyph name: uni1E60	Contours detected: 10	Expected: 2

- Glyph name: uni1E61	Contours detected: 6	Expected: 2

- Glyph name: uni1E62	Contours detected: 10	Expected: 2

- Glyph name: uni1E63	Contours detected: 6	Expected: 2

- Glyph name: uni1E6C	Contours detected: 8	Expected: 2

- Glyph name: uni1E6D	Contours detected: 9	Expected: 2

- Glyph name: uni1E6E	Contours detected: 8	Expected: 2

- Glyph name: uni1E6F	Contours detected: 9	Expected: 2

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 13	Expected: 2

- Glyph name: uni1E92	Contours detected: 8	Expected: 2

- Glyph name: uni1E93	Contours detected: 6	Expected: 2

- Glyph name: uni1E97	Contours detected: 10	Expected: 3

- Glyph name: uni2117	Contours detected: 19	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 15	Expected: 2

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 12	Expected: 1

- Glyph name: uring	Contours detected: 14	Expected: 3

- Glyph name: utilde	Contours detected: 14	Expected: 2

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 12	Expected: 1

- Glyph name: yacute	Contours detected: 14	Expected: 2

- Glyph name: ycircumflex	Contours detected: 15	Expected: 2

- Glyph name: ydieresis	Contours detected: 14	Expected: 3

- Glyph name: yen	Contours detected: 9	Expected: 1 or 2

- Glyph name: ygrave	Contours detected: 14	Expected: 2

- Glyph name: z	Contours detected: 5	Expected: 1

- Glyph name: zacute	Contours detected: 7	Expected: 2

- Glyph name: zcaron	Contours detected: 8	Expected: 2

- Glyph name: zdotaccent	Contours detected: 6	Expected: 2

- Glyph name: zero	Contours detected: 13	Expected: 2 or 3
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



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

<details><summary>[9] MatrixSansScreenSC-Regular.ttf</summary>
<div>
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

- Glyph name: plus	Contours detected: 9	Expected: 1

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: hyphen	Contours detected: 4	Expected: 1

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: zero	Contours detected: 19	Expected: 2 or 3

- Glyph name: one	Contours detected: 10	Expected: 1

- Glyph name: two	Contours detected: 15	Expected: 1

- Glyph name: three	Contours detected: 14	Expected: 1

- Glyph name: four	Contours detected: 14	Expected: 1 or 2

- Glyph name: five	Contours detected: 17	Expected: 1

- Glyph name: six	Contours detected: 15	Expected: 1 or 2

- Glyph name: seven	Contours detected: 11	Expected: 1

- Glyph name: eight	Contours detected: 17	Expected: 3

- Glyph name: nine	Contours detected: 15	Expected: 1 or 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: equal	Contours detected: 10	Expected: 2

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: question	Contours detected: 10	Expected: 2

- Glyph name: at	Contours detected: 20	Expected: 2

- Glyph name: A	Contours detected: 16	Expected: 2

- Glyph name: B	Contours detected: 20	Expected: 2 or 3

- Glyph name: C	Contours detected: 13	Expected: 1

- Glyph name: D	Contours detected: 16	Expected: 2

- Glyph name: E	Contours detected: 18	Expected: 1

- Glyph name: F	Contours detected: 14	Expected: 1

- Glyph name: G	Contours detected: 17	Expected: 1

- Glyph name: H	Contours detected: 17	Expected: 1

- Glyph name: I	Contours detected: 11	Expected: 1

- Glyph name: J	Contours detected: 11	Expected: 1

- Glyph name: K	Contours detected: 14	Expected: 1 or 2

- Glyph name: L	Contours detected: 11	Expected: 1

- Glyph name: M	Contours detected: 18	Expected: 1

- Glyph name: N	Contours detected: 17	Expected: 1

- Glyph name: O	Contours detected: 16	Expected: 2

- Glyph name: P	Contours detected: 15	Expected: 1 or 2

- Glyph name: Q	Contours detected: 17	Expected: 2

- Glyph name: R	Contours detected: 18	Expected: 1 or 2

- Glyph name: S	Contours detected: 15	Expected: 1

- Glyph name: T	Contours detected: 11	Expected: 1

- Glyph name: U	Contours detected: 15	Expected: 1

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Z	Contours detected: 15	Expected: 1

- Glyph name: bracketleft	Contours detected: 11	Expected: 1

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bracketright	Contours detected: 11	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: underscore	Contours detected: 6	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 14	Expected: 2

- Glyph name: b	Contours detected: 16	Expected: 2

- Glyph name: c	Contours detected: 11	Expected: 1

- Glyph name: d	Contours detected: 16	Expected: 2

- Glyph name: e	Contours detected: 14	Expected: 2

- Glyph name: f	Contours detected: 12	Expected: 1

- Glyph name: g	Contours detected: 18	Expected: 2 or 3

- Glyph name: h	Contours detected: 14	Expected: 1

- Glyph name: i	Contours detected: 9	Expected: 2

- Glyph name: j	Contours detected: 11	Expected: 2

- Glyph name: k	Contours detected: 13	Expected: 1 or 2

- Glyph name: l	Contours detected: 10	Expected: 1

- Glyph name: m	Contours detected: 14	Expected: 1

- Glyph name: n	Contours detected: 12	Expected: 1

- Glyph name: o	Contours detected: 12	Expected: 2

- Glyph name: p	Contours detected: 16	Expected: 2

- Glyph name: q	Contours detected: 16	Expected: 2

- Glyph name: r	Contours detected: 9	Expected: 1

- Glyph name: s	Contours detected: 13	Expected: 1

- Glyph name: t	Contours detected: 12	Expected: 1

- Glyph name: u	Contours detected: 12	Expected: 1

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 16	Expected: 1

- Glyph name: z	Contours detected: 13	Expected: 1

- Glyph name: braceleft	Contours detected: 10	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceright	Contours detected: 10	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: cent	Contours detected: 16	Expected: 1 or 2

- Glyph name: sterling	Contours detected: 15	Expected: 1 or 2

- Glyph name: currency	Contours detected: 12	Expected: 2

- Glyph name: yen	Contours detected: 13	Expected: 1 or 2

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: section	Contours detected: 20	Expected: 2

- Glyph name: copyright	Contours detected: 26	Expected: 3

- Glyph name: ordfeminine	Contours detected: 14	Expected: 2 or 3

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: logicalnot	Contours detected: 7	Expected: 1

- Glyph name: uni00AD	Contours detected: 4	Expected: 0

- Glyph name: registered	Contours detected: 30	Expected: 3 or 4

- Glyph name: macron	Contours detected: 3	Expected: 1

- Glyph name: degree	Contours detected: 8	Expected: 2

- Glyph name: plusminus	Contours detected: 14	Expected: 1 or 2

- Glyph name: twosuperior	Contours detected: 8	Expected: 1

- Glyph name: threesuperior	Contours detected: 8	Expected: 1

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: micro	Contours detected: 14	Expected: 1

- Glyph name: paragraph	Contours detected: 23	Expected: 1, 2 or 3

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: onesuperior	Contours detected: 8	Expected: 1

- Glyph name: ordmasculine	Contours detected: 12	Expected: 2 or 3

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: onequarter	Contours detected: 17	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 16	Expected: 3

- Glyph name: threequarters	Contours detected: 17	Expected: 3 or 4

- Glyph name: questiondown	Contours detected: 10	Expected: 2

- Glyph name: Agrave	Contours detected: 18	Expected: 3

- Glyph name: Aacute	Contours detected: 18	Expected: 3

- Glyph name: Acircumflex	Contours detected: 19	Expected: 3

- Glyph name: Atilde	Contours detected: 22	Expected: 3

- Glyph name: Adieresis	Contours detected: 18	Expected: 4

- Glyph name: Aring	Contours detected: 20	Expected: 3 or 4

- Glyph name: AE	Contours detected: 24	Expected: 2

- Glyph name: Ccedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Egrave	Contours detected: 20	Expected: 2

- Glyph name: Eacute	Contours detected: 20	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 21	Expected: 2

- Glyph name: Edieresis	Contours detected: 20	Expected: 3

- Glyph name: Igrave	Contours detected: 13	Expected: 2

- Glyph name: Iacute	Contours detected: 13	Expected: 2

- Glyph name: Icircumflex	Contours detected: 14	Expected: 2

- Glyph name: Idieresis	Contours detected: 13	Expected: 3

- Glyph name: Eth	Contours detected: 18	Expected: 2

- Glyph name: Ntilde	Contours detected: 23	Expected: 2

- Glyph name: Ograve	Contours detected: 18	Expected: 3

- Glyph name: Oacute	Contours detected: 18	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 19	Expected: 3

- Glyph name: Otilde	Contours detected: 22	Expected: 3

- Glyph name: Odieresis	Contours detected: 18	Expected: 4

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: Oslash	Contours detected: 17	Expected: 2 or 3

- Glyph name: Ugrave	Contours detected: 17	Expected: 2

- Glyph name: Uacute	Contours detected: 17	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 18	Expected: 2

- Glyph name: Udieresis	Contours detected: 17	Expected: 3

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Thorn	Contours detected: 16	Expected: 1 or 2

- Glyph name: germandbls	Contours detected: 16	Expected: 1

- Glyph name: agrave	Contours detected: 16	Expected: 3

- Glyph name: aacute	Contours detected: 16	Expected: 3

- Glyph name: acircumflex	Contours detected: 17	Expected: 3

- Glyph name: atilde	Contours detected: 20	Expected: 3

- Glyph name: adieresis	Contours detected: 16	Expected: 4

- Glyph name: aring	Contours detected: 18	Expected: 4

- Glyph name: ae	Contours detected: 18	Expected: 3

- Glyph name: ccedilla	Contours detected: 14	Expected: 1 or 2

- Glyph name: egrave	Contours detected: 16	Expected: 3

- Glyph name: eacute	Contours detected: 16	Expected: 3

- Glyph name: ecircumflex	Contours detected: 17	Expected: 3

- Glyph name: edieresis	Contours detected: 16	Expected: 4

- Glyph name: igrave	Contours detected: 10	Expected: 2

- Glyph name: iacute	Contours detected: 10	Expected: 2

- Glyph name: icircumflex	Contours detected: 11	Expected: 2

- Glyph name: idieresis	Contours detected: 10	Expected: 3

- Glyph name: eth	Contours detected: 16	Expected: 2

- Glyph name: ntilde	Contours detected: 18	Expected: 2

- Glyph name: ograve	Contours detected: 14	Expected: 3

- Glyph name: oacute	Contours detected: 14	Expected: 3

- Glyph name: ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: otilde	Contours detected: 18	Expected: 3

- Glyph name: odieresis	Contours detected: 14	Expected: 4

- Glyph name: divide	Contours detected: 7	Expected: 3

- Glyph name: oslash	Contours detected: 13	Expected: 3

- Glyph name: ugrave	Contours detected: 14	Expected: 2

- Glyph name: uacute	Contours detected: 14	Expected: 2

- Glyph name: ucircumflex	Contours detected: 15	Expected: 2

- Glyph name: udieresis	Contours detected: 14	Expected: 3

- Glyph name: yacute	Contours detected: 18	Expected: 2

- Glyph name: thorn	Contours detected: 18	Expected: 2

- Glyph name: ydieresis	Contours detected: 18	Expected: 3

- Glyph name: Amacron	Contours detected: 19	Expected: 3

- Glyph name: amacron	Contours detected: 17	Expected: 3

- Glyph name: Abreve	Contours detected: 21	Expected: 3

- Glyph name: abreve	Contours detected: 19	Expected: 3

- Glyph name: Aogonek	Contours detected: 19	Expected: 2 or 3

- Glyph name: aogonek	Contours detected: 17	Expected: 2

- Glyph name: Cacute	Contours detected: 15	Expected: 2

- Glyph name: cacute	Contours detected: 13	Expected: 2

- Glyph name: Ccircumflex	Contours detected: 16	Expected: 2

- Glyph name: ccircumflex	Contours detected: 14	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 14	Expected: 2

- Glyph name: cdotaccent	Contours detected: 12	Expected: 2

- Glyph name: Ccaron	Contours detected: 16	Expected: 2

- Glyph name: ccaron	Contours detected: 14	Expected: 2

- Glyph name: Dcaron	Contours detected: 19	Expected: 3

- Glyph name: dcaron	Contours detected: 18	Expected: 3

- Glyph name: Dcroat	Contours detected: 18	Expected: 2

- Glyph name: dcroat	Contours detected: 18	Expected: 2

- Glyph name: Emacron	Contours detected: 21	Expected: 2

- Glyph name: emacron	Contours detected: 17	Expected: 3

- Glyph name: Ebreve	Contours detected: 23	Expected: 2

- Glyph name: ebreve	Contours detected: 19	Expected: 3

- Glyph name: Edotaccent	Contours detected: 19	Expected: 2

- Glyph name: edotaccent	Contours detected: 15	Expected: 3

- Glyph name: Eogonek	Contours detected: 21	Expected: 1 or 2

- Glyph name: eogonek	Contours detected: 17	Expected: 2

- Glyph name: Ecaron	Contours detected: 21	Expected: 2

- Glyph name: ecaron	Contours detected: 17	Expected: 3

- Glyph name: Gcircumflex	Contours detected: 20	Expected: 2

- Glyph name: gcircumflex	Contours detected: 21	Expected: 3 or 4

- Glyph name: Gbreve	Contours detected: 22	Expected: 2

- Glyph name: gbreve	Contours detected: 23	Expected: 3 or 4

- Glyph name: Gdotaccent	Contours detected: 18	Expected: 2

- Glyph name: gdotaccent	Contours detected: 19	Expected: 3 or 4

- Glyph name: Gcommaaccent	Contours detected: 19	Expected: 2

- Glyph name: gcommaaccent	Contours detected: 20	Expected: 3 or 4

- Glyph name: Hcircumflex	Contours detected: 20	Expected: 2

- Glyph name: hcircumflex	Contours detected: 17	Expected: 2

- Glyph name: Hbar	Contours detected: 20	Expected: 2

- Glyph name: hbar	Contours detected: 16	Expected: 1

- Glyph name: Itilde	Contours detected: 17	Expected: 2

- Glyph name: itilde	Contours detected: 14	Expected: 2

- Glyph name: Imacron	Contours detected: 14	Expected: 2

- Glyph name: imacron	Contours detected: 11	Expected: 2

- Glyph name: Iogonek	Contours detected: 14	Expected: 1 or 2

- Glyph name: iogonek	Contours detected: 12	Expected: 2 or 3

- Glyph name: Idotaccent	Contours detected: 12	Expected: 2

- Glyph name: dotlessi	Contours detected: 8	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: ij	Contours detected: 19	Expected: 3 or 4

- Glyph name: Jcircumflex	Contours detected: 14	Expected: 2

- Glyph name: jcircumflex	Contours detected: 13	Expected: 2

- Glyph name: Kcommaaccent	Contours detected: 16	Expected: 2 or 3

- Glyph name: kcommaaccent	Contours detected: 15	Expected: 2 or 3

- Glyph name: kgreenlandic	Contours detected: 11	Expected: 1 or 2

- Glyph name: Lacute	Contours detected: 13	Expected: 2

- Glyph name: lacute	Contours detected: 12	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 12	Expected: 2

- Glyph name: Lcaron	Contours detected: 13	Expected: 2

- Glyph name: lcaron	Contours detected: 12	Expected: 2

- Glyph name: Ldot	Contours detected: 12	Expected: 2

- Glyph name: ldot	Contours detected: 11	Expected: 2

- Glyph name: Lslash	Contours detected: 13	Expected: 1

- Glyph name: lslash	Contours detected: 12	Expected: 1

- Glyph name: Nacute	Contours detected: 19	Expected: 2

- Glyph name: nacute	Contours detected: 14	Expected: 2

- Glyph name: Ncommaaccent	Contours detected: 19	Expected: 2

- Glyph name: ncommaaccent	Contours detected: 14	Expected: 2

- Glyph name: Ncaron	Contours detected: 20	Expected: 2

- Glyph name: ncaron	Contours detected: 15	Expected: 2

- Glyph name: napostrophe	Contours detected: 15	Expected: 2

- Glyph name: Eng	Contours detected: 19	Expected: 1

- Glyph name: eng	Contours detected: 15	Expected: 1

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: Ohungarumlaut	Contours detected: 20	Expected: 4

- Glyph name: ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: OE	Contours detected: 24	Expected: 2

- Glyph name: oe	Contours detected: 18	Expected: 3

- Glyph name: Racute	Contours detected: 20	Expected: 3

- Glyph name: racute	Contours detected: 11	Expected: 2

- Glyph name: Rcommaaccent	Contours detected: 20	Expected: 3

- Glyph name: rcommaaccent	Contours detected: 11	Expected: 2

- Glyph name: Rcaron	Contours detected: 21	Expected: 3

- Glyph name: rcaron	Contours detected: 12	Expected: 2

- Glyph name: Sacute	Contours detected: 17	Expected: 2

- Glyph name: sacute	Contours detected: 15	Expected: 2

- Glyph name: Scircumflex	Contours detected: 18	Expected: 2

- Glyph name: scircumflex	Contours detected: 16	Expected: 2

- Glyph name: Scedilla	Contours detected: 18	Expected: 1 or 2

- Glyph name: scedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Scaron	Contours detected: 18	Expected: 2

- Glyph name: scaron	Contours detected: 16	Expected: 2

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: Tcaron	Contours detected: 14	Expected: 2

- Glyph name: tcaron	Contours detected: 14	Expected: 2

- Glyph name: Utilde	Contours detected: 21	Expected: 2

- Glyph name: utilde	Contours detected: 18	Expected: 2

- Glyph name: Umacron	Contours detected: 18	Expected: 2

- Glyph name: umacron	Contours detected: 15	Expected: 2

- Glyph name: Ubreve	Contours detected: 20	Expected: 2

- Glyph name: ubreve	Contours detected: 17	Expected: 2

- Glyph name: Uring	Contours detected: 19	Expected: 3

- Glyph name: uring	Contours detected: 16	Expected: 3

- Glyph name: Uhungarumlaut	Contours detected: 19	Expected: 3

- Glyph name: uhungarumlaut	Contours detected: 16	Expected: 3

- Glyph name: Uogonek	Contours detected: 18	Expected: 1

- Glyph name: uogonek	Contours detected: 15	Expected: 1

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: ycircumflex	Contours detected: 19	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Zacute	Contours detected: 17	Expected: 2

- Glyph name: zacute	Contours detected: 15	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 16	Expected: 2

- Glyph name: zdotaccent	Contours detected: 14	Expected: 2

- Glyph name: Zcaron	Contours detected: 18	Expected: 2

- Glyph name: zcaron	Contours detected: 16	Expected: 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: florin	Contours detected: 14	Expected: 1

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: uni01CD	Contours detected: 19	Expected: 3

- Glyph name: uni01CE	Contours detected: 17	Expected: 3

- Glyph name: uni01CF	Contours detected: 14	Expected: 2

- Glyph name: uni01D0	Contours detected: 11	Expected: 2

- Glyph name: uni01D1	Contours detected: 19	Expected: 3

- Glyph name: uni01D2	Contours detected: 15	Expected: 3

- Glyph name: uni01D3	Contours detected: 18	Expected: 2

- Glyph name: uni01D4	Contours detected: 15	Expected: 2

- Glyph name: uni01D5	Contours detected: 18	Expected: 4

- Glyph name: uni01D6	Contours detected: 17	Expected: 4

- Glyph name: uni01D7	Contours detected: 15	Expected: 4

- Glyph name: uni01D8	Contours detected: 16	Expected: 4

- Glyph name: uni01D9	Contours detected: 16	Expected: 4

- Glyph name: uni01DA	Contours detected: 17	Expected: 4

- Glyph name: uni01DB	Contours detected: 15	Expected: 4

- Glyph name: uni01DC	Contours detected: 16	Expected: 4

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Scommaaccent	Contours detected: 17	Expected: 2

- Glyph name: scommaaccent	Contours detected: 15	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 14	Expected: 2

- Glyph name: jdotless	Contours detected: 10	Expected: 1

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: breve	Contours detected: 5	Expected: 1

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: ogonek	Contours detected: 3	Expected: 1

- Glyph name: tilde	Contours detected: 6	Expected: 1

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: gravecomb	Contours detected: 2	Expected: 1

- Glyph name: acutecomb	Contours detected: 2	Expected: 1

- Glyph name: circumflexcomb	Contours detected: 3	Expected: 1

- Glyph name: tildecomb	Contours detected: 6	Expected: 1

- Glyph name: macroncomb	Contours detected: 3	Expected: 1

- Glyph name: brevecomb	Contours detected: 5	Expected: 1

- Glyph name: hookabovecomb	Contours detected: 3	Expected: 1

- Glyph name: ringcomb	Contours detected: 4	Expected: 2

- Glyph name: hungarumlautcomb	Contours detected: 4	Expected: 2

- Glyph name: caroncomb	Contours detected: 3	Expected: 1

- Glyph name: commaturnedabovecomb	Contours detected: 2	Expected: 1

- Glyph name: horncomb	Contours detected: 3	Expected: 1

- Glyph name: commaaccentcomb	Contours detected: 2	Expected: 1

- Glyph name: cedillacomb	Contours detected: 3	Expected: 1

- Glyph name: ogonekcomb	Contours detected: 3	Expected: 1

- Glyph name: uni032E	Contours detected: 5	Expected: 1

- Glyph name: uni0331	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: baht	Contours detected: 20	Expected: 3 or 5

- Glyph name: uni1E0C	Contours detected: 17	Expected: 3

- Glyph name: uni1E0D	Contours detected: 17	Expected: 3

- Glyph name: uni1E0E	Contours detected: 19	Expected: 3

- Glyph name: uni1E0F	Contours detected: 19	Expected: 3

- Glyph name: uni1E20	Contours detected: 20	Expected: 2

- Glyph name: uni1E21	Contours detected: 21	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 18	Expected: 2

- Glyph name: uni1E25	Contours detected: 15	Expected: 2

- Glyph name: uni1E2A	Contours detected: 20	Expected: 2

- Glyph name: uni1E2B	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: uni1E44	Contours detected: 18	Expected: 2

- Glyph name: uni1E45	Contours detected: 13	Expected: 2

- Glyph name: uni1E46	Contours detected: 18	Expected: 2

- Glyph name: uni1E47	Contours detected: 13	Expected: 2

- Glyph name: uni1E48	Contours detected: 20	Expected: 2

- Glyph name: uni1E49	Contours detected: 15	Expected: 2

- Glyph name: uni1E5A	Contours detected: 19	Expected: 3

- Glyph name: uni1E5B	Contours detected: 10	Expected: 2

- Glyph name: uni1E5C	Contours detected: 22	Expected: 4

- Glyph name: uni1E5D	Contours detected: 13	Expected: 3

- Glyph name: uni1E5E	Contours detected: 21	Expected: 3

- Glyph name: uni1E5F	Contours detected: 12	Expected: 2

- Glyph name: uni1E60	Contours detected: 16	Expected: 2

- Glyph name: uni1E61	Contours detected: 14	Expected: 2

- Glyph name: uni1E62	Contours detected: 16	Expected: 2

- Glyph name: uni1E63	Contours detected: 14	Expected: 2

- Glyph name: uni1E6C	Contours detected: 12	Expected: 2

- Glyph name: uni1E6D	Contours detected: 13	Expected: 2

- Glyph name: uni1E6E	Contours detected: 14	Expected: 2

- Glyph name: uni1E6F	Contours detected: 15	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: uni1E92	Contours detected: 16	Expected: 2

- Glyph name: uni1E93	Contours detected: 14	Expected: 2

- Glyph name: uni1E97	Contours detected: 14	Expected: 3

- Glyph name: Germandbls	Contours detected: 18	Expected: 1

- Glyph name: Adotbelow	Contours detected: 17	Expected: 3

- Glyph name: adotbelow	Contours detected: 15	Expected: 3

- Glyph name: Ahookabove	Contours detected: 19	Expected: 3

- Glyph name: ahookabove	Contours detected: 17	Expected: 3

- Glyph name: Acircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: acircumflexacute	Contours detected: 19	Expected: 4

- Glyph name: Acircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: acircumflexgrave	Contours detected: 19	Expected: 4

- Glyph name: Acircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: acircumflexhookabove	Contours detected: 20	Expected: 4

- Glyph name: Acircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: acircumflextilde	Contours detected: 23	Expected: 4

- Glyph name: Acircumflexdotbelow	Contours detected: 20	Expected: 4

- Glyph name: acircumflexdotbelow	Contours detected: 18	Expected: 4

- Glyph name: Abreveacute	Contours detected: 19	Expected: 4

- Glyph name: abreveacute	Contours detected: 21	Expected: 4

- Glyph name: Abrevegrave	Contours detected: 19	Expected: 4

- Glyph name: abrevegrave	Contours detected: 21	Expected: 4

- Glyph name: Abrevehookabove	Contours detected: 20	Expected: 4

- Glyph name: abrevehookabove	Contours detected: 22	Expected: 4

- Glyph name: Abrevetilde	Contours detected: 23	Expected: 4

- Glyph name: abrevetilde	Contours detected: 25	Expected: 4

- Glyph name: Abrevedotbelow	Contours detected: 22	Expected: 4

- Glyph name: abrevedotbelow	Contours detected: 20	Expected: 4

- Glyph name: Edotbelow	Contours detected: 19	Expected: 2

- Glyph name: edotbelow	Contours detected: 15	Expected: 3

- Glyph name: Ehookabove	Contours detected: 21	Expected: 2

- Glyph name: ehookabove	Contours detected: 17	Expected: 3

- Glyph name: Etilde	Contours detected: 24	Expected: 2

- Glyph name: etilde	Contours detected: 20	Expected: 3

- Glyph name: Ecircumflexacute	Contours detected: 21	Expected: 3

- Glyph name: ecircumflexacute	Contours detected: 19	Expected: 4

- Glyph name: Ecircumflexgrave	Contours detected: 21	Expected: 3

- Glyph name: ecircumflexgrave	Contours detected: 19	Expected: 4

- Glyph name: Ecircumflexhookabove	Contours detected: 22	Expected: 3

- Glyph name: ecircumflexhookabove	Contours detected: 20	Expected: 4

- Glyph name: Ecircumflextilde	Contours detected: 25	Expected: 3

- Glyph name: ecircumflextilde	Contours detected: 23	Expected: 4

- Glyph name: Ecircumflexdotbelow	Contours detected: 22	Expected: 3

- Glyph name: ecircumflexdotbelow	Contours detected: 18	Expected: 4

- Glyph name: Ihookabove	Contours detected: 14	Expected: 2

- Glyph name: ihookabove	Contours detected: 11	Expected: 2

- Glyph name: Idotbelow	Contours detected: 12	Expected: 2

- Glyph name: idotbelow	Contours detected: 10	Expected: 3

- Glyph name: Odotbelow	Contours detected: 17	Expected: 3

- Glyph name: odotbelow	Contours detected: 13	Expected: 3

- Glyph name: Ohookabove	Contours detected: 19	Expected: 3

- Glyph name: ohookabove	Contours detected: 15	Expected: 3

- Glyph name: Ocircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: ocircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: Ocircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: ocircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: Ocircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: ocircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: Ocircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: ocircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: Ocircumflexdotbelow	Contours detected: 20	Expected: 4

- Glyph name: ocircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: Ohornacute	Contours detected: 21	Expected: 3 or 4

- Glyph name: ohornacute	Contours detected: 17	Expected: 3

- Glyph name: Ohorngrave	Contours detected: 21	Expected: 3 or 4

- Glyph name: ohorngrave	Contours detected: 17	Expected: 3

- Glyph name: Ohornhookabove	Contours detected: 22	Expected: 3 or 4

- Glyph name: ohornhookabove	Contours detected: 18	Expected: 3

- Glyph name: Ohorntilde	Contours detected: 25	Expected: 3 or 4

- Glyph name: ohorntilde	Contours detected: 21	Expected: 3

- Glyph name: Ohorndotbelow	Contours detected: 20	Expected: 3 or 4

- Glyph name: ohorndotbelow	Contours detected: 16	Expected: 3

- Glyph name: Udotbelow	Contours detected: 16	Expected: 2

- Glyph name: udotbelow	Contours detected: 13	Expected: 2

- Glyph name: Uhookabove	Contours detected: 18	Expected: 2

- Glyph name: uhookabove	Contours detected: 15	Expected: 2

- Glyph name: Uhornacute	Contours detected: 20	Expected: 2

- Glyph name: uhornacute	Contours detected: 17	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 20	Expected: 2

- Glyph name: uhorngrave	Contours detected: 17	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 21	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 18	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 24	Expected: 2

- Glyph name: uhorntilde	Contours detected: 21	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 19	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 16	Expected: 2

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: ygrave	Contours detected: 18	Expected: 2

- Glyph name: Ydotbelow	Contours detected: 11	Expected: 2

- Glyph name: ydotbelow	Contours detected: 13	Expected: 2

- Glyph name: Yhookabove	Contours detected: 13	Expected: 2

- Glyph name: yhookabove	Contours detected: 19	Expected: 2

- Glyph name: Ytilde	Contours detected: 16	Expected: 2

- Glyph name: ytilde	Contours detected: 22	Expected: 2

- Glyph name: uni2010	Contours detected: 4	Expected: 1

- Glyph name: uni2011	Contours detected: 4	Expected: 1

- Glyph name: figuredash	Contours detected: 5	Expected: 1

- Glyph name: endash	Contours detected: 5	Expected: 1

- Glyph name: emdash	Contours detected: 6	Expected: 1

- Glyph name: uni2015	Contours detected: 6	Expected: 1

- Glyph name: dblverticalbar	Contours detected: 14	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: dagger	Contours detected: 13	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 17	Expected: 1 or 3

- Glyph name: bullet	Contours detected: 9	Expected: 1

- Glyph name: perthousand	Contours detected: 17	Expected: 6 or 7

- Glyph name: minute	Contours detected: 3	Expected: 1

- Glyph name: second	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: uni2070	Contours detected: 8	Expected: 2 or 3

- Glyph name: foursuperior	Contours detected: 9	Expected: 1 or 2

- Glyph name: fivesuperior	Contours detected: 9	Expected: 1

- Glyph name: sixsuperior	Contours detected: 8	Expected: 2

- Glyph name: sevensuperior	Contours detected: 7	Expected: 1

- Glyph name: eightsuperior	Contours detected: 13	Expected: 3

- Glyph name: ninesuperior	Contours detected: 8	Expected: 2

- Glyph name: uni207D	Contours detected: 5	Expected: 1

- Glyph name: uni207E	Contours detected: 5	Expected: 1

- Glyph name: uni207F	Contours detected: 8	Expected: 1

- Glyph name: uni2080	Contours detected: 8	Expected: 2 or 3

- Glyph name: oneinferior	Contours detected: 8	Expected: 1

- Glyph name: twoinferior	Contours detected: 8	Expected: 1

- Glyph name: threeinferior	Contours detected: 8	Expected: 1

- Glyph name: fourinferior	Contours detected: 9	Expected: 1 or 2

- Glyph name: fiveinferior	Contours detected: 9	Expected: 1

- Glyph name: sixinferior	Contours detected: 8	Expected: 2

- Glyph name: seveninferior	Contours detected: 7	Expected: 1

- Glyph name: eightinferior	Contours detected: 13	Expected: 3

- Glyph name: nineinferior	Contours detected: 8	Expected: 2

- Glyph name: uni208D	Contours detected: 5	Expected: 1

- Glyph name: uni208E	Contours detected: 5	Expected: 1

- Glyph name: colonmonetary	Contours detected: 16	Expected: 1 or 3

- Glyph name: lira	Contours detected: 17	Expected: 1

- Glyph name: naira	Contours detected: 26	Expected: 1, 3 or 5

- Glyph name: peseta	Contours detected: 26	Expected: 2, 3 or 4

- Glyph name: rupee	Contours detected: 23	Expected: 3

- Glyph name: won	Contours detected: 26	Expected: 1, 3, 4 or 7

- Glyph name: sheqel	Contours detected: 24	Expected: 2

- Glyph name: dong	Contours detected: 23	Expected: 3 or 4

- Glyph name: Euro	Contours detected: 15	Expected: 1 or 2

- Glyph name: kip	Contours detected: 17	Expected: 1

- Glyph name: tugrik	Contours detected: 15	Expected: 1

- Glyph name: peso	Contours detected: 15	Expected: 1, 2 or 4

- Glyph name: guarani	Contours detected: 19	Expected: 1, 2 or 3

- Glyph name: hryvnia	Contours detected: 17	Expected: 1 or 2

- Glyph name: cedi	Contours detected: 16	Expected: 1 or 2

- Glyph name: tenge	Contours detected: 14	Expected: 2

- Glyph name: rupeeIndian	Contours detected: 17	Expected: 1

- Glyph name: liraTurkish	Contours detected: 15	Expected: 1

- Glyph name: manat	Contours detected: 17	Expected: 1

- Glyph name: ruble	Contours detected: 16	Expected: 2

- Glyph name: bitcoin	Contours detected: 20	Expected: 3

- Glyph name: literSign	Contours detected: 13	Expected: 2

- Glyph name: numero	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2117	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 18	Expected: 2

- Glyph name: trademark	Contours detected: 18	Expected: 2

- Glyph name: Ohm	Contours detected: 17	Expected: 1

- Glyph name: onethird	Contours detected: 16	Expected: 3

- Glyph name: twothirds	Contours detected: 16	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 21	Expected: 5

- Glyph name: threeeighths	Contours detected: 21	Expected: 5

- Glyph name: fiveeighths	Contours detected: 22	Expected: 5

- Glyph name: seveneighths	Contours detected: 20	Expected: 5

- Glyph name: arrowleft	Contours detected: 11	Expected: 1

- Glyph name: arrowup	Contours detected: 11	Expected: 1

- Glyph name: arrowright	Contours detected: 11	Expected: 1

- Glyph name: arrowdown	Contours detected: 11	Expected: 1

- Glyph name: arrowboth	Contours detected: 15	Expected: 1

- Glyph name: arrowupdn	Contours detected: 15	Expected: 1

- Glyph name: northWestArrow	Contours detected: 12	Expected: 1

- Glyph name: northEastArrow	Contours detected: 12	Expected: 1

- Glyph name: southEastArrow	Contours detected: 12	Expected: 1

- Glyph name: southWestArrow	Contours detected: 12	Expected: 1

- Glyph name: partialdiff	Contours detected: 15	Expected: 2

- Glyph name: emptyset	Contours detected: 21	Expected: 3

- Glyph name: increment	Contours detected: 15	Expected: 2

- Glyph name: product	Contours detected: 21	Expected: 1

- Glyph name: summation	Contours detected: 17	Expected: 1

- Glyph name: minus	Contours detected: 5	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 11	Expected: 1

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: approxequal	Contours detected: 12	Expected: 2

- Glyph name: notequal	Contours detected: 15	Expected: 1

- Glyph name: lessequal	Contours detected: 8	Expected: 2

- Glyph name: greaterequal	Contours detected: 8	Expected: 2

- Glyph name: filledbox	Contours detected: 42	Expected: 1

- Glyph name: whiteSquare	Contours detected: 24	Expected: 2

- Glyph name: blackSmallSquare	Contours detected: 9	Expected: 1

- Glyph name: whiteSmallSquare	Contours detected: 8	Expected: 2

- Glyph name: triagup	Contours detected: 31	Expected: 1

- Glyph name: upWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: rightBlackTriangle	Contours detected: 31	Expected: 1

- Glyph name: rightWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: triagdn	Contours detected: 31	Expected: 1

- Glyph name: downWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: leftBlackTriangle	Contours detected: 31	Expected: 1

- Glyph name: leftWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: blackDiamond	Contours detected: 25	Expected: 1

- Glyph name: whiteDiamond	Contours detected: 12	Expected: 2

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: circle	Contours detected: 16	Expected: 2

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: blackCircle	Contours detected: 37	Expected: 1

- Glyph name: leftanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: rightanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: uniFB01	Contours detected: 16	Expected: 1, 2 or 3

- Glyph name: uniFB02	Contours detected: 17	Expected: 1 or 2

- Glyph name: A	Contours detected: 16	Expected: 2

- Glyph name: AE	Contours detected: 24	Expected: 2

- Glyph name: Aacute	Contours detected: 18	Expected: 3

- Glyph name: Abreve	Contours detected: 21	Expected: 3

- Glyph name: Acircumflex	Contours detected: 19	Expected: 3

- Glyph name: Adieresis	Contours detected: 18	Expected: 4

- Glyph name: Agrave	Contours detected: 18	Expected: 3

- Glyph name: Amacron	Contours detected: 19	Expected: 3

- Glyph name: Aogonek	Contours detected: 19	Expected: 2 or 3

- Glyph name: Aring	Contours detected: 20	Expected: 3 or 4

- Glyph name: Atilde	Contours detected: 22	Expected: 3

- Glyph name: B	Contours detected: 20	Expected: 2 or 3

- Glyph name: C	Contours detected: 13	Expected: 1

- Glyph name: Cacute	Contours detected: 15	Expected: 2

- Glyph name: Ccaron	Contours detected: 16	Expected: 2

- Glyph name: Ccedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Ccircumflex	Contours detected: 16	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 14	Expected: 2

- Glyph name: D	Contours detected: 16	Expected: 2

- Glyph name: Dcaron	Contours detected: 19	Expected: 3

- Glyph name: Dcroat	Contours detected: 18	Expected: 2

- Glyph name: E	Contours detected: 18	Expected: 1

- Glyph name: Eacute	Contours detected: 20	Expected: 2

- Glyph name: Ebreve	Contours detected: 23	Expected: 2

- Glyph name: Ecaron	Contours detected: 21	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 21	Expected: 2

- Glyph name: Edieresis	Contours detected: 20	Expected: 3

- Glyph name: Edotaccent	Contours detected: 19	Expected: 2

- Glyph name: Egrave	Contours detected: 20	Expected: 2

- Glyph name: Emacron	Contours detected: 21	Expected: 2

- Glyph name: Eng	Contours detected: 19	Expected: 1

- Glyph name: Eogonek	Contours detected: 21	Expected: 1 or 2

- Glyph name: Eth	Contours detected: 18	Expected: 2

- Glyph name: Euro	Contours detected: 15	Expected: 1 or 2

- Glyph name: F	Contours detected: 14	Expected: 1

- Glyph name: G	Contours detected: 17	Expected: 1

- Glyph name: Gbreve	Contours detected: 22	Expected: 2

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: Gcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Gdotaccent	Contours detected: 18	Expected: 2

- Glyph name: H	Contours detected: 17	Expected: 1

- Glyph name: Hbar	Contours detected: 20	Expected: 2

- Glyph name: Hcircumflex	Contours detected: 20	Expected: 2

- Glyph name: I	Contours detected: 11	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: Iacute	Contours detected: 13	Expected: 2

- Glyph name: Icircumflex	Contours detected: 14	Expected: 2

- Glyph name: Idieresis	Contours detected: 13	Expected: 3

- Glyph name: Idotaccent	Contours detected: 12	Expected: 2

- Glyph name: Igrave	Contours detected: 13	Expected: 2

- Glyph name: Imacron	Contours detected: 14	Expected: 2

- Glyph name: Iogonek	Contours detected: 14	Expected: 1 or 2

- Glyph name: Itilde	Contours detected: 17	Expected: 2

- Glyph name: J	Contours detected: 11	Expected: 1

- Glyph name: Jcircumflex	Contours detected: 14	Expected: 2

- Glyph name: K	Contours detected: 14	Expected: 1 or 2

- Glyph name: L	Contours detected: 11	Expected: 1

- Glyph name: Lacute	Contours detected: 13	Expected: 2

- Glyph name: Lcaron	Contours detected: 13	Expected: 2

- Glyph name: Ldot	Contours detected: 12	Expected: 2

- Glyph name: Lslash	Contours detected: 13	Expected: 1

- Glyph name: M	Contours detected: 18	Expected: 1

- Glyph name: N	Contours detected: 17	Expected: 1

- Glyph name: Nacute	Contours detected: 19	Expected: 2

- Glyph name: Ncaron	Contours detected: 20	Expected: 2

- Glyph name: Ntilde	Contours detected: 23	Expected: 2

- Glyph name: O	Contours detected: 16	Expected: 2

- Glyph name: OE	Contours detected: 24	Expected: 2

- Glyph name: Oacute	Contours detected: 18	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 19	Expected: 3

- Glyph name: Odieresis	Contours detected: 18	Expected: 4

- Glyph name: Ograve	Contours detected: 18	Expected: 3

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: Ohungarumlaut	Contours detected: 20	Expected: 4

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: Oslash	Contours detected: 17	Expected: 2 or 3

- Glyph name: Otilde	Contours detected: 22	Expected: 3

- Glyph name: P	Contours detected: 15	Expected: 1 or 2

- Glyph name: Q	Contours detected: 17	Expected: 2

- Glyph name: R	Contours detected: 18	Expected: 1 or 2

- Glyph name: Racute	Contours detected: 20	Expected: 3

- Glyph name: Rcaron	Contours detected: 21	Expected: 3

- Glyph name: S	Contours detected: 15	Expected: 1

- Glyph name: Sacute	Contours detected: 17	Expected: 2

- Glyph name: Scaron	Contours detected: 18	Expected: 2

- Glyph name: Scircumflex	Contours detected: 18	Expected: 2

- Glyph name: T	Contours detected: 11	Expected: 1

- Glyph name: Tcaron	Contours detected: 14	Expected: 2

- Glyph name: Thorn	Contours detected: 16	Expected: 1 or 2

- Glyph name: U	Contours detected: 15	Expected: 1

- Glyph name: Uacute	Contours detected: 17	Expected: 2

- Glyph name: Ubreve	Contours detected: 20	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 18	Expected: 2

- Glyph name: Udieresis	Contours detected: 17	Expected: 3

- Glyph name: Ugrave	Contours detected: 17	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: Uhungarumlaut	Contours detected: 19	Expected: 3

- Glyph name: Umacron	Contours detected: 18	Expected: 2

- Glyph name: Uogonek	Contours detected: 18	Expected: 1

- Glyph name: Uring	Contours detected: 19	Expected: 3

- Glyph name: Utilde	Contours detected: 21	Expected: 2

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: Z	Contours detected: 15	Expected: 1

- Glyph name: Zacute	Contours detected: 17	Expected: 2

- Glyph name: Zcaron	Contours detected: 18	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 16	Expected: 2

- Glyph name: a	Contours detected: 14	Expected: 2

- Glyph name: aacute	Contours detected: 16	Expected: 3

- Glyph name: abreve	Contours detected: 19	Expected: 3

- Glyph name: acircumflex	Contours detected: 17	Expected: 3

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: adieresis	Contours detected: 16	Expected: 4

- Glyph name: ae	Contours detected: 18	Expected: 3

- Glyph name: agrave	Contours detected: 16	Expected: 3

- Glyph name: amacron	Contours detected: 17	Expected: 3

- Glyph name: ampersand	Contours detected: 14	Expected: 1, 2 or 3

- Glyph name: aogonek	Contours detected: 17	Expected: 2

- Glyph name: approxequal	Contours detected: 12	Expected: 2

- Glyph name: aring	Contours detected: 18	Expected: 4

- Glyph name: arrowboth	Contours detected: 15	Expected: 1

- Glyph name: arrowdown	Contours detected: 11	Expected: 1

- Glyph name: arrowup	Contours detected: 11	Expected: 1

- Glyph name: arrowupdn	Contours detected: 15	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 11	Expected: 1 or 4

- Glyph name: at	Contours detected: 20	Expected: 2

- Glyph name: atilde	Contours detected: 20	Expected: 3

- Glyph name: b	Contours detected: 16	Expected: 2

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceleft	Contours detected: 10	Expected: 1

- Glyph name: braceright	Contours detected: 10	Expected: 1

- Glyph name: bracketleft	Contours detected: 11	Expected: 1

- Glyph name: bracketright	Contours detected: 11	Expected: 1

- Glyph name: breve	Contours detected: 5	Expected: 1

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: bullet	Contours detected: 9	Expected: 1

- Glyph name: c	Contours detected: 11	Expected: 1

- Glyph name: cacute	Contours detected: 13	Expected: 2

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: ccaron	Contours detected: 14	Expected: 2

- Glyph name: ccedilla	Contours detected: 14	Expected: 1 or 2

- Glyph name: ccircumflex	Contours detected: 14	Expected: 2

- Glyph name: cdotaccent	Contours detected: 12	Expected: 2

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: cent	Contours detected: 16	Expected: 1 or 2

- Glyph name: circle	Contours detected: 16	Expected: 2

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: colonmonetary	Contours detected: 16	Expected: 1 or 3

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: copyright	Contours detected: 26	Expected: 3

- Glyph name: currency	Contours detected: 12	Expected: 2

- Glyph name: d	Contours detected: 16	Expected: 2

- Glyph name: dagger	Contours detected: 13	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 17	Expected: 1 or 3

- Glyph name: dcaron	Contours detected: 18	Expected: 3

- Glyph name: dcroat	Contours detected: 18	Expected: 2

- Glyph name: degree	Contours detected: 8	Expected: 2

- Glyph name: divide	Contours detected: 7	Expected: 3

- Glyph name: dollar	Contours detected: 17	Expected: 1, 3 or 5

- Glyph name: dong	Contours detected: 23	Expected: 3 or 4

- Glyph name: dotlessi	Contours detected: 8	Expected: 1

- Glyph name: e	Contours detected: 14	Expected: 2

- Glyph name: eacute	Contours detected: 16	Expected: 3

- Glyph name: ebreve	Contours detected: 19	Expected: 3

- Glyph name: ecaron	Contours detected: 17	Expected: 3

- Glyph name: ecircumflex	Contours detected: 17	Expected: 3

- Glyph name: edieresis	Contours detected: 16	Expected: 4

- Glyph name: edotaccent	Contours detected: 15	Expected: 3

- Glyph name: egrave	Contours detected: 16	Expected: 3

- Glyph name: eight	Contours detected: 17	Expected: 3

- Glyph name: emacron	Contours detected: 17	Expected: 3

- Glyph name: emdash	Contours detected: 6	Expected: 1

- Glyph name: emptyset	Contours detected: 21	Expected: 3

- Glyph name: endash	Contours detected: 5	Expected: 1

- Glyph name: eng	Contours detected: 15	Expected: 1

- Glyph name: eogonek	Contours detected: 17	Expected: 2

- Glyph name: equal	Contours detected: 10	Expected: 2

- Glyph name: eth	Contours detected: 16	Expected: 2

- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: f	Contours detected: 12	Expected: 1

- Glyph name: figuredash	Contours detected: 5	Expected: 1

- Glyph name: five	Contours detected: 17	Expected: 1

- Glyph name: fiveeighths	Contours detected: 22	Expected: 5

- Glyph name: four	Contours detected: 14	Expected: 1 or 2

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: g	Contours detected: 18	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 23	Expected: 3 or 4

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 21	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 19	Expected: 3 or 4

- Glyph name: germandbls	Contours detected: 16	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: greaterequal	Contours detected: 8	Expected: 2

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: h	Contours detected: 14	Expected: 1

- Glyph name: hbar	Contours detected: 16	Expected: 1

- Glyph name: hcircumflex	Contours detected: 17	Expected: 2

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: hyphen	Contours detected: 4	Expected: 1

- Glyph name: i	Contours detected: 9	Expected: 2

- Glyph name: iacute	Contours detected: 10	Expected: 2

- Glyph name: icircumflex	Contours detected: 11	Expected: 2

- Glyph name: idieresis	Contours detected: 10	Expected: 3

- Glyph name: igrave	Contours detected: 10	Expected: 2

- Glyph name: ij	Contours detected: 19	Expected: 3 or 4

- Glyph name: imacron	Contours detected: 11	Expected: 2

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: iogonek	Contours detected: 12	Expected: 2 or 3

- Glyph name: itilde	Contours detected: 14	Expected: 2

- Glyph name: j	Contours detected: 11	Expected: 2

- Glyph name: jcircumflex	Contours detected: 13	Expected: 2

- Glyph name: k	Contours detected: 13	Expected: 1 or 2

- Glyph name: kgreenlandic	Contours detected: 11	Expected: 1 or 2

- Glyph name: l	Contours detected: 10	Expected: 1

- Glyph name: lacute	Contours detected: 12	Expected: 2

- Glyph name: lcaron	Contours detected: 12	Expected: 2

- Glyph name: ldot	Contours detected: 11	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: lessequal	Contours detected: 8	Expected: 2

- Glyph name: lira	Contours detected: 17	Expected: 1

- Glyph name: logicalnot	Contours detected: 7	Expected: 1

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: lslash	Contours detected: 12	Expected: 1

- Glyph name: m	Contours detected: 14	Expected: 1

- Glyph name: macron	Contours detected: 3	Expected: 1

- Glyph name: minus	Contours detected: 5	Expected: 1

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: n	Contours detected: 12	Expected: 1

- Glyph name: nacute	Contours detected: 14	Expected: 2

- Glyph name: napostrophe	Contours detected: 15	Expected: 2

- Glyph name: ncaron	Contours detected: 15	Expected: 2

- Glyph name: nine	Contours detected: 15	Expected: 1 or 2

- Glyph name: notequal	Contours detected: 15	Expected: 1

- Glyph name: ntilde	Contours detected: 18	Expected: 2

- Glyph name: numbersign	Contours detected: 20	Expected: 2

- Glyph name: o	Contours detected: 12	Expected: 2

- Glyph name: oacute	Contours detected: 14	Expected: 3

- Glyph name: ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: odieresis	Contours detected: 14	Expected: 4

- Glyph name: oe	Contours detected: 18	Expected: 3

- Glyph name: ogonek	Contours detected: 3	Expected: 1

- Glyph name: ograve	Contours detected: 14	Expected: 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: one	Contours detected: 10	Expected: 1

- Glyph name: oneeighth	Contours detected: 21	Expected: 5

- Glyph name: onehalf	Contours detected: 16	Expected: 3

- Glyph name: onequarter	Contours detected: 17	Expected: 3 or 4

- Glyph name: onethird	Contours detected: 16	Expected: 3

- Glyph name: ordfeminine	Contours detected: 14	Expected: 2 or 3

- Glyph name: ordmasculine	Contours detected: 12	Expected: 2 or 3

- Glyph name: oslash	Contours detected: 13	Expected: 3

- Glyph name: otilde	Contours detected: 18	Expected: 3

- Glyph name: p	Contours detected: 16	Expected: 2

- Glyph name: paragraph	Contours detected: 23	Expected: 1, 2 or 3

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: partialdiff	Contours detected: 15	Expected: 2

- Glyph name: percent	Contours detected: 13	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 17	Expected: 6 or 7

- Glyph name: peseta	Contours detected: 26	Expected: 2, 3 or 4

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: plus	Contours detected: 9	Expected: 1

- Glyph name: plusminus	Contours detected: 14	Expected: 1 or 2

- Glyph name: product	Contours detected: 21	Expected: 1

- Glyph name: q	Contours detected: 16	Expected: 2

- Glyph name: question	Contours detected: 10	Expected: 2

- Glyph name: questiondown	Contours detected: 10	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: r	Contours detected: 9	Expected: 1

- Glyph name: racute	Contours detected: 11	Expected: 2

- Glyph name: radical	Contours detected: 11	Expected: 1

- Glyph name: rcaron	Contours detected: 12	Expected: 2

- Glyph name: registered	Contours detected: 30	Expected: 3 or 4

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: rupee	Contours detected: 23	Expected: 3

- Glyph name: s	Contours detected: 13	Expected: 1

- Glyph name: sacute	Contours detected: 15	Expected: 2

- Glyph name: scaron	Contours detected: 16	Expected: 2

- Glyph name: scircumflex	Contours detected: 16	Expected: 2

- Glyph name: section	Contours detected: 20	Expected: 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: seven	Contours detected: 11	Expected: 1

- Glyph name: seveneighths	Contours detected: 20	Expected: 5

- Glyph name: six	Contours detected: 15	Expected: 1 or 2

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: sterling	Contours detected: 15	Expected: 1 or 2

- Glyph name: summation	Contours detected: 17	Expected: 1

- Glyph name: t	Contours detected: 12	Expected: 1

- Glyph name: tcaron	Contours detected: 14	Expected: 2

- Glyph name: thorn	Contours detected: 18	Expected: 2

- Glyph name: three	Contours detected: 14	Expected: 1

- Glyph name: threeeighths	Contours detected: 21	Expected: 5

- Glyph name: threequarters	Contours detected: 17	Expected: 3 or 4

- Glyph name: tilde	Contours detected: 6	Expected: 1

- Glyph name: trademark	Contours detected: 18	Expected: 2

- Glyph name: triagdn	Contours detected: 31	Expected: 1

- Glyph name: triagup	Contours detected: 31	Expected: 1

- Glyph name: two	Contours detected: 15	Expected: 1

- Glyph name: twothirds	Contours detected: 16	Expected: 1 or 3

- Glyph name: u	Contours detected: 12	Expected: 1

- Glyph name: uacute	Contours detected: 14	Expected: 2

- Glyph name: ubreve	Contours detected: 17	Expected: 2

- Glyph name: ucircumflex	Contours detected: 15	Expected: 2

- Glyph name: udieresis	Contours detected: 14	Expected: 3

- Glyph name: ugrave	Contours detected: 14	Expected: 2

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: uhungarumlaut	Contours detected: 16	Expected: 3

- Glyph name: umacron	Contours detected: 15	Expected: 2

- Glyph name: underscore	Contours detected: 6	Expected: 1

- Glyph name: uni00AD	Contours detected: 4	Expected: 0

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: uni01CD	Contours detected: 19	Expected: 3

- Glyph name: uni01CE	Contours detected: 17	Expected: 3

- Glyph name: uni01CF	Contours detected: 14	Expected: 2

- Glyph name: uni01D0	Contours detected: 11	Expected: 2

- Glyph name: uni01D1	Contours detected: 19	Expected: 3

- Glyph name: uni01D2	Contours detected: 15	Expected: 3

- Glyph name: uni01D3	Contours detected: 18	Expected: 2

- Glyph name: uni01D4	Contours detected: 15	Expected: 2

- Glyph name: uni01D5	Contours detected: 18	Expected: 4

- Glyph name: uni01D6	Contours detected: 17	Expected: 4

- Glyph name: uni01D7	Contours detected: 15	Expected: 4

- Glyph name: uni01D8	Contours detected: 16	Expected: 4

- Glyph name: uni01D9	Contours detected: 16	Expected: 4

- Glyph name: uni01DA	Contours detected: 17	Expected: 4

- Glyph name: uni01DB	Contours detected: 15	Expected: 4

- Glyph name: uni01DC	Contours detected: 16	Expected: 4

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni032E	Contours detected: 5	Expected: 1

- Glyph name: uni0331	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: uni1E0C	Contours detected: 17	Expected: 3

- Glyph name: uni1E0D	Contours detected: 17	Expected: 3

- Glyph name: uni1E0E	Contours detected: 19	Expected: 3

- Glyph name: uni1E0F	Contours detected: 19	Expected: 3

- Glyph name: uni1E20	Contours detected: 20	Expected: 2

- Glyph name: uni1E21	Contours detected: 21	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 18	Expected: 2

- Glyph name: uni1E25	Contours detected: 15	Expected: 2

- Glyph name: uni1E2A	Contours detected: 20	Expected: 2

- Glyph name: uni1E2B	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: uni1E44	Contours detected: 18	Expected: 2

- Glyph name: uni1E45	Contours detected: 13	Expected: 2

- Glyph name: uni1E46	Contours detected: 18	Expected: 2

- Glyph name: uni1E47	Contours detected: 13	Expected: 2

- Glyph name: uni1E48	Contours detected: 20	Expected: 2

- Glyph name: uni1E49	Contours detected: 15	Expected: 2

- Glyph name: uni1E5A	Contours detected: 19	Expected: 3

- Glyph name: uni1E5B	Contours detected: 10	Expected: 2

- Glyph name: uni1E5C	Contours detected: 22	Expected: 4

- Glyph name: uni1E5D	Contours detected: 13	Expected: 3

- Glyph name: uni1E5E	Contours detected: 21	Expected: 3

- Glyph name: uni1E5F	Contours detected: 12	Expected: 2

- Glyph name: uni1E60	Contours detected: 16	Expected: 2

- Glyph name: uni1E61	Contours detected: 14	Expected: 2

- Glyph name: uni1E62	Contours detected: 16	Expected: 2

- Glyph name: uni1E63	Contours detected: 14	Expected: 2

- Glyph name: uni1E6C	Contours detected: 12	Expected: 2

- Glyph name: uni1E6D	Contours detected: 13	Expected: 2

- Glyph name: uni1E6E	Contours detected: 14	Expected: 2

- Glyph name: uni1E6F	Contours detected: 15	Expected: 2

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: uni1E92	Contours detected: 16	Expected: 2

- Glyph name: uni1E93	Contours detected: 14	Expected: 2

- Glyph name: uni1E97	Contours detected: 14	Expected: 3

- Glyph name: uni2010	Contours detected: 4	Expected: 1

- Glyph name: uni2011	Contours detected: 4	Expected: 1

- Glyph name: uni2015	Contours detected: 6	Expected: 1

- Glyph name: uni2117	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 18	Expected: 2

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 15	Expected: 1

- Glyph name: uring	Contours detected: 16	Expected: 3

- Glyph name: utilde	Contours detected: 18	Expected: 2

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 16	Expected: 1

- Glyph name: yacute	Contours detected: 18	Expected: 2

- Glyph name: ycircumflex	Contours detected: 19	Expected: 2

- Glyph name: ydieresis	Contours detected: 18	Expected: 3

- Glyph name: yen	Contours detected: 13	Expected: 1 or 2

- Glyph name: ygrave	Contours detected: 18	Expected: 2

- Glyph name: z	Contours detected: 13	Expected: 1

- Glyph name: zacute	Contours detected: 15	Expected: 2

- Glyph name: zcaron	Contours detected: 16	Expected: 2

- Glyph name: zdotaccent	Contours detected: 14	Expected: 2

- Glyph name: zero	Contours detected: 19	Expected: 2 or 3
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



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

<details><summary>[11] MatrixSansVideo-Regular.ttf</summary>
<div>
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

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: Scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: ohornacute	Contours detected: 4	Expected: 3

- Glyph name: ohorngrave	Contours detected: 4	Expected: 3

- Glyph name: ohornhookabove	Contours detected: 4	Expected: 3

- Glyph name: ohorntilde	Contours detected: 4	Expected: 3

- Glyph name: ohorndotbelow	Contours detected: 4	Expected: 3

- Glyph name: Uhornacute	Contours detected: 3	Expected: 2

- Glyph name: uhornacute	Contours detected: 3	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 3	Expected: 2

- Glyph name: uhorntilde	Contours detected: 3	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 3	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 3	Expected: 2

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: won	Contours detected: 5	Expected: 1, 3, 4 or 7

- Glyph name: peso	Contours detected: 3	Expected: 1, 2 or 4

- Glyph name: onethird	Contours detected: 2	Expected: 3

- Glyph name: twothirds	Contours detected: 2	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 4	Expected: 5

- Glyph name: threeeighths	Contours detected: 4	Expected: 5

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

- Glyph name: seveneighths	Contours detected: 4	Expected: 5

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

- Glyph name: ohorn	Contours detected: 3	Expected: 2

- Glyph name: oneeighth	Contours detected: 4	Expected: 5

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: onethird	Contours detected: 2	Expected: 3

- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: seveneighths	Contours detected: 4	Expected: 5

- Glyph name: threeeighths	Contours detected: 4	Expected: 5

- Glyph name: twothirds	Contours detected: 2	Expected: 1 or 3

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 3	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Heiltsuk (Latn, 300 speakers), Ekpeye (Latn, 226,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ejagham (Latn, 120,000 speakers), Mango (Latn, 77,000 speakers), Ma’di (Latn, 584,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Dan (Latn, 1,099,244 speakers), Mfumte (Latn, 79,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Makaa (Latn, 221,000 speakers), Kaska (Latn, 125 speakers), Belarusian (Cyrl, 10,064,517 speakers), Fur (Latn, 1,230,163 speakers), Aghem (Latn, 38,843 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Teke-Ebo (Latn, 260,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Yala (Latn, 200,000 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Lugbara (Latn, 2,200,000 speakers), Gulay (Latn, 250,478 speakers), Nateni (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), South Central Banda (Latn, 244,000 speakers), Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Han (Latn, 6 speakers).</p>
 [code: soft-dotted]



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

<details><summary>[10] MatrixSansRaster-Regular.ttf</summary>
<div>
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

- Glyph name: plus	Contours detected: 5	Expected: 1

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: zero	Contours detected: 13	Expected: 2 or 3

- Glyph name: one	Contours detected: 7	Expected: 1

- Glyph name: two	Contours detected: 8	Expected: 1

- Glyph name: three	Contours detected: 9	Expected: 1

- Glyph name: four	Contours detected: 9	Expected: 1 or 2

- Glyph name: five	Contours detected: 8	Expected: 1

- Glyph name: six	Contours detected: 9	Expected: 1 or 2

- Glyph name: seven	Contours detected: 7	Expected: 1

- Glyph name: eight	Contours detected: 11	Expected: 3

- Glyph name: nine	Contours detected: 9	Expected: 1 or 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: question	Contours detected: 7	Expected: 2

- Glyph name: at	Contours detected: 12	Expected: 2

- Glyph name: A	Contours detected: 12	Expected: 2

- Glyph name: B	Contours detected: 11	Expected: 2 or 3

- Glyph name: C	Contours detected: 9	Expected: 1

- Glyph name: D	Contours detected: 12	Expected: 2

- Glyph name: E	Contours detected: 7	Expected: 1

- Glyph name: F	Contours detected: 7	Expected: 1

- Glyph name: G	Contours detected: 11	Expected: 1

- Glyph name: H	Contours detected: 13	Expected: 1

- Glyph name: I	Contours detected: 7	Expected: 1

- Glyph name: J	Contours detected: 8	Expected: 1

- Glyph name: K	Contours detected: 13	Expected: 1 or 2

- Glyph name: L	Contours detected: 7	Expected: 1

- Glyph name: M	Contours detected: 16	Expected: 1

- Glyph name: N	Contours detected: 15	Expected: 1

- Glyph name: O	Contours detected: 12	Expected: 2

- Glyph name: P	Contours detected: 9	Expected: 1 or 2

- Glyph name: Q	Contours detected: 14	Expected: 2

- Glyph name: R	Contours detected: 12	Expected: 1 or 2

- Glyph name: S	Contours detected: 9	Expected: 1

- Glyph name: T	Contours detected: 7	Expected: 1

- Glyph name: U	Contours detected: 13	Expected: 1

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Z	Contours detected: 7	Expected: 1

- Glyph name: bracketleft	Contours detected: 7	Expected: 1

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bracketright	Contours detected: 7	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 6	Expected: 2

- Glyph name: b	Contours detected: 12	Expected: 2

- Glyph name: c	Contours detected: 7	Expected: 1

- Glyph name: d	Contours detected: 12	Expected: 2

- Glyph name: e	Contours detected: 6	Expected: 2

- Glyph name: f	Contours detected: 8	Expected: 1

- Glyph name: g	Contours detected: 12	Expected: 2 or 3

- Glyph name: h	Contours detected: 12	Expected: 1

- Glyph name: i	Contours detected: 6	Expected: 2

- Glyph name: j	Contours detected: 9	Expected: 2

- Glyph name: k	Contours detected: 11	Expected: 1 or 2

- Glyph name: l	Contours detected: 7	Expected: 1

- Glyph name: m	Contours detected: 13	Expected: 1

- Glyph name: n	Contours detected: 10	Expected: 1

- Glyph name: o	Contours detected: 8	Expected: 2

- Glyph name: p	Contours detected: 12	Expected: 2

- Glyph name: q	Contours detected: 12	Expected: 2

- Glyph name: r	Contours detected: 7	Expected: 1

- Glyph name: s	Contours detected: 5	Expected: 1

- Glyph name: t	Contours detected: 8	Expected: 1

- Glyph name: u	Contours detected: 10	Expected: 1

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 12	Expected: 1

- Glyph name: z	Contours detected: 5	Expected: 1

- Glyph name: braceleft	Contours detected: 7	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceright	Contours detected: 7	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: cent	Contours detected: 12	Expected: 1 or 2

- Glyph name: sterling	Contours detected: 8	Expected: 1 or 2

- Glyph name: currency	Contours detected: 8	Expected: 2

- Glyph name: yen	Contours detected: 9	Expected: 1 or 2

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: section	Contours detected: 12	Expected: 2

- Glyph name: copyright	Contours detected: 18	Expected: 3

- Glyph name: ordfeminine	Contours detected: 7	Expected: 2 or 3

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: logicalnot	Contours detected: 3	Expected: 1

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 20	Expected: 3 or 4

- Glyph name: degree	Contours detected: 6	Expected: 2

- Glyph name: plusminus	Contours detected: 6	Expected: 1 or 2

- Glyph name: twosuperior	Contours detected: 5	Expected: 1

- Glyph name: threesuperior	Contours detected: 5	Expected: 1

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: micro	Contours detected: 12	Expected: 1

- Glyph name: paragraph	Contours detected: 19	Expected: 1, 2 or 3

- Glyph name: cedilla	Contours detected: 2	Expected: 1

- Glyph name: onesuperior	Contours detected: 5	Expected: 1

- Glyph name: ordmasculine	Contours detected: 7	Expected: 2 or 3

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: onequarter	Contours detected: 11	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 10	Expected: 3

- Glyph name: threequarters	Contours detected: 11	Expected: 3 or 4

- Glyph name: questiondown	Contours detected: 7	Expected: 2

- Glyph name: Agrave	Contours detected: 14	Expected: 3

- Glyph name: Aacute	Contours detected: 14	Expected: 3

- Glyph name: Acircumflex	Contours detected: 15	Expected: 3

- Glyph name: Atilde	Contours detected: 16	Expected: 3

- Glyph name: Adieresis	Contours detected: 14	Expected: 4

- Glyph name: Aring	Contours detected: 16	Expected: 3 or 4

- Glyph name: AE	Contours detected: 12	Expected: 2

- Glyph name: Ccedilla	Contours detected: 11	Expected: 1 or 2

- Glyph name: Egrave	Contours detected: 9	Expected: 2

- Glyph name: Eacute	Contours detected: 9	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 10	Expected: 2

- Glyph name: Edieresis	Contours detected: 9	Expected: 3

- Glyph name: Igrave	Contours detected: 9	Expected: 2

- Glyph name: Iacute	Contours detected: 9	Expected: 2

- Glyph name: Icircumflex	Contours detected: 10	Expected: 2

- Glyph name: Idieresis	Contours detected: 9	Expected: 3

- Glyph name: Eth	Contours detected: 12	Expected: 2

- Glyph name: Ntilde	Contours detected: 19	Expected: 2

- Glyph name: Ograve	Contours detected: 14	Expected: 3

- Glyph name: Oacute	Contours detected: 14	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: Otilde	Contours detected: 16	Expected: 3

- Glyph name: Odieresis	Contours detected: 14	Expected: 4

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: Oslash	Contours detected: 13	Expected: 2 or 3

- Glyph name: Ugrave	Contours detected: 15	Expected: 2

- Glyph name: Uacute	Contours detected: 15	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 16	Expected: 2

- Glyph name: Udieresis	Contours detected: 15	Expected: 3

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Thorn	Contours detected: 10	Expected: 1 or 2

- Glyph name: germandbls	Contours detected: 13	Expected: 1

- Glyph name: agrave	Contours detected: 8	Expected: 3

- Glyph name: aacute	Contours detected: 8	Expected: 3

- Glyph name: acircumflex	Contours detected: 9	Expected: 3

- Glyph name: atilde	Contours detected: 10	Expected: 3

- Glyph name: adieresis	Contours detected: 8	Expected: 4

- Glyph name: aring	Contours detected: 10	Expected: 4

- Glyph name: ae	Contours detected: 9	Expected: 3

- Glyph name: ccedilla	Contours detected: 9	Expected: 1 or 2

- Glyph name: egrave	Contours detected: 8	Expected: 3

- Glyph name: eacute	Contours detected: 8	Expected: 3

- Glyph name: ecircumflex	Contours detected: 9	Expected: 3

- Glyph name: edieresis	Contours detected: 8	Expected: 4

- Glyph name: igrave	Contours detected: 7	Expected: 2

- Glyph name: iacute	Contours detected: 7	Expected: 2

- Glyph name: icircumflex	Contours detected: 8	Expected: 2

- Glyph name: idieresis	Contours detected: 7	Expected: 3

- Glyph name: eth	Contours detected: 10	Expected: 2

- Glyph name: ntilde	Contours detected: 14	Expected: 2

- Glyph name: ograve	Contours detected: 10	Expected: 3

- Glyph name: oacute	Contours detected: 10	Expected: 3

- Glyph name: ocircumflex	Contours detected: 11	Expected: 3

- Glyph name: otilde	Contours detected: 12	Expected: 3

- Glyph name: odieresis	Contours detected: 10	Expected: 4

- Glyph name: oslash	Contours detected: 11	Expected: 3

- Glyph name: ugrave	Contours detected: 12	Expected: 2

- Glyph name: uacute	Contours detected: 12	Expected: 2

- Glyph name: ucircumflex	Contours detected: 13	Expected: 2

- Glyph name: udieresis	Contours detected: 12	Expected: 3

- Glyph name: yacute	Contours detected: 14	Expected: 2

- Glyph name: thorn	Contours detected: 14	Expected: 2

- Glyph name: ydieresis	Contours detected: 14	Expected: 3

- Glyph name: Amacron	Contours detected: 13	Expected: 3

- Glyph name: amacron	Contours detected: 7	Expected: 3

- Glyph name: Abreve	Contours detected: 15	Expected: 3

- Glyph name: abreve	Contours detected: 9	Expected: 3

- Glyph name: Aogonek	Contours detected: 14	Expected: 2 or 3

- Glyph name: aogonek	Contours detected: 8	Expected: 2

- Glyph name: Cacute	Contours detected: 11	Expected: 2

- Glyph name: cacute	Contours detected: 9	Expected: 2

- Glyph name: Ccircumflex	Contours detected: 12	Expected: 2

- Glyph name: ccircumflex	Contours detected: 10	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 10	Expected: 2

- Glyph name: cdotaccent	Contours detected: 8	Expected: 2

- Glyph name: Ccaron	Contours detected: 12	Expected: 2

- Glyph name: ccaron	Contours detected: 10	Expected: 2

- Glyph name: Dcaron	Contours detected: 15	Expected: 3

- Glyph name: dcaron	Contours detected: 14	Expected: 3

- Glyph name: Dcroat	Contours detected: 12	Expected: 2

- Glyph name: dcroat	Contours detected: 11	Expected: 2

- Glyph name: Emacron	Contours detected: 8	Expected: 2

- Glyph name: emacron	Contours detected: 7	Expected: 3

- Glyph name: Ebreve	Contours detected: 10	Expected: 2

- Glyph name: ebreve	Contours detected: 9	Expected: 3

- Glyph name: Edotaccent	Contours detected: 8	Expected: 2

- Glyph name: edotaccent	Contours detected: 7	Expected: 3

- Glyph name: Eogonek	Contours detected: 9	Expected: 1 or 2

- Glyph name: eogonek	Contours detected: 8	Expected: 2

- Glyph name: Ecaron	Contours detected: 10	Expected: 2

- Glyph name: ecaron	Contours detected: 9	Expected: 3

- Glyph name: Gcircumflex	Contours detected: 14	Expected: 2

- Glyph name: gcircumflex	Contours detected: 15	Expected: 3 or 4

- Glyph name: Gbreve	Contours detected: 14	Expected: 2

- Glyph name: gbreve	Contours detected: 15	Expected: 3 or 4

- Glyph name: Gdotaccent	Contours detected: 12	Expected: 2

- Glyph name: gdotaccent	Contours detected: 13	Expected: 3 or 4

- Glyph name: Gcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: gcommaaccent	Contours detected: 14	Expected: 3 or 4

- Glyph name: Hcircumflex	Contours detected: 16	Expected: 2

- Glyph name: hcircumflex	Contours detected: 15	Expected: 2

- Glyph name: Hbar	Contours detected: 12	Expected: 2

- Glyph name: hbar	Contours detected: 11	Expected: 1

- Glyph name: Itilde	Contours detected: 11	Expected: 2

- Glyph name: itilde	Contours detected: 9	Expected: 2

- Glyph name: Imacron	Contours detected: 8	Expected: 2

- Glyph name: imacron	Contours detected: 6	Expected: 2

- Glyph name: Iogonek	Contours detected: 9	Expected: 1 or 2

- Glyph name: iogonek	Contours detected: 8	Expected: 2 or 3

- Glyph name: Idotaccent	Contours detected: 8	Expected: 2

- Glyph name: dotlessi	Contours detected: 5	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: ij	Contours detected: 14	Expected: 3 or 4

- Glyph name: Jcircumflex	Contours detected: 11	Expected: 2

- Glyph name: jcircumflex	Contours detected: 11	Expected: 2

- Glyph name: Kcommaaccent	Contours detected: 15	Expected: 2 or 3

- Glyph name: kcommaaccent	Contours detected: 13	Expected: 2 or 3

- Glyph name: kgreenlandic	Contours detected: 9	Expected: 1 or 2

- Glyph name: Lacute	Contours detected: 9	Expected: 2

- Glyph name: lacute	Contours detected: 9	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: Lcaron	Contours detected: 9	Expected: 2

- Glyph name: lcaron	Contours detected: 9	Expected: 2

- Glyph name: Ldot	Contours detected: 8	Expected: 2

- Glyph name: ldot	Contours detected: 8	Expected: 2

- Glyph name: Lslash	Contours detected: 8	Expected: 1

- Glyph name: lslash	Contours detected: 7	Expected: 1

- Glyph name: Nacute	Contours detected: 17	Expected: 2

- Glyph name: nacute	Contours detected: 12	Expected: 2

- Glyph name: Ncommaaccent	Contours detected: 17	Expected: 2

- Glyph name: ncommaaccent	Contours detected: 12	Expected: 2

- Glyph name: Ncaron	Contours detected: 18	Expected: 2

- Glyph name: ncaron	Contours detected: 13	Expected: 2

- Glyph name: napostrophe	Contours detected: 13	Expected: 2

- Glyph name: Eng	Contours detected: 16	Expected: 1

- Glyph name: eng	Contours detected: 12	Expected: 1

- Glyph name: Omacron	Contours detected: 13	Expected: 3

- Glyph name: omacron	Contours detected: 9	Expected: 3

- Glyph name: Ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: ohungarumlaut	Contours detected: 12	Expected: 4

- Glyph name: OE	Contours detected: 12	Expected: 2

- Glyph name: oe	Contours detected: 11	Expected: 3

- Glyph name: Racute	Contours detected: 14	Expected: 3

- Glyph name: racute	Contours detected: 9	Expected: 2

- Glyph name: Rcommaaccent	Contours detected: 14	Expected: 3

- Glyph name: rcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: Rcaron	Contours detected: 15	Expected: 3

- Glyph name: rcaron	Contours detected: 10	Expected: 2

- Glyph name: Sacute	Contours detected: 11	Expected: 2

- Glyph name: sacute	Contours detected: 7	Expected: 2

- Glyph name: Scircumflex	Contours detected: 12	Expected: 2

- Glyph name: scircumflex	Contours detected: 8	Expected: 2

- Glyph name: Scedilla	Contours detected: 11	Expected: 1 or 2

- Glyph name: scedilla	Contours detected: 7	Expected: 1 or 2

- Glyph name: Scaron	Contours detected: 12	Expected: 2

- Glyph name: scaron	Contours detected: 8	Expected: 2

- Glyph name: uni0162	Contours detected: 9	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 10	Expected: 1 or 2

- Glyph name: Tcaron	Contours detected: 10	Expected: 2

- Glyph name: tcaron	Contours detected: 10	Expected: 2

- Glyph name: Utilde	Contours detected: 17	Expected: 2

- Glyph name: utilde	Contours detected: 14	Expected: 2

- Glyph name: Umacron	Contours detected: 14	Expected: 2

- Glyph name: umacron	Contours detected: 11	Expected: 2

- Glyph name: Ubreve	Contours detected: 16	Expected: 2

- Glyph name: ubreve	Contours detected: 13	Expected: 2

- Glyph name: Uring	Contours detected: 17	Expected: 3

- Glyph name: uring	Contours detected: 14	Expected: 3

- Glyph name: Uhungarumlaut	Contours detected: 17	Expected: 3

- Glyph name: uhungarumlaut	Contours detected: 14	Expected: 3

- Glyph name: Uogonek	Contours detected: 15	Expected: 1

- Glyph name: uogonek	Contours detected: 12	Expected: 1

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: ycircumflex	Contours detected: 15	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Zacute	Contours detected: 9	Expected: 2

- Glyph name: zacute	Contours detected: 7	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 8	Expected: 2

- Glyph name: zdotaccent	Contours detected: 6	Expected: 2

- Glyph name: Zcaron	Contours detected: 10	Expected: 2

- Glyph name: zcaron	Contours detected: 8	Expected: 2

- Glyph name: uni018F	Contours detected: 10	Expected: 2

- Glyph name: florin	Contours detected: 9	Expected: 1

- Glyph name: Ohorn	Contours detected: 15	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 11	Expected: 2

- Glyph name: Uhorn	Contours detected: 16	Expected: 1

- Glyph name: uhorn	Contours detected: 13	Expected: 1

- Glyph name: uni01CD	Contours detected: 15	Expected: 3

- Glyph name: uni01CE	Contours detected: 9	Expected: 3

- Glyph name: uni01CF	Contours detected: 10	Expected: 2

- Glyph name: uni01D0	Contours detected: 8	Expected: 2

- Glyph name: uni01D1	Contours detected: 15	Expected: 3

- Glyph name: uni01D2	Contours detected: 11	Expected: 3

- Glyph name: uni01D3	Contours detected: 16	Expected: 2

- Glyph name: uni01D4	Contours detected: 13	Expected: 2

- Glyph name: uni01D5	Contours detected: 14	Expected: 4

- Glyph name: uni01D6	Contours detected: 13	Expected: 4

- Glyph name: uni01D7	Contours detected: 13	Expected: 4

- Glyph name: uni01D8	Contours detected: 14	Expected: 4

- Glyph name: uni01D9	Contours detected: 14	Expected: 4

- Glyph name: uni01DA	Contours detected: 15	Expected: 4

- Glyph name: uni01DB	Contours detected: 13	Expected: 4

- Glyph name: uni01DC	Contours detected: 14	Expected: 4

- Glyph name: Gcaron	Contours detected: 14	Expected: 2

- Glyph name: gcaron	Contours detected: 15	Expected: 3 or 4

- Glyph name: Scommaaccent	Contours detected: 11	Expected: 2

- Glyph name: scommaaccent	Contours detected: 7	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 10	Expected: 2

- Glyph name: jdotless	Contours detected: 8	Expected: 1

- Glyph name: uni0251	Contours detected: 10	Expected: 2

- Glyph name: uni0259	Contours detected: 6	Expected: 2

- Glyph name: uni0261	Contours detected: 12	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: breve	Contours detected: 3	Expected: 1

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: ogonek	Contours detected: 2	Expected: 1

- Glyph name: tilde	Contours detected: 4	Expected: 1

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: gravecomb	Contours detected: 2	Expected: 1

- Glyph name: acutecomb	Contours detected: 2	Expected: 1

- Glyph name: circumflexcomb	Contours detected: 3	Expected: 1

- Glyph name: tildecomb	Contours detected: 4	Expected: 1

- Glyph name: brevecomb	Contours detected: 3	Expected: 1

- Glyph name: hookabovecomb	Contours detected: 3	Expected: 1

- Glyph name: ringcomb	Contours detected: 4	Expected: 2

- Glyph name: hungarumlautcomb	Contours detected: 4	Expected: 2

- Glyph name: caroncomb	Contours detected: 3	Expected: 1

- Glyph name: commaturnedabovecomb	Contours detected: 2	Expected: 1

- Glyph name: horncomb	Contours detected: 3	Expected: 1

- Glyph name: commaaccentcomb	Contours detected: 2	Expected: 1

- Glyph name: cedillacomb	Contours detected: 2	Expected: 1

- Glyph name: ogonekcomb	Contours detected: 2	Expected: 1

- Glyph name: uni032E	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 11	Expected: 2

- Glyph name: uni03A9	Contours detected: 13	Expected: 1

- Glyph name: uni03BC	Contours detected: 12	Expected: 1

- Glyph name: pi	Contours detected: 9	Expected: 1

- Glyph name: baht	Contours detected: 11	Expected: 3 or 5

- Glyph name: uni1E0C	Contours detected: 13	Expected: 3

- Glyph name: uni1E0D	Contours detected: 13	Expected: 3

- Glyph name: uni1E0E	Contours detected: 13	Expected: 3

- Glyph name: uni1E0F	Contours detected: 13	Expected: 3

- Glyph name: uni1E20	Contours detected: 12	Expected: 2

- Glyph name: uni1E21	Contours detected: 13	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 14	Expected: 2

- Glyph name: uni1E25	Contours detected: 13	Expected: 2

- Glyph name: uni1E2A	Contours detected: 14	Expected: 2

- Glyph name: uni1E2B	Contours detected: 13	Expected: 2

- Glyph name: uni1E36	Contours detected: 8	Expected: 2

- Glyph name: uni1E37	Contours detected: 8	Expected: 2

- Glyph name: uni1E38	Contours detected: 9	Expected: 3

- Glyph name: uni1E39	Contours detected: 9	Expected: 3

- Glyph name: uni1E3A	Contours detected: 8	Expected: 2

- Glyph name: uni1E3B	Contours detected: 8	Expected: 2

- Glyph name: uni1E42	Contours detected: 17	Expected: 2

- Glyph name: uni1E43	Contours detected: 14	Expected: 2

- Glyph name: uni1E44	Contours detected: 16	Expected: 2

- Glyph name: uni1E45	Contours detected: 11	Expected: 2

- Glyph name: uni1E46	Contours detected: 16	Expected: 2

- Glyph name: uni1E47	Contours detected: 11	Expected: 2

- Glyph name: uni1E48	Contours detected: 16	Expected: 2

- Glyph name: uni1E49	Contours detected: 11	Expected: 2

- Glyph name: uni1E5A	Contours detected: 13	Expected: 3

- Glyph name: uni1E5B	Contours detected: 8	Expected: 2

- Glyph name: uni1E5C	Contours detected: 14	Expected: 4

- Glyph name: uni1E5D	Contours detected: 9	Expected: 3

- Glyph name: uni1E5E	Contours detected: 13	Expected: 3

- Glyph name: uni1E5F	Contours detected: 8	Expected: 2

- Glyph name: uni1E60	Contours detected: 10	Expected: 2

- Glyph name: uni1E61	Contours detected: 6	Expected: 2

- Glyph name: uni1E62	Contours detected: 10	Expected: 2

- Glyph name: uni1E63	Contours detected: 6	Expected: 2

- Glyph name: uni1E6C	Contours detected: 8	Expected: 2

- Glyph name: uni1E6D	Contours detected: 9	Expected: 2

- Glyph name: uni1E6E	Contours detected: 8	Expected: 2

- Glyph name: uni1E6F	Contours detected: 9	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 13	Expected: 2

- Glyph name: uni1E92	Contours detected: 8	Expected: 2

- Glyph name: uni1E93	Contours detected: 6	Expected: 2

- Glyph name: uni1E97	Contours detected: 10	Expected: 3

- Glyph name: Germandbls	Contours detected: 13	Expected: 1

- Glyph name: Adotbelow	Contours detected: 13	Expected: 3

- Glyph name: adotbelow	Contours detected: 7	Expected: 3

- Glyph name: Ahookabove	Contours detected: 15	Expected: 3

- Glyph name: ahookabove	Contours detected: 9	Expected: 3

- Glyph name: Acircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: acircumflexacute	Contours detected: 11	Expected: 4

- Glyph name: Acircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: acircumflexgrave	Contours detected: 11	Expected: 4

- Glyph name: Acircumflexhookabove	Contours detected: 14	Expected: 4

- Glyph name: acircumflexhookabove	Contours detected: 12	Expected: 4

- Glyph name: Acircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: acircumflextilde	Contours detected: 13	Expected: 4

- Glyph name: Acircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: acircumflexdotbelow	Contours detected: 10	Expected: 4

- Glyph name: Abreveacute	Contours detected: 13	Expected: 4

- Glyph name: abreveacute	Contours detected: 11	Expected: 4

- Glyph name: Abrevegrave	Contours detected: 13	Expected: 4

- Glyph name: abrevegrave	Contours detected: 11	Expected: 4

- Glyph name: Abrevehookabove	Contours detected: 14	Expected: 4

- Glyph name: abrevehookabove	Contours detected: 12	Expected: 4

- Glyph name: Abrevetilde	Contours detected: 15	Expected: 4

- Glyph name: abrevetilde	Contours detected: 13	Expected: 4

- Glyph name: Abrevedotbelow	Contours detected: 16	Expected: 4

- Glyph name: abrevedotbelow	Contours detected: 10	Expected: 4

- Glyph name: Edotbelow	Contours detected: 8	Expected: 2

- Glyph name: edotbelow	Contours detected: 7	Expected: 3

- Glyph name: Ehookabove	Contours detected: 10	Expected: 2

- Glyph name: ehookabove	Contours detected: 9	Expected: 3

- Glyph name: Etilde	Contours detected: 11	Expected: 2

- Glyph name: etilde	Contours detected: 10	Expected: 3

- Glyph name: Ecircumflexacute	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexacute	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflexgrave	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexgrave	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflexhookabove	Contours detected: 11	Expected: 3

- Glyph name: ecircumflexhookabove	Contours detected: 12	Expected: 4

- Glyph name: Ecircumflextilde	Contours detected: 12	Expected: 3

- Glyph name: ecircumflextilde	Contours detected: 13	Expected: 4

- Glyph name: Ecircumflexdotbelow	Contours detected: 11	Expected: 3

- Glyph name: ecircumflexdotbelow	Contours detected: 10	Expected: 4

- Glyph name: Ihookabove	Contours detected: 10	Expected: 2

- Glyph name: ihookabove	Contours detected: 8	Expected: 2

- Glyph name: Idotbelow	Contours detected: 8	Expected: 2

- Glyph name: idotbelow	Contours detected: 7	Expected: 3

- Glyph name: Odotbelow	Contours detected: 13	Expected: 3

- Glyph name: odotbelow	Contours detected: 9	Expected: 3

- Glyph name: Ohookabove	Contours detected: 15	Expected: 3

- Glyph name: ohookabove	Contours detected: 11	Expected: 3

- Glyph name: Ocircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflexhookabove	Contours detected: 14	Expected: 4

- Glyph name: ocircumflexhookabove	Contours detected: 14	Expected: 4

- Glyph name: Ocircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: ocircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: Ocircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: ocircumflexdotbelow	Contours detected: 12	Expected: 4

- Glyph name: Ohornacute	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohornacute	Contours detected: 13	Expected: 3

- Glyph name: Ohorngrave	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohorngrave	Contours detected: 13	Expected: 3

- Glyph name: Ohornhookabove	Contours detected: 18	Expected: 3 or 4

- Glyph name: ohornhookabove	Contours detected: 14	Expected: 3

- Glyph name: Ohorntilde	Contours detected: 19	Expected: 3 or 4

- Glyph name: ohorntilde	Contours detected: 15	Expected: 3

- Glyph name: Ohorndotbelow	Contours detected: 16	Expected: 3 or 4

- Glyph name: ohorndotbelow	Contours detected: 12	Expected: 3

- Glyph name: Udotbelow	Contours detected: 14	Expected: 2

- Glyph name: udotbelow	Contours detected: 11	Expected: 2

- Glyph name: Uhookabove	Contours detected: 16	Expected: 2

- Glyph name: uhookabove	Contours detected: 13	Expected: 2

- Glyph name: Uhornacute	Contours detected: 18	Expected: 2

- Glyph name: uhornacute	Contours detected: 15	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 18	Expected: 2

- Glyph name: uhorngrave	Contours detected: 15	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 19	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 16	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 20	Expected: 2

- Glyph name: uhorntilde	Contours detected: 17	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 17	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 14	Expected: 2

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: ygrave	Contours detected: 14	Expected: 2

- Glyph name: Ydotbelow	Contours detected: 11	Expected: 2

- Glyph name: ydotbelow	Contours detected: 8	Expected: 2

- Glyph name: Yhookabove	Contours detected: 13	Expected: 2

- Glyph name: yhookabove	Contours detected: 15	Expected: 2

- Glyph name: Ytilde	Contours detected: 14	Expected: 2

- Glyph name: ytilde	Contours detected: 16	Expected: 2

- Glyph name: dblverticalbar	Contours detected: 14	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: dagger	Contours detected: 9	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 9	Expected: 1 or 3

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: perthousand	Contours detected: 11	Expected: 6 or 7

- Glyph name: minute	Contours detected: 3	Expected: 1

- Glyph name: second	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: uni2070	Contours detected: 8	Expected: 2 or 3

- Glyph name: foursuperior	Contours detected: 6	Expected: 1 or 2

- Glyph name: fivesuperior	Contours detected: 5	Expected: 1

- Glyph name: sixsuperior	Contours detected: 6	Expected: 2

- Glyph name: sevensuperior	Contours detected: 5	Expected: 1

- Glyph name: eightsuperior	Contours detected: 7	Expected: 3

- Glyph name: ninesuperior	Contours detected: 6	Expected: 2

- Glyph name: uni207D	Contours detected: 5	Expected: 1

- Glyph name: uni207E	Contours detected: 5	Expected: 1

- Glyph name: uni207F	Contours detected: 7	Expected: 1

- Glyph name: uni2080	Contours detected: 8	Expected: 2 or 3

- Glyph name: oneinferior	Contours detected: 5	Expected: 1

- Glyph name: twoinferior	Contours detected: 5	Expected: 1

- Glyph name: threeinferior	Contours detected: 5	Expected: 1

- Glyph name: fourinferior	Contours detected: 6	Expected: 1 or 2

- Glyph name: fiveinferior	Contours detected: 5	Expected: 1

- Glyph name: sixinferior	Contours detected: 6	Expected: 2

- Glyph name: seveninferior	Contours detected: 5	Expected: 1

- Glyph name: eightinferior	Contours detected: 7	Expected: 3

- Glyph name: nineinferior	Contours detected: 6	Expected: 2

- Glyph name: uni208D	Contours detected: 5	Expected: 1

- Glyph name: uni208E	Contours detected: 5	Expected: 1

- Glyph name: colonmonetary	Contours detected: 12	Expected: 1 or 3

- Glyph name: lira	Contours detected: 8	Expected: 1

- Glyph name: naira	Contours detected: 12	Expected: 1, 3 or 5

- Glyph name: peseta	Contours detected: 19	Expected: 2, 3 or 4

- Glyph name: rupee	Contours detected: 17	Expected: 3

- Glyph name: won	Contours detected: 14	Expected: 1, 3, 4 or 7

- Glyph name: sheqel	Contours detected: 18	Expected: 2

- Glyph name: dong	Contours detected: 12	Expected: 3 or 4

- Glyph name: Euro	Contours detected: 9	Expected: 1 or 2

- Glyph name: kip	Contours detected: 11	Expected: 1

- Glyph name: tugrik	Contours detected: 7	Expected: 1

- Glyph name: peso	Contours detected: 9	Expected: 1, 2 or 4

- Glyph name: guarani	Contours detected: 11	Expected: 1, 2 or 3

- Glyph name: hryvnia	Contours detected: 7	Expected: 1 or 2

- Glyph name: cedi	Contours detected: 12	Expected: 1 or 2

- Glyph name: tenge	Contours detected: 6	Expected: 2

- Glyph name: rupeeIndian	Contours detected: 7	Expected: 1

- Glyph name: liraTurkish	Contours detected: 9	Expected: 1

- Glyph name: manat	Contours detected: 15	Expected: 1

- Glyph name: ruble	Contours detected: 9	Expected: 2

- Glyph name: bitcoin	Contours detected: 11	Expected: 3

- Glyph name: literSign	Contours detected: 10	Expected: 2

- Glyph name: numero	Contours detected: 22	Expected: 3 or 4

- Glyph name: uni2117	Contours detected: 19	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 15	Expected: 2

- Glyph name: trademark	Contours detected: 16	Expected: 2

- Glyph name: Ohm	Contours detected: 13	Expected: 1

- Glyph name: onethird	Contours detected: 10	Expected: 3

- Glyph name: twothirds	Contours detected: 10	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 12	Expected: 5

- Glyph name: threeeighths	Contours detected: 12	Expected: 5

- Glyph name: fiveeighths	Contours detected: 12	Expected: 5

- Glyph name: seveneighths	Contours detected: 12	Expected: 5

- Glyph name: arrowleft	Contours detected: 5	Expected: 1

- Glyph name: arrowup	Contours detected: 9	Expected: 1

- Glyph name: arrowright	Contours detected: 5	Expected: 1

- Glyph name: arrowdown	Contours detected: 9	Expected: 1

- Glyph name: arrowboth	Contours detected: 9	Expected: 1

- Glyph name: arrowupdn	Contours detected: 11	Expected: 1

- Glyph name: northWestArrow	Contours detected: 8	Expected: 1

- Glyph name: northEastArrow	Contours detected: 8	Expected: 1

- Glyph name: southEastArrow	Contours detected: 8	Expected: 1

- Glyph name: southWestArrow	Contours detected: 8	Expected: 1

- Glyph name: partialdiff	Contours detected: 9	Expected: 2

- Glyph name: emptyset	Contours detected: 17	Expected: 3

- Glyph name: increment	Contours detected: 11	Expected: 2

- Glyph name: product	Contours detected: 17	Expected: 1

- Glyph name: summation	Contours detected: 9	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 8	Expected: 1

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: approxequal	Contours detected: 8	Expected: 2

- Glyph name: notequal	Contours detected: 7	Expected: 1

- Glyph name: lessequal	Contours detected: 6	Expected: 2

- Glyph name: greaterequal	Contours detected: 6	Expected: 2

- Glyph name: filledbox	Contours detected: 7	Expected: 1

- Glyph name: whiteSquare	Contours detected: 12	Expected: 2

- Glyph name: blackSmallSquare	Contours detected: 3	Expected: 1

- Glyph name: whiteSmallSquare	Contours detected: 4	Expected: 2

- Glyph name: triagup	Contours detected: 7	Expected: 1

- Glyph name: upWhiteTriangle	Contours detected: 12	Expected: 2

- Glyph name: rightBlackTriangle	Contours detected: 7	Expected: 1

- Glyph name: rightWhiteTriangle	Contours detected: 12	Expected: 2

- Glyph name: triagdn	Contours detected: 7	Expected: 1

- Glyph name: downWhiteTriangle	Contours detected: 12	Expected: 2

- Glyph name: leftBlackTriangle	Contours detected: 7	Expected: 1

- Glyph name: leftWhiteTriangle	Contours detected: 12	Expected: 2

- Glyph name: blackDiamond	Contours detected: 7	Expected: 1

- Glyph name: whiteDiamond	Contours detected: 12	Expected: 2

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: circle	Contours detected: 12	Expected: 2

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: blackCircle	Contours detected: 7	Expected: 1

- Glyph name: leftanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: rightanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: uniFB01	Contours detected: 11	Expected: 1, 2 or 3

- Glyph name: uniFB02	Contours detected: 13	Expected: 1 or 2

- Glyph name: A	Contours detected: 12	Expected: 2

- Glyph name: AE	Contours detected: 12	Expected: 2

- Glyph name: Aacute	Contours detected: 14	Expected: 3

- Glyph name: Abreve	Contours detected: 15	Expected: 3

- Glyph name: Acircumflex	Contours detected: 15	Expected: 3

- Glyph name: Adieresis	Contours detected: 14	Expected: 4

- Glyph name: Agrave	Contours detected: 14	Expected: 3

- Glyph name: Amacron	Contours detected: 13	Expected: 3

- Glyph name: Aogonek	Contours detected: 14	Expected: 2 or 3

- Glyph name: Aring	Contours detected: 16	Expected: 3 or 4

- Glyph name: Atilde	Contours detected: 16	Expected: 3

- Glyph name: B	Contours detected: 11	Expected: 2 or 3

- Glyph name: C	Contours detected: 9	Expected: 1

- Glyph name: Cacute	Contours detected: 11	Expected: 2

- Glyph name: Ccaron	Contours detected: 12	Expected: 2

- Glyph name: Ccedilla	Contours detected: 11	Expected: 1 or 2

- Glyph name: Ccircumflex	Contours detected: 12	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 10	Expected: 2

- Glyph name: D	Contours detected: 12	Expected: 2

- Glyph name: Dcaron	Contours detected: 15	Expected: 3

- Glyph name: Dcroat	Contours detected: 12	Expected: 2

- Glyph name: E	Contours detected: 7	Expected: 1

- Glyph name: Eacute	Contours detected: 9	Expected: 2

- Glyph name: Ebreve	Contours detected: 10	Expected: 2

- Glyph name: Ecaron	Contours detected: 10	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 10	Expected: 2

- Glyph name: Edieresis	Contours detected: 9	Expected: 3

- Glyph name: Edotaccent	Contours detected: 8	Expected: 2

- Glyph name: Egrave	Contours detected: 9	Expected: 2

- Glyph name: Emacron	Contours detected: 8	Expected: 2

- Glyph name: Eng	Contours detected: 16	Expected: 1

- Glyph name: Eogonek	Contours detected: 9	Expected: 1 or 2

- Glyph name: Eth	Contours detected: 12	Expected: 2

- Glyph name: Euro	Contours detected: 9	Expected: 1 or 2

- Glyph name: F	Contours detected: 7	Expected: 1

- Glyph name: G	Contours detected: 11	Expected: 1

- Glyph name: Gbreve	Contours detected: 14	Expected: 2

- Glyph name: Gcaron	Contours detected: 14	Expected: 2

- Glyph name: Gcircumflex	Contours detected: 14	Expected: 2

- Glyph name: Gdotaccent	Contours detected: 12	Expected: 2

- Glyph name: H	Contours detected: 13	Expected: 1

- Glyph name: Hbar	Contours detected: 12	Expected: 2

- Glyph name: Hcircumflex	Contours detected: 16	Expected: 2

- Glyph name: I	Contours detected: 7	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: Iacute	Contours detected: 9	Expected: 2

- Glyph name: Icircumflex	Contours detected: 10	Expected: 2

- Glyph name: Idieresis	Contours detected: 9	Expected: 3

- Glyph name: Idotaccent	Contours detected: 8	Expected: 2

- Glyph name: Igrave	Contours detected: 9	Expected: 2

- Glyph name: Imacron	Contours detected: 8	Expected: 2

- Glyph name: Iogonek	Contours detected: 9	Expected: 1 or 2

- Glyph name: Itilde	Contours detected: 11	Expected: 2

- Glyph name: J	Contours detected: 8	Expected: 1

- Glyph name: Jcircumflex	Contours detected: 11	Expected: 2

- Glyph name: K	Contours detected: 13	Expected: 1 or 2

- Glyph name: L	Contours detected: 7	Expected: 1

- Glyph name: Lacute	Contours detected: 9	Expected: 2

- Glyph name: Lcaron	Contours detected: 9	Expected: 2

- Glyph name: Ldot	Contours detected: 8	Expected: 2

- Glyph name: Lslash	Contours detected: 8	Expected: 1

- Glyph name: M	Contours detected: 16	Expected: 1

- Glyph name: N	Contours detected: 15	Expected: 1

- Glyph name: Nacute	Contours detected: 17	Expected: 2

- Glyph name: Ncaron	Contours detected: 18	Expected: 2

- Glyph name: Ntilde	Contours detected: 19	Expected: 2

- Glyph name: O	Contours detected: 12	Expected: 2

- Glyph name: OE	Contours detected: 12	Expected: 2

- Glyph name: Oacute	Contours detected: 14	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: Odieresis	Contours detected: 14	Expected: 4

- Glyph name: Ograve	Contours detected: 14	Expected: 3

- Glyph name: Ohorn	Contours detected: 15	Expected: 2 or 3

- Glyph name: Ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: Omacron	Contours detected: 13	Expected: 3

- Glyph name: Oslash	Contours detected: 13	Expected: 2 or 3

- Glyph name: Otilde	Contours detected: 16	Expected: 3

- Glyph name: P	Contours detected: 9	Expected: 1 or 2

- Glyph name: Q	Contours detected: 14	Expected: 2

- Glyph name: R	Contours detected: 12	Expected: 1 or 2

- Glyph name: Racute	Contours detected: 14	Expected: 3

- Glyph name: Rcaron	Contours detected: 15	Expected: 3

- Glyph name: S	Contours detected: 9	Expected: 1

- Glyph name: Sacute	Contours detected: 11	Expected: 2

- Glyph name: Scaron	Contours detected: 12	Expected: 2

- Glyph name: Scircumflex	Contours detected: 12	Expected: 2

- Glyph name: T	Contours detected: 7	Expected: 1

- Glyph name: Tcaron	Contours detected: 10	Expected: 2

- Glyph name: Thorn	Contours detected: 10	Expected: 1 or 2

- Glyph name: U	Contours detected: 13	Expected: 1

- Glyph name: Uacute	Contours detected: 15	Expected: 2

- Glyph name: Ubreve	Contours detected: 16	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 16	Expected: 2

- Glyph name: Udieresis	Contours detected: 15	Expected: 3

- Glyph name: Ugrave	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 16	Expected: 1

- Glyph name: Uhungarumlaut	Contours detected: 17	Expected: 3

- Glyph name: Umacron	Contours detected: 14	Expected: 2

- Glyph name: Uogonek	Contours detected: 15	Expected: 1

- Glyph name: Uring	Contours detected: 17	Expected: 3

- Glyph name: Utilde	Contours detected: 17	Expected: 2

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: Z	Contours detected: 7	Expected: 1

- Glyph name: Zacute	Contours detected: 9	Expected: 2

- Glyph name: Zcaron	Contours detected: 10	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 8	Expected: 2

- Glyph name: a	Contours detected: 6	Expected: 2

- Glyph name: aacute	Contours detected: 8	Expected: 3

- Glyph name: abreve	Contours detected: 9	Expected: 3

- Glyph name: acircumflex	Contours detected: 9	Expected: 3

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: adieresis	Contours detected: 8	Expected: 4

- Glyph name: ae	Contours detected: 9	Expected: 3

- Glyph name: agrave	Contours detected: 8	Expected: 3

- Glyph name: amacron	Contours detected: 7	Expected: 3

- Glyph name: ampersand	Contours detected: 13	Expected: 1, 2 or 3

- Glyph name: aogonek	Contours detected: 8	Expected: 2

- Glyph name: approxequal	Contours detected: 8	Expected: 2

- Glyph name: aring	Contours detected: 10	Expected: 4

- Glyph name: arrowboth	Contours detected: 9	Expected: 1

- Glyph name: arrowdown	Contours detected: 9	Expected: 1

- Glyph name: arrowup	Contours detected: 9	Expected: 1

- Glyph name: arrowupdn	Contours detected: 11	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 9	Expected: 1 or 4

- Glyph name: at	Contours detected: 12	Expected: 2

- Glyph name: atilde	Contours detected: 10	Expected: 3

- Glyph name: b	Contours detected: 12	Expected: 2

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceleft	Contours detected: 7	Expected: 1

- Glyph name: braceright	Contours detected: 7	Expected: 1

- Glyph name: bracketleft	Contours detected: 7	Expected: 1

- Glyph name: bracketright	Contours detected: 7	Expected: 1

- Glyph name: breve	Contours detected: 3	Expected: 1

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: c	Contours detected: 7	Expected: 1

- Glyph name: cacute	Contours detected: 9	Expected: 2

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: ccaron	Contours detected: 10	Expected: 2

- Glyph name: ccedilla	Contours detected: 9	Expected: 1 or 2

- Glyph name: ccircumflex	Contours detected: 10	Expected: 2

- Glyph name: cdotaccent	Contours detected: 8	Expected: 2

- Glyph name: cedilla	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 12	Expected: 1 or 2

- Glyph name: circle	Contours detected: 12	Expected: 2

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: colonmonetary	Contours detected: 12	Expected: 1 or 3

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: copyright	Contours detected: 18	Expected: 3

- Glyph name: currency	Contours detected: 8	Expected: 2

- Glyph name: d	Contours detected: 12	Expected: 2

- Glyph name: dagger	Contours detected: 9	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 9	Expected: 1 or 3

- Glyph name: dcaron	Contours detected: 14	Expected: 3

- Glyph name: dcroat	Contours detected: 11	Expected: 2

- Glyph name: degree	Contours detected: 6	Expected: 2

- Glyph name: dollar	Contours detected: 9	Expected: 1, 3 or 5

- Glyph name: dong	Contours detected: 12	Expected: 3 or 4

- Glyph name: dotlessi	Contours detected: 5	Expected: 1

- Glyph name: e	Contours detected: 6	Expected: 2

- Glyph name: eacute	Contours detected: 8	Expected: 3

- Glyph name: ebreve	Contours detected: 9	Expected: 3

- Glyph name: ecaron	Contours detected: 9	Expected: 3

- Glyph name: ecircumflex	Contours detected: 9	Expected: 3

- Glyph name: edieresis	Contours detected: 8	Expected: 4

- Glyph name: edotaccent	Contours detected: 7	Expected: 3

- Glyph name: egrave	Contours detected: 8	Expected: 3

- Glyph name: eight	Contours detected: 11	Expected: 3

- Glyph name: emacron	Contours detected: 7	Expected: 3

- Glyph name: emptyset	Contours detected: 17	Expected: 3

- Glyph name: eng	Contours detected: 12	Expected: 1

- Glyph name: eogonek	Contours detected: 8	Expected: 2

- Glyph name: eth	Contours detected: 10	Expected: 2

- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: f	Contours detected: 8	Expected: 1

- Glyph name: five	Contours detected: 8	Expected: 1

- Glyph name: fiveeighths	Contours detected: 12	Expected: 5

- Glyph name: four	Contours detected: 9	Expected: 1 or 2

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: g	Contours detected: 12	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 15	Expected: 3 or 4

- Glyph name: gcaron	Contours detected: 15	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 15	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 13	Expected: 3 or 4

- Glyph name: germandbls	Contours detected: 13	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: greaterequal	Contours detected: 6	Expected: 2

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: h	Contours detected: 12	Expected: 1

- Glyph name: hbar	Contours detected: 11	Expected: 1

- Glyph name: hcircumflex	Contours detected: 15	Expected: 2

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: i	Contours detected: 6	Expected: 2

- Glyph name: iacute	Contours detected: 7	Expected: 2

- Glyph name: icircumflex	Contours detected: 8	Expected: 2

- Glyph name: idieresis	Contours detected: 7	Expected: 3

- Glyph name: igrave	Contours detected: 7	Expected: 2

- Glyph name: ij	Contours detected: 14	Expected: 3 or 4

- Glyph name: imacron	Contours detected: 6	Expected: 2

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: iogonek	Contours detected: 8	Expected: 2 or 3

- Glyph name: itilde	Contours detected: 9	Expected: 2

- Glyph name: j	Contours detected: 9	Expected: 2

- Glyph name: jcircumflex	Contours detected: 11	Expected: 2

- Glyph name: k	Contours detected: 11	Expected: 1 or 2

- Glyph name: kgreenlandic	Contours detected: 9	Expected: 1 or 2

- Glyph name: l	Contours detected: 7	Expected: 1

- Glyph name: lacute	Contours detected: 9	Expected: 2

- Glyph name: lcaron	Contours detected: 9	Expected: 2

- Glyph name: ldot	Contours detected: 8	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: lessequal	Contours detected: 6	Expected: 2

- Glyph name: lira	Contours detected: 8	Expected: 1

- Glyph name: logicalnot	Contours detected: 3	Expected: 1

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: lslash	Contours detected: 7	Expected: 1

- Glyph name: m	Contours detected: 13	Expected: 1

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: n	Contours detected: 10	Expected: 1

- Glyph name: nacute	Contours detected: 12	Expected: 2

- Glyph name: napostrophe	Contours detected: 13	Expected: 2

- Glyph name: ncaron	Contours detected: 13	Expected: 2

- Glyph name: nine	Contours detected: 9	Expected: 1 or 2

- Glyph name: notequal	Contours detected: 7	Expected: 1

- Glyph name: ntilde	Contours detected: 14	Expected: 2

- Glyph name: numbersign	Contours detected: 12	Expected: 2

- Glyph name: o	Contours detected: 8	Expected: 2

- Glyph name: oacute	Contours detected: 10	Expected: 3

- Glyph name: ocircumflex	Contours detected: 11	Expected: 3

- Glyph name: odieresis	Contours detected: 10	Expected: 4

- Glyph name: oe	Contours detected: 11	Expected: 3

- Glyph name: ogonek	Contours detected: 2	Expected: 1

- Glyph name: ograve	Contours detected: 10	Expected: 3

- Glyph name: ohorn	Contours detected: 11	Expected: 2

- Glyph name: ohungarumlaut	Contours detected: 12	Expected: 4

- Glyph name: omacron	Contours detected: 9	Expected: 3

- Glyph name: one	Contours detected: 7	Expected: 1

- Glyph name: oneeighth	Contours detected: 12	Expected: 5

- Glyph name: onehalf	Contours detected: 10	Expected: 3

- Glyph name: onequarter	Contours detected: 11	Expected: 3 or 4

- Glyph name: onethird	Contours detected: 10	Expected: 3

- Glyph name: ordfeminine	Contours detected: 7	Expected: 2 or 3

- Glyph name: ordmasculine	Contours detected: 7	Expected: 2 or 3

- Glyph name: oslash	Contours detected: 11	Expected: 3

- Glyph name: otilde	Contours detected: 12	Expected: 3

- Glyph name: p	Contours detected: 12	Expected: 2

- Glyph name: paragraph	Contours detected: 19	Expected: 1, 2 or 3

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: partialdiff	Contours detected: 9	Expected: 2

- Glyph name: percent	Contours detected: 9	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 11	Expected: 6 or 7

- Glyph name: peseta	Contours detected: 19	Expected: 2, 3 or 4

- Glyph name: pi	Contours detected: 9	Expected: 1

- Glyph name: plus	Contours detected: 5	Expected: 1

- Glyph name: plusminus	Contours detected: 6	Expected: 1 or 2

- Glyph name: product	Contours detected: 17	Expected: 1

- Glyph name: q	Contours detected: 12	Expected: 2

- Glyph name: question	Contours detected: 7	Expected: 2

- Glyph name: questiondown	Contours detected: 7	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: r	Contours detected: 7	Expected: 1

- Glyph name: racute	Contours detected: 9	Expected: 2

- Glyph name: radical	Contours detected: 8	Expected: 1

- Glyph name: rcaron	Contours detected: 10	Expected: 2

- Glyph name: registered	Contours detected: 20	Expected: 3 or 4

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: rupee	Contours detected: 17	Expected: 3

- Glyph name: s	Contours detected: 5	Expected: 1

- Glyph name: sacute	Contours detected: 7	Expected: 2

- Glyph name: scaron	Contours detected: 8	Expected: 2

- Glyph name: scircumflex	Contours detected: 8	Expected: 2

- Glyph name: section	Contours detected: 12	Expected: 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: seven	Contours detected: 7	Expected: 1

- Glyph name: seveneighths	Contours detected: 12	Expected: 5

- Glyph name: six	Contours detected: 9	Expected: 1 or 2

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: sterling	Contours detected: 8	Expected: 1 or 2

- Glyph name: summation	Contours detected: 9	Expected: 1

- Glyph name: t	Contours detected: 8	Expected: 1

- Glyph name: tcaron	Contours detected: 10	Expected: 2

- Glyph name: thorn	Contours detected: 14	Expected: 2

- Glyph name: three	Contours detected: 9	Expected: 1

- Glyph name: threeeighths	Contours detected: 12	Expected: 5

- Glyph name: threequarters	Contours detected: 11	Expected: 3 or 4

- Glyph name: tilde	Contours detected: 4	Expected: 1

- Glyph name: trademark	Contours detected: 16	Expected: 2

- Glyph name: triagdn	Contours detected: 7	Expected: 1

- Glyph name: triagup	Contours detected: 7	Expected: 1

- Glyph name: two	Contours detected: 8	Expected: 1

- Glyph name: twothirds	Contours detected: 10	Expected: 1 or 3

- Glyph name: u	Contours detected: 10	Expected: 1

- Glyph name: uacute	Contours detected: 12	Expected: 2

- Glyph name: ubreve	Contours detected: 13	Expected: 2

- Glyph name: ucircumflex	Contours detected: 13	Expected: 2

- Glyph name: udieresis	Contours detected: 12	Expected: 3

- Glyph name: ugrave	Contours detected: 12	Expected: 2

- Glyph name: uhorn	Contours detected: 13	Expected: 1

- Glyph name: uhungarumlaut	Contours detected: 14	Expected: 3

- Glyph name: umacron	Contours detected: 11	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni0162	Contours detected: 9	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 10	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 10	Expected: 2

- Glyph name: uni01CD	Contours detected: 15	Expected: 3

- Glyph name: uni01CE	Contours detected: 9	Expected: 3

- Glyph name: uni01CF	Contours detected: 10	Expected: 2

- Glyph name: uni01D0	Contours detected: 8	Expected: 2

- Glyph name: uni01D1	Contours detected: 15	Expected: 3

- Glyph name: uni01D2	Contours detected: 11	Expected: 3

- Glyph name: uni01D3	Contours detected: 16	Expected: 2

- Glyph name: uni01D4	Contours detected: 13	Expected: 2

- Glyph name: uni01D5	Contours detected: 14	Expected: 4

- Glyph name: uni01D6	Contours detected: 13	Expected: 4

- Glyph name: uni01D7	Contours detected: 13	Expected: 4

- Glyph name: uni01D8	Contours detected: 14	Expected: 4

- Glyph name: uni01D9	Contours detected: 14	Expected: 4

- Glyph name: uni01DA	Contours detected: 15	Expected: 4

- Glyph name: uni01DB	Contours detected: 13	Expected: 4

- Glyph name: uni01DC	Contours detected: 14	Expected: 4

- Glyph name: uni0251	Contours detected: 10	Expected: 2

- Glyph name: uni0259	Contours detected: 6	Expected: 2

- Glyph name: uni0261	Contours detected: 12	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni032E	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 11	Expected: 2

- Glyph name: uni03A9	Contours detected: 13	Expected: 1

- Glyph name: uni03BC	Contours detected: 12	Expected: 1

- Glyph name: uni1E0C	Contours detected: 13	Expected: 3

- Glyph name: uni1E0D	Contours detected: 13	Expected: 3

- Glyph name: uni1E0E	Contours detected: 13	Expected: 3

- Glyph name: uni1E0F	Contours detected: 13	Expected: 3

- Glyph name: uni1E20	Contours detected: 12	Expected: 2

- Glyph name: uni1E21	Contours detected: 13	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 14	Expected: 2

- Glyph name: uni1E25	Contours detected: 13	Expected: 2

- Glyph name: uni1E2A	Contours detected: 14	Expected: 2

- Glyph name: uni1E2B	Contours detected: 13	Expected: 2

- Glyph name: uni1E36	Contours detected: 8	Expected: 2

- Glyph name: uni1E37	Contours detected: 8	Expected: 2

- Glyph name: uni1E38	Contours detected: 9	Expected: 3

- Glyph name: uni1E39	Contours detected: 9	Expected: 3

- Glyph name: uni1E3A	Contours detected: 8	Expected: 2

- Glyph name: uni1E3B	Contours detected: 8	Expected: 2

- Glyph name: uni1E42	Contours detected: 17	Expected: 2

- Glyph name: uni1E43	Contours detected: 14	Expected: 2

- Glyph name: uni1E44	Contours detected: 16	Expected: 2

- Glyph name: uni1E45	Contours detected: 11	Expected: 2

- Glyph name: uni1E46	Contours detected: 16	Expected: 2

- Glyph name: uni1E47	Contours detected: 11	Expected: 2

- Glyph name: uni1E48	Contours detected: 16	Expected: 2

- Glyph name: uni1E49	Contours detected: 11	Expected: 2

- Glyph name: uni1E5A	Contours detected: 13	Expected: 3

- Glyph name: uni1E5B	Contours detected: 8	Expected: 2

- Glyph name: uni1E5C	Contours detected: 14	Expected: 4

- Glyph name: uni1E5D	Contours detected: 9	Expected: 3

- Glyph name: uni1E5E	Contours detected: 13	Expected: 3

- Glyph name: uni1E5F	Contours detected: 8	Expected: 2

- Glyph name: uni1E60	Contours detected: 10	Expected: 2

- Glyph name: uni1E61	Contours detected: 6	Expected: 2

- Glyph name: uni1E62	Contours detected: 10	Expected: 2

- Glyph name: uni1E63	Contours detected: 6	Expected: 2

- Glyph name: uni1E6C	Contours detected: 8	Expected: 2

- Glyph name: uni1E6D	Contours detected: 9	Expected: 2

- Glyph name: uni1E6E	Contours detected: 8	Expected: 2

- Glyph name: uni1E6F	Contours detected: 9	Expected: 2

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 13	Expected: 2

- Glyph name: uni1E92	Contours detected: 8	Expected: 2

- Glyph name: uni1E93	Contours detected: 6	Expected: 2

- Glyph name: uni1E97	Contours detected: 10	Expected: 3

- Glyph name: uni2117	Contours detected: 19	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 15	Expected: 2

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 12	Expected: 1

- Glyph name: uring	Contours detected: 14	Expected: 3

- Glyph name: utilde	Contours detected: 14	Expected: 2

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 12	Expected: 1

- Glyph name: yacute	Contours detected: 14	Expected: 2

- Glyph name: ycircumflex	Contours detected: 15	Expected: 2

- Glyph name: ydieresis	Contours detected: 14	Expected: 3

- Glyph name: yen	Contours detected: 9	Expected: 1 or 2

- Glyph name: ygrave	Contours detected: 14	Expected: 2

- Glyph name: z	Contours detected: 5	Expected: 1

- Glyph name: zacute	Contours detected: 7	Expected: 2

- Glyph name: zcaron	Contours detected: 8	Expected: 2

- Glyph name: zdotaccent	Contours detected: 6	Expected: 2

- Glyph name: zero	Contours detected: 13	Expected: 2 or 3
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Heiltsuk (Latn, 300 speakers), Ekpeye (Latn, 226,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ejagham (Latn, 120,000 speakers), Mango (Latn, 77,000 speakers), Ma’di (Latn, 584,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Dan (Latn, 1,099,244 speakers), Mfumte (Latn, 79,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Makaa (Latn, 221,000 speakers), Kaska (Latn, 125 speakers), Belarusian (Cyrl, 10,064,517 speakers), Fur (Latn, 1,230,163 speakers), Aghem (Latn, 38,843 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Teke-Ebo (Latn, 260,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Yala (Latn, 200,000 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Lugbara (Latn, 2,200,000 speakers), Gulay (Latn, 250,478 speakers), Nateni (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), South Central Banda (Latn, 244,000 speakers), Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Han (Latn, 6 speakers).</p>
 [code: soft-dotted]



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

<details><summary>[10] MatrixSansVideoSC-Regular.ttf</summary>
<div>
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

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: Scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: ohornacute	Contours detected: 4	Expected: 3

- Glyph name: ohorngrave	Contours detected: 4	Expected: 3

- Glyph name: ohornhookabove	Contours detected: 4	Expected: 3

- Glyph name: ohorntilde	Contours detected: 4	Expected: 3

- Glyph name: ohorndotbelow	Contours detected: 4	Expected: 3

- Glyph name: Uhornacute	Contours detected: 3	Expected: 2

- Glyph name: uhornacute	Contours detected: 3	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 3	Expected: 2

- Glyph name: uhorntilde	Contours detected: 3	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 3	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 3	Expected: 2

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: won	Contours detected: 5	Expected: 1, 3, 4 or 7

- Glyph name: peso	Contours detected: 3	Expected: 1, 2 or 4

- Glyph name: onethird	Contours detected: 2	Expected: 3

- Glyph name: twothirds	Contours detected: 2	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 4	Expected: 5

- Glyph name: threeeighths	Contours detected: 4	Expected: 5

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

- Glyph name: seveneighths	Contours detected: 4	Expected: 5

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

- Glyph name: ohorn	Contours detected: 3	Expected: 2

- Glyph name: oneeighth	Contours detected: 4	Expected: 5

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: onethird	Contours detected: 2	Expected: 3

- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: seveneighths	Contours detected: 4	Expected: 5

- Glyph name: threeeighths	Contours detected: 4	Expected: 5

- Glyph name: twothirds	Contours detected: 2	Expected: 1 or 3

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 3	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



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

<details><summary>[10] MatrixSansScreen-Regular.ttf</summary>
<div>
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

- Glyph name: plus	Contours detected: 9	Expected: 1

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: hyphen	Contours detected: 4	Expected: 1

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: zero	Contours detected: 19	Expected: 2 or 3

- Glyph name: one	Contours detected: 10	Expected: 1

- Glyph name: two	Contours detected: 15	Expected: 1

- Glyph name: three	Contours detected: 14	Expected: 1

- Glyph name: four	Contours detected: 14	Expected: 1 or 2

- Glyph name: five	Contours detected: 17	Expected: 1

- Glyph name: six	Contours detected: 15	Expected: 1 or 2

- Glyph name: seven	Contours detected: 11	Expected: 1

- Glyph name: eight	Contours detected: 17	Expected: 3

- Glyph name: nine	Contours detected: 15	Expected: 1 or 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: equal	Contours detected: 10	Expected: 2

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: question	Contours detected: 10	Expected: 2

- Glyph name: at	Contours detected: 20	Expected: 2

- Glyph name: A	Contours detected: 16	Expected: 2

- Glyph name: B	Contours detected: 20	Expected: 2 or 3

- Glyph name: C	Contours detected: 13	Expected: 1

- Glyph name: D	Contours detected: 16	Expected: 2

- Glyph name: E	Contours detected: 18	Expected: 1

- Glyph name: F	Contours detected: 14	Expected: 1

- Glyph name: G	Contours detected: 17	Expected: 1

- Glyph name: H	Contours detected: 17	Expected: 1

- Glyph name: I	Contours detected: 11	Expected: 1

- Glyph name: J	Contours detected: 11	Expected: 1

- Glyph name: K	Contours detected: 14	Expected: 1 or 2

- Glyph name: L	Contours detected: 11	Expected: 1

- Glyph name: M	Contours detected: 18	Expected: 1

- Glyph name: N	Contours detected: 17	Expected: 1

- Glyph name: O	Contours detected: 16	Expected: 2

- Glyph name: P	Contours detected: 15	Expected: 1 or 2

- Glyph name: Q	Contours detected: 17	Expected: 2

- Glyph name: R	Contours detected: 18	Expected: 1 or 2

- Glyph name: S	Contours detected: 15	Expected: 1

- Glyph name: T	Contours detected: 11	Expected: 1

- Glyph name: U	Contours detected: 15	Expected: 1

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Z	Contours detected: 15	Expected: 1

- Glyph name: bracketleft	Contours detected: 11	Expected: 1

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bracketright	Contours detected: 11	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: underscore	Contours detected: 6	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 14	Expected: 2

- Glyph name: b	Contours detected: 16	Expected: 2

- Glyph name: c	Contours detected: 11	Expected: 1

- Glyph name: d	Contours detected: 16	Expected: 2

- Glyph name: e	Contours detected: 14	Expected: 2

- Glyph name: f	Contours detected: 12	Expected: 1

- Glyph name: g	Contours detected: 18	Expected: 2 or 3

- Glyph name: h	Contours detected: 14	Expected: 1

- Glyph name: i	Contours detected: 9	Expected: 2

- Glyph name: j	Contours detected: 11	Expected: 2

- Glyph name: k	Contours detected: 13	Expected: 1 or 2

- Glyph name: l	Contours detected: 10	Expected: 1

- Glyph name: m	Contours detected: 14	Expected: 1

- Glyph name: n	Contours detected: 12	Expected: 1

- Glyph name: o	Contours detected: 12	Expected: 2

- Glyph name: p	Contours detected: 16	Expected: 2

- Glyph name: q	Contours detected: 16	Expected: 2

- Glyph name: r	Contours detected: 9	Expected: 1

- Glyph name: s	Contours detected: 13	Expected: 1

- Glyph name: t	Contours detected: 12	Expected: 1

- Glyph name: u	Contours detected: 12	Expected: 1

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 16	Expected: 1

- Glyph name: z	Contours detected: 13	Expected: 1

- Glyph name: braceleft	Contours detected: 10	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceright	Contours detected: 10	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: cent	Contours detected: 16	Expected: 1 or 2

- Glyph name: sterling	Contours detected: 15	Expected: 1 or 2

- Glyph name: currency	Contours detected: 12	Expected: 2

- Glyph name: yen	Contours detected: 13	Expected: 1 or 2

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: section	Contours detected: 20	Expected: 2

- Glyph name: copyright	Contours detected: 26	Expected: 3

- Glyph name: ordfeminine	Contours detected: 14	Expected: 2 or 3

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: logicalnot	Contours detected: 7	Expected: 1

- Glyph name: uni00AD	Contours detected: 4	Expected: 0

- Glyph name: registered	Contours detected: 30	Expected: 3 or 4

- Glyph name: macron	Contours detected: 3	Expected: 1

- Glyph name: degree	Contours detected: 8	Expected: 2

- Glyph name: plusminus	Contours detected: 14	Expected: 1 or 2

- Glyph name: twosuperior	Contours detected: 8	Expected: 1

- Glyph name: threesuperior	Contours detected: 8	Expected: 1

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: micro	Contours detected: 14	Expected: 1

- Glyph name: paragraph	Contours detected: 23	Expected: 1, 2 or 3

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: onesuperior	Contours detected: 8	Expected: 1

- Glyph name: ordmasculine	Contours detected: 12	Expected: 2 or 3

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: onequarter	Contours detected: 17	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 16	Expected: 3

- Glyph name: threequarters	Contours detected: 17	Expected: 3 or 4

- Glyph name: questiondown	Contours detected: 10	Expected: 2

- Glyph name: Agrave	Contours detected: 18	Expected: 3

- Glyph name: Aacute	Contours detected: 18	Expected: 3

- Glyph name: Acircumflex	Contours detected: 19	Expected: 3

- Glyph name: Atilde	Contours detected: 22	Expected: 3

- Glyph name: Adieresis	Contours detected: 18	Expected: 4

- Glyph name: Aring	Contours detected: 20	Expected: 3 or 4

- Glyph name: AE	Contours detected: 24	Expected: 2

- Glyph name: Ccedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Egrave	Contours detected: 20	Expected: 2

- Glyph name: Eacute	Contours detected: 20	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 21	Expected: 2

- Glyph name: Edieresis	Contours detected: 20	Expected: 3

- Glyph name: Igrave	Contours detected: 13	Expected: 2

- Glyph name: Iacute	Contours detected: 13	Expected: 2

- Glyph name: Icircumflex	Contours detected: 14	Expected: 2

- Glyph name: Idieresis	Contours detected: 13	Expected: 3

- Glyph name: Eth	Contours detected: 18	Expected: 2

- Glyph name: Ntilde	Contours detected: 23	Expected: 2

- Glyph name: Ograve	Contours detected: 18	Expected: 3

- Glyph name: Oacute	Contours detected: 18	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 19	Expected: 3

- Glyph name: Otilde	Contours detected: 22	Expected: 3

- Glyph name: Odieresis	Contours detected: 18	Expected: 4

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: Oslash	Contours detected: 17	Expected: 2 or 3

- Glyph name: Ugrave	Contours detected: 17	Expected: 2

- Glyph name: Uacute	Contours detected: 17	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 18	Expected: 2

- Glyph name: Udieresis	Contours detected: 17	Expected: 3

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Thorn	Contours detected: 16	Expected: 1 or 2

- Glyph name: germandbls	Contours detected: 16	Expected: 1

- Glyph name: agrave	Contours detected: 16	Expected: 3

- Glyph name: aacute	Contours detected: 16	Expected: 3

- Glyph name: acircumflex	Contours detected: 17	Expected: 3

- Glyph name: atilde	Contours detected: 20	Expected: 3

- Glyph name: adieresis	Contours detected: 16	Expected: 4

- Glyph name: aring	Contours detected: 18	Expected: 4

- Glyph name: ae	Contours detected: 18	Expected: 3

- Glyph name: ccedilla	Contours detected: 14	Expected: 1 or 2

- Glyph name: egrave	Contours detected: 16	Expected: 3

- Glyph name: eacute	Contours detected: 16	Expected: 3

- Glyph name: ecircumflex	Contours detected: 17	Expected: 3

- Glyph name: edieresis	Contours detected: 16	Expected: 4

- Glyph name: igrave	Contours detected: 10	Expected: 2

- Glyph name: iacute	Contours detected: 10	Expected: 2

- Glyph name: icircumflex	Contours detected: 11	Expected: 2

- Glyph name: idieresis	Contours detected: 10	Expected: 3

- Glyph name: eth	Contours detected: 16	Expected: 2

- Glyph name: ntilde	Contours detected: 18	Expected: 2

- Glyph name: ograve	Contours detected: 14	Expected: 3

- Glyph name: oacute	Contours detected: 14	Expected: 3

- Glyph name: ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: otilde	Contours detected: 18	Expected: 3

- Glyph name: odieresis	Contours detected: 14	Expected: 4

- Glyph name: divide	Contours detected: 7	Expected: 3

- Glyph name: oslash	Contours detected: 13	Expected: 3

- Glyph name: ugrave	Contours detected: 14	Expected: 2

- Glyph name: uacute	Contours detected: 14	Expected: 2

- Glyph name: ucircumflex	Contours detected: 15	Expected: 2

- Glyph name: udieresis	Contours detected: 14	Expected: 3

- Glyph name: yacute	Contours detected: 18	Expected: 2

- Glyph name: thorn	Contours detected: 18	Expected: 2

- Glyph name: ydieresis	Contours detected: 18	Expected: 3

- Glyph name: Amacron	Contours detected: 19	Expected: 3

- Glyph name: amacron	Contours detected: 17	Expected: 3

- Glyph name: Abreve	Contours detected: 21	Expected: 3

- Glyph name: abreve	Contours detected: 19	Expected: 3

- Glyph name: Aogonek	Contours detected: 19	Expected: 2 or 3

- Glyph name: aogonek	Contours detected: 17	Expected: 2

- Glyph name: Cacute	Contours detected: 15	Expected: 2

- Glyph name: cacute	Contours detected: 13	Expected: 2

- Glyph name: Ccircumflex	Contours detected: 16	Expected: 2

- Glyph name: ccircumflex	Contours detected: 14	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 14	Expected: 2

- Glyph name: cdotaccent	Contours detected: 12	Expected: 2

- Glyph name: Ccaron	Contours detected: 16	Expected: 2

- Glyph name: ccaron	Contours detected: 14	Expected: 2

- Glyph name: Dcaron	Contours detected: 19	Expected: 3

- Glyph name: dcaron	Contours detected: 18	Expected: 3

- Glyph name: Dcroat	Contours detected: 18	Expected: 2

- Glyph name: dcroat	Contours detected: 18	Expected: 2

- Glyph name: Emacron	Contours detected: 21	Expected: 2

- Glyph name: emacron	Contours detected: 17	Expected: 3

- Glyph name: Ebreve	Contours detected: 23	Expected: 2

- Glyph name: ebreve	Contours detected: 19	Expected: 3

- Glyph name: Edotaccent	Contours detected: 19	Expected: 2

- Glyph name: edotaccent	Contours detected: 15	Expected: 3

- Glyph name: Eogonek	Contours detected: 21	Expected: 1 or 2

- Glyph name: eogonek	Contours detected: 17	Expected: 2

- Glyph name: Ecaron	Contours detected: 21	Expected: 2

- Glyph name: ecaron	Contours detected: 17	Expected: 3

- Glyph name: Gcircumflex	Contours detected: 20	Expected: 2

- Glyph name: gcircumflex	Contours detected: 21	Expected: 3 or 4

- Glyph name: Gbreve	Contours detected: 22	Expected: 2

- Glyph name: gbreve	Contours detected: 23	Expected: 3 or 4

- Glyph name: Gdotaccent	Contours detected: 18	Expected: 2

- Glyph name: gdotaccent	Contours detected: 19	Expected: 3 or 4

- Glyph name: Gcommaaccent	Contours detected: 19	Expected: 2

- Glyph name: gcommaaccent	Contours detected: 20	Expected: 3 or 4

- Glyph name: Hcircumflex	Contours detected: 20	Expected: 2

- Glyph name: hcircumflex	Contours detected: 17	Expected: 2

- Glyph name: Hbar	Contours detected: 20	Expected: 2

- Glyph name: hbar	Contours detected: 16	Expected: 1

- Glyph name: Itilde	Contours detected: 17	Expected: 2

- Glyph name: itilde	Contours detected: 14	Expected: 2

- Glyph name: Imacron	Contours detected: 14	Expected: 2

- Glyph name: imacron	Contours detected: 11	Expected: 2

- Glyph name: Iogonek	Contours detected: 14	Expected: 1 or 2

- Glyph name: iogonek	Contours detected: 12	Expected: 2 or 3

- Glyph name: Idotaccent	Contours detected: 12	Expected: 2

- Glyph name: dotlessi	Contours detected: 8	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: ij	Contours detected: 19	Expected: 3 or 4

- Glyph name: Jcircumflex	Contours detected: 14	Expected: 2

- Glyph name: jcircumflex	Contours detected: 13	Expected: 2

- Glyph name: Kcommaaccent	Contours detected: 16	Expected: 2 or 3

- Glyph name: kcommaaccent	Contours detected: 15	Expected: 2 or 3

- Glyph name: kgreenlandic	Contours detected: 11	Expected: 1 or 2

- Glyph name: Lacute	Contours detected: 13	Expected: 2

- Glyph name: lacute	Contours detected: 12	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 12	Expected: 2

- Glyph name: Lcaron	Contours detected: 13	Expected: 2

- Glyph name: lcaron	Contours detected: 12	Expected: 2

- Glyph name: Ldot	Contours detected: 12	Expected: 2

- Glyph name: ldot	Contours detected: 11	Expected: 2

- Glyph name: Lslash	Contours detected: 13	Expected: 1

- Glyph name: lslash	Contours detected: 12	Expected: 1

- Glyph name: Nacute	Contours detected: 19	Expected: 2

- Glyph name: nacute	Contours detected: 14	Expected: 2

- Glyph name: Ncommaaccent	Contours detected: 19	Expected: 2

- Glyph name: ncommaaccent	Contours detected: 14	Expected: 2

- Glyph name: Ncaron	Contours detected: 20	Expected: 2

- Glyph name: ncaron	Contours detected: 15	Expected: 2

- Glyph name: napostrophe	Contours detected: 15	Expected: 2

- Glyph name: Eng	Contours detected: 19	Expected: 1

- Glyph name: eng	Contours detected: 15	Expected: 1

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: Ohungarumlaut	Contours detected: 20	Expected: 4

- Glyph name: ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: OE	Contours detected: 24	Expected: 2

- Glyph name: oe	Contours detected: 18	Expected: 3

- Glyph name: Racute	Contours detected: 20	Expected: 3

- Glyph name: racute	Contours detected: 11	Expected: 2

- Glyph name: Rcommaaccent	Contours detected: 20	Expected: 3

- Glyph name: rcommaaccent	Contours detected: 11	Expected: 2

- Glyph name: Rcaron	Contours detected: 21	Expected: 3

- Glyph name: rcaron	Contours detected: 12	Expected: 2

- Glyph name: Sacute	Contours detected: 17	Expected: 2

- Glyph name: sacute	Contours detected: 15	Expected: 2

- Glyph name: Scircumflex	Contours detected: 18	Expected: 2

- Glyph name: scircumflex	Contours detected: 16	Expected: 2

- Glyph name: Scedilla	Contours detected: 18	Expected: 1 or 2

- Glyph name: scedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Scaron	Contours detected: 18	Expected: 2

- Glyph name: scaron	Contours detected: 16	Expected: 2

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: Tcaron	Contours detected: 14	Expected: 2

- Glyph name: tcaron	Contours detected: 14	Expected: 2

- Glyph name: Utilde	Contours detected: 21	Expected: 2

- Glyph name: utilde	Contours detected: 18	Expected: 2

- Glyph name: Umacron	Contours detected: 18	Expected: 2

- Glyph name: umacron	Contours detected: 15	Expected: 2

- Glyph name: Ubreve	Contours detected: 20	Expected: 2

- Glyph name: ubreve	Contours detected: 17	Expected: 2

- Glyph name: Uring	Contours detected: 19	Expected: 3

- Glyph name: uring	Contours detected: 16	Expected: 3

- Glyph name: Uhungarumlaut	Contours detected: 19	Expected: 3

- Glyph name: uhungarumlaut	Contours detected: 16	Expected: 3

- Glyph name: Uogonek	Contours detected: 18	Expected: 1

- Glyph name: uogonek	Contours detected: 15	Expected: 1

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: ycircumflex	Contours detected: 19	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Zacute	Contours detected: 17	Expected: 2

- Glyph name: zacute	Contours detected: 15	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 16	Expected: 2

- Glyph name: zdotaccent	Contours detected: 14	Expected: 2

- Glyph name: Zcaron	Contours detected: 18	Expected: 2

- Glyph name: zcaron	Contours detected: 16	Expected: 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: florin	Contours detected: 14	Expected: 1

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: uni01CD	Contours detected: 19	Expected: 3

- Glyph name: uni01CE	Contours detected: 17	Expected: 3

- Glyph name: uni01CF	Contours detected: 14	Expected: 2

- Glyph name: uni01D0	Contours detected: 11	Expected: 2

- Glyph name: uni01D1	Contours detected: 19	Expected: 3

- Glyph name: uni01D2	Contours detected: 15	Expected: 3

- Glyph name: uni01D3	Contours detected: 18	Expected: 2

- Glyph name: uni01D4	Contours detected: 15	Expected: 2

- Glyph name: uni01D5	Contours detected: 18	Expected: 4

- Glyph name: uni01D6	Contours detected: 17	Expected: 4

- Glyph name: uni01D7	Contours detected: 15	Expected: 4

- Glyph name: uni01D8	Contours detected: 16	Expected: 4

- Glyph name: uni01D9	Contours detected: 16	Expected: 4

- Glyph name: uni01DA	Contours detected: 17	Expected: 4

- Glyph name: uni01DB	Contours detected: 15	Expected: 4

- Glyph name: uni01DC	Contours detected: 16	Expected: 4

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Scommaaccent	Contours detected: 17	Expected: 2

- Glyph name: scommaaccent	Contours detected: 15	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 14	Expected: 2

- Glyph name: jdotless	Contours detected: 10	Expected: 1

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: breve	Contours detected: 5	Expected: 1

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: ogonek	Contours detected: 3	Expected: 1

- Glyph name: tilde	Contours detected: 6	Expected: 1

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: gravecomb	Contours detected: 2	Expected: 1

- Glyph name: acutecomb	Contours detected: 2	Expected: 1

- Glyph name: circumflexcomb	Contours detected: 3	Expected: 1

- Glyph name: tildecomb	Contours detected: 6	Expected: 1

- Glyph name: macroncomb	Contours detected: 3	Expected: 1

- Glyph name: brevecomb	Contours detected: 5	Expected: 1

- Glyph name: hookabovecomb	Contours detected: 3	Expected: 1

- Glyph name: ringcomb	Contours detected: 4	Expected: 2

- Glyph name: hungarumlautcomb	Contours detected: 4	Expected: 2

- Glyph name: caroncomb	Contours detected: 3	Expected: 1

- Glyph name: commaturnedabovecomb	Contours detected: 2	Expected: 1

- Glyph name: horncomb	Contours detected: 3	Expected: 1

- Glyph name: commaaccentcomb	Contours detected: 2	Expected: 1

- Glyph name: cedillacomb	Contours detected: 3	Expected: 1

- Glyph name: ogonekcomb	Contours detected: 3	Expected: 1

- Glyph name: uni032E	Contours detected: 5	Expected: 1

- Glyph name: uni0331	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: baht	Contours detected: 20	Expected: 3 or 5

- Glyph name: uni1E0C	Contours detected: 17	Expected: 3

- Glyph name: uni1E0D	Contours detected: 17	Expected: 3

- Glyph name: uni1E0E	Contours detected: 19	Expected: 3

- Glyph name: uni1E0F	Contours detected: 19	Expected: 3

- Glyph name: uni1E20	Contours detected: 20	Expected: 2

- Glyph name: uni1E21	Contours detected: 21	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 18	Expected: 2

- Glyph name: uni1E25	Contours detected: 15	Expected: 2

- Glyph name: uni1E2A	Contours detected: 20	Expected: 2

- Glyph name: uni1E2B	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: uni1E44	Contours detected: 18	Expected: 2

- Glyph name: uni1E45	Contours detected: 13	Expected: 2

- Glyph name: uni1E46	Contours detected: 18	Expected: 2

- Glyph name: uni1E47	Contours detected: 13	Expected: 2

- Glyph name: uni1E48	Contours detected: 20	Expected: 2

- Glyph name: uni1E49	Contours detected: 15	Expected: 2

- Glyph name: uni1E5A	Contours detected: 19	Expected: 3

- Glyph name: uni1E5B	Contours detected: 10	Expected: 2

- Glyph name: uni1E5C	Contours detected: 22	Expected: 4

- Glyph name: uni1E5D	Contours detected: 13	Expected: 3

- Glyph name: uni1E5E	Contours detected: 21	Expected: 3

- Glyph name: uni1E5F	Contours detected: 12	Expected: 2

- Glyph name: uni1E60	Contours detected: 16	Expected: 2

- Glyph name: uni1E61	Contours detected: 14	Expected: 2

- Glyph name: uni1E62	Contours detected: 16	Expected: 2

- Glyph name: uni1E63	Contours detected: 14	Expected: 2

- Glyph name: uni1E6C	Contours detected: 12	Expected: 2

- Glyph name: uni1E6D	Contours detected: 13	Expected: 2

- Glyph name: uni1E6E	Contours detected: 14	Expected: 2

- Glyph name: uni1E6F	Contours detected: 15	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: uni1E92	Contours detected: 16	Expected: 2

- Glyph name: uni1E93	Contours detected: 14	Expected: 2

- Glyph name: uni1E97	Contours detected: 14	Expected: 3

- Glyph name: Germandbls	Contours detected: 18	Expected: 1

- Glyph name: Adotbelow	Contours detected: 17	Expected: 3

- Glyph name: adotbelow	Contours detected: 15	Expected: 3

- Glyph name: Ahookabove	Contours detected: 19	Expected: 3

- Glyph name: ahookabove	Contours detected: 17	Expected: 3

- Glyph name: Acircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: acircumflexacute	Contours detected: 19	Expected: 4

- Glyph name: Acircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: acircumflexgrave	Contours detected: 19	Expected: 4

- Glyph name: Acircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: acircumflexhookabove	Contours detected: 20	Expected: 4

- Glyph name: Acircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: acircumflextilde	Contours detected: 23	Expected: 4

- Glyph name: Acircumflexdotbelow	Contours detected: 20	Expected: 4

- Glyph name: acircumflexdotbelow	Contours detected: 18	Expected: 4

- Glyph name: Abreveacute	Contours detected: 19	Expected: 4

- Glyph name: abreveacute	Contours detected: 21	Expected: 4

- Glyph name: Abrevegrave	Contours detected: 19	Expected: 4

- Glyph name: abrevegrave	Contours detected: 21	Expected: 4

- Glyph name: Abrevehookabove	Contours detected: 20	Expected: 4

- Glyph name: abrevehookabove	Contours detected: 22	Expected: 4

- Glyph name: Abrevetilde	Contours detected: 23	Expected: 4

- Glyph name: abrevetilde	Contours detected: 25	Expected: 4

- Glyph name: Abrevedotbelow	Contours detected: 22	Expected: 4

- Glyph name: abrevedotbelow	Contours detected: 20	Expected: 4

- Glyph name: Edotbelow	Contours detected: 19	Expected: 2

- Glyph name: edotbelow	Contours detected: 15	Expected: 3

- Glyph name: Ehookabove	Contours detected: 21	Expected: 2

- Glyph name: ehookabove	Contours detected: 17	Expected: 3

- Glyph name: Etilde	Contours detected: 24	Expected: 2

- Glyph name: etilde	Contours detected: 20	Expected: 3

- Glyph name: Ecircumflexacute	Contours detected: 21	Expected: 3

- Glyph name: ecircumflexacute	Contours detected: 19	Expected: 4

- Glyph name: Ecircumflexgrave	Contours detected: 21	Expected: 3

- Glyph name: ecircumflexgrave	Contours detected: 19	Expected: 4

- Glyph name: Ecircumflexhookabove	Contours detected: 22	Expected: 3

- Glyph name: ecircumflexhookabove	Contours detected: 20	Expected: 4

- Glyph name: Ecircumflextilde	Contours detected: 25	Expected: 3

- Glyph name: ecircumflextilde	Contours detected: 23	Expected: 4

- Glyph name: Ecircumflexdotbelow	Contours detected: 22	Expected: 3

- Glyph name: ecircumflexdotbelow	Contours detected: 18	Expected: 4

- Glyph name: Ihookabove	Contours detected: 14	Expected: 2

- Glyph name: ihookabove	Contours detected: 11	Expected: 2

- Glyph name: Idotbelow	Contours detected: 12	Expected: 2

- Glyph name: idotbelow	Contours detected: 10	Expected: 3

- Glyph name: Odotbelow	Contours detected: 17	Expected: 3

- Glyph name: odotbelow	Contours detected: 13	Expected: 3

- Glyph name: Ohookabove	Contours detected: 19	Expected: 3

- Glyph name: ohookabove	Contours detected: 15	Expected: 3

- Glyph name: Ocircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: ocircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: Ocircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: ocircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: Ocircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: ocircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: Ocircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: ocircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: Ocircumflexdotbelow	Contours detected: 20	Expected: 4

- Glyph name: ocircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: Ohornacute	Contours detected: 21	Expected: 3 or 4

- Glyph name: ohornacute	Contours detected: 17	Expected: 3

- Glyph name: Ohorngrave	Contours detected: 21	Expected: 3 or 4

- Glyph name: ohorngrave	Contours detected: 17	Expected: 3

- Glyph name: Ohornhookabove	Contours detected: 22	Expected: 3 or 4

- Glyph name: ohornhookabove	Contours detected: 18	Expected: 3

- Glyph name: Ohorntilde	Contours detected: 25	Expected: 3 or 4

- Glyph name: ohorntilde	Contours detected: 21	Expected: 3

- Glyph name: Ohorndotbelow	Contours detected: 20	Expected: 3 or 4

- Glyph name: ohorndotbelow	Contours detected: 16	Expected: 3

- Glyph name: Udotbelow	Contours detected: 16	Expected: 2

- Glyph name: udotbelow	Contours detected: 13	Expected: 2

- Glyph name: Uhookabove	Contours detected: 18	Expected: 2

- Glyph name: uhookabove	Contours detected: 15	Expected: 2

- Glyph name: Uhornacute	Contours detected: 20	Expected: 2

- Glyph name: uhornacute	Contours detected: 17	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 20	Expected: 2

- Glyph name: uhorngrave	Contours detected: 17	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 21	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 18	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 24	Expected: 2

- Glyph name: uhorntilde	Contours detected: 21	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 19	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 16	Expected: 2

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: ygrave	Contours detected: 18	Expected: 2

- Glyph name: Ydotbelow	Contours detected: 11	Expected: 2

- Glyph name: ydotbelow	Contours detected: 13	Expected: 2

- Glyph name: Yhookabove	Contours detected: 13	Expected: 2

- Glyph name: yhookabove	Contours detected: 19	Expected: 2

- Glyph name: Ytilde	Contours detected: 16	Expected: 2

- Glyph name: ytilde	Contours detected: 22	Expected: 2

- Glyph name: uni2010	Contours detected: 4	Expected: 1

- Glyph name: uni2011	Contours detected: 4	Expected: 1

- Glyph name: figuredash	Contours detected: 5	Expected: 1

- Glyph name: endash	Contours detected: 5	Expected: 1

- Glyph name: emdash	Contours detected: 6	Expected: 1

- Glyph name: uni2015	Contours detected: 6	Expected: 1

- Glyph name: dblverticalbar	Contours detected: 14	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: dagger	Contours detected: 13	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 17	Expected: 1 or 3

- Glyph name: bullet	Contours detected: 9	Expected: 1

- Glyph name: perthousand	Contours detected: 17	Expected: 6 or 7

- Glyph name: minute	Contours detected: 3	Expected: 1

- Glyph name: second	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: uni2070	Contours detected: 8	Expected: 2 or 3

- Glyph name: foursuperior	Contours detected: 9	Expected: 1 or 2

- Glyph name: fivesuperior	Contours detected: 9	Expected: 1

- Glyph name: sixsuperior	Contours detected: 8	Expected: 2

- Glyph name: sevensuperior	Contours detected: 7	Expected: 1

- Glyph name: eightsuperior	Contours detected: 13	Expected: 3

- Glyph name: ninesuperior	Contours detected: 8	Expected: 2

- Glyph name: uni207D	Contours detected: 5	Expected: 1

- Glyph name: uni207E	Contours detected: 5	Expected: 1

- Glyph name: uni207F	Contours detected: 8	Expected: 1

- Glyph name: uni2080	Contours detected: 8	Expected: 2 or 3

- Glyph name: oneinferior	Contours detected: 8	Expected: 1

- Glyph name: twoinferior	Contours detected: 8	Expected: 1

- Glyph name: threeinferior	Contours detected: 8	Expected: 1

- Glyph name: fourinferior	Contours detected: 9	Expected: 1 or 2

- Glyph name: fiveinferior	Contours detected: 9	Expected: 1

- Glyph name: sixinferior	Contours detected: 8	Expected: 2

- Glyph name: seveninferior	Contours detected: 7	Expected: 1

- Glyph name: eightinferior	Contours detected: 13	Expected: 3

- Glyph name: nineinferior	Contours detected: 8	Expected: 2

- Glyph name: uni208D	Contours detected: 5	Expected: 1

- Glyph name: uni208E	Contours detected: 5	Expected: 1

- Glyph name: colonmonetary	Contours detected: 16	Expected: 1 or 3

- Glyph name: lira	Contours detected: 17	Expected: 1

- Glyph name: naira	Contours detected: 26	Expected: 1, 3 or 5

- Glyph name: peseta	Contours detected: 26	Expected: 2, 3 or 4

- Glyph name: rupee	Contours detected: 23	Expected: 3

- Glyph name: won	Contours detected: 26	Expected: 1, 3, 4 or 7

- Glyph name: sheqel	Contours detected: 24	Expected: 2

- Glyph name: dong	Contours detected: 23	Expected: 3 or 4

- Glyph name: Euro	Contours detected: 15	Expected: 1 or 2

- Glyph name: kip	Contours detected: 17	Expected: 1

- Glyph name: tugrik	Contours detected: 15	Expected: 1

- Glyph name: peso	Contours detected: 15	Expected: 1, 2 or 4

- Glyph name: guarani	Contours detected: 19	Expected: 1, 2 or 3

- Glyph name: hryvnia	Contours detected: 17	Expected: 1 or 2

- Glyph name: cedi	Contours detected: 16	Expected: 1 or 2

- Glyph name: tenge	Contours detected: 14	Expected: 2

- Glyph name: rupeeIndian	Contours detected: 17	Expected: 1

- Glyph name: liraTurkish	Contours detected: 15	Expected: 1

- Glyph name: manat	Contours detected: 17	Expected: 1

- Glyph name: ruble	Contours detected: 16	Expected: 2

- Glyph name: bitcoin	Contours detected: 20	Expected: 3

- Glyph name: literSign	Contours detected: 13	Expected: 2

- Glyph name: numero	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2117	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 18	Expected: 2

- Glyph name: trademark	Contours detected: 18	Expected: 2

- Glyph name: Ohm	Contours detected: 17	Expected: 1

- Glyph name: onethird	Contours detected: 16	Expected: 3

- Glyph name: twothirds	Contours detected: 16	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 21	Expected: 5

- Glyph name: threeeighths	Contours detected: 21	Expected: 5

- Glyph name: fiveeighths	Contours detected: 22	Expected: 5

- Glyph name: seveneighths	Contours detected: 20	Expected: 5

- Glyph name: arrowleft	Contours detected: 11	Expected: 1

- Glyph name: arrowup	Contours detected: 11	Expected: 1

- Glyph name: arrowright	Contours detected: 11	Expected: 1

- Glyph name: arrowdown	Contours detected: 11	Expected: 1

- Glyph name: arrowboth	Contours detected: 15	Expected: 1

- Glyph name: arrowupdn	Contours detected: 15	Expected: 1

- Glyph name: northWestArrow	Contours detected: 12	Expected: 1

- Glyph name: northEastArrow	Contours detected: 12	Expected: 1

- Glyph name: southEastArrow	Contours detected: 12	Expected: 1

- Glyph name: southWestArrow	Contours detected: 12	Expected: 1

- Glyph name: partialdiff	Contours detected: 15	Expected: 2

- Glyph name: emptyset	Contours detected: 21	Expected: 3

- Glyph name: increment	Contours detected: 15	Expected: 2

- Glyph name: product	Contours detected: 21	Expected: 1

- Glyph name: summation	Contours detected: 17	Expected: 1

- Glyph name: minus	Contours detected: 5	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 11	Expected: 1

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: approxequal	Contours detected: 12	Expected: 2

- Glyph name: notequal	Contours detected: 15	Expected: 1

- Glyph name: lessequal	Contours detected: 8	Expected: 2

- Glyph name: greaterequal	Contours detected: 8	Expected: 2

- Glyph name: filledbox	Contours detected: 42	Expected: 1

- Glyph name: whiteSquare	Contours detected: 24	Expected: 2

- Glyph name: blackSmallSquare	Contours detected: 9	Expected: 1

- Glyph name: whiteSmallSquare	Contours detected: 8	Expected: 2

- Glyph name: triagup	Contours detected: 31	Expected: 1

- Glyph name: upWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: rightBlackTriangle	Contours detected: 31	Expected: 1

- Glyph name: rightWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: triagdn	Contours detected: 31	Expected: 1

- Glyph name: downWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: leftBlackTriangle	Contours detected: 31	Expected: 1

- Glyph name: leftWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: blackDiamond	Contours detected: 25	Expected: 1

- Glyph name: whiteDiamond	Contours detected: 12	Expected: 2

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: circle	Contours detected: 16	Expected: 2

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: blackCircle	Contours detected: 37	Expected: 1

- Glyph name: leftanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: rightanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: uniFB01	Contours detected: 16	Expected: 1, 2 or 3

- Glyph name: uniFB02	Contours detected: 17	Expected: 1 or 2

- Glyph name: A	Contours detected: 16	Expected: 2

- Glyph name: AE	Contours detected: 24	Expected: 2

- Glyph name: Aacute	Contours detected: 18	Expected: 3

- Glyph name: Abreve	Contours detected: 21	Expected: 3

- Glyph name: Acircumflex	Contours detected: 19	Expected: 3

- Glyph name: Adieresis	Contours detected: 18	Expected: 4

- Glyph name: Agrave	Contours detected: 18	Expected: 3

- Glyph name: Amacron	Contours detected: 19	Expected: 3

- Glyph name: Aogonek	Contours detected: 19	Expected: 2 or 3

- Glyph name: Aring	Contours detected: 20	Expected: 3 or 4

- Glyph name: Atilde	Contours detected: 22	Expected: 3

- Glyph name: B	Contours detected: 20	Expected: 2 or 3

- Glyph name: C	Contours detected: 13	Expected: 1

- Glyph name: Cacute	Contours detected: 15	Expected: 2

- Glyph name: Ccaron	Contours detected: 16	Expected: 2

- Glyph name: Ccedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Ccircumflex	Contours detected: 16	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 14	Expected: 2

- Glyph name: D	Contours detected: 16	Expected: 2

- Glyph name: Dcaron	Contours detected: 19	Expected: 3

- Glyph name: Dcroat	Contours detected: 18	Expected: 2

- Glyph name: E	Contours detected: 18	Expected: 1

- Glyph name: Eacute	Contours detected: 20	Expected: 2

- Glyph name: Ebreve	Contours detected: 23	Expected: 2

- Glyph name: Ecaron	Contours detected: 21	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 21	Expected: 2

- Glyph name: Edieresis	Contours detected: 20	Expected: 3

- Glyph name: Edotaccent	Contours detected: 19	Expected: 2

- Glyph name: Egrave	Contours detected: 20	Expected: 2

- Glyph name: Emacron	Contours detected: 21	Expected: 2

- Glyph name: Eng	Contours detected: 19	Expected: 1

- Glyph name: Eogonek	Contours detected: 21	Expected: 1 or 2

- Glyph name: Eth	Contours detected: 18	Expected: 2

- Glyph name: Euro	Contours detected: 15	Expected: 1 or 2

- Glyph name: F	Contours detected: 14	Expected: 1

- Glyph name: G	Contours detected: 17	Expected: 1

- Glyph name: Gbreve	Contours detected: 22	Expected: 2

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: Gcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Gdotaccent	Contours detected: 18	Expected: 2

- Glyph name: H	Contours detected: 17	Expected: 1

- Glyph name: Hbar	Contours detected: 20	Expected: 2

- Glyph name: Hcircumflex	Contours detected: 20	Expected: 2

- Glyph name: I	Contours detected: 11	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: Iacute	Contours detected: 13	Expected: 2

- Glyph name: Icircumflex	Contours detected: 14	Expected: 2

- Glyph name: Idieresis	Contours detected: 13	Expected: 3

- Glyph name: Idotaccent	Contours detected: 12	Expected: 2

- Glyph name: Igrave	Contours detected: 13	Expected: 2

- Glyph name: Imacron	Contours detected: 14	Expected: 2

- Glyph name: Iogonek	Contours detected: 14	Expected: 1 or 2

- Glyph name: Itilde	Contours detected: 17	Expected: 2

- Glyph name: J	Contours detected: 11	Expected: 1

- Glyph name: Jcircumflex	Contours detected: 14	Expected: 2

- Glyph name: K	Contours detected: 14	Expected: 1 or 2

- Glyph name: L	Contours detected: 11	Expected: 1

- Glyph name: Lacute	Contours detected: 13	Expected: 2

- Glyph name: Lcaron	Contours detected: 13	Expected: 2

- Glyph name: Ldot	Contours detected: 12	Expected: 2

- Glyph name: Lslash	Contours detected: 13	Expected: 1

- Glyph name: M	Contours detected: 18	Expected: 1

- Glyph name: N	Contours detected: 17	Expected: 1

- Glyph name: Nacute	Contours detected: 19	Expected: 2

- Glyph name: Ncaron	Contours detected: 20	Expected: 2

- Glyph name: Ntilde	Contours detected: 23	Expected: 2

- Glyph name: O	Contours detected: 16	Expected: 2

- Glyph name: OE	Contours detected: 24	Expected: 2

- Glyph name: Oacute	Contours detected: 18	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 19	Expected: 3

- Glyph name: Odieresis	Contours detected: 18	Expected: 4

- Glyph name: Ograve	Contours detected: 18	Expected: 3

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: Ohungarumlaut	Contours detected: 20	Expected: 4

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: Oslash	Contours detected: 17	Expected: 2 or 3

- Glyph name: Otilde	Contours detected: 22	Expected: 3

- Glyph name: P	Contours detected: 15	Expected: 1 or 2

- Glyph name: Q	Contours detected: 17	Expected: 2

- Glyph name: R	Contours detected: 18	Expected: 1 or 2

- Glyph name: Racute	Contours detected: 20	Expected: 3

- Glyph name: Rcaron	Contours detected: 21	Expected: 3

- Glyph name: S	Contours detected: 15	Expected: 1

- Glyph name: Sacute	Contours detected: 17	Expected: 2

- Glyph name: Scaron	Contours detected: 18	Expected: 2

- Glyph name: Scircumflex	Contours detected: 18	Expected: 2

- Glyph name: T	Contours detected: 11	Expected: 1

- Glyph name: Tcaron	Contours detected: 14	Expected: 2

- Glyph name: Thorn	Contours detected: 16	Expected: 1 or 2

- Glyph name: U	Contours detected: 15	Expected: 1

- Glyph name: Uacute	Contours detected: 17	Expected: 2

- Glyph name: Ubreve	Contours detected: 20	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 18	Expected: 2

- Glyph name: Udieresis	Contours detected: 17	Expected: 3

- Glyph name: Ugrave	Contours detected: 17	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: Uhungarumlaut	Contours detected: 19	Expected: 3

- Glyph name: Umacron	Contours detected: 18	Expected: 2

- Glyph name: Uogonek	Contours detected: 18	Expected: 1

- Glyph name: Uring	Contours detected: 19	Expected: 3

- Glyph name: Utilde	Contours detected: 21	Expected: 2

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: Z	Contours detected: 15	Expected: 1

- Glyph name: Zacute	Contours detected: 17	Expected: 2

- Glyph name: Zcaron	Contours detected: 18	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 16	Expected: 2

- Glyph name: a	Contours detected: 14	Expected: 2

- Glyph name: aacute	Contours detected: 16	Expected: 3

- Glyph name: abreve	Contours detected: 19	Expected: 3

- Glyph name: acircumflex	Contours detected: 17	Expected: 3

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: adieresis	Contours detected: 16	Expected: 4

- Glyph name: ae	Contours detected: 18	Expected: 3

- Glyph name: agrave	Contours detected: 16	Expected: 3

- Glyph name: amacron	Contours detected: 17	Expected: 3

- Glyph name: ampersand	Contours detected: 14	Expected: 1, 2 or 3

- Glyph name: aogonek	Contours detected: 17	Expected: 2

- Glyph name: approxequal	Contours detected: 12	Expected: 2

- Glyph name: aring	Contours detected: 18	Expected: 4

- Glyph name: arrowboth	Contours detected: 15	Expected: 1

- Glyph name: arrowdown	Contours detected: 11	Expected: 1

- Glyph name: arrowup	Contours detected: 11	Expected: 1

- Glyph name: arrowupdn	Contours detected: 15	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 11	Expected: 1 or 4

- Glyph name: at	Contours detected: 20	Expected: 2

- Glyph name: atilde	Contours detected: 20	Expected: 3

- Glyph name: b	Contours detected: 16	Expected: 2

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceleft	Contours detected: 10	Expected: 1

- Glyph name: braceright	Contours detected: 10	Expected: 1

- Glyph name: bracketleft	Contours detected: 11	Expected: 1

- Glyph name: bracketright	Contours detected: 11	Expected: 1

- Glyph name: breve	Contours detected: 5	Expected: 1

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: bullet	Contours detected: 9	Expected: 1

- Glyph name: c	Contours detected: 11	Expected: 1

- Glyph name: cacute	Contours detected: 13	Expected: 2

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: ccaron	Contours detected: 14	Expected: 2

- Glyph name: ccedilla	Contours detected: 14	Expected: 1 or 2

- Glyph name: ccircumflex	Contours detected: 14	Expected: 2

- Glyph name: cdotaccent	Contours detected: 12	Expected: 2

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: cent	Contours detected: 16	Expected: 1 or 2

- Glyph name: circle	Contours detected: 16	Expected: 2

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: colonmonetary	Contours detected: 16	Expected: 1 or 3

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: copyright	Contours detected: 26	Expected: 3

- Glyph name: currency	Contours detected: 12	Expected: 2

- Glyph name: d	Contours detected: 16	Expected: 2

- Glyph name: dagger	Contours detected: 13	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 17	Expected: 1 or 3

- Glyph name: dcaron	Contours detected: 18	Expected: 3

- Glyph name: dcroat	Contours detected: 18	Expected: 2

- Glyph name: degree	Contours detected: 8	Expected: 2

- Glyph name: divide	Contours detected: 7	Expected: 3

- Glyph name: dollar	Contours detected: 17	Expected: 1, 3 or 5

- Glyph name: dong	Contours detected: 23	Expected: 3 or 4

- Glyph name: dotlessi	Contours detected: 8	Expected: 1

- Glyph name: e	Contours detected: 14	Expected: 2

- Glyph name: eacute	Contours detected: 16	Expected: 3

- Glyph name: ebreve	Contours detected: 19	Expected: 3

- Glyph name: ecaron	Contours detected: 17	Expected: 3

- Glyph name: ecircumflex	Contours detected: 17	Expected: 3

- Glyph name: edieresis	Contours detected: 16	Expected: 4

- Glyph name: edotaccent	Contours detected: 15	Expected: 3

- Glyph name: egrave	Contours detected: 16	Expected: 3

- Glyph name: eight	Contours detected: 17	Expected: 3

- Glyph name: emacron	Contours detected: 17	Expected: 3

- Glyph name: emdash	Contours detected: 6	Expected: 1

- Glyph name: emptyset	Contours detected: 21	Expected: 3

- Glyph name: endash	Contours detected: 5	Expected: 1

- Glyph name: eng	Contours detected: 15	Expected: 1

- Glyph name: eogonek	Contours detected: 17	Expected: 2

- Glyph name: equal	Contours detected: 10	Expected: 2

- Glyph name: eth	Contours detected: 16	Expected: 2

- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: f	Contours detected: 12	Expected: 1

- Glyph name: figuredash	Contours detected: 5	Expected: 1

- Glyph name: five	Contours detected: 17	Expected: 1

- Glyph name: fiveeighths	Contours detected: 22	Expected: 5

- Glyph name: four	Contours detected: 14	Expected: 1 or 2

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: g	Contours detected: 18	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 23	Expected: 3 or 4

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 21	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 19	Expected: 3 or 4

- Glyph name: germandbls	Contours detected: 16	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: greaterequal	Contours detected: 8	Expected: 2

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: h	Contours detected: 14	Expected: 1

- Glyph name: hbar	Contours detected: 16	Expected: 1

- Glyph name: hcircumflex	Contours detected: 17	Expected: 2

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: hyphen	Contours detected: 4	Expected: 1

- Glyph name: i	Contours detected: 9	Expected: 2

- Glyph name: iacute	Contours detected: 10	Expected: 2

- Glyph name: icircumflex	Contours detected: 11	Expected: 2

- Glyph name: idieresis	Contours detected: 10	Expected: 3

- Glyph name: igrave	Contours detected: 10	Expected: 2

- Glyph name: ij	Contours detected: 19	Expected: 3 or 4

- Glyph name: imacron	Contours detected: 11	Expected: 2

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: iogonek	Contours detected: 12	Expected: 2 or 3

- Glyph name: itilde	Contours detected: 14	Expected: 2

- Glyph name: j	Contours detected: 11	Expected: 2

- Glyph name: jcircumflex	Contours detected: 13	Expected: 2

- Glyph name: k	Contours detected: 13	Expected: 1 or 2

- Glyph name: kgreenlandic	Contours detected: 11	Expected: 1 or 2

- Glyph name: l	Contours detected: 10	Expected: 1

- Glyph name: lacute	Contours detected: 12	Expected: 2

- Glyph name: lcaron	Contours detected: 12	Expected: 2

- Glyph name: ldot	Contours detected: 11	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: lessequal	Contours detected: 8	Expected: 2

- Glyph name: lira	Contours detected: 17	Expected: 1

- Glyph name: logicalnot	Contours detected: 7	Expected: 1

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: lslash	Contours detected: 12	Expected: 1

- Glyph name: m	Contours detected: 14	Expected: 1

- Glyph name: macron	Contours detected: 3	Expected: 1

- Glyph name: minus	Contours detected: 5	Expected: 1

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: n	Contours detected: 12	Expected: 1

- Glyph name: nacute	Contours detected: 14	Expected: 2

- Glyph name: napostrophe	Contours detected: 15	Expected: 2

- Glyph name: ncaron	Contours detected: 15	Expected: 2

- Glyph name: nine	Contours detected: 15	Expected: 1 or 2

- Glyph name: notequal	Contours detected: 15	Expected: 1

- Glyph name: ntilde	Contours detected: 18	Expected: 2

- Glyph name: numbersign	Contours detected: 20	Expected: 2

- Glyph name: o	Contours detected: 12	Expected: 2

- Glyph name: oacute	Contours detected: 14	Expected: 3

- Glyph name: ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: odieresis	Contours detected: 14	Expected: 4

- Glyph name: oe	Contours detected: 18	Expected: 3

- Glyph name: ogonek	Contours detected: 3	Expected: 1

- Glyph name: ograve	Contours detected: 14	Expected: 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: one	Contours detected: 10	Expected: 1

- Glyph name: oneeighth	Contours detected: 21	Expected: 5

- Glyph name: onehalf	Contours detected: 16	Expected: 3

- Glyph name: onequarter	Contours detected: 17	Expected: 3 or 4

- Glyph name: onethird	Contours detected: 16	Expected: 3

- Glyph name: ordfeminine	Contours detected: 14	Expected: 2 or 3

- Glyph name: ordmasculine	Contours detected: 12	Expected: 2 or 3

- Glyph name: oslash	Contours detected: 13	Expected: 3

- Glyph name: otilde	Contours detected: 18	Expected: 3

- Glyph name: p	Contours detected: 16	Expected: 2

- Glyph name: paragraph	Contours detected: 23	Expected: 1, 2 or 3

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: partialdiff	Contours detected: 15	Expected: 2

- Glyph name: percent	Contours detected: 13	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 17	Expected: 6 or 7

- Glyph name: peseta	Contours detected: 26	Expected: 2, 3 or 4

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: plus	Contours detected: 9	Expected: 1

- Glyph name: plusminus	Contours detected: 14	Expected: 1 or 2

- Glyph name: product	Contours detected: 21	Expected: 1

- Glyph name: q	Contours detected: 16	Expected: 2

- Glyph name: question	Contours detected: 10	Expected: 2

- Glyph name: questiondown	Contours detected: 10	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: r	Contours detected: 9	Expected: 1

- Glyph name: racute	Contours detected: 11	Expected: 2

- Glyph name: radical	Contours detected: 11	Expected: 1

- Glyph name: rcaron	Contours detected: 12	Expected: 2

- Glyph name: registered	Contours detected: 30	Expected: 3 or 4

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: rupee	Contours detected: 23	Expected: 3

- Glyph name: s	Contours detected: 13	Expected: 1

- Glyph name: sacute	Contours detected: 15	Expected: 2

- Glyph name: scaron	Contours detected: 16	Expected: 2

- Glyph name: scircumflex	Contours detected: 16	Expected: 2

- Glyph name: section	Contours detected: 20	Expected: 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: seven	Contours detected: 11	Expected: 1

- Glyph name: seveneighths	Contours detected: 20	Expected: 5

- Glyph name: six	Contours detected: 15	Expected: 1 or 2

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: sterling	Contours detected: 15	Expected: 1 or 2

- Glyph name: summation	Contours detected: 17	Expected: 1

- Glyph name: t	Contours detected: 12	Expected: 1

- Glyph name: tcaron	Contours detected: 14	Expected: 2

- Glyph name: thorn	Contours detected: 18	Expected: 2

- Glyph name: three	Contours detected: 14	Expected: 1

- Glyph name: threeeighths	Contours detected: 21	Expected: 5

- Glyph name: threequarters	Contours detected: 17	Expected: 3 or 4

- Glyph name: tilde	Contours detected: 6	Expected: 1

- Glyph name: trademark	Contours detected: 18	Expected: 2

- Glyph name: triagdn	Contours detected: 31	Expected: 1

- Glyph name: triagup	Contours detected: 31	Expected: 1

- Glyph name: two	Contours detected: 15	Expected: 1

- Glyph name: twothirds	Contours detected: 16	Expected: 1 or 3

- Glyph name: u	Contours detected: 12	Expected: 1

- Glyph name: uacute	Contours detected: 14	Expected: 2

- Glyph name: ubreve	Contours detected: 17	Expected: 2

- Glyph name: ucircumflex	Contours detected: 15	Expected: 2

- Glyph name: udieresis	Contours detected: 14	Expected: 3

- Glyph name: ugrave	Contours detected: 14	Expected: 2

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: uhungarumlaut	Contours detected: 16	Expected: 3

- Glyph name: umacron	Contours detected: 15	Expected: 2

- Glyph name: underscore	Contours detected: 6	Expected: 1

- Glyph name: uni00AD	Contours detected: 4	Expected: 0

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: uni01CD	Contours detected: 19	Expected: 3

- Glyph name: uni01CE	Contours detected: 17	Expected: 3

- Glyph name: uni01CF	Contours detected: 14	Expected: 2

- Glyph name: uni01D0	Contours detected: 11	Expected: 2

- Glyph name: uni01D1	Contours detected: 19	Expected: 3

- Glyph name: uni01D2	Contours detected: 15	Expected: 3

- Glyph name: uni01D3	Contours detected: 18	Expected: 2

- Glyph name: uni01D4	Contours detected: 15	Expected: 2

- Glyph name: uni01D5	Contours detected: 18	Expected: 4

- Glyph name: uni01D6	Contours detected: 17	Expected: 4

- Glyph name: uni01D7	Contours detected: 15	Expected: 4

- Glyph name: uni01D8	Contours detected: 16	Expected: 4

- Glyph name: uni01D9	Contours detected: 16	Expected: 4

- Glyph name: uni01DA	Contours detected: 17	Expected: 4

- Glyph name: uni01DB	Contours detected: 15	Expected: 4

- Glyph name: uni01DC	Contours detected: 16	Expected: 4

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni032E	Contours detected: 5	Expected: 1

- Glyph name: uni0331	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: uni1E0C	Contours detected: 17	Expected: 3

- Glyph name: uni1E0D	Contours detected: 17	Expected: 3

- Glyph name: uni1E0E	Contours detected: 19	Expected: 3

- Glyph name: uni1E0F	Contours detected: 19	Expected: 3

- Glyph name: uni1E20	Contours detected: 20	Expected: 2

- Glyph name: uni1E21	Contours detected: 21	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 18	Expected: 2

- Glyph name: uni1E25	Contours detected: 15	Expected: 2

- Glyph name: uni1E2A	Contours detected: 20	Expected: 2

- Glyph name: uni1E2B	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: uni1E44	Contours detected: 18	Expected: 2

- Glyph name: uni1E45	Contours detected: 13	Expected: 2

- Glyph name: uni1E46	Contours detected: 18	Expected: 2

- Glyph name: uni1E47	Contours detected: 13	Expected: 2

- Glyph name: uni1E48	Contours detected: 20	Expected: 2

- Glyph name: uni1E49	Contours detected: 15	Expected: 2

- Glyph name: uni1E5A	Contours detected: 19	Expected: 3

- Glyph name: uni1E5B	Contours detected: 10	Expected: 2

- Glyph name: uni1E5C	Contours detected: 22	Expected: 4

- Glyph name: uni1E5D	Contours detected: 13	Expected: 3

- Glyph name: uni1E5E	Contours detected: 21	Expected: 3

- Glyph name: uni1E5F	Contours detected: 12	Expected: 2

- Glyph name: uni1E60	Contours detected: 16	Expected: 2

- Glyph name: uni1E61	Contours detected: 14	Expected: 2

- Glyph name: uni1E62	Contours detected: 16	Expected: 2

- Glyph name: uni1E63	Contours detected: 14	Expected: 2

- Glyph name: uni1E6C	Contours detected: 12	Expected: 2

- Glyph name: uni1E6D	Contours detected: 13	Expected: 2

- Glyph name: uni1E6E	Contours detected: 14	Expected: 2

- Glyph name: uni1E6F	Contours detected: 15	Expected: 2

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: uni1E92	Contours detected: 16	Expected: 2

- Glyph name: uni1E93	Contours detected: 14	Expected: 2

- Glyph name: uni1E97	Contours detected: 14	Expected: 3

- Glyph name: uni2010	Contours detected: 4	Expected: 1

- Glyph name: uni2011	Contours detected: 4	Expected: 1

- Glyph name: uni2015	Contours detected: 6	Expected: 1

- Glyph name: uni2117	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 18	Expected: 2

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 15	Expected: 1

- Glyph name: uring	Contours detected: 16	Expected: 3

- Glyph name: utilde	Contours detected: 18	Expected: 2

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 16	Expected: 1

- Glyph name: yacute	Contours detected: 18	Expected: 2

- Glyph name: ycircumflex	Contours detected: 19	Expected: 2

- Glyph name: ydieresis	Contours detected: 18	Expected: 3

- Glyph name: yen	Contours detected: 13	Expected: 1 or 2

- Glyph name: ygrave	Contours detected: 18	Expected: 2

- Glyph name: z	Contours detected: 13	Expected: 1

- Glyph name: zacute	Contours detected: 15	Expected: 2

- Glyph name: zcaron	Contours detected: 16	Expected: 2

- Glyph name: zdotaccent	Contours detected: 14	Expected: 2

- Glyph name: zero	Contours detected: 19	Expected: 2 or 3
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Heiltsuk (Latn, 300 speakers), Ekpeye (Latn, 226,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ejagham (Latn, 120,000 speakers), Mango (Latn, 77,000 speakers), Ma’di (Latn, 584,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Dan (Latn, 1,099,244 speakers), Mfumte (Latn, 79,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Makaa (Latn, 221,000 speakers), Kaska (Latn, 125 speakers), Belarusian (Cyrl, 10,064,517 speakers), Fur (Latn, 1,230,163 speakers), Aghem (Latn, 38,843 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Teke-Ebo (Latn, 260,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Yala (Latn, 200,000 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Lugbara (Latn, 2,200,000 speakers), Gulay (Latn, 250,478 speakers), Nateni (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), South Central Banda (Latn, 244,000 speakers), Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Han (Latn, 6 speakers).</p>
 [code: soft-dotted]



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

<details><summary>[11] MatrixSans-Regular.ttf</summary>
<div>
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

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: Scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: ohornacute	Contours detected: 4	Expected: 3

- Glyph name: ohorngrave	Contours detected: 4	Expected: 3

- Glyph name: ohornhookabove	Contours detected: 4	Expected: 3

- Glyph name: ohorntilde	Contours detected: 4	Expected: 3

- Glyph name: ohorndotbelow	Contours detected: 4	Expected: 3

- Glyph name: Uhornacute	Contours detected: 3	Expected: 2

- Glyph name: uhornacute	Contours detected: 3	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 3	Expected: 2

- Glyph name: uhorntilde	Contours detected: 3	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 3	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 3	Expected: 2

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: won	Contours detected: 5	Expected: 1, 3, 4 or 7

- Glyph name: peso	Contours detected: 3	Expected: 1, 2 or 4

- Glyph name: onethird	Contours detected: 2	Expected: 3

- Glyph name: twothirds	Contours detected: 2	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 4	Expected: 5

- Glyph name: threeeighths	Contours detected: 4	Expected: 5

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

- Glyph name: seveneighths	Contours detected: 4	Expected: 5

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

- Glyph name: ohorn	Contours detected: 3	Expected: 2

- Glyph name: oneeighth	Contours detected: 4	Expected: 5

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: onethird	Contours detected: 2	Expected: 3

- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: seveneighths	Contours detected: 4	Expected: 5

- Glyph name: threeeighths	Contours detected: 4	Expected: 5

- Glyph name: twothirds	Contours detected: 2	Expected: 1 or 3

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Heiltsuk (Latn, 300 speakers), Ekpeye (Latn, 226,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ejagham (Latn, 120,000 speakers), Mango (Latn, 77,000 speakers), Ma’di (Latn, 584,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Dan (Latn, 1,099,244 speakers), Mfumte (Latn, 79,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Makaa (Latn, 221,000 speakers), Kaska (Latn, 125 speakers), Belarusian (Cyrl, 10,064,517 speakers), Fur (Latn, 1,230,163 speakers), Aghem (Latn, 38,843 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Teke-Ebo (Latn, 260,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Yala (Latn, 200,000 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Lugbara (Latn, 2,200,000 speakers), Gulay (Latn, 250,478 speakers), Nateni (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), South Central Banda (Latn, 244,000 speakers), Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Han (Latn, 6 speakers).</p>
 [code: soft-dotted]



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

<details><summary>[10] MatrixSansSC-Regular.ttf</summary>
<div>
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

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: Scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: ohornacute	Contours detected: 4	Expected: 3

- Glyph name: ohorngrave	Contours detected: 4	Expected: 3

- Glyph name: ohornhookabove	Contours detected: 4	Expected: 3

- Glyph name: ohorntilde	Contours detected: 4	Expected: 3

- Glyph name: ohorndotbelow	Contours detected: 4	Expected: 3

- Glyph name: Uhornacute	Contours detected: 3	Expected: 2

- Glyph name: uhornacute	Contours detected: 3	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 3	Expected: 2

- Glyph name: uhorntilde	Contours detected: 3	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 3	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 3	Expected: 2

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: won	Contours detected: 5	Expected: 1, 3, 4 or 7

- Glyph name: peso	Contours detected: 3	Expected: 1, 2 or 4

- Glyph name: onethird	Contours detected: 2	Expected: 3

- Glyph name: twothirds	Contours detected: 2	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 4	Expected: 5

- Glyph name: threeeighths	Contours detected: 4	Expected: 5

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

- Glyph name: seveneighths	Contours detected: 4	Expected: 5

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: Uhorn	Contours detected: 2	Expected: 1

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

- Glyph name: ohorn	Contours detected: 3	Expected: 2

- Glyph name: oneeighth	Contours detected: 4	Expected: 5

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: onethird	Contours detected: 2	Expected: 3

- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: seveneighths	Contours detected: 4	Expected: 5

- Glyph name: threeeighths	Contours detected: 4	Expected: 5

- Glyph name: twothirds	Contours detected: 2	Expected: 1 or 3

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



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

<details><summary>[10] MatrixSansPrint-Regular.ttf</summary>
<div>
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

- Glyph name: plus	Contours detected: 9	Expected: 1

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: hyphen	Contours detected: 4	Expected: 1

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: zero	Contours detected: 19	Expected: 2 or 3

- Glyph name: one	Contours detected: 10	Expected: 1

- Glyph name: two	Contours detected: 15	Expected: 1

- Glyph name: three	Contours detected: 14	Expected: 1

- Glyph name: four	Contours detected: 14	Expected: 1 or 2

- Glyph name: five	Contours detected: 17	Expected: 1

- Glyph name: six	Contours detected: 15	Expected: 1 or 2

- Glyph name: seven	Contours detected: 11	Expected: 1

- Glyph name: eight	Contours detected: 17	Expected: 3

- Glyph name: nine	Contours detected: 15	Expected: 1 or 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: equal	Contours detected: 10	Expected: 2

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: question	Contours detected: 10	Expected: 2

- Glyph name: at	Contours detected: 20	Expected: 2

- Glyph name: A	Contours detected: 16	Expected: 2

- Glyph name: B	Contours detected: 20	Expected: 2 or 3

- Glyph name: C	Contours detected: 13	Expected: 1

- Glyph name: D	Contours detected: 16	Expected: 2

- Glyph name: E	Contours detected: 18	Expected: 1

- Glyph name: F	Contours detected: 14	Expected: 1

- Glyph name: G	Contours detected: 17	Expected: 1

- Glyph name: H	Contours detected: 17	Expected: 1

- Glyph name: I	Contours detected: 11	Expected: 1

- Glyph name: J	Contours detected: 11	Expected: 1

- Glyph name: K	Contours detected: 14	Expected: 1 or 2

- Glyph name: L	Contours detected: 11	Expected: 1

- Glyph name: M	Contours detected: 18	Expected: 1

- Glyph name: N	Contours detected: 17	Expected: 1

- Glyph name: O	Contours detected: 16	Expected: 2

- Glyph name: P	Contours detected: 15	Expected: 1 or 2

- Glyph name: Q	Contours detected: 17	Expected: 2

- Glyph name: R	Contours detected: 18	Expected: 1 or 2

- Glyph name: S	Contours detected: 15	Expected: 1

- Glyph name: T	Contours detected: 11	Expected: 1

- Glyph name: U	Contours detected: 15	Expected: 1

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Z	Contours detected: 15	Expected: 1

- Glyph name: bracketleft	Contours detected: 11	Expected: 1

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bracketright	Contours detected: 11	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: underscore	Contours detected: 6	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 14	Expected: 2

- Glyph name: b	Contours detected: 16	Expected: 2

- Glyph name: c	Contours detected: 11	Expected: 1

- Glyph name: d	Contours detected: 16	Expected: 2

- Glyph name: e	Contours detected: 14	Expected: 2

- Glyph name: f	Contours detected: 12	Expected: 1

- Glyph name: g	Contours detected: 18	Expected: 2 or 3

- Glyph name: h	Contours detected: 14	Expected: 1

- Glyph name: i	Contours detected: 9	Expected: 2

- Glyph name: j	Contours detected: 11	Expected: 2

- Glyph name: k	Contours detected: 13	Expected: 1 or 2

- Glyph name: l	Contours detected: 10	Expected: 1

- Glyph name: m	Contours detected: 14	Expected: 1

- Glyph name: n	Contours detected: 12	Expected: 1

- Glyph name: o	Contours detected: 12	Expected: 2

- Glyph name: p	Contours detected: 16	Expected: 2

- Glyph name: q	Contours detected: 16	Expected: 2

- Glyph name: r	Contours detected: 9	Expected: 1

- Glyph name: s	Contours detected: 13	Expected: 1

- Glyph name: t	Contours detected: 12	Expected: 1

- Glyph name: u	Contours detected: 12	Expected: 1

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 16	Expected: 1

- Glyph name: z	Contours detected: 13	Expected: 1

- Glyph name: braceleft	Contours detected: 10	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceright	Contours detected: 10	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: cent	Contours detected: 16	Expected: 1 or 2

- Glyph name: sterling	Contours detected: 15	Expected: 1 or 2

- Glyph name: currency	Contours detected: 12	Expected: 2

- Glyph name: yen	Contours detected: 13	Expected: 1 or 2

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: section	Contours detected: 20	Expected: 2

- Glyph name: copyright	Contours detected: 26	Expected: 3

- Glyph name: ordfeminine	Contours detected: 14	Expected: 2 or 3

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: logicalnot	Contours detected: 7	Expected: 1

- Glyph name: uni00AD	Contours detected: 4	Expected: 0

- Glyph name: registered	Contours detected: 30	Expected: 3 or 4

- Glyph name: macron	Contours detected: 3	Expected: 1

- Glyph name: degree	Contours detected: 8	Expected: 2

- Glyph name: plusminus	Contours detected: 14	Expected: 1 or 2

- Glyph name: twosuperior	Contours detected: 8	Expected: 1

- Glyph name: threesuperior	Contours detected: 8	Expected: 1

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: micro	Contours detected: 14	Expected: 1

- Glyph name: paragraph	Contours detected: 23	Expected: 1, 2 or 3

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: onesuperior	Contours detected: 8	Expected: 1

- Glyph name: ordmasculine	Contours detected: 12	Expected: 2 or 3

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: onequarter	Contours detected: 17	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 16	Expected: 3

- Glyph name: threequarters	Contours detected: 17	Expected: 3 or 4

- Glyph name: questiondown	Contours detected: 10	Expected: 2

- Glyph name: Agrave	Contours detected: 18	Expected: 3

- Glyph name: Aacute	Contours detected: 18	Expected: 3

- Glyph name: Acircumflex	Contours detected: 19	Expected: 3

- Glyph name: Atilde	Contours detected: 22	Expected: 3

- Glyph name: Adieresis	Contours detected: 18	Expected: 4

- Glyph name: Aring	Contours detected: 20	Expected: 3 or 4

- Glyph name: AE	Contours detected: 24	Expected: 2

- Glyph name: Ccedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Egrave	Contours detected: 20	Expected: 2

- Glyph name: Eacute	Contours detected: 20	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 21	Expected: 2

- Glyph name: Edieresis	Contours detected: 20	Expected: 3

- Glyph name: Igrave	Contours detected: 13	Expected: 2

- Glyph name: Iacute	Contours detected: 13	Expected: 2

- Glyph name: Icircumflex	Contours detected: 14	Expected: 2

- Glyph name: Idieresis	Contours detected: 13	Expected: 3

- Glyph name: Eth	Contours detected: 18	Expected: 2

- Glyph name: Ntilde	Contours detected: 23	Expected: 2

- Glyph name: Ograve	Contours detected: 18	Expected: 3

- Glyph name: Oacute	Contours detected: 18	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 19	Expected: 3

- Glyph name: Otilde	Contours detected: 22	Expected: 3

- Glyph name: Odieresis	Contours detected: 18	Expected: 4

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: Oslash	Contours detected: 17	Expected: 2 or 3

- Glyph name: Ugrave	Contours detected: 17	Expected: 2

- Glyph name: Uacute	Contours detected: 17	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 18	Expected: 2

- Glyph name: Udieresis	Contours detected: 17	Expected: 3

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Thorn	Contours detected: 16	Expected: 1 or 2

- Glyph name: germandbls	Contours detected: 16	Expected: 1

- Glyph name: agrave	Contours detected: 16	Expected: 3

- Glyph name: aacute	Contours detected: 16	Expected: 3

- Glyph name: acircumflex	Contours detected: 17	Expected: 3

- Glyph name: atilde	Contours detected: 20	Expected: 3

- Glyph name: adieresis	Contours detected: 16	Expected: 4

- Glyph name: aring	Contours detected: 18	Expected: 4

- Glyph name: ae	Contours detected: 18	Expected: 3

- Glyph name: ccedilla	Contours detected: 14	Expected: 1 or 2

- Glyph name: egrave	Contours detected: 16	Expected: 3

- Glyph name: eacute	Contours detected: 16	Expected: 3

- Glyph name: ecircumflex	Contours detected: 17	Expected: 3

- Glyph name: edieresis	Contours detected: 16	Expected: 4

- Glyph name: igrave	Contours detected: 10	Expected: 2

- Glyph name: iacute	Contours detected: 10	Expected: 2

- Glyph name: icircumflex	Contours detected: 11	Expected: 2

- Glyph name: idieresis	Contours detected: 10	Expected: 3

- Glyph name: eth	Contours detected: 16	Expected: 2

- Glyph name: ntilde	Contours detected: 18	Expected: 2

- Glyph name: ograve	Contours detected: 14	Expected: 3

- Glyph name: oacute	Contours detected: 14	Expected: 3

- Glyph name: ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: otilde	Contours detected: 18	Expected: 3

- Glyph name: odieresis	Contours detected: 14	Expected: 4

- Glyph name: divide	Contours detected: 7	Expected: 3

- Glyph name: oslash	Contours detected: 13	Expected: 3

- Glyph name: ugrave	Contours detected: 14	Expected: 2

- Glyph name: uacute	Contours detected: 14	Expected: 2

- Glyph name: ucircumflex	Contours detected: 15	Expected: 2

- Glyph name: udieresis	Contours detected: 14	Expected: 3

- Glyph name: yacute	Contours detected: 18	Expected: 2

- Glyph name: thorn	Contours detected: 18	Expected: 2

- Glyph name: ydieresis	Contours detected: 18	Expected: 3

- Glyph name: Amacron	Contours detected: 19	Expected: 3

- Glyph name: amacron	Contours detected: 17	Expected: 3

- Glyph name: Abreve	Contours detected: 21	Expected: 3

- Glyph name: abreve	Contours detected: 19	Expected: 3

- Glyph name: Aogonek	Contours detected: 19	Expected: 2 or 3

- Glyph name: aogonek	Contours detected: 17	Expected: 2

- Glyph name: Cacute	Contours detected: 15	Expected: 2

- Glyph name: cacute	Contours detected: 13	Expected: 2

- Glyph name: Ccircumflex	Contours detected: 16	Expected: 2

- Glyph name: ccircumflex	Contours detected: 14	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 14	Expected: 2

- Glyph name: cdotaccent	Contours detected: 12	Expected: 2

- Glyph name: Ccaron	Contours detected: 16	Expected: 2

- Glyph name: ccaron	Contours detected: 14	Expected: 2

- Glyph name: Dcaron	Contours detected: 19	Expected: 3

- Glyph name: dcaron	Contours detected: 18	Expected: 3

- Glyph name: Dcroat	Contours detected: 18	Expected: 2

- Glyph name: dcroat	Contours detected: 18	Expected: 2

- Glyph name: Emacron	Contours detected: 21	Expected: 2

- Glyph name: emacron	Contours detected: 17	Expected: 3

- Glyph name: Ebreve	Contours detected: 23	Expected: 2

- Glyph name: ebreve	Contours detected: 19	Expected: 3

- Glyph name: Edotaccent	Contours detected: 19	Expected: 2

- Glyph name: edotaccent	Contours detected: 15	Expected: 3

- Glyph name: Eogonek	Contours detected: 21	Expected: 1 or 2

- Glyph name: eogonek	Contours detected: 17	Expected: 2

- Glyph name: Ecaron	Contours detected: 21	Expected: 2

- Glyph name: ecaron	Contours detected: 17	Expected: 3

- Glyph name: Gcircumflex	Contours detected: 20	Expected: 2

- Glyph name: gcircumflex	Contours detected: 21	Expected: 3 or 4

- Glyph name: Gbreve	Contours detected: 22	Expected: 2

- Glyph name: gbreve	Contours detected: 23	Expected: 3 or 4

- Glyph name: Gdotaccent	Contours detected: 18	Expected: 2

- Glyph name: gdotaccent	Contours detected: 19	Expected: 3 or 4

- Glyph name: Gcommaaccent	Contours detected: 19	Expected: 2

- Glyph name: gcommaaccent	Contours detected: 20	Expected: 3 or 4

- Glyph name: Hcircumflex	Contours detected: 20	Expected: 2

- Glyph name: hcircumflex	Contours detected: 17	Expected: 2

- Glyph name: Hbar	Contours detected: 20	Expected: 2

- Glyph name: hbar	Contours detected: 16	Expected: 1

- Glyph name: Itilde	Contours detected: 17	Expected: 2

- Glyph name: itilde	Contours detected: 14	Expected: 2

- Glyph name: Imacron	Contours detected: 14	Expected: 2

- Glyph name: imacron	Contours detected: 11	Expected: 2

- Glyph name: Iogonek	Contours detected: 14	Expected: 1 or 2

- Glyph name: iogonek	Contours detected: 12	Expected: 2 or 3

- Glyph name: Idotaccent	Contours detected: 12	Expected: 2

- Glyph name: dotlessi	Contours detected: 8	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: ij	Contours detected: 19	Expected: 3 or 4

- Glyph name: Jcircumflex	Contours detected: 14	Expected: 2

- Glyph name: jcircumflex	Contours detected: 13	Expected: 2

- Glyph name: Kcommaaccent	Contours detected: 16	Expected: 2 or 3

- Glyph name: kcommaaccent	Contours detected: 15	Expected: 2 or 3

- Glyph name: kgreenlandic	Contours detected: 11	Expected: 1 or 2

- Glyph name: Lacute	Contours detected: 13	Expected: 2

- Glyph name: lacute	Contours detected: 12	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 12	Expected: 2

- Glyph name: Lcaron	Contours detected: 13	Expected: 2

- Glyph name: lcaron	Contours detected: 12	Expected: 2

- Glyph name: Ldot	Contours detected: 12	Expected: 2

- Glyph name: ldot	Contours detected: 11	Expected: 2

- Glyph name: Lslash	Contours detected: 13	Expected: 1

- Glyph name: lslash	Contours detected: 12	Expected: 1

- Glyph name: Nacute	Contours detected: 19	Expected: 2

- Glyph name: nacute	Contours detected: 14	Expected: 2

- Glyph name: Ncommaaccent	Contours detected: 19	Expected: 2

- Glyph name: ncommaaccent	Contours detected: 14	Expected: 2

- Glyph name: Ncaron	Contours detected: 20	Expected: 2

- Glyph name: ncaron	Contours detected: 15	Expected: 2

- Glyph name: napostrophe	Contours detected: 15	Expected: 2

- Glyph name: Eng	Contours detected: 19	Expected: 1

- Glyph name: eng	Contours detected: 15	Expected: 1

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: Ohungarumlaut	Contours detected: 20	Expected: 4

- Glyph name: ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: OE	Contours detected: 24	Expected: 2

- Glyph name: oe	Contours detected: 18	Expected: 3

- Glyph name: Racute	Contours detected: 20	Expected: 3

- Glyph name: racute	Contours detected: 11	Expected: 2

- Glyph name: Rcommaaccent	Contours detected: 20	Expected: 3

- Glyph name: rcommaaccent	Contours detected: 11	Expected: 2

- Glyph name: Rcaron	Contours detected: 21	Expected: 3

- Glyph name: rcaron	Contours detected: 12	Expected: 2

- Glyph name: Sacute	Contours detected: 17	Expected: 2

- Glyph name: sacute	Contours detected: 15	Expected: 2

- Glyph name: Scircumflex	Contours detected: 18	Expected: 2

- Glyph name: scircumflex	Contours detected: 16	Expected: 2

- Glyph name: Scedilla	Contours detected: 18	Expected: 1 or 2

- Glyph name: scedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Scaron	Contours detected: 18	Expected: 2

- Glyph name: scaron	Contours detected: 16	Expected: 2

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: Tcaron	Contours detected: 14	Expected: 2

- Glyph name: tcaron	Contours detected: 14	Expected: 2

- Glyph name: Utilde	Contours detected: 21	Expected: 2

- Glyph name: utilde	Contours detected: 18	Expected: 2

- Glyph name: Umacron	Contours detected: 18	Expected: 2

- Glyph name: umacron	Contours detected: 15	Expected: 2

- Glyph name: Ubreve	Contours detected: 20	Expected: 2

- Glyph name: ubreve	Contours detected: 17	Expected: 2

- Glyph name: Uring	Contours detected: 19	Expected: 3

- Glyph name: uring	Contours detected: 16	Expected: 3

- Glyph name: Uhungarumlaut	Contours detected: 19	Expected: 3

- Glyph name: uhungarumlaut	Contours detected: 16	Expected: 3

- Glyph name: Uogonek	Contours detected: 18	Expected: 1

- Glyph name: uogonek	Contours detected: 15	Expected: 1

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: ycircumflex	Contours detected: 19	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Zacute	Contours detected: 17	Expected: 2

- Glyph name: zacute	Contours detected: 15	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 16	Expected: 2

- Glyph name: zdotaccent	Contours detected: 14	Expected: 2

- Glyph name: Zcaron	Contours detected: 18	Expected: 2

- Glyph name: zcaron	Contours detected: 16	Expected: 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: florin	Contours detected: 14	Expected: 1

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: uni01CD	Contours detected: 19	Expected: 3

- Glyph name: uni01CE	Contours detected: 17	Expected: 3

- Glyph name: uni01CF	Contours detected: 14	Expected: 2

- Glyph name: uni01D0	Contours detected: 11	Expected: 2

- Glyph name: uni01D1	Contours detected: 19	Expected: 3

- Glyph name: uni01D2	Contours detected: 15	Expected: 3

- Glyph name: uni01D3	Contours detected: 18	Expected: 2

- Glyph name: uni01D4	Contours detected: 15	Expected: 2

- Glyph name: uni01D5	Contours detected: 18	Expected: 4

- Glyph name: uni01D6	Contours detected: 17	Expected: 4

- Glyph name: uni01D7	Contours detected: 15	Expected: 4

- Glyph name: uni01D8	Contours detected: 16	Expected: 4

- Glyph name: uni01D9	Contours detected: 16	Expected: 4

- Glyph name: uni01DA	Contours detected: 17	Expected: 4

- Glyph name: uni01DB	Contours detected: 15	Expected: 4

- Glyph name: uni01DC	Contours detected: 16	Expected: 4

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Scommaaccent	Contours detected: 17	Expected: 2

- Glyph name: scommaaccent	Contours detected: 15	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 14	Expected: 2

- Glyph name: jdotless	Contours detected: 10	Expected: 1

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: breve	Contours detected: 5	Expected: 1

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: ogonek	Contours detected: 3	Expected: 1

- Glyph name: tilde	Contours detected: 6	Expected: 1

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: gravecomb	Contours detected: 2	Expected: 1

- Glyph name: acutecomb	Contours detected: 2	Expected: 1

- Glyph name: circumflexcomb	Contours detected: 3	Expected: 1

- Glyph name: tildecomb	Contours detected: 6	Expected: 1

- Glyph name: macroncomb	Contours detected: 3	Expected: 1

- Glyph name: brevecomb	Contours detected: 5	Expected: 1

- Glyph name: hookabovecomb	Contours detected: 3	Expected: 1

- Glyph name: ringcomb	Contours detected: 4	Expected: 2

- Glyph name: hungarumlautcomb	Contours detected: 4	Expected: 2

- Glyph name: caroncomb	Contours detected: 3	Expected: 1

- Glyph name: commaturnedabovecomb	Contours detected: 2	Expected: 1

- Glyph name: horncomb	Contours detected: 3	Expected: 1

- Glyph name: commaaccentcomb	Contours detected: 2	Expected: 1

- Glyph name: cedillacomb	Contours detected: 3	Expected: 1

- Glyph name: ogonekcomb	Contours detected: 3	Expected: 1

- Glyph name: uni032E	Contours detected: 5	Expected: 1

- Glyph name: uni0331	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: baht	Contours detected: 20	Expected: 3 or 5

- Glyph name: uni1E0C	Contours detected: 17	Expected: 3

- Glyph name: uni1E0D	Contours detected: 17	Expected: 3

- Glyph name: uni1E0E	Contours detected: 19	Expected: 3

- Glyph name: uni1E0F	Contours detected: 19	Expected: 3

- Glyph name: uni1E20	Contours detected: 20	Expected: 2

- Glyph name: uni1E21	Contours detected: 21	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 18	Expected: 2

- Glyph name: uni1E25	Contours detected: 15	Expected: 2

- Glyph name: uni1E2A	Contours detected: 20	Expected: 2

- Glyph name: uni1E2B	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: uni1E44	Contours detected: 18	Expected: 2

- Glyph name: uni1E45	Contours detected: 13	Expected: 2

- Glyph name: uni1E46	Contours detected: 18	Expected: 2

- Glyph name: uni1E47	Contours detected: 13	Expected: 2

- Glyph name: uni1E48	Contours detected: 20	Expected: 2

- Glyph name: uni1E49	Contours detected: 15	Expected: 2

- Glyph name: uni1E5A	Contours detected: 19	Expected: 3

- Glyph name: uni1E5B	Contours detected: 10	Expected: 2

- Glyph name: uni1E5C	Contours detected: 22	Expected: 4

- Glyph name: uni1E5D	Contours detected: 13	Expected: 3

- Glyph name: uni1E5E	Contours detected: 21	Expected: 3

- Glyph name: uni1E5F	Contours detected: 12	Expected: 2

- Glyph name: uni1E60	Contours detected: 16	Expected: 2

- Glyph name: uni1E61	Contours detected: 14	Expected: 2

- Glyph name: uni1E62	Contours detected: 16	Expected: 2

- Glyph name: uni1E63	Contours detected: 14	Expected: 2

- Glyph name: uni1E6C	Contours detected: 12	Expected: 2

- Glyph name: uni1E6D	Contours detected: 13	Expected: 2

- Glyph name: uni1E6E	Contours detected: 14	Expected: 2

- Glyph name: uni1E6F	Contours detected: 15	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: uni1E92	Contours detected: 16	Expected: 2

- Glyph name: uni1E93	Contours detected: 14	Expected: 2

- Glyph name: uni1E97	Contours detected: 14	Expected: 3

- Glyph name: Germandbls	Contours detected: 18	Expected: 1

- Glyph name: Adotbelow	Contours detected: 17	Expected: 3

- Glyph name: adotbelow	Contours detected: 15	Expected: 3

- Glyph name: Ahookabove	Contours detected: 19	Expected: 3

- Glyph name: ahookabove	Contours detected: 17	Expected: 3

- Glyph name: Acircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: acircumflexacute	Contours detected: 19	Expected: 4

- Glyph name: Acircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: acircumflexgrave	Contours detected: 19	Expected: 4

- Glyph name: Acircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: acircumflexhookabove	Contours detected: 20	Expected: 4

- Glyph name: Acircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: acircumflextilde	Contours detected: 23	Expected: 4

- Glyph name: Acircumflexdotbelow	Contours detected: 20	Expected: 4

- Glyph name: acircumflexdotbelow	Contours detected: 18	Expected: 4

- Glyph name: Abreveacute	Contours detected: 19	Expected: 4

- Glyph name: abreveacute	Contours detected: 21	Expected: 4

- Glyph name: Abrevegrave	Contours detected: 19	Expected: 4

- Glyph name: abrevegrave	Contours detected: 21	Expected: 4

- Glyph name: Abrevehookabove	Contours detected: 20	Expected: 4

- Glyph name: abrevehookabove	Contours detected: 22	Expected: 4

- Glyph name: Abrevetilde	Contours detected: 23	Expected: 4

- Glyph name: abrevetilde	Contours detected: 25	Expected: 4

- Glyph name: Abrevedotbelow	Contours detected: 22	Expected: 4

- Glyph name: abrevedotbelow	Contours detected: 20	Expected: 4

- Glyph name: Edotbelow	Contours detected: 19	Expected: 2

- Glyph name: edotbelow	Contours detected: 15	Expected: 3

- Glyph name: Ehookabove	Contours detected: 21	Expected: 2

- Glyph name: ehookabove	Contours detected: 17	Expected: 3

- Glyph name: Etilde	Contours detected: 24	Expected: 2

- Glyph name: etilde	Contours detected: 20	Expected: 3

- Glyph name: Ecircumflexacute	Contours detected: 21	Expected: 3

- Glyph name: ecircumflexacute	Contours detected: 19	Expected: 4

- Glyph name: Ecircumflexgrave	Contours detected: 21	Expected: 3

- Glyph name: ecircumflexgrave	Contours detected: 19	Expected: 4

- Glyph name: Ecircumflexhookabove	Contours detected: 22	Expected: 3

- Glyph name: ecircumflexhookabove	Contours detected: 20	Expected: 4

- Glyph name: Ecircumflextilde	Contours detected: 25	Expected: 3

- Glyph name: ecircumflextilde	Contours detected: 23	Expected: 4

- Glyph name: Ecircumflexdotbelow	Contours detected: 22	Expected: 3

- Glyph name: ecircumflexdotbelow	Contours detected: 18	Expected: 4

- Glyph name: Ihookabove	Contours detected: 14	Expected: 2

- Glyph name: ihookabove	Contours detected: 11	Expected: 2

- Glyph name: Idotbelow	Contours detected: 12	Expected: 2

- Glyph name: idotbelow	Contours detected: 10	Expected: 3

- Glyph name: Odotbelow	Contours detected: 17	Expected: 3

- Glyph name: odotbelow	Contours detected: 13	Expected: 3

- Glyph name: Ohookabove	Contours detected: 19	Expected: 3

- Glyph name: ohookabove	Contours detected: 15	Expected: 3

- Glyph name: Ocircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: ocircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: Ocircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: ocircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: Ocircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: ocircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: Ocircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: ocircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: Ocircumflexdotbelow	Contours detected: 20	Expected: 4

- Glyph name: ocircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: Ohornacute	Contours detected: 21	Expected: 3 or 4

- Glyph name: ohornacute	Contours detected: 17	Expected: 3

- Glyph name: Ohorngrave	Contours detected: 21	Expected: 3 or 4

- Glyph name: ohorngrave	Contours detected: 17	Expected: 3

- Glyph name: Ohornhookabove	Contours detected: 22	Expected: 3 or 4

- Glyph name: ohornhookabove	Contours detected: 18	Expected: 3

- Glyph name: Ohorntilde	Contours detected: 25	Expected: 3 or 4

- Glyph name: ohorntilde	Contours detected: 21	Expected: 3

- Glyph name: Ohorndotbelow	Contours detected: 20	Expected: 3 or 4

- Glyph name: ohorndotbelow	Contours detected: 16	Expected: 3

- Glyph name: Udotbelow	Contours detected: 16	Expected: 2

- Glyph name: udotbelow	Contours detected: 13	Expected: 2

- Glyph name: Uhookabove	Contours detected: 18	Expected: 2

- Glyph name: uhookabove	Contours detected: 15	Expected: 2

- Glyph name: Uhornacute	Contours detected: 20	Expected: 2

- Glyph name: uhornacute	Contours detected: 17	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 20	Expected: 2

- Glyph name: uhorngrave	Contours detected: 17	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 21	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 18	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 24	Expected: 2

- Glyph name: uhorntilde	Contours detected: 21	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 19	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 16	Expected: 2

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: ygrave	Contours detected: 18	Expected: 2

- Glyph name: Ydotbelow	Contours detected: 11	Expected: 2

- Glyph name: ydotbelow	Contours detected: 13	Expected: 2

- Glyph name: Yhookabove	Contours detected: 13	Expected: 2

- Glyph name: yhookabove	Contours detected: 19	Expected: 2

- Glyph name: Ytilde	Contours detected: 16	Expected: 2

- Glyph name: ytilde	Contours detected: 22	Expected: 2

- Glyph name: uni2010	Contours detected: 4	Expected: 1

- Glyph name: uni2011	Contours detected: 4	Expected: 1

- Glyph name: figuredash	Contours detected: 5	Expected: 1

- Glyph name: endash	Contours detected: 5	Expected: 1

- Glyph name: emdash	Contours detected: 6	Expected: 1

- Glyph name: uni2015	Contours detected: 6	Expected: 1

- Glyph name: dblverticalbar	Contours detected: 14	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: dagger	Contours detected: 13	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 17	Expected: 1 or 3

- Glyph name: bullet	Contours detected: 9	Expected: 1

- Glyph name: perthousand	Contours detected: 17	Expected: 6 or 7

- Glyph name: minute	Contours detected: 3	Expected: 1

- Glyph name: second	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: uni2070	Contours detected: 8	Expected: 2 or 3

- Glyph name: foursuperior	Contours detected: 9	Expected: 1 or 2

- Glyph name: fivesuperior	Contours detected: 9	Expected: 1

- Glyph name: sixsuperior	Contours detected: 8	Expected: 2

- Glyph name: sevensuperior	Contours detected: 7	Expected: 1

- Glyph name: eightsuperior	Contours detected: 13	Expected: 3

- Glyph name: ninesuperior	Contours detected: 8	Expected: 2

- Glyph name: uni207D	Contours detected: 5	Expected: 1

- Glyph name: uni207E	Contours detected: 5	Expected: 1

- Glyph name: uni207F	Contours detected: 8	Expected: 1

- Glyph name: uni2080	Contours detected: 8	Expected: 2 or 3

- Glyph name: oneinferior	Contours detected: 8	Expected: 1

- Glyph name: twoinferior	Contours detected: 8	Expected: 1

- Glyph name: threeinferior	Contours detected: 8	Expected: 1

- Glyph name: fourinferior	Contours detected: 9	Expected: 1 or 2

- Glyph name: fiveinferior	Contours detected: 9	Expected: 1

- Glyph name: sixinferior	Contours detected: 8	Expected: 2

- Glyph name: seveninferior	Contours detected: 7	Expected: 1

- Glyph name: eightinferior	Contours detected: 13	Expected: 3

- Glyph name: nineinferior	Contours detected: 8	Expected: 2

- Glyph name: uni208D	Contours detected: 5	Expected: 1

- Glyph name: uni208E	Contours detected: 5	Expected: 1

- Glyph name: colonmonetary	Contours detected: 16	Expected: 1 or 3

- Glyph name: lira	Contours detected: 17	Expected: 1

- Glyph name: naira	Contours detected: 26	Expected: 1, 3 or 5

- Glyph name: peseta	Contours detected: 26	Expected: 2, 3 or 4

- Glyph name: rupee	Contours detected: 23	Expected: 3

- Glyph name: won	Contours detected: 26	Expected: 1, 3, 4 or 7

- Glyph name: sheqel	Contours detected: 24	Expected: 2

- Glyph name: dong	Contours detected: 23	Expected: 3 or 4

- Glyph name: Euro	Contours detected: 15	Expected: 1 or 2

- Glyph name: kip	Contours detected: 17	Expected: 1

- Glyph name: tugrik	Contours detected: 15	Expected: 1

- Glyph name: peso	Contours detected: 15	Expected: 1, 2 or 4

- Glyph name: guarani	Contours detected: 19	Expected: 1, 2 or 3

- Glyph name: hryvnia	Contours detected: 17	Expected: 1 or 2

- Glyph name: cedi	Contours detected: 16	Expected: 1 or 2

- Glyph name: tenge	Contours detected: 14	Expected: 2

- Glyph name: rupeeIndian	Contours detected: 17	Expected: 1

- Glyph name: liraTurkish	Contours detected: 15	Expected: 1

- Glyph name: manat	Contours detected: 17	Expected: 1

- Glyph name: ruble	Contours detected: 16	Expected: 2

- Glyph name: bitcoin	Contours detected: 20	Expected: 3

- Glyph name: literSign	Contours detected: 13	Expected: 2

- Glyph name: numero	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2117	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 18	Expected: 2

- Glyph name: trademark	Contours detected: 18	Expected: 2

- Glyph name: Ohm	Contours detected: 17	Expected: 1

- Glyph name: onethird	Contours detected: 16	Expected: 3

- Glyph name: twothirds	Contours detected: 16	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 21	Expected: 5

- Glyph name: threeeighths	Contours detected: 21	Expected: 5

- Glyph name: fiveeighths	Contours detected: 22	Expected: 5

- Glyph name: seveneighths	Contours detected: 20	Expected: 5

- Glyph name: arrowleft	Contours detected: 11	Expected: 1

- Glyph name: arrowup	Contours detected: 11	Expected: 1

- Glyph name: arrowright	Contours detected: 11	Expected: 1

- Glyph name: arrowdown	Contours detected: 11	Expected: 1

- Glyph name: arrowboth	Contours detected: 15	Expected: 1

- Glyph name: arrowupdn	Contours detected: 15	Expected: 1

- Glyph name: northWestArrow	Contours detected: 12	Expected: 1

- Glyph name: northEastArrow	Contours detected: 12	Expected: 1

- Glyph name: southEastArrow	Contours detected: 12	Expected: 1

- Glyph name: southWestArrow	Contours detected: 12	Expected: 1

- Glyph name: partialdiff	Contours detected: 15	Expected: 2

- Glyph name: emptyset	Contours detected: 21	Expected: 3

- Glyph name: increment	Contours detected: 15	Expected: 2

- Glyph name: product	Contours detected: 21	Expected: 1

- Glyph name: summation	Contours detected: 17	Expected: 1

- Glyph name: minus	Contours detected: 5	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 11	Expected: 1

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: approxequal	Contours detected: 12	Expected: 2

- Glyph name: notequal	Contours detected: 15	Expected: 1

- Glyph name: lessequal	Contours detected: 8	Expected: 2

- Glyph name: greaterequal	Contours detected: 8	Expected: 2

- Glyph name: filledbox	Contours detected: 42	Expected: 1

- Glyph name: whiteSquare	Contours detected: 24	Expected: 2

- Glyph name: blackSmallSquare	Contours detected: 9	Expected: 1

- Glyph name: whiteSmallSquare	Contours detected: 8	Expected: 2

- Glyph name: triagup	Contours detected: 31	Expected: 1

- Glyph name: upWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: rightBlackTriangle	Contours detected: 31	Expected: 1

- Glyph name: rightWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: triagdn	Contours detected: 31	Expected: 1

- Glyph name: downWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: leftBlackTriangle	Contours detected: 31	Expected: 1

- Glyph name: leftWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: blackDiamond	Contours detected: 25	Expected: 1

- Glyph name: whiteDiamond	Contours detected: 12	Expected: 2

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: circle	Contours detected: 16	Expected: 2

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: blackCircle	Contours detected: 37	Expected: 1

- Glyph name: leftanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: rightanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: uniFB01	Contours detected: 16	Expected: 1, 2 or 3

- Glyph name: uniFB02	Contours detected: 17	Expected: 1 or 2

- Glyph name: A	Contours detected: 16	Expected: 2

- Glyph name: AE	Contours detected: 24	Expected: 2

- Glyph name: Aacute	Contours detected: 18	Expected: 3

- Glyph name: Abreve	Contours detected: 21	Expected: 3

- Glyph name: Acircumflex	Contours detected: 19	Expected: 3

- Glyph name: Adieresis	Contours detected: 18	Expected: 4

- Glyph name: Agrave	Contours detected: 18	Expected: 3

- Glyph name: Amacron	Contours detected: 19	Expected: 3

- Glyph name: Aogonek	Contours detected: 19	Expected: 2 or 3

- Glyph name: Aring	Contours detected: 20	Expected: 3 or 4

- Glyph name: Atilde	Contours detected: 22	Expected: 3

- Glyph name: B	Contours detected: 20	Expected: 2 or 3

- Glyph name: C	Contours detected: 13	Expected: 1

- Glyph name: Cacute	Contours detected: 15	Expected: 2

- Glyph name: Ccaron	Contours detected: 16	Expected: 2

- Glyph name: Ccedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Ccircumflex	Contours detected: 16	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 14	Expected: 2

- Glyph name: D	Contours detected: 16	Expected: 2

- Glyph name: Dcaron	Contours detected: 19	Expected: 3

- Glyph name: Dcroat	Contours detected: 18	Expected: 2

- Glyph name: E	Contours detected: 18	Expected: 1

- Glyph name: Eacute	Contours detected: 20	Expected: 2

- Glyph name: Ebreve	Contours detected: 23	Expected: 2

- Glyph name: Ecaron	Contours detected: 21	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 21	Expected: 2

- Glyph name: Edieresis	Contours detected: 20	Expected: 3

- Glyph name: Edotaccent	Contours detected: 19	Expected: 2

- Glyph name: Egrave	Contours detected: 20	Expected: 2

- Glyph name: Emacron	Contours detected: 21	Expected: 2

- Glyph name: Eng	Contours detected: 19	Expected: 1

- Glyph name: Eogonek	Contours detected: 21	Expected: 1 or 2

- Glyph name: Eth	Contours detected: 18	Expected: 2

- Glyph name: Euro	Contours detected: 15	Expected: 1 or 2

- Glyph name: F	Contours detected: 14	Expected: 1

- Glyph name: G	Contours detected: 17	Expected: 1

- Glyph name: Gbreve	Contours detected: 22	Expected: 2

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: Gcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Gdotaccent	Contours detected: 18	Expected: 2

- Glyph name: H	Contours detected: 17	Expected: 1

- Glyph name: Hbar	Contours detected: 20	Expected: 2

- Glyph name: Hcircumflex	Contours detected: 20	Expected: 2

- Glyph name: I	Contours detected: 11	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: Iacute	Contours detected: 13	Expected: 2

- Glyph name: Icircumflex	Contours detected: 14	Expected: 2

- Glyph name: Idieresis	Contours detected: 13	Expected: 3

- Glyph name: Idotaccent	Contours detected: 12	Expected: 2

- Glyph name: Igrave	Contours detected: 13	Expected: 2

- Glyph name: Imacron	Contours detected: 14	Expected: 2

- Glyph name: Iogonek	Contours detected: 14	Expected: 1 or 2

- Glyph name: Itilde	Contours detected: 17	Expected: 2

- Glyph name: J	Contours detected: 11	Expected: 1

- Glyph name: Jcircumflex	Contours detected: 14	Expected: 2

- Glyph name: K	Contours detected: 14	Expected: 1 or 2

- Glyph name: L	Contours detected: 11	Expected: 1

- Glyph name: Lacute	Contours detected: 13	Expected: 2

- Glyph name: Lcaron	Contours detected: 13	Expected: 2

- Glyph name: Ldot	Contours detected: 12	Expected: 2

- Glyph name: Lslash	Contours detected: 13	Expected: 1

- Glyph name: M	Contours detected: 18	Expected: 1

- Glyph name: N	Contours detected: 17	Expected: 1

- Glyph name: Nacute	Contours detected: 19	Expected: 2

- Glyph name: Ncaron	Contours detected: 20	Expected: 2

- Glyph name: Ntilde	Contours detected: 23	Expected: 2

- Glyph name: O	Contours detected: 16	Expected: 2

- Glyph name: OE	Contours detected: 24	Expected: 2

- Glyph name: Oacute	Contours detected: 18	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 19	Expected: 3

- Glyph name: Odieresis	Contours detected: 18	Expected: 4

- Glyph name: Ograve	Contours detected: 18	Expected: 3

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: Ohungarumlaut	Contours detected: 20	Expected: 4

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: Oslash	Contours detected: 17	Expected: 2 or 3

- Glyph name: Otilde	Contours detected: 22	Expected: 3

- Glyph name: P	Contours detected: 15	Expected: 1 or 2

- Glyph name: Q	Contours detected: 17	Expected: 2

- Glyph name: R	Contours detected: 18	Expected: 1 or 2

- Glyph name: Racute	Contours detected: 20	Expected: 3

- Glyph name: Rcaron	Contours detected: 21	Expected: 3

- Glyph name: S	Contours detected: 15	Expected: 1

- Glyph name: Sacute	Contours detected: 17	Expected: 2

- Glyph name: Scaron	Contours detected: 18	Expected: 2

- Glyph name: Scircumflex	Contours detected: 18	Expected: 2

- Glyph name: T	Contours detected: 11	Expected: 1

- Glyph name: Tcaron	Contours detected: 14	Expected: 2

- Glyph name: Thorn	Contours detected: 16	Expected: 1 or 2

- Glyph name: U	Contours detected: 15	Expected: 1

- Glyph name: Uacute	Contours detected: 17	Expected: 2

- Glyph name: Ubreve	Contours detected: 20	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 18	Expected: 2

- Glyph name: Udieresis	Contours detected: 17	Expected: 3

- Glyph name: Ugrave	Contours detected: 17	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: Uhungarumlaut	Contours detected: 19	Expected: 3

- Glyph name: Umacron	Contours detected: 18	Expected: 2

- Glyph name: Uogonek	Contours detected: 18	Expected: 1

- Glyph name: Uring	Contours detected: 19	Expected: 3

- Glyph name: Utilde	Contours detected: 21	Expected: 2

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: Z	Contours detected: 15	Expected: 1

- Glyph name: Zacute	Contours detected: 17	Expected: 2

- Glyph name: Zcaron	Contours detected: 18	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 16	Expected: 2

- Glyph name: a	Contours detected: 14	Expected: 2

- Glyph name: aacute	Contours detected: 16	Expected: 3

- Glyph name: abreve	Contours detected: 19	Expected: 3

- Glyph name: acircumflex	Contours detected: 17	Expected: 3

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: adieresis	Contours detected: 16	Expected: 4

- Glyph name: ae	Contours detected: 18	Expected: 3

- Glyph name: agrave	Contours detected: 16	Expected: 3

- Glyph name: amacron	Contours detected: 17	Expected: 3

- Glyph name: ampersand	Contours detected: 14	Expected: 1, 2 or 3

- Glyph name: aogonek	Contours detected: 17	Expected: 2

- Glyph name: approxequal	Contours detected: 12	Expected: 2

- Glyph name: aring	Contours detected: 18	Expected: 4

- Glyph name: arrowboth	Contours detected: 15	Expected: 1

- Glyph name: arrowdown	Contours detected: 11	Expected: 1

- Glyph name: arrowup	Contours detected: 11	Expected: 1

- Glyph name: arrowupdn	Contours detected: 15	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 11	Expected: 1 or 4

- Glyph name: at	Contours detected: 20	Expected: 2

- Glyph name: atilde	Contours detected: 20	Expected: 3

- Glyph name: b	Contours detected: 16	Expected: 2

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceleft	Contours detected: 10	Expected: 1

- Glyph name: braceright	Contours detected: 10	Expected: 1

- Glyph name: bracketleft	Contours detected: 11	Expected: 1

- Glyph name: bracketright	Contours detected: 11	Expected: 1

- Glyph name: breve	Contours detected: 5	Expected: 1

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: bullet	Contours detected: 9	Expected: 1

- Glyph name: c	Contours detected: 11	Expected: 1

- Glyph name: cacute	Contours detected: 13	Expected: 2

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: ccaron	Contours detected: 14	Expected: 2

- Glyph name: ccedilla	Contours detected: 14	Expected: 1 or 2

- Glyph name: ccircumflex	Contours detected: 14	Expected: 2

- Glyph name: cdotaccent	Contours detected: 12	Expected: 2

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: cent	Contours detected: 16	Expected: 1 or 2

- Glyph name: circle	Contours detected: 16	Expected: 2

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: colonmonetary	Contours detected: 16	Expected: 1 or 3

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: copyright	Contours detected: 26	Expected: 3

- Glyph name: currency	Contours detected: 12	Expected: 2

- Glyph name: d	Contours detected: 16	Expected: 2

- Glyph name: dagger	Contours detected: 13	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 17	Expected: 1 or 3

- Glyph name: dcaron	Contours detected: 18	Expected: 3

- Glyph name: dcroat	Contours detected: 18	Expected: 2

- Glyph name: degree	Contours detected: 8	Expected: 2

- Glyph name: divide	Contours detected: 7	Expected: 3

- Glyph name: dollar	Contours detected: 17	Expected: 1, 3 or 5

- Glyph name: dong	Contours detected: 23	Expected: 3 or 4

- Glyph name: dotlessi	Contours detected: 8	Expected: 1

- Glyph name: e	Contours detected: 14	Expected: 2

- Glyph name: eacute	Contours detected: 16	Expected: 3

- Glyph name: ebreve	Contours detected: 19	Expected: 3

- Glyph name: ecaron	Contours detected: 17	Expected: 3

- Glyph name: ecircumflex	Contours detected: 17	Expected: 3

- Glyph name: edieresis	Contours detected: 16	Expected: 4

- Glyph name: edotaccent	Contours detected: 15	Expected: 3

- Glyph name: egrave	Contours detected: 16	Expected: 3

- Glyph name: eight	Contours detected: 17	Expected: 3

- Glyph name: emacron	Contours detected: 17	Expected: 3

- Glyph name: emdash	Contours detected: 6	Expected: 1

- Glyph name: emptyset	Contours detected: 21	Expected: 3

- Glyph name: endash	Contours detected: 5	Expected: 1

- Glyph name: eng	Contours detected: 15	Expected: 1

- Glyph name: eogonek	Contours detected: 17	Expected: 2

- Glyph name: equal	Contours detected: 10	Expected: 2

- Glyph name: eth	Contours detected: 16	Expected: 2

- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: f	Contours detected: 12	Expected: 1

- Glyph name: figuredash	Contours detected: 5	Expected: 1

- Glyph name: five	Contours detected: 17	Expected: 1

- Glyph name: fiveeighths	Contours detected: 22	Expected: 5

- Glyph name: four	Contours detected: 14	Expected: 1 or 2

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: g	Contours detected: 18	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 23	Expected: 3 or 4

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 21	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 19	Expected: 3 or 4

- Glyph name: germandbls	Contours detected: 16	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: greaterequal	Contours detected: 8	Expected: 2

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: h	Contours detected: 14	Expected: 1

- Glyph name: hbar	Contours detected: 16	Expected: 1

- Glyph name: hcircumflex	Contours detected: 17	Expected: 2

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: hyphen	Contours detected: 4	Expected: 1

- Glyph name: i	Contours detected: 9	Expected: 2

- Glyph name: iacute	Contours detected: 10	Expected: 2

- Glyph name: icircumflex	Contours detected: 11	Expected: 2

- Glyph name: idieresis	Contours detected: 10	Expected: 3

- Glyph name: igrave	Contours detected: 10	Expected: 2

- Glyph name: ij	Contours detected: 19	Expected: 3 or 4

- Glyph name: imacron	Contours detected: 11	Expected: 2

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: iogonek	Contours detected: 12	Expected: 2 or 3

- Glyph name: itilde	Contours detected: 14	Expected: 2

- Glyph name: j	Contours detected: 11	Expected: 2

- Glyph name: jcircumflex	Contours detected: 13	Expected: 2

- Glyph name: k	Contours detected: 13	Expected: 1 or 2

- Glyph name: kgreenlandic	Contours detected: 11	Expected: 1 or 2

- Glyph name: l	Contours detected: 10	Expected: 1

- Glyph name: lacute	Contours detected: 12	Expected: 2

- Glyph name: lcaron	Contours detected: 12	Expected: 2

- Glyph name: ldot	Contours detected: 11	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: lessequal	Contours detected: 8	Expected: 2

- Glyph name: lira	Contours detected: 17	Expected: 1

- Glyph name: logicalnot	Contours detected: 7	Expected: 1

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: lslash	Contours detected: 12	Expected: 1

- Glyph name: m	Contours detected: 14	Expected: 1

- Glyph name: macron	Contours detected: 3	Expected: 1

- Glyph name: minus	Contours detected: 5	Expected: 1

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: n	Contours detected: 12	Expected: 1

- Glyph name: nacute	Contours detected: 14	Expected: 2

- Glyph name: napostrophe	Contours detected: 15	Expected: 2

- Glyph name: ncaron	Contours detected: 15	Expected: 2

- Glyph name: nine	Contours detected: 15	Expected: 1 or 2

- Glyph name: notequal	Contours detected: 15	Expected: 1

- Glyph name: ntilde	Contours detected: 18	Expected: 2

- Glyph name: numbersign	Contours detected: 20	Expected: 2

- Glyph name: o	Contours detected: 12	Expected: 2

- Glyph name: oacute	Contours detected: 14	Expected: 3

- Glyph name: ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: odieresis	Contours detected: 14	Expected: 4

- Glyph name: oe	Contours detected: 18	Expected: 3

- Glyph name: ogonek	Contours detected: 3	Expected: 1

- Glyph name: ograve	Contours detected: 14	Expected: 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: one	Contours detected: 10	Expected: 1

- Glyph name: oneeighth	Contours detected: 21	Expected: 5

- Glyph name: onehalf	Contours detected: 16	Expected: 3

- Glyph name: onequarter	Contours detected: 17	Expected: 3 or 4

- Glyph name: onethird	Contours detected: 16	Expected: 3

- Glyph name: ordfeminine	Contours detected: 14	Expected: 2 or 3

- Glyph name: ordmasculine	Contours detected: 12	Expected: 2 or 3

- Glyph name: oslash	Contours detected: 13	Expected: 3

- Glyph name: otilde	Contours detected: 18	Expected: 3

- Glyph name: p	Contours detected: 16	Expected: 2

- Glyph name: paragraph	Contours detected: 23	Expected: 1, 2 or 3

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: partialdiff	Contours detected: 15	Expected: 2

- Glyph name: percent	Contours detected: 13	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 17	Expected: 6 or 7

- Glyph name: peseta	Contours detected: 26	Expected: 2, 3 or 4

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: plus	Contours detected: 9	Expected: 1

- Glyph name: plusminus	Contours detected: 14	Expected: 1 or 2

- Glyph name: product	Contours detected: 21	Expected: 1

- Glyph name: q	Contours detected: 16	Expected: 2

- Glyph name: question	Contours detected: 10	Expected: 2

- Glyph name: questiondown	Contours detected: 10	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: r	Contours detected: 9	Expected: 1

- Glyph name: racute	Contours detected: 11	Expected: 2

- Glyph name: radical	Contours detected: 11	Expected: 1

- Glyph name: rcaron	Contours detected: 12	Expected: 2

- Glyph name: registered	Contours detected: 30	Expected: 3 or 4

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: rupee	Contours detected: 23	Expected: 3

- Glyph name: s	Contours detected: 13	Expected: 1

- Glyph name: sacute	Contours detected: 15	Expected: 2

- Glyph name: scaron	Contours detected: 16	Expected: 2

- Glyph name: scircumflex	Contours detected: 16	Expected: 2

- Glyph name: section	Contours detected: 20	Expected: 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: seven	Contours detected: 11	Expected: 1

- Glyph name: seveneighths	Contours detected: 20	Expected: 5

- Glyph name: six	Contours detected: 15	Expected: 1 or 2

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: sterling	Contours detected: 15	Expected: 1 or 2

- Glyph name: summation	Contours detected: 17	Expected: 1

- Glyph name: t	Contours detected: 12	Expected: 1

- Glyph name: tcaron	Contours detected: 14	Expected: 2

- Glyph name: thorn	Contours detected: 18	Expected: 2

- Glyph name: three	Contours detected: 14	Expected: 1

- Glyph name: threeeighths	Contours detected: 21	Expected: 5

- Glyph name: threequarters	Contours detected: 17	Expected: 3 or 4

- Glyph name: tilde	Contours detected: 6	Expected: 1

- Glyph name: trademark	Contours detected: 18	Expected: 2

- Glyph name: triagdn	Contours detected: 31	Expected: 1

- Glyph name: triagup	Contours detected: 31	Expected: 1

- Glyph name: two	Contours detected: 15	Expected: 1

- Glyph name: twothirds	Contours detected: 16	Expected: 1 or 3

- Glyph name: u	Contours detected: 12	Expected: 1

- Glyph name: uacute	Contours detected: 14	Expected: 2

- Glyph name: ubreve	Contours detected: 17	Expected: 2

- Glyph name: ucircumflex	Contours detected: 15	Expected: 2

- Glyph name: udieresis	Contours detected: 14	Expected: 3

- Glyph name: ugrave	Contours detected: 14	Expected: 2

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: uhungarumlaut	Contours detected: 16	Expected: 3

- Glyph name: umacron	Contours detected: 15	Expected: 2

- Glyph name: underscore	Contours detected: 6	Expected: 1

- Glyph name: uni00AD	Contours detected: 4	Expected: 0

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: uni01CD	Contours detected: 19	Expected: 3

- Glyph name: uni01CE	Contours detected: 17	Expected: 3

- Glyph name: uni01CF	Contours detected: 14	Expected: 2

- Glyph name: uni01D0	Contours detected: 11	Expected: 2

- Glyph name: uni01D1	Contours detected: 19	Expected: 3

- Glyph name: uni01D2	Contours detected: 15	Expected: 3

- Glyph name: uni01D3	Contours detected: 18	Expected: 2

- Glyph name: uni01D4	Contours detected: 15	Expected: 2

- Glyph name: uni01D5	Contours detected: 18	Expected: 4

- Glyph name: uni01D6	Contours detected: 17	Expected: 4

- Glyph name: uni01D7	Contours detected: 15	Expected: 4

- Glyph name: uni01D8	Contours detected: 16	Expected: 4

- Glyph name: uni01D9	Contours detected: 16	Expected: 4

- Glyph name: uni01DA	Contours detected: 17	Expected: 4

- Glyph name: uni01DB	Contours detected: 15	Expected: 4

- Glyph name: uni01DC	Contours detected: 16	Expected: 4

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni032E	Contours detected: 5	Expected: 1

- Glyph name: uni0331	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: uni1E0C	Contours detected: 17	Expected: 3

- Glyph name: uni1E0D	Contours detected: 17	Expected: 3

- Glyph name: uni1E0E	Contours detected: 19	Expected: 3

- Glyph name: uni1E0F	Contours detected: 19	Expected: 3

- Glyph name: uni1E20	Contours detected: 20	Expected: 2

- Glyph name: uni1E21	Contours detected: 21	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 18	Expected: 2

- Glyph name: uni1E25	Contours detected: 15	Expected: 2

- Glyph name: uni1E2A	Contours detected: 20	Expected: 2

- Glyph name: uni1E2B	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: uni1E44	Contours detected: 18	Expected: 2

- Glyph name: uni1E45	Contours detected: 13	Expected: 2

- Glyph name: uni1E46	Contours detected: 18	Expected: 2

- Glyph name: uni1E47	Contours detected: 13	Expected: 2

- Glyph name: uni1E48	Contours detected: 20	Expected: 2

- Glyph name: uni1E49	Contours detected: 15	Expected: 2

- Glyph name: uni1E5A	Contours detected: 19	Expected: 3

- Glyph name: uni1E5B	Contours detected: 10	Expected: 2

- Glyph name: uni1E5C	Contours detected: 22	Expected: 4

- Glyph name: uni1E5D	Contours detected: 13	Expected: 3

- Glyph name: uni1E5E	Contours detected: 21	Expected: 3

- Glyph name: uni1E5F	Contours detected: 12	Expected: 2

- Glyph name: uni1E60	Contours detected: 16	Expected: 2

- Glyph name: uni1E61	Contours detected: 14	Expected: 2

- Glyph name: uni1E62	Contours detected: 16	Expected: 2

- Glyph name: uni1E63	Contours detected: 14	Expected: 2

- Glyph name: uni1E6C	Contours detected: 12	Expected: 2

- Glyph name: uni1E6D	Contours detected: 13	Expected: 2

- Glyph name: uni1E6E	Contours detected: 14	Expected: 2

- Glyph name: uni1E6F	Contours detected: 15	Expected: 2

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: uni1E92	Contours detected: 16	Expected: 2

- Glyph name: uni1E93	Contours detected: 14	Expected: 2

- Glyph name: uni1E97	Contours detected: 14	Expected: 3

- Glyph name: uni2010	Contours detected: 4	Expected: 1

- Glyph name: uni2011	Contours detected: 4	Expected: 1

- Glyph name: uni2015	Contours detected: 6	Expected: 1

- Glyph name: uni2117	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 18	Expected: 2

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 15	Expected: 1

- Glyph name: uring	Contours detected: 16	Expected: 3

- Glyph name: utilde	Contours detected: 18	Expected: 2

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 16	Expected: 1

- Glyph name: yacute	Contours detected: 18	Expected: 2

- Glyph name: ycircumflex	Contours detected: 19	Expected: 2

- Glyph name: ydieresis	Contours detected: 18	Expected: 3

- Glyph name: yen	Contours detected: 13	Expected: 1 or 2

- Glyph name: ygrave	Contours detected: 18	Expected: 2

- Glyph name: z	Contours detected: 13	Expected: 1

- Glyph name: zacute	Contours detected: 15	Expected: 2

- Glyph name: zcaron	Contours detected: 16	Expected: 2

- Glyph name: zdotaccent	Contours detected: 14	Expected: 2

- Glyph name: zero	Contours detected: 19	Expected: 2 or 3
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Heiltsuk (Latn, 300 speakers), Ekpeye (Latn, 226,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Zapotec (Latn, 490,000 speakers), Ejagham (Latn, 120,000 speakers), Mango (Latn, 77,000 speakers), Ma’di (Latn, 584,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Navajo (Latn, 166,319 speakers), Ebira (Latn, 2,200,000 speakers), Mundani (Latn, 34,000 speakers), Sar (Latn, 500,000 speakers), Dan (Latn, 1,099,244 speakers), Mfumte (Latn, 79,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Makaa (Latn, 221,000 speakers), Kaska (Latn, 125 speakers), Belarusian (Cyrl, 10,064,517 speakers), Fur (Latn, 1,230,163 speakers), Aghem (Latn, 38,843 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Teke-Ebo (Latn, 260,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Yala (Latn, 200,000 speakers), Vute (Latn, 21,000 speakers), Bafut (Latn, 158,146 speakers), Lugbara (Latn, 2,200,000 speakers), Gulay (Latn, 250,478 speakers), Nateni (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), South Central Banda (Latn, 244,000 speakers), Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Han (Latn, 6 speakers).</p>
 [code: soft-dotted]



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

<details><summary>[9] MatrixSansPrintSC-Regular.ttf</summary>
<div>
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

- Glyph name: plus	Contours detected: 9	Expected: 1

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: hyphen	Contours detected: 4	Expected: 1

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: zero	Contours detected: 19	Expected: 2 or 3

- Glyph name: one	Contours detected: 10	Expected: 1

- Glyph name: two	Contours detected: 15	Expected: 1

- Glyph name: three	Contours detected: 14	Expected: 1

- Glyph name: four	Contours detected: 14	Expected: 1 or 2

- Glyph name: five	Contours detected: 17	Expected: 1

- Glyph name: six	Contours detected: 15	Expected: 1 or 2

- Glyph name: seven	Contours detected: 11	Expected: 1

- Glyph name: eight	Contours detected: 17	Expected: 3

- Glyph name: nine	Contours detected: 15	Expected: 1 or 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: equal	Contours detected: 10	Expected: 2

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: question	Contours detected: 10	Expected: 2

- Glyph name: at	Contours detected: 20	Expected: 2

- Glyph name: A	Contours detected: 16	Expected: 2

- Glyph name: B	Contours detected: 20	Expected: 2 or 3

- Glyph name: C	Contours detected: 13	Expected: 1

- Glyph name: D	Contours detected: 16	Expected: 2

- Glyph name: E	Contours detected: 18	Expected: 1

- Glyph name: F	Contours detected: 14	Expected: 1

- Glyph name: G	Contours detected: 17	Expected: 1

- Glyph name: H	Contours detected: 17	Expected: 1

- Glyph name: I	Contours detected: 11	Expected: 1

- Glyph name: J	Contours detected: 11	Expected: 1

- Glyph name: K	Contours detected: 14	Expected: 1 or 2

- Glyph name: L	Contours detected: 11	Expected: 1

- Glyph name: M	Contours detected: 18	Expected: 1

- Glyph name: N	Contours detected: 17	Expected: 1

- Glyph name: O	Contours detected: 16	Expected: 2

- Glyph name: P	Contours detected: 15	Expected: 1 or 2

- Glyph name: Q	Contours detected: 17	Expected: 2

- Glyph name: R	Contours detected: 18	Expected: 1 or 2

- Glyph name: S	Contours detected: 15	Expected: 1

- Glyph name: T	Contours detected: 11	Expected: 1

- Glyph name: U	Contours detected: 15	Expected: 1

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Z	Contours detected: 15	Expected: 1

- Glyph name: bracketleft	Contours detected: 11	Expected: 1

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bracketright	Contours detected: 11	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: underscore	Contours detected: 6	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 14	Expected: 2

- Glyph name: b	Contours detected: 16	Expected: 2

- Glyph name: c	Contours detected: 11	Expected: 1

- Glyph name: d	Contours detected: 16	Expected: 2

- Glyph name: e	Contours detected: 14	Expected: 2

- Glyph name: f	Contours detected: 12	Expected: 1

- Glyph name: g	Contours detected: 18	Expected: 2 or 3

- Glyph name: h	Contours detected: 14	Expected: 1

- Glyph name: i	Contours detected: 9	Expected: 2

- Glyph name: j	Contours detected: 11	Expected: 2

- Glyph name: k	Contours detected: 13	Expected: 1 or 2

- Glyph name: l	Contours detected: 10	Expected: 1

- Glyph name: m	Contours detected: 14	Expected: 1

- Glyph name: n	Contours detected: 12	Expected: 1

- Glyph name: o	Contours detected: 12	Expected: 2

- Glyph name: p	Contours detected: 16	Expected: 2

- Glyph name: q	Contours detected: 16	Expected: 2

- Glyph name: r	Contours detected: 9	Expected: 1

- Glyph name: s	Contours detected: 13	Expected: 1

- Glyph name: t	Contours detected: 12	Expected: 1

- Glyph name: u	Contours detected: 12	Expected: 1

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 16	Expected: 1

- Glyph name: z	Contours detected: 13	Expected: 1

- Glyph name: braceleft	Contours detected: 10	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceright	Contours detected: 10	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: cent	Contours detected: 16	Expected: 1 or 2

- Glyph name: sterling	Contours detected: 15	Expected: 1 or 2

- Glyph name: currency	Contours detected: 12	Expected: 2

- Glyph name: yen	Contours detected: 13	Expected: 1 or 2

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: section	Contours detected: 20	Expected: 2

- Glyph name: copyright	Contours detected: 26	Expected: 3

- Glyph name: ordfeminine	Contours detected: 14	Expected: 2 or 3

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: logicalnot	Contours detected: 7	Expected: 1

- Glyph name: uni00AD	Contours detected: 4	Expected: 0

- Glyph name: registered	Contours detected: 30	Expected: 3 or 4

- Glyph name: macron	Contours detected: 3	Expected: 1

- Glyph name: degree	Contours detected: 8	Expected: 2

- Glyph name: plusminus	Contours detected: 14	Expected: 1 or 2

- Glyph name: twosuperior	Contours detected: 8	Expected: 1

- Glyph name: threesuperior	Contours detected: 8	Expected: 1

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: micro	Contours detected: 14	Expected: 1

- Glyph name: paragraph	Contours detected: 23	Expected: 1, 2 or 3

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: onesuperior	Contours detected: 8	Expected: 1

- Glyph name: ordmasculine	Contours detected: 12	Expected: 2 or 3

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: onequarter	Contours detected: 17	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 16	Expected: 3

- Glyph name: threequarters	Contours detected: 17	Expected: 3 or 4

- Glyph name: questiondown	Contours detected: 10	Expected: 2

- Glyph name: Agrave	Contours detected: 18	Expected: 3

- Glyph name: Aacute	Contours detected: 18	Expected: 3

- Glyph name: Acircumflex	Contours detected: 19	Expected: 3

- Glyph name: Atilde	Contours detected: 22	Expected: 3

- Glyph name: Adieresis	Contours detected: 18	Expected: 4

- Glyph name: Aring	Contours detected: 20	Expected: 3 or 4

- Glyph name: AE	Contours detected: 24	Expected: 2

- Glyph name: Ccedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Egrave	Contours detected: 20	Expected: 2

- Glyph name: Eacute	Contours detected: 20	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 21	Expected: 2

- Glyph name: Edieresis	Contours detected: 20	Expected: 3

- Glyph name: Igrave	Contours detected: 13	Expected: 2

- Glyph name: Iacute	Contours detected: 13	Expected: 2

- Glyph name: Icircumflex	Contours detected: 14	Expected: 2

- Glyph name: Idieresis	Contours detected: 13	Expected: 3

- Glyph name: Eth	Contours detected: 18	Expected: 2

- Glyph name: Ntilde	Contours detected: 23	Expected: 2

- Glyph name: Ograve	Contours detected: 18	Expected: 3

- Glyph name: Oacute	Contours detected: 18	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 19	Expected: 3

- Glyph name: Otilde	Contours detected: 22	Expected: 3

- Glyph name: Odieresis	Contours detected: 18	Expected: 4

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: Oslash	Contours detected: 17	Expected: 2 or 3

- Glyph name: Ugrave	Contours detected: 17	Expected: 2

- Glyph name: Uacute	Contours detected: 17	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 18	Expected: 2

- Glyph name: Udieresis	Contours detected: 17	Expected: 3

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Thorn	Contours detected: 16	Expected: 1 or 2

- Glyph name: germandbls	Contours detected: 16	Expected: 1

- Glyph name: agrave	Contours detected: 16	Expected: 3

- Glyph name: aacute	Contours detected: 16	Expected: 3

- Glyph name: acircumflex	Contours detected: 17	Expected: 3

- Glyph name: atilde	Contours detected: 20	Expected: 3

- Glyph name: adieresis	Contours detected: 16	Expected: 4

- Glyph name: aring	Contours detected: 18	Expected: 4

- Glyph name: ae	Contours detected: 18	Expected: 3

- Glyph name: ccedilla	Contours detected: 14	Expected: 1 or 2

- Glyph name: egrave	Contours detected: 16	Expected: 3

- Glyph name: eacute	Contours detected: 16	Expected: 3

- Glyph name: ecircumflex	Contours detected: 17	Expected: 3

- Glyph name: edieresis	Contours detected: 16	Expected: 4

- Glyph name: igrave	Contours detected: 10	Expected: 2

- Glyph name: iacute	Contours detected: 10	Expected: 2

- Glyph name: icircumflex	Contours detected: 11	Expected: 2

- Glyph name: idieresis	Contours detected: 10	Expected: 3

- Glyph name: eth	Contours detected: 16	Expected: 2

- Glyph name: ntilde	Contours detected: 18	Expected: 2

- Glyph name: ograve	Contours detected: 14	Expected: 3

- Glyph name: oacute	Contours detected: 14	Expected: 3

- Glyph name: ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: otilde	Contours detected: 18	Expected: 3

- Glyph name: odieresis	Contours detected: 14	Expected: 4

- Glyph name: divide	Contours detected: 7	Expected: 3

- Glyph name: oslash	Contours detected: 13	Expected: 3

- Glyph name: ugrave	Contours detected: 14	Expected: 2

- Glyph name: uacute	Contours detected: 14	Expected: 2

- Glyph name: ucircumflex	Contours detected: 15	Expected: 2

- Glyph name: udieresis	Contours detected: 14	Expected: 3

- Glyph name: yacute	Contours detected: 18	Expected: 2

- Glyph name: thorn	Contours detected: 18	Expected: 2

- Glyph name: ydieresis	Contours detected: 18	Expected: 3

- Glyph name: Amacron	Contours detected: 19	Expected: 3

- Glyph name: amacron	Contours detected: 17	Expected: 3

- Glyph name: Abreve	Contours detected: 21	Expected: 3

- Glyph name: abreve	Contours detected: 19	Expected: 3

- Glyph name: Aogonek	Contours detected: 19	Expected: 2 or 3

- Glyph name: aogonek	Contours detected: 17	Expected: 2

- Glyph name: Cacute	Contours detected: 15	Expected: 2

- Glyph name: cacute	Contours detected: 13	Expected: 2

- Glyph name: Ccircumflex	Contours detected: 16	Expected: 2

- Glyph name: ccircumflex	Contours detected: 14	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 14	Expected: 2

- Glyph name: cdotaccent	Contours detected: 12	Expected: 2

- Glyph name: Ccaron	Contours detected: 16	Expected: 2

- Glyph name: ccaron	Contours detected: 14	Expected: 2

- Glyph name: Dcaron	Contours detected: 19	Expected: 3

- Glyph name: dcaron	Contours detected: 18	Expected: 3

- Glyph name: Dcroat	Contours detected: 18	Expected: 2

- Glyph name: dcroat	Contours detected: 18	Expected: 2

- Glyph name: Emacron	Contours detected: 21	Expected: 2

- Glyph name: emacron	Contours detected: 17	Expected: 3

- Glyph name: Ebreve	Contours detected: 23	Expected: 2

- Glyph name: ebreve	Contours detected: 19	Expected: 3

- Glyph name: Edotaccent	Contours detected: 19	Expected: 2

- Glyph name: edotaccent	Contours detected: 15	Expected: 3

- Glyph name: Eogonek	Contours detected: 21	Expected: 1 or 2

- Glyph name: eogonek	Contours detected: 17	Expected: 2

- Glyph name: Ecaron	Contours detected: 21	Expected: 2

- Glyph name: ecaron	Contours detected: 17	Expected: 3

- Glyph name: Gcircumflex	Contours detected: 20	Expected: 2

- Glyph name: gcircumflex	Contours detected: 21	Expected: 3 or 4

- Glyph name: Gbreve	Contours detected: 22	Expected: 2

- Glyph name: gbreve	Contours detected: 23	Expected: 3 or 4

- Glyph name: Gdotaccent	Contours detected: 18	Expected: 2

- Glyph name: gdotaccent	Contours detected: 19	Expected: 3 or 4

- Glyph name: Gcommaaccent	Contours detected: 19	Expected: 2

- Glyph name: gcommaaccent	Contours detected: 20	Expected: 3 or 4

- Glyph name: Hcircumflex	Contours detected: 20	Expected: 2

- Glyph name: hcircumflex	Contours detected: 17	Expected: 2

- Glyph name: Hbar	Contours detected: 20	Expected: 2

- Glyph name: hbar	Contours detected: 16	Expected: 1

- Glyph name: Itilde	Contours detected: 17	Expected: 2

- Glyph name: itilde	Contours detected: 14	Expected: 2

- Glyph name: Imacron	Contours detected: 14	Expected: 2

- Glyph name: imacron	Contours detected: 11	Expected: 2

- Glyph name: Iogonek	Contours detected: 14	Expected: 1 or 2

- Glyph name: iogonek	Contours detected: 12	Expected: 2 or 3

- Glyph name: Idotaccent	Contours detected: 12	Expected: 2

- Glyph name: dotlessi	Contours detected: 8	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: ij	Contours detected: 19	Expected: 3 or 4

- Glyph name: Jcircumflex	Contours detected: 14	Expected: 2

- Glyph name: jcircumflex	Contours detected: 13	Expected: 2

- Glyph name: Kcommaaccent	Contours detected: 16	Expected: 2 or 3

- Glyph name: kcommaaccent	Contours detected: 15	Expected: 2 or 3

- Glyph name: kgreenlandic	Contours detected: 11	Expected: 1 or 2

- Glyph name: Lacute	Contours detected: 13	Expected: 2

- Glyph name: lacute	Contours detected: 12	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 12	Expected: 2

- Glyph name: Lcaron	Contours detected: 13	Expected: 2

- Glyph name: lcaron	Contours detected: 12	Expected: 2

- Glyph name: Ldot	Contours detected: 12	Expected: 2

- Glyph name: ldot	Contours detected: 11	Expected: 2

- Glyph name: Lslash	Contours detected: 13	Expected: 1

- Glyph name: lslash	Contours detected: 12	Expected: 1

- Glyph name: Nacute	Contours detected: 19	Expected: 2

- Glyph name: nacute	Contours detected: 14	Expected: 2

- Glyph name: Ncommaaccent	Contours detected: 19	Expected: 2

- Glyph name: ncommaaccent	Contours detected: 14	Expected: 2

- Glyph name: Ncaron	Contours detected: 20	Expected: 2

- Glyph name: ncaron	Contours detected: 15	Expected: 2

- Glyph name: napostrophe	Contours detected: 15	Expected: 2

- Glyph name: Eng	Contours detected: 19	Expected: 1

- Glyph name: eng	Contours detected: 15	Expected: 1

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: Ohungarumlaut	Contours detected: 20	Expected: 4

- Glyph name: ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: OE	Contours detected: 24	Expected: 2

- Glyph name: oe	Contours detected: 18	Expected: 3

- Glyph name: Racute	Contours detected: 20	Expected: 3

- Glyph name: racute	Contours detected: 11	Expected: 2

- Glyph name: Rcommaaccent	Contours detected: 20	Expected: 3

- Glyph name: rcommaaccent	Contours detected: 11	Expected: 2

- Glyph name: Rcaron	Contours detected: 21	Expected: 3

- Glyph name: rcaron	Contours detected: 12	Expected: 2

- Glyph name: Sacute	Contours detected: 17	Expected: 2

- Glyph name: sacute	Contours detected: 15	Expected: 2

- Glyph name: Scircumflex	Contours detected: 18	Expected: 2

- Glyph name: scircumflex	Contours detected: 16	Expected: 2

- Glyph name: Scedilla	Contours detected: 18	Expected: 1 or 2

- Glyph name: scedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Scaron	Contours detected: 18	Expected: 2

- Glyph name: scaron	Contours detected: 16	Expected: 2

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: Tcaron	Contours detected: 14	Expected: 2

- Glyph name: tcaron	Contours detected: 14	Expected: 2

- Glyph name: Utilde	Contours detected: 21	Expected: 2

- Glyph name: utilde	Contours detected: 18	Expected: 2

- Glyph name: Umacron	Contours detected: 18	Expected: 2

- Glyph name: umacron	Contours detected: 15	Expected: 2

- Glyph name: Ubreve	Contours detected: 20	Expected: 2

- Glyph name: ubreve	Contours detected: 17	Expected: 2

- Glyph name: Uring	Contours detected: 19	Expected: 3

- Glyph name: uring	Contours detected: 16	Expected: 3

- Glyph name: Uhungarumlaut	Contours detected: 19	Expected: 3

- Glyph name: uhungarumlaut	Contours detected: 16	Expected: 3

- Glyph name: Uogonek	Contours detected: 18	Expected: 1

- Glyph name: uogonek	Contours detected: 15	Expected: 1

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: ycircumflex	Contours detected: 19	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Zacute	Contours detected: 17	Expected: 2

- Glyph name: zacute	Contours detected: 15	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 16	Expected: 2

- Glyph name: zdotaccent	Contours detected: 14	Expected: 2

- Glyph name: Zcaron	Contours detected: 18	Expected: 2

- Glyph name: zcaron	Contours detected: 16	Expected: 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: florin	Contours detected: 14	Expected: 1

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: uni01CD	Contours detected: 19	Expected: 3

- Glyph name: uni01CE	Contours detected: 17	Expected: 3

- Glyph name: uni01CF	Contours detected: 14	Expected: 2

- Glyph name: uni01D0	Contours detected: 11	Expected: 2

- Glyph name: uni01D1	Contours detected: 19	Expected: 3

- Glyph name: uni01D2	Contours detected: 15	Expected: 3

- Glyph name: uni01D3	Contours detected: 18	Expected: 2

- Glyph name: uni01D4	Contours detected: 15	Expected: 2

- Glyph name: uni01D5	Contours detected: 18	Expected: 4

- Glyph name: uni01D6	Contours detected: 17	Expected: 4

- Glyph name: uni01D7	Contours detected: 15	Expected: 4

- Glyph name: uni01D8	Contours detected: 16	Expected: 4

- Glyph name: uni01D9	Contours detected: 16	Expected: 4

- Glyph name: uni01DA	Contours detected: 17	Expected: 4

- Glyph name: uni01DB	Contours detected: 15	Expected: 4

- Glyph name: uni01DC	Contours detected: 16	Expected: 4

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Scommaaccent	Contours detected: 17	Expected: 2

- Glyph name: scommaaccent	Contours detected: 15	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 14	Expected: 2

- Glyph name: jdotless	Contours detected: 10	Expected: 1

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: breve	Contours detected: 5	Expected: 1

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: ogonek	Contours detected: 3	Expected: 1

- Glyph name: tilde	Contours detected: 6	Expected: 1

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: gravecomb	Contours detected: 2	Expected: 1

- Glyph name: acutecomb	Contours detected: 2	Expected: 1

- Glyph name: circumflexcomb	Contours detected: 3	Expected: 1

- Glyph name: tildecomb	Contours detected: 6	Expected: 1

- Glyph name: macroncomb	Contours detected: 3	Expected: 1

- Glyph name: brevecomb	Contours detected: 5	Expected: 1

- Glyph name: hookabovecomb	Contours detected: 3	Expected: 1

- Glyph name: ringcomb	Contours detected: 4	Expected: 2

- Glyph name: hungarumlautcomb	Contours detected: 4	Expected: 2

- Glyph name: caroncomb	Contours detected: 3	Expected: 1

- Glyph name: commaturnedabovecomb	Contours detected: 2	Expected: 1

- Glyph name: horncomb	Contours detected: 3	Expected: 1

- Glyph name: commaaccentcomb	Contours detected: 2	Expected: 1

- Glyph name: cedillacomb	Contours detected: 3	Expected: 1

- Glyph name: ogonekcomb	Contours detected: 3	Expected: 1

- Glyph name: uni032E	Contours detected: 5	Expected: 1

- Glyph name: uni0331	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: baht	Contours detected: 20	Expected: 3 or 5

- Glyph name: uni1E0C	Contours detected: 17	Expected: 3

- Glyph name: uni1E0D	Contours detected: 17	Expected: 3

- Glyph name: uni1E0E	Contours detected: 19	Expected: 3

- Glyph name: uni1E0F	Contours detected: 19	Expected: 3

- Glyph name: uni1E20	Contours detected: 20	Expected: 2

- Glyph name: uni1E21	Contours detected: 21	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 18	Expected: 2

- Glyph name: uni1E25	Contours detected: 15	Expected: 2

- Glyph name: uni1E2A	Contours detected: 20	Expected: 2

- Glyph name: uni1E2B	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: uni1E44	Contours detected: 18	Expected: 2

- Glyph name: uni1E45	Contours detected: 13	Expected: 2

- Glyph name: uni1E46	Contours detected: 18	Expected: 2

- Glyph name: uni1E47	Contours detected: 13	Expected: 2

- Glyph name: uni1E48	Contours detected: 20	Expected: 2

- Glyph name: uni1E49	Contours detected: 15	Expected: 2

- Glyph name: uni1E5A	Contours detected: 19	Expected: 3

- Glyph name: uni1E5B	Contours detected: 10	Expected: 2

- Glyph name: uni1E5C	Contours detected: 22	Expected: 4

- Glyph name: uni1E5D	Contours detected: 13	Expected: 3

- Glyph name: uni1E5E	Contours detected: 21	Expected: 3

- Glyph name: uni1E5F	Contours detected: 12	Expected: 2

- Glyph name: uni1E60	Contours detected: 16	Expected: 2

- Glyph name: uni1E61	Contours detected: 14	Expected: 2

- Glyph name: uni1E62	Contours detected: 16	Expected: 2

- Glyph name: uni1E63	Contours detected: 14	Expected: 2

- Glyph name: uni1E6C	Contours detected: 12	Expected: 2

- Glyph name: uni1E6D	Contours detected: 13	Expected: 2

- Glyph name: uni1E6E	Contours detected: 14	Expected: 2

- Glyph name: uni1E6F	Contours detected: 15	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: uni1E92	Contours detected: 16	Expected: 2

- Glyph name: uni1E93	Contours detected: 14	Expected: 2

- Glyph name: uni1E97	Contours detected: 14	Expected: 3

- Glyph name: Germandbls	Contours detected: 18	Expected: 1

- Glyph name: Adotbelow	Contours detected: 17	Expected: 3

- Glyph name: adotbelow	Contours detected: 15	Expected: 3

- Glyph name: Ahookabove	Contours detected: 19	Expected: 3

- Glyph name: ahookabove	Contours detected: 17	Expected: 3

- Glyph name: Acircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: acircumflexacute	Contours detected: 19	Expected: 4

- Glyph name: Acircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: acircumflexgrave	Contours detected: 19	Expected: 4

- Glyph name: Acircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: acircumflexhookabove	Contours detected: 20	Expected: 4

- Glyph name: Acircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: acircumflextilde	Contours detected: 23	Expected: 4

- Glyph name: Acircumflexdotbelow	Contours detected: 20	Expected: 4

- Glyph name: acircumflexdotbelow	Contours detected: 18	Expected: 4

- Glyph name: Abreveacute	Contours detected: 19	Expected: 4

- Glyph name: abreveacute	Contours detected: 21	Expected: 4

- Glyph name: Abrevegrave	Contours detected: 19	Expected: 4

- Glyph name: abrevegrave	Contours detected: 21	Expected: 4

- Glyph name: Abrevehookabove	Contours detected: 20	Expected: 4

- Glyph name: abrevehookabove	Contours detected: 22	Expected: 4

- Glyph name: Abrevetilde	Contours detected: 23	Expected: 4

- Glyph name: abrevetilde	Contours detected: 25	Expected: 4

- Glyph name: Abrevedotbelow	Contours detected: 22	Expected: 4

- Glyph name: abrevedotbelow	Contours detected: 20	Expected: 4

- Glyph name: Edotbelow	Contours detected: 19	Expected: 2

- Glyph name: edotbelow	Contours detected: 15	Expected: 3

- Glyph name: Ehookabove	Contours detected: 21	Expected: 2

- Glyph name: ehookabove	Contours detected: 17	Expected: 3

- Glyph name: Etilde	Contours detected: 24	Expected: 2

- Glyph name: etilde	Contours detected: 20	Expected: 3

- Glyph name: Ecircumflexacute	Contours detected: 21	Expected: 3

- Glyph name: ecircumflexacute	Contours detected: 19	Expected: 4

- Glyph name: Ecircumflexgrave	Contours detected: 21	Expected: 3

- Glyph name: ecircumflexgrave	Contours detected: 19	Expected: 4

- Glyph name: Ecircumflexhookabove	Contours detected: 22	Expected: 3

- Glyph name: ecircumflexhookabove	Contours detected: 20	Expected: 4

- Glyph name: Ecircumflextilde	Contours detected: 25	Expected: 3

- Glyph name: ecircumflextilde	Contours detected: 23	Expected: 4

- Glyph name: Ecircumflexdotbelow	Contours detected: 22	Expected: 3

- Glyph name: ecircumflexdotbelow	Contours detected: 18	Expected: 4

- Glyph name: Ihookabove	Contours detected: 14	Expected: 2

- Glyph name: ihookabove	Contours detected: 11	Expected: 2

- Glyph name: Idotbelow	Contours detected: 12	Expected: 2

- Glyph name: idotbelow	Contours detected: 10	Expected: 3

- Glyph name: Odotbelow	Contours detected: 17	Expected: 3

- Glyph name: odotbelow	Contours detected: 13	Expected: 3

- Glyph name: Ohookabove	Contours detected: 19	Expected: 3

- Glyph name: ohookabove	Contours detected: 15	Expected: 3

- Glyph name: Ocircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: ocircumflexacute	Contours detected: 17	Expected: 4

- Glyph name: Ocircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: ocircumflexgrave	Contours detected: 17	Expected: 4

- Glyph name: Ocircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: ocircumflexhookabove	Contours detected: 18	Expected: 4

- Glyph name: Ocircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: ocircumflextilde	Contours detected: 21	Expected: 4

- Glyph name: Ocircumflexdotbelow	Contours detected: 20	Expected: 4

- Glyph name: ocircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: Ohornacute	Contours detected: 21	Expected: 3 or 4

- Glyph name: ohornacute	Contours detected: 17	Expected: 3

- Glyph name: Ohorngrave	Contours detected: 21	Expected: 3 or 4

- Glyph name: ohorngrave	Contours detected: 17	Expected: 3

- Glyph name: Ohornhookabove	Contours detected: 22	Expected: 3 or 4

- Glyph name: ohornhookabove	Contours detected: 18	Expected: 3

- Glyph name: Ohorntilde	Contours detected: 25	Expected: 3 or 4

- Glyph name: ohorntilde	Contours detected: 21	Expected: 3

- Glyph name: Ohorndotbelow	Contours detected: 20	Expected: 3 or 4

- Glyph name: ohorndotbelow	Contours detected: 16	Expected: 3

- Glyph name: Udotbelow	Contours detected: 16	Expected: 2

- Glyph name: udotbelow	Contours detected: 13	Expected: 2

- Glyph name: Uhookabove	Contours detected: 18	Expected: 2

- Glyph name: uhookabove	Contours detected: 15	Expected: 2

- Glyph name: Uhornacute	Contours detected: 20	Expected: 2

- Glyph name: uhornacute	Contours detected: 17	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 20	Expected: 2

- Glyph name: uhorngrave	Contours detected: 17	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 21	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 18	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 24	Expected: 2

- Glyph name: uhorntilde	Contours detected: 21	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 19	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 16	Expected: 2

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: ygrave	Contours detected: 18	Expected: 2

- Glyph name: Ydotbelow	Contours detected: 11	Expected: 2

- Glyph name: ydotbelow	Contours detected: 13	Expected: 2

- Glyph name: Yhookabove	Contours detected: 13	Expected: 2

- Glyph name: yhookabove	Contours detected: 19	Expected: 2

- Glyph name: Ytilde	Contours detected: 16	Expected: 2

- Glyph name: ytilde	Contours detected: 22	Expected: 2

- Glyph name: uni2010	Contours detected: 4	Expected: 1

- Glyph name: uni2011	Contours detected: 4	Expected: 1

- Glyph name: figuredash	Contours detected: 5	Expected: 1

- Glyph name: endash	Contours detected: 5	Expected: 1

- Glyph name: emdash	Contours detected: 6	Expected: 1

- Glyph name: uni2015	Contours detected: 6	Expected: 1

- Glyph name: dblverticalbar	Contours detected: 14	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: dagger	Contours detected: 13	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 17	Expected: 1 or 3

- Glyph name: bullet	Contours detected: 9	Expected: 1

- Glyph name: perthousand	Contours detected: 17	Expected: 6 or 7

- Glyph name: minute	Contours detected: 3	Expected: 1

- Glyph name: second	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: uni2070	Contours detected: 8	Expected: 2 or 3

- Glyph name: foursuperior	Contours detected: 9	Expected: 1 or 2

- Glyph name: fivesuperior	Contours detected: 9	Expected: 1

- Glyph name: sixsuperior	Contours detected: 8	Expected: 2

- Glyph name: sevensuperior	Contours detected: 7	Expected: 1

- Glyph name: eightsuperior	Contours detected: 13	Expected: 3

- Glyph name: ninesuperior	Contours detected: 8	Expected: 2

- Glyph name: uni207D	Contours detected: 5	Expected: 1

- Glyph name: uni207E	Contours detected: 5	Expected: 1

- Glyph name: uni207F	Contours detected: 8	Expected: 1

- Glyph name: uni2080	Contours detected: 8	Expected: 2 or 3

- Glyph name: oneinferior	Contours detected: 8	Expected: 1

- Glyph name: twoinferior	Contours detected: 8	Expected: 1

- Glyph name: threeinferior	Contours detected: 8	Expected: 1

- Glyph name: fourinferior	Contours detected: 9	Expected: 1 or 2

- Glyph name: fiveinferior	Contours detected: 9	Expected: 1

- Glyph name: sixinferior	Contours detected: 8	Expected: 2

- Glyph name: seveninferior	Contours detected: 7	Expected: 1

- Glyph name: eightinferior	Contours detected: 13	Expected: 3

- Glyph name: nineinferior	Contours detected: 8	Expected: 2

- Glyph name: uni208D	Contours detected: 5	Expected: 1

- Glyph name: uni208E	Contours detected: 5	Expected: 1

- Glyph name: colonmonetary	Contours detected: 16	Expected: 1 or 3

- Glyph name: lira	Contours detected: 17	Expected: 1

- Glyph name: naira	Contours detected: 26	Expected: 1, 3 or 5

- Glyph name: peseta	Contours detected: 26	Expected: 2, 3 or 4

- Glyph name: rupee	Contours detected: 23	Expected: 3

- Glyph name: won	Contours detected: 26	Expected: 1, 3, 4 or 7

- Glyph name: sheqel	Contours detected: 24	Expected: 2

- Glyph name: dong	Contours detected: 23	Expected: 3 or 4

- Glyph name: Euro	Contours detected: 15	Expected: 1 or 2

- Glyph name: kip	Contours detected: 17	Expected: 1

- Glyph name: tugrik	Contours detected: 15	Expected: 1

- Glyph name: peso	Contours detected: 15	Expected: 1, 2 or 4

- Glyph name: guarani	Contours detected: 19	Expected: 1, 2 or 3

- Glyph name: hryvnia	Contours detected: 17	Expected: 1 or 2

- Glyph name: cedi	Contours detected: 16	Expected: 1 or 2

- Glyph name: tenge	Contours detected: 14	Expected: 2

- Glyph name: rupeeIndian	Contours detected: 17	Expected: 1

- Glyph name: liraTurkish	Contours detected: 15	Expected: 1

- Glyph name: manat	Contours detected: 17	Expected: 1

- Glyph name: ruble	Contours detected: 16	Expected: 2

- Glyph name: bitcoin	Contours detected: 20	Expected: 3

- Glyph name: literSign	Contours detected: 13	Expected: 2

- Glyph name: numero	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2117	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 18	Expected: 2

- Glyph name: trademark	Contours detected: 18	Expected: 2

- Glyph name: Ohm	Contours detected: 17	Expected: 1

- Glyph name: onethird	Contours detected: 16	Expected: 3

- Glyph name: twothirds	Contours detected: 16	Expected: 1 or 3

- Glyph name: oneeighth	Contours detected: 21	Expected: 5

- Glyph name: threeeighths	Contours detected: 21	Expected: 5

- Glyph name: fiveeighths	Contours detected: 22	Expected: 5

- Glyph name: seveneighths	Contours detected: 20	Expected: 5

- Glyph name: arrowleft	Contours detected: 11	Expected: 1

- Glyph name: arrowup	Contours detected: 11	Expected: 1

- Glyph name: arrowright	Contours detected: 11	Expected: 1

- Glyph name: arrowdown	Contours detected: 11	Expected: 1

- Glyph name: arrowboth	Contours detected: 15	Expected: 1

- Glyph name: arrowupdn	Contours detected: 15	Expected: 1

- Glyph name: northWestArrow	Contours detected: 12	Expected: 1

- Glyph name: northEastArrow	Contours detected: 12	Expected: 1

- Glyph name: southEastArrow	Contours detected: 12	Expected: 1

- Glyph name: southWestArrow	Contours detected: 12	Expected: 1

- Glyph name: partialdiff	Contours detected: 15	Expected: 2

- Glyph name: emptyset	Contours detected: 21	Expected: 3

- Glyph name: increment	Contours detected: 15	Expected: 2

- Glyph name: product	Contours detected: 21	Expected: 1

- Glyph name: summation	Contours detected: 17	Expected: 1

- Glyph name: minus	Contours detected: 5	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 11	Expected: 1

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: approxequal	Contours detected: 12	Expected: 2

- Glyph name: notequal	Contours detected: 15	Expected: 1

- Glyph name: lessequal	Contours detected: 8	Expected: 2

- Glyph name: greaterequal	Contours detected: 8	Expected: 2

- Glyph name: filledbox	Contours detected: 42	Expected: 1

- Glyph name: whiteSquare	Contours detected: 24	Expected: 2

- Glyph name: blackSmallSquare	Contours detected: 9	Expected: 1

- Glyph name: whiteSmallSquare	Contours detected: 8	Expected: 2

- Glyph name: triagup	Contours detected: 31	Expected: 1

- Glyph name: upWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: rightBlackTriangle	Contours detected: 31	Expected: 1

- Glyph name: rightWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: triagdn	Contours detected: 31	Expected: 1

- Glyph name: downWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: leftBlackTriangle	Contours detected: 31	Expected: 1

- Glyph name: leftWhiteTriangle	Contours detected: 18	Expected: 2

- Glyph name: blackDiamond	Contours detected: 25	Expected: 1

- Glyph name: whiteDiamond	Contours detected: 12	Expected: 2

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: circle	Contours detected: 16	Expected: 2

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: blackCircle	Contours detected: 37	Expected: 1

- Glyph name: leftanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: rightanglebracket_math	Contours detected: 7	Expected: 1

- Glyph name: uniFB01	Contours detected: 16	Expected: 1, 2 or 3

- Glyph name: uniFB02	Contours detected: 17	Expected: 1 or 2

- Glyph name: A	Contours detected: 16	Expected: 2

- Glyph name: AE	Contours detected: 24	Expected: 2

- Glyph name: Aacute	Contours detected: 18	Expected: 3

- Glyph name: Abreve	Contours detected: 21	Expected: 3

- Glyph name: Acircumflex	Contours detected: 19	Expected: 3

- Glyph name: Adieresis	Contours detected: 18	Expected: 4

- Glyph name: Agrave	Contours detected: 18	Expected: 3

- Glyph name: Amacron	Contours detected: 19	Expected: 3

- Glyph name: Aogonek	Contours detected: 19	Expected: 2 or 3

- Glyph name: Aring	Contours detected: 20	Expected: 3 or 4

- Glyph name: Atilde	Contours detected: 22	Expected: 3

- Glyph name: B	Contours detected: 20	Expected: 2 or 3

- Glyph name: C	Contours detected: 13	Expected: 1

- Glyph name: Cacute	Contours detected: 15	Expected: 2

- Glyph name: Ccaron	Contours detected: 16	Expected: 2

- Glyph name: Ccedilla	Contours detected: 16	Expected: 1 or 2

- Glyph name: Ccircumflex	Contours detected: 16	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 14	Expected: 2

- Glyph name: D	Contours detected: 16	Expected: 2

- Glyph name: Dcaron	Contours detected: 19	Expected: 3

- Glyph name: Dcroat	Contours detected: 18	Expected: 2

- Glyph name: E	Contours detected: 18	Expected: 1

- Glyph name: Eacute	Contours detected: 20	Expected: 2

- Glyph name: Ebreve	Contours detected: 23	Expected: 2

- Glyph name: Ecaron	Contours detected: 21	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 21	Expected: 2

- Glyph name: Edieresis	Contours detected: 20	Expected: 3

- Glyph name: Edotaccent	Contours detected: 19	Expected: 2

- Glyph name: Egrave	Contours detected: 20	Expected: 2

- Glyph name: Emacron	Contours detected: 21	Expected: 2

- Glyph name: Eng	Contours detected: 19	Expected: 1

- Glyph name: Eogonek	Contours detected: 21	Expected: 1 or 2

- Glyph name: Eth	Contours detected: 18	Expected: 2

- Glyph name: Euro	Contours detected: 15	Expected: 1 or 2

- Glyph name: F	Contours detected: 14	Expected: 1

- Glyph name: G	Contours detected: 17	Expected: 1

- Glyph name: Gbreve	Contours detected: 22	Expected: 2

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: Gcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Gdotaccent	Contours detected: 18	Expected: 2

- Glyph name: H	Contours detected: 17	Expected: 1

- Glyph name: Hbar	Contours detected: 20	Expected: 2

- Glyph name: Hcircumflex	Contours detected: 20	Expected: 2

- Glyph name: I	Contours detected: 11	Expected: 1

- Glyph name: IJ	Contours detected: 15	Expected: 1 or 2

- Glyph name: Iacute	Contours detected: 13	Expected: 2

- Glyph name: Icircumflex	Contours detected: 14	Expected: 2

- Glyph name: Idieresis	Contours detected: 13	Expected: 3

- Glyph name: Idotaccent	Contours detected: 12	Expected: 2

- Glyph name: Igrave	Contours detected: 13	Expected: 2

- Glyph name: Imacron	Contours detected: 14	Expected: 2

- Glyph name: Iogonek	Contours detected: 14	Expected: 1 or 2

- Glyph name: Itilde	Contours detected: 17	Expected: 2

- Glyph name: J	Contours detected: 11	Expected: 1

- Glyph name: Jcircumflex	Contours detected: 14	Expected: 2

- Glyph name: K	Contours detected: 14	Expected: 1 or 2

- Glyph name: L	Contours detected: 11	Expected: 1

- Glyph name: Lacute	Contours detected: 13	Expected: 2

- Glyph name: Lcaron	Contours detected: 13	Expected: 2

- Glyph name: Ldot	Contours detected: 12	Expected: 2

- Glyph name: Lslash	Contours detected: 13	Expected: 1

- Glyph name: M	Contours detected: 18	Expected: 1

- Glyph name: N	Contours detected: 17	Expected: 1

- Glyph name: Nacute	Contours detected: 19	Expected: 2

- Glyph name: Ncaron	Contours detected: 20	Expected: 2

- Glyph name: Ntilde	Contours detected: 23	Expected: 2

- Glyph name: O	Contours detected: 16	Expected: 2

- Glyph name: OE	Contours detected: 24	Expected: 2

- Glyph name: Oacute	Contours detected: 18	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 19	Expected: 3

- Glyph name: Odieresis	Contours detected: 18	Expected: 4

- Glyph name: Ograve	Contours detected: 18	Expected: 3

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: Ohungarumlaut	Contours detected: 20	Expected: 4

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: Oslash	Contours detected: 17	Expected: 2 or 3

- Glyph name: Otilde	Contours detected: 22	Expected: 3

- Glyph name: P	Contours detected: 15	Expected: 1 or 2

- Glyph name: Q	Contours detected: 17	Expected: 2

- Glyph name: R	Contours detected: 18	Expected: 1 or 2

- Glyph name: Racute	Contours detected: 20	Expected: 3

- Glyph name: Rcaron	Contours detected: 21	Expected: 3

- Glyph name: S	Contours detected: 15	Expected: 1

- Glyph name: Sacute	Contours detected: 17	Expected: 2

- Glyph name: Scaron	Contours detected: 18	Expected: 2

- Glyph name: Scircumflex	Contours detected: 18	Expected: 2

- Glyph name: T	Contours detected: 11	Expected: 1

- Glyph name: Tcaron	Contours detected: 14	Expected: 2

- Glyph name: Thorn	Contours detected: 16	Expected: 1 or 2

- Glyph name: U	Contours detected: 15	Expected: 1

- Glyph name: Uacute	Contours detected: 17	Expected: 2

- Glyph name: Ubreve	Contours detected: 20	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 18	Expected: 2

- Glyph name: Udieresis	Contours detected: 17	Expected: 3

- Glyph name: Ugrave	Contours detected: 17	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: Uhungarumlaut	Contours detected: 19	Expected: 3

- Glyph name: Umacron	Contours detected: 18	Expected: 2

- Glyph name: Uogonek	Contours detected: 18	Expected: 1

- Glyph name: Uring	Contours detected: 19	Expected: 3

- Glyph name: Utilde	Contours detected: 21	Expected: 2

- Glyph name: V	Contours detected: 13	Expected: 1

- Glyph name: W	Contours detected: 17	Expected: 1 or 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: Wcircumflex	Contours detected: 20	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: X	Contours detected: 13	Expected: 1

- Glyph name: Y	Contours detected: 10	Expected: 1

- Glyph name: Yacute	Contours detected: 12	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 13	Expected: 2

- Glyph name: Ydieresis	Contours detected: 12	Expected: 3

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: Z	Contours detected: 15	Expected: 1

- Glyph name: Zacute	Contours detected: 17	Expected: 2

- Glyph name: Zcaron	Contours detected: 18	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 16	Expected: 2

- Glyph name: a	Contours detected: 14	Expected: 2

- Glyph name: aacute	Contours detected: 16	Expected: 3

- Glyph name: abreve	Contours detected: 19	Expected: 3

- Glyph name: acircumflex	Contours detected: 17	Expected: 3

- Glyph name: acute	Contours detected: 2	Expected: 1

- Glyph name: adieresis	Contours detected: 16	Expected: 4

- Glyph name: ae	Contours detected: 18	Expected: 3

- Glyph name: agrave	Contours detected: 16	Expected: 3

- Glyph name: amacron	Contours detected: 17	Expected: 3

- Glyph name: ampersand	Contours detected: 14	Expected: 1, 2 or 3

- Glyph name: aogonek	Contours detected: 17	Expected: 2

- Glyph name: approxequal	Contours detected: 12	Expected: 2

- Glyph name: aring	Contours detected: 18	Expected: 4

- Glyph name: arrowboth	Contours detected: 15	Expected: 1

- Glyph name: arrowdown	Contours detected: 11	Expected: 1

- Glyph name: arrowup	Contours detected: 11	Expected: 1

- Glyph name: arrowupdn	Contours detected: 15	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: asciitilde	Contours detected: 7	Expected: 1

- Glyph name: asterisk	Contours detected: 11	Expected: 1 or 4

- Glyph name: at	Contours detected: 20	Expected: 2

- Glyph name: atilde	Contours detected: 20	Expected: 3

- Glyph name: b	Contours detected: 16	Expected: 2

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: bar	Contours detected: 7	Expected: 1

- Glyph name: braceleft	Contours detected: 10	Expected: 1

- Glyph name: braceright	Contours detected: 10	Expected: 1

- Glyph name: bracketleft	Contours detected: 11	Expected: 1

- Glyph name: bracketright	Contours detected: 11	Expected: 1

- Glyph name: breve	Contours detected: 5	Expected: 1

- Glyph name: brokenbar	Contours detected: 6	Expected: 2

- Glyph name: bullet	Contours detected: 9	Expected: 1

- Glyph name: c	Contours detected: 11	Expected: 1

- Glyph name: cacute	Contours detected: 13	Expected: 2

- Glyph name: caron	Contours detected: 3	Expected: 1

- Glyph name: ccaron	Contours detected: 14	Expected: 2

- Glyph name: ccedilla	Contours detected: 14	Expected: 1 or 2

- Glyph name: ccircumflex	Contours detected: 14	Expected: 2

- Glyph name: cdotaccent	Contours detected: 12	Expected: 2

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: cent	Contours detected: 16	Expected: 1 or 2

- Glyph name: circle	Contours detected: 16	Expected: 2

- Glyph name: circumflex	Contours detected: 3	Expected: 1

- Glyph name: colonmonetary	Contours detected: 16	Expected: 1 or 3

- Glyph name: comma	Contours detected: 3	Expected: 1

- Glyph name: copyright	Contours detected: 26	Expected: 3

- Glyph name: currency	Contours detected: 12	Expected: 2

- Glyph name: d	Contours detected: 16	Expected: 2

- Glyph name: dagger	Contours detected: 13	Expected: 1 or 2

- Glyph name: daggerdbl	Contours detected: 17	Expected: 1 or 3

- Glyph name: dcaron	Contours detected: 18	Expected: 3

- Glyph name: dcroat	Contours detected: 18	Expected: 2

- Glyph name: degree	Contours detected: 8	Expected: 2

- Glyph name: divide	Contours detected: 7	Expected: 3

- Glyph name: dollar	Contours detected: 17	Expected: 1, 3 or 5

- Glyph name: dong	Contours detected: 23	Expected: 3 or 4

- Glyph name: dotlessi	Contours detected: 8	Expected: 1

- Glyph name: e	Contours detected: 14	Expected: 2

- Glyph name: eacute	Contours detected: 16	Expected: 3

- Glyph name: ebreve	Contours detected: 19	Expected: 3

- Glyph name: ecaron	Contours detected: 17	Expected: 3

- Glyph name: ecircumflex	Contours detected: 17	Expected: 3

- Glyph name: edieresis	Contours detected: 16	Expected: 4

- Glyph name: edotaccent	Contours detected: 15	Expected: 3

- Glyph name: egrave	Contours detected: 16	Expected: 3

- Glyph name: eight	Contours detected: 17	Expected: 3

- Glyph name: emacron	Contours detected: 17	Expected: 3

- Glyph name: emdash	Contours detected: 6	Expected: 1

- Glyph name: emptyset	Contours detected: 21	Expected: 3

- Glyph name: endash	Contours detected: 5	Expected: 1

- Glyph name: eng	Contours detected: 15	Expected: 1

- Glyph name: eogonek	Contours detected: 17	Expected: 2

- Glyph name: equal	Contours detected: 10	Expected: 2

- Glyph name: eth	Contours detected: 16	Expected: 2

- Glyph name: exclam	Contours detected: 6	Expected: 2

- Glyph name: exclamdown	Contours detected: 6	Expected: 2

- Glyph name: f	Contours detected: 12	Expected: 1

- Glyph name: figuredash	Contours detected: 5	Expected: 1

- Glyph name: five	Contours detected: 17	Expected: 1

- Glyph name: fiveeighths	Contours detected: 22	Expected: 5

- Glyph name: four	Contours detected: 14	Expected: 1 or 2

- Glyph name: fraction	Contours detected: 5	Expected: 1

- Glyph name: g	Contours detected: 18	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 23	Expected: 3 or 4

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 21	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 19	Expected: 3 or 4

- Glyph name: germandbls	Contours detected: 16	Expected: 1

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: greater	Contours detected: 5	Expected: 1

- Glyph name: greaterequal	Contours detected: 8	Expected: 2

- Glyph name: guillemotleft	Contours detected: 6	Expected: 2

- Glyph name: guillemotright	Contours detected: 6	Expected: 2

- Glyph name: guilsinglleft	Contours detected: 3	Expected: 1

- Glyph name: guilsinglright	Contours detected: 3	Expected: 1

- Glyph name: h	Contours detected: 14	Expected: 1

- Glyph name: hbar	Contours detected: 16	Expected: 1

- Glyph name: hcircumflex	Contours detected: 17	Expected: 2

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: hyphen	Contours detected: 4	Expected: 1

- Glyph name: i	Contours detected: 9	Expected: 2

- Glyph name: iacute	Contours detected: 10	Expected: 2

- Glyph name: icircumflex	Contours detected: 11	Expected: 2

- Glyph name: idieresis	Contours detected: 10	Expected: 3

- Glyph name: igrave	Contours detected: 10	Expected: 2

- Glyph name: ij	Contours detected: 19	Expected: 3 or 4

- Glyph name: imacron	Contours detected: 11	Expected: 2

- Glyph name: infinity	Contours detected: 10	Expected: 3

- Glyph name: integral	Contours detected: 11	Expected: 1

- Glyph name: iogonek	Contours detected: 12	Expected: 2 or 3

- Glyph name: itilde	Contours detected: 14	Expected: 2

- Glyph name: j	Contours detected: 11	Expected: 2

- Glyph name: jcircumflex	Contours detected: 13	Expected: 2

- Glyph name: k	Contours detected: 13	Expected: 1 or 2

- Glyph name: kgreenlandic	Contours detected: 11	Expected: 1 or 2

- Glyph name: l	Contours detected: 10	Expected: 1

- Glyph name: lacute	Contours detected: 12	Expected: 2

- Glyph name: lcaron	Contours detected: 12	Expected: 2

- Glyph name: ldot	Contours detected: 11	Expected: 2

- Glyph name: less	Contours detected: 5	Expected: 1

- Glyph name: lessequal	Contours detected: 8	Expected: 2

- Glyph name: lira	Contours detected: 17	Expected: 1

- Glyph name: logicalnot	Contours detected: 7	Expected: 1

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: lslash	Contours detected: 12	Expected: 1

- Glyph name: m	Contours detected: 14	Expected: 1

- Glyph name: macron	Contours detected: 3	Expected: 1

- Glyph name: minus	Contours detected: 5	Expected: 1

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: n	Contours detected: 12	Expected: 1

- Glyph name: nacute	Contours detected: 14	Expected: 2

- Glyph name: napostrophe	Contours detected: 15	Expected: 2

- Glyph name: ncaron	Contours detected: 15	Expected: 2

- Glyph name: nine	Contours detected: 15	Expected: 1 or 2

- Glyph name: notequal	Contours detected: 15	Expected: 1

- Glyph name: ntilde	Contours detected: 18	Expected: 2

- Glyph name: numbersign	Contours detected: 20	Expected: 2

- Glyph name: o	Contours detected: 12	Expected: 2

- Glyph name: oacute	Contours detected: 14	Expected: 3

- Glyph name: ocircumflex	Contours detected: 15	Expected: 3

- Glyph name: odieresis	Contours detected: 14	Expected: 4

- Glyph name: oe	Contours detected: 18	Expected: 3

- Glyph name: ogonek	Contours detected: 3	Expected: 1

- Glyph name: ograve	Contours detected: 14	Expected: 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: ohungarumlaut	Contours detected: 16	Expected: 4

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: one	Contours detected: 10	Expected: 1

- Glyph name: oneeighth	Contours detected: 21	Expected: 5

- Glyph name: onehalf	Contours detected: 16	Expected: 3

- Glyph name: onequarter	Contours detected: 17	Expected: 3 or 4

- Glyph name: onethird	Contours detected: 16	Expected: 3

- Glyph name: ordfeminine	Contours detected: 14	Expected: 2 or 3

- Glyph name: ordmasculine	Contours detected: 12	Expected: 2 or 3

- Glyph name: oslash	Contours detected: 13	Expected: 3

- Glyph name: otilde	Contours detected: 18	Expected: 3

- Glyph name: p	Contours detected: 16	Expected: 2

- Glyph name: paragraph	Contours detected: 23	Expected: 1, 2 or 3

- Glyph name: parenleft	Contours detected: 7	Expected: 1

- Glyph name: parenright	Contours detected: 7	Expected: 1

- Glyph name: partialdiff	Contours detected: 15	Expected: 2

- Glyph name: percent	Contours detected: 13	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 17	Expected: 6 or 7

- Glyph name: peseta	Contours detected: 26	Expected: 2, 3 or 4

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: plus	Contours detected: 9	Expected: 1

- Glyph name: plusminus	Contours detected: 14	Expected: 1 or 2

- Glyph name: product	Contours detected: 21	Expected: 1

- Glyph name: q	Contours detected: 16	Expected: 2

- Glyph name: question	Contours detected: 10	Expected: 2

- Glyph name: questiondown	Contours detected: 10	Expected: 2

- Glyph name: quotedbl	Contours detected: 6	Expected: 2

- Glyph name: quotedblbase	Contours detected: 6	Expected: 2

- Glyph name: quotedblleft	Contours detected: 6	Expected: 2

- Glyph name: quotedblright	Contours detected: 6	Expected: 2

- Glyph name: quoteleft	Contours detected: 3	Expected: 1

- Glyph name: quoteright	Contours detected: 3	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 3	Expected: 1

- Glyph name: quotesingle	Contours detected: 3	Expected: 1

- Glyph name: r	Contours detected: 9	Expected: 1

- Glyph name: racute	Contours detected: 11	Expected: 2

- Glyph name: radical	Contours detected: 11	Expected: 1

- Glyph name: rcaron	Contours detected: 12	Expected: 2

- Glyph name: registered	Contours detected: 30	Expected: 3 or 4

- Glyph name: ring	Contours detected: 4	Expected: 2

- Glyph name: rupee	Contours detected: 23	Expected: 3

- Glyph name: s	Contours detected: 13	Expected: 1

- Glyph name: sacute	Contours detected: 15	Expected: 2

- Glyph name: scaron	Contours detected: 16	Expected: 2

- Glyph name: scircumflex	Contours detected: 16	Expected: 2

- Glyph name: section	Contours detected: 20	Expected: 2

- Glyph name: semicolon	Contours detected: 4	Expected: 2

- Glyph name: seven	Contours detected: 11	Expected: 1

- Glyph name: seveneighths	Contours detected: 20	Expected: 5

- Glyph name: six	Contours detected: 15	Expected: 1 or 2

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: sterling	Contours detected: 15	Expected: 1 or 2

- Glyph name: summation	Contours detected: 17	Expected: 1

- Glyph name: t	Contours detected: 12	Expected: 1

- Glyph name: tcaron	Contours detected: 14	Expected: 2

- Glyph name: thorn	Contours detected: 18	Expected: 2

- Glyph name: three	Contours detected: 14	Expected: 1

- Glyph name: threeeighths	Contours detected: 21	Expected: 5

- Glyph name: threequarters	Contours detected: 17	Expected: 3 or 4

- Glyph name: tilde	Contours detected: 6	Expected: 1

- Glyph name: trademark	Contours detected: 18	Expected: 2

- Glyph name: triagdn	Contours detected: 31	Expected: 1

- Glyph name: triagup	Contours detected: 31	Expected: 1

- Glyph name: two	Contours detected: 15	Expected: 1

- Glyph name: twothirds	Contours detected: 16	Expected: 1 or 3

- Glyph name: u	Contours detected: 12	Expected: 1

- Glyph name: uacute	Contours detected: 14	Expected: 2

- Glyph name: ubreve	Contours detected: 17	Expected: 2

- Glyph name: ucircumflex	Contours detected: 15	Expected: 2

- Glyph name: udieresis	Contours detected: 14	Expected: 3

- Glyph name: ugrave	Contours detected: 14	Expected: 2

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: uhungarumlaut	Contours detected: 16	Expected: 3

- Glyph name: umacron	Contours detected: 15	Expected: 2

- Glyph name: underscore	Contours detected: 6	Expected: 1

- Glyph name: uni00AD	Contours detected: 4	Expected: 0

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: uni01CD	Contours detected: 19	Expected: 3

- Glyph name: uni01CE	Contours detected: 17	Expected: 3

- Glyph name: uni01CF	Contours detected: 14	Expected: 2

- Glyph name: uni01D0	Contours detected: 11	Expected: 2

- Glyph name: uni01D1	Contours detected: 19	Expected: 3

- Glyph name: uni01D2	Contours detected: 15	Expected: 3

- Glyph name: uni01D3	Contours detected: 18	Expected: 2

- Glyph name: uni01D4	Contours detected: 15	Expected: 2

- Glyph name: uni01D5	Contours detected: 18	Expected: 4

- Glyph name: uni01D6	Contours detected: 17	Expected: 4

- Glyph name: uni01D7	Contours detected: 15	Expected: 4

- Glyph name: uni01D8	Contours detected: 16	Expected: 4

- Glyph name: uni01D9	Contours detected: 16	Expected: 4

- Glyph name: uni01DA	Contours detected: 17	Expected: 4

- Glyph name: uni01DB	Contours detected: 15	Expected: 4

- Glyph name: uni01DC	Contours detected: 16	Expected: 4

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02BC	Contours detected: 3	Expected: 1

- Glyph name: uni02BE	Contours detected: 3	Expected: 1

- Glyph name: uni02BF	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni032E	Contours detected: 5	Expected: 1

- Glyph name: uni0331	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: uni1E0C	Contours detected: 17	Expected: 3

- Glyph name: uni1E0D	Contours detected: 17	Expected: 3

- Glyph name: uni1E0E	Contours detected: 19	Expected: 3

- Glyph name: uni1E0F	Contours detected: 19	Expected: 3

- Glyph name: uni1E20	Contours detected: 20	Expected: 2

- Glyph name: uni1E21	Contours detected: 21	Expected: 3 or 4

- Glyph name: uni1E24	Contours detected: 18	Expected: 2

- Glyph name: uni1E25	Contours detected: 15	Expected: 2

- Glyph name: uni1E2A	Contours detected: 20	Expected: 2

- Glyph name: uni1E2B	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: uni1E44	Contours detected: 18	Expected: 2

- Glyph name: uni1E45	Contours detected: 13	Expected: 2

- Glyph name: uni1E46	Contours detected: 18	Expected: 2

- Glyph name: uni1E47	Contours detected: 13	Expected: 2

- Glyph name: uni1E48	Contours detected: 20	Expected: 2

- Glyph name: uni1E49	Contours detected: 15	Expected: 2

- Glyph name: uni1E5A	Contours detected: 19	Expected: 3

- Glyph name: uni1E5B	Contours detected: 10	Expected: 2

- Glyph name: uni1E5C	Contours detected: 22	Expected: 4

- Glyph name: uni1E5D	Contours detected: 13	Expected: 3

- Glyph name: uni1E5E	Contours detected: 21	Expected: 3

- Glyph name: uni1E5F	Contours detected: 12	Expected: 2

- Glyph name: uni1E60	Contours detected: 16	Expected: 2

- Glyph name: uni1E61	Contours detected: 14	Expected: 2

- Glyph name: uni1E62	Contours detected: 16	Expected: 2

- Glyph name: uni1E63	Contours detected: 14	Expected: 2

- Glyph name: uni1E6C	Contours detected: 12	Expected: 2

- Glyph name: uni1E6D	Contours detected: 13	Expected: 2

- Glyph name: uni1E6E	Contours detected: 14	Expected: 2

- Glyph name: uni1E6F	Contours detected: 15	Expected: 2

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: uni1E92	Contours detected: 16	Expected: 2

- Glyph name: uni1E93	Contours detected: 14	Expected: 2

- Glyph name: uni1E97	Contours detected: 14	Expected: 3

- Glyph name: uni2010	Contours detected: 4	Expected: 1

- Glyph name: uni2011	Contours detected: 4	Expected: 1

- Glyph name: uni2015	Contours detected: 6	Expected: 1

- Glyph name: uni2117	Contours detected: 29	Expected: 3 or 4

- Glyph name: uni2120	Contours detected: 18	Expected: 2

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni25CC	Contours detected: 6	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 15	Expected: 1

- Glyph name: uring	Contours detected: 16	Expected: 3

- Glyph name: utilde	Contours detected: 18	Expected: 2

- Glyph name: v	Contours detected: 9	Expected: 1

- Glyph name: w	Contours detected: 13	Expected: 1

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: wcircumflex	Contours detected: 16	Expected: 2

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: y	Contours detected: 16	Expected: 1

- Glyph name: yacute	Contours detected: 18	Expected: 2

- Glyph name: ycircumflex	Contours detected: 19	Expected: 2

- Glyph name: ydieresis	Contours detected: 18	Expected: 3

- Glyph name: yen	Contours detected: 13	Expected: 1 or 2

- Glyph name: ygrave	Contours detected: 18	Expected: 2

- Glyph name: z	Contours detected: 13	Expected: 1

- Glyph name: zacute	Contours detected: 15	Expected: 2

- Glyph name: zcaron	Contours detected: 16	Expected: 2

- Glyph name: zdotaccent	Contours detected: 14	Expected: 2

- Glyph name: zero	Contours detected: 19	Expected: 2 or 3
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 9 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 400:
greater, greaterequal, lessequal, less</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, old-permic, tai-le, syriac, hebrew, math, canadian-aboriginal, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, syriac, cherokee, thai, tifinagh, sunuwar, gothic</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: elbasan, greek, math</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, sundanese, armenian, arabic, hebrew, kayah-li, kharoshthi, yi, cham, syloti-nagri, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: phags-pa, gujarati, khudawadi, yi, tifinagh, gunjala-gondi, javanese, new-tai-lue, mandaic, lao, tagbanwa, tagalog, mahajani, sharada, bengali, bassa-vah, meetei-mayek, osage, malayalam, balinese, manichaean, buginese, symbols, wancho, cham, miao, soyombo, syloti-nagri, saurashtra, gurmukhi, marchen, takri, old-permic, elbasan, masaram-gondi, tai-tham, tai-viet, caucasian-albanian, thai, hebrew, tirhuta, duployan, khojki, dogra, coptic, khmer, mongolian, modi, tai-le, sundanese, canadian-aboriginal, grantha, chakma, kayah-li, batak, bhaiksuki, siddham, kharoshthi, psalter-pahlavi, kaithi, tamil, sogdian, hanunoo, math, music, warang-citi, pahawh-hmong, armenian, devanagari, kannada, tibetan, hanifi-rohingya, lepcha, rejang, newa, sinhala, limbu, oriya, adlam, zanabazar-square, thaana, myanmar, nko, syriac, mende-kikakui, buhid, brahmi, telugu, ahom</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



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
| 0 | 0 | 1 | 99 | 1153 | 81 | 1014 | 0 | 
| 0% | 0% | 0% | 4% | 49% | 3% | 43% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
