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

<details><summary>[9] MatrixSansVideo-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: Gcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uogonek	Contours detected: 3	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: Scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uhornacute	Contours detected: 3	Expected: 2

- Glyph name: uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: uhorntilde	Contours detected: 3	Expected: 2

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

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̛̇ i̛̊ i̛̋ i̛̍ i̛̒ i̤̇ i̤̊ i̤̋ i̤̍ i̤̒ i̦̇ i̦̊ i̦̋ i̦̍ i̦̒ i̧̇ i̧̊ i̧̋ i̧̍ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[9] MatrixSansVideoSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ä; both buffers returned adieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ë; both buffers returned edieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ï; both buffers returned idieresis.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ü; both buffers returned udieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ý; both buffers returned yacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: å; both buffers returned aring.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ã; both buffers returned atilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: æ; both buffers returned ae.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: œ; both buffers returned oe.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ñ; both buffers returned ntilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɓ; both buffers returned bhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɗ; both buffers returned dhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƙ; both buffers returned khook.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƴ; both buffers returned yhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ị; both buffers returned idotbelow.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṅ; both buffers returned ndotaccent.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ụ; both buffers returned udotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ā; both buffers returned amacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ē; both buffers returned emacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ī; both buffers returned imacron.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ū; both buffers returned umacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: Gcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uogonek	Contours detected: 3	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: Scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uhornacute	Contours detected: 3	Expected: 2

- Glyph name: uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: uhorntilde	Contours detected: 3	Expected: 2

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

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: і̀ і̂ і̃ і̄ і̆ і̇ і̉ і̊ і̋ і̌ і̍ і̒ і̛̀ і̛́ і̛̂ і̛̃ і̛̄ і̛̆ і̛̇ і̛̉</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[9] MatrixSans-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: Gcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: Scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uhornacute	Contours detected: 3	Expected: 2

- Glyph name: uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: uhorntilde	Contours detected: 3	Expected: 2

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

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̛̇ i̛̊ i̛̋ i̛̍ i̛̒ i̤̇ i̤̊ i̤̋ i̤̍ i̤̒ i̦̇ i̦̊ i̦̋ i̦̍ i̦̒ i̧̇ i̧̊ i̧̋ i̧̍ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[9] MatrixSansSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ä; both buffers returned adieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ë; both buffers returned edieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ï; both buffers returned idieresis.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ü; both buffers returned udieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ý; both buffers returned yacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: å; both buffers returned aring.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ã; both buffers returned atilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: æ; both buffers returned ae.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: œ; both buffers returned oe.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ñ; both buffers returned ntilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɓ; both buffers returned bhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɗ; both buffers returned dhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƙ; both buffers returned khook.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƴ; both buffers returned yhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ị; both buffers returned idotbelow.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṅ; both buffers returned ndotaccent.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ụ; both buffers returned udotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ā; both buffers returned amacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ē; both buffers returned emacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ī; both buffers returned imacron.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ū; both buffers returned umacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: Gcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: lcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uhorn	Contours detected: 2	Expected: 1

- Glyph name: Scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: scommaaccent	Contours detected: 1	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 1	Expected: 2

- Glyph name: uhornacute	Contours detected: 3	Expected: 2

- Glyph name: uhorngrave	Contours detected: 3	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 3	Expected: 2

- Glyph name: uhorntilde	Contours detected: 3	Expected: 2

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

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: colonmonetary	Contours detected: 2	Expected: 1 or 3

- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: і̀ і̂ і̃ і̄ і̆ і̇ і̉ і̊ і̋ і̌ і̍ і̒ і̛̀ і̛́ і̛̂ і̛̃ і̛̄ і̛̆ і̛̇ і̛̉</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[8] MatrixSansRasterSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ä; both buffers returned adieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ë; both buffers returned edieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ï; both buffers returned idieresis.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ü; both buffers returned udieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ý; both buffers returned yacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: å; both buffers returned aring.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ã; both buffers returned atilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: æ; both buffers returned ae.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: œ; both buffers returned oe.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ñ; both buffers returned ntilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɓ; both buffers returned bhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɗ; both buffers returned dhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƙ; both buffers returned khook.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƴ; both buffers returned yhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ị; both buffers returned idotbelow.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṅ; both buffers returned ndotaccent.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ụ; both buffers returned udotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ā; both buffers returned amacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ē; both buffers returned emacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ī; both buffers returned imacron.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ū; both buffers returned umacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: Ibreve	Contours detected: 10	Expected: 2

- Glyph name: ibreve	Contours detected: 8	Expected: 2

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

- Glyph name: Eng	Contours detected: 14	Expected: 1

- Glyph name: eng	Contours detected: 12	Expected: 1

- Glyph name: Omacron	Contours detected: 13	Expected: 3

- Glyph name: omacron	Contours detected: 9	Expected: 3

- Glyph name: Obreve	Contours detected: 15	Expected: 3

- Glyph name: obreve	Contours detected: 11	Expected: 3

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

- Glyph name: Bhook	Contours detected: 13	Expected: 3

- Glyph name: Oopen	Contours detected: 9	Expected: 1

- Glyph name: Dhook	Contours detected: 14	Expected: 2

- Glyph name: uni018F	Contours detected: 10	Expected: 2

- Glyph name: Eopen	Contours detected: 9	Expected: 1

- Glyph name: florin	Contours detected: 10	Expected: 1

- Glyph name: Khook	Contours detected: 13	Expected: 1

- Glyph name: khook	Contours detected: 11	Expected: 1

- Glyph name: Nhookleft	Contours detected: 17	Expected: 1

- Glyph name: Ohorn	Contours detected: 15	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 11	Expected: 2

- Glyph name: Uhorn	Contours detected: 16	Expected: 1

- Glyph name: uhorn	Contours detected: 13	Expected: 1

- Glyph name: Yhook	Contours detected: 12	Expected: 1

- Glyph name: yhook	Contours detected: 14	Expected: 1

- Glyph name: Acaron	Contours detected: 15	Expected: 3

- Glyph name: acaron	Contours detected: 9	Expected: 3

- Glyph name: Icaron	Contours detected: 10	Expected: 2

- Glyph name: icaron	Contours detected: 8	Expected: 2

- Glyph name: Ocaron	Contours detected: 15	Expected: 3

- Glyph name: ocaron	Contours detected: 11	Expected: 3

- Glyph name: Ucaron	Contours detected: 16	Expected: 2

- Glyph name: ucaron	Contours detected: 13	Expected: 2

- Glyph name: Udieresismacron	Contours detected: 14	Expected: 4

- Glyph name: udieresismacron	Contours detected: 13	Expected: 4

- Glyph name: Udieresisacute	Contours detected: 13	Expected: 4

- Glyph name: udieresisacute	Contours detected: 14	Expected: 4

- Glyph name: Udieresiscaron	Contours detected: 14	Expected: 4

- Glyph name: udieresiscaron	Contours detected: 15	Expected: 4

- Glyph name: Udieresisgrave	Contours detected: 13	Expected: 4

- Glyph name: udieresisgrave	Contours detected: 14	Expected: 4

- Glyph name: Gcaron	Contours detected: 14	Expected: 2

- Glyph name: gcaron	Contours detected: 15	Expected: 3 or 4

- Glyph name: Ngrave	Contours detected: 17	Expected: 2

- Glyph name: ngrave	Contours detected: 12	Expected: 2

- Glyph name: Scommaaccent	Contours detected: 11	Expected: 2

- Glyph name: scommaaccent	Contours detected: 7	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 10	Expected: 2

- Glyph name: Ymacron	Contours detected: 11	Expected: 2

- Glyph name: ymacron	Contours detected: 13	Expected: 2

- Glyph name: jdotless	Contours detected: 8	Expected: 1

- Glyph name: uni0251	Contours detected: 10	Expected: 2

- Glyph name: uni0259	Contours detected: 6	Expected: 2

- Glyph name: uni0261	Contours detected: 12	Expected: 2

- Glyph name: nhookleft	Contours detected: 12	Expected: 1

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: apostrophemod	Contours detected: 3	Expected: 1

- Glyph name: ringhalfright	Contours detected: 3	Expected: 1

- Glyph name: ringhalfleft	Contours detected: 3	Expected: 1

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

- Glyph name: hookabovecomb	Contours detected: 2	Expected: 1

- Glyph name: ringcomb	Contours detected: 4	Expected: 2

- Glyph name: hungarumlautcomb	Contours detected: 4	Expected: 2

- Glyph name: caroncomb	Contours detected: 3	Expected: 1

- Glyph name: commaturnedabovecomb	Contours detected: 2	Expected: 1

- Glyph name: horncomb	Contours detected: 3	Expected: 1

- Glyph name: commaaccentcomb	Contours detected: 2	Expected: 1

- Glyph name: cedillacomb	Contours detected: 2	Expected: 1

- Glyph name: ogonekcomb	Contours detected: 2	Expected: 1

- Glyph name: brevebelowcomb	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 11	Expected: 2

- Glyph name: uni03A9	Contours detected: 13	Expected: 1

- Glyph name: uni03BC	Contours detected: 12	Expected: 1

- Glyph name: pi	Contours detected: 9	Expected: 1

- Glyph name: uni0400	Contours detected: 9	Expected: 2

- Glyph name: Io-cy	Contours detected: 9	Expected: 3

- Glyph name: Dje-cy	Contours detected: 10	Expected: 1

- Glyph name: uni0403	Contours detected: 9	Expected: 2

- Glyph name: E-cy	Contours detected: 9	Expected: 1

- Glyph name: uni0405	Contours detected: 9	Expected: 1

- Glyph name: I-cy	Contours detected: 7	Expected: 1

- Glyph name: Yi-cy	Contours detected: 9	Expected: 3

- Glyph name: Je-cy	Contours detected: 8	Expected: 1

- Glyph name: Lje-cy	Contours detected: 15	Expected: 2

- Glyph name: Nje-cy	Contours detected: 15	Expected: 2

- Glyph name: Tshe-cy	Contours detected: 10	Expected: 1

- Glyph name: uni040C	Contours detected: 15	Expected: 2

- Glyph name: uni040D	Contours detected: 17	Expected: 2

- Glyph name: Ushort-cy	Contours detected: 14	Expected: 2

- Glyph name: Dzhe-cy	Contours detected: 14	Expected: 1

- Glyph name: A-cy	Contours detected: 12	Expected: 2

- Glyph name: Be-cy	Contours detected: 9	Expected: 2

- Glyph name: Ve-cy	Contours detected: 11	Expected: 3

- Glyph name: Ge-cy	Contours detected: 7	Expected: 1

- Glyph name: De-cy	Contours detected: 14	Expected: 2

- Glyph name: Ie-cy	Contours detected: 7	Expected: 1

- Glyph name: Zhe-cy	Contours detected: 19	Expected: 1

- Glyph name: Ze-cy	Contours detected: 9	Expected: 1

- Glyph name: Ii-cy	Contours detected: 15	Expected: 1

- Glyph name: Iishort-cy	Contours detected: 18	Expected: 2

- Glyph name: Ka-cy	Contours detected: 13	Expected: 1

- Glyph name: El-cy	Contours detected: 13	Expected: 1

- Glyph name: Em-cy	Contours detected: 16	Expected: 1

- Glyph name: En-cy	Contours detected: 13	Expected: 1

- Glyph name: O-cy	Contours detected: 12	Expected: 2

- Glyph name: Pe-cy	Contours detected: 13	Expected: 1

- Glyph name: Er-cy	Contours detected: 9	Expected: 1 or 2

- Glyph name: Es-cy	Contours detected: 9	Expected: 1

- Glyph name: Te-cy	Contours detected: 7	Expected: 1

- Glyph name: U-cy	Contours detected: 11	Expected: 1

- Glyph name: Ef-cy	Contours detected: 13	Expected: 3

- Glyph name: Ha-cy	Contours detected: 13	Expected: 1

- Glyph name: Tse-cy	Contours detected: 14	Expected: 1

- Glyph name: Che-cy	Contours detected: 10	Expected: 1

- Glyph name: Sha-cy	Contours detected: 19	Expected: 1

- Glyph name: Shcha-cy	Contours detected: 20	Expected: 1

- Glyph name: Hardsign-cy	Contours detected: 9	Expected: 2

- Glyph name: Yeru-cy	Contours detected: 16	Expected: 3

- Glyph name: Softsign-cy	Contours detected: 9	Expected: 2

- Glyph name: Ereversed-cy	Contours detected: 9	Expected: 1

- Glyph name: Yu-cy	Contours detected: 18	Expected: 2

- Glyph name: Ya-cy	Contours detected: 12	Expected: 2

- Glyph name: a-cy	Contours detected: 6	Expected: 2

- Glyph name: be-cy	Contours detected: 9	Expected: 2

- Glyph name: ve-cy	Contours detected: 7	Expected: 3

- Glyph name: ge-cy	Contours detected: 5	Expected: 1

- Glyph name: de-cy	Contours detected: 10	Expected: 2

- Glyph name: ie-cy	Contours detected: 6	Expected: 2

- Glyph name: zhe-cy	Contours detected: 13	Expected: 1

- Glyph name: ze-cy	Contours detected: 5	Expected: 1

- Glyph name: ii-cy	Contours detected: 11	Expected: 1

- Glyph name: iishort-cy	Contours detected: 14	Expected: 2

- Glyph name: ka-cy	Contours detected: 9	Expected: 1

- Glyph name: el-cy	Contours detected: 9	Expected: 1

- Glyph name: em-cy	Contours detected: 12	Expected: 1

- Glyph name: en-cy	Contours detected: 9	Expected: 1

- Glyph name: o-cy	Contours detected: 8	Expected: 2

- Glyph name: pe-cy	Contours detected: 9	Expected: 1

- Glyph name: er-cy	Contours detected: 12	Expected: 2

- Glyph name: es-cy	Contours detected: 7	Expected: 1

- Glyph name: te-cy	Contours detected: 5	Expected: 1

- Glyph name: u-cy	Contours detected: 12	Expected: 1

- Glyph name: ef-cy	Contours detected: 15	Expected: 3

- Glyph name: ha-cy	Contours detected: 9	Expected: 1

- Glyph name: tse-cy	Contours detected: 10	Expected: 1

- Glyph name: che-cy	Contours detected: 7	Expected: 1

- Glyph name: sha-cy	Contours detected: 13	Expected: 1

- Glyph name: shcha-cy	Contours detected: 14	Expected: 1

- Glyph name: hardsign-cy	Contours detected: 6	Expected: 2

- Glyph name: yeru-cy	Contours detected: 11	Expected: 3

- Glyph name: softsign-cy	Contours detected: 6	Expected: 2

- Glyph name: ereversed-cy	Contours detected: 5	Expected: 1

- Glyph name: yu-cy	Contours detected: 12	Expected: 2

- Glyph name: ya-cy	Contours detected: 8	Expected: 2

- Glyph name: uni0450	Contours detected: 8	Expected: 3

- Glyph name: io-cy	Contours detected: 8	Expected: 4

- Glyph name: dje-cy	Contours detected: 13	Expected: 1

- Glyph name: uni0453	Contours detected: 7	Expected: 2

- Glyph name: e-cy	Contours detected: 5	Expected: 1

- Glyph name: uni0455	Contours detected: 5	Expected: 1

- Glyph name: i-cy	Contours detected: 6	Expected: 2

- Glyph name: yi-cy	Contours detected: 7	Expected: 3

- Glyph name: je-cy	Contours detected: 9	Expected: 2

- Glyph name: lje-cy	Contours detected: 10	Expected: 2

- Glyph name: nje-cy	Contours detected: 10	Expected: 2

- Glyph name: tshe-cy	Contours detected: 11	Expected: 1

- Glyph name: uni045C	Contours detected: 11	Expected: 2

- Glyph name: uni045D	Contours detected: 13	Expected: 2

- Glyph name: ushort-cy	Contours detected: 15	Expected: 2

- Glyph name: dzhe-cy	Contours detected: 10	Expected: 1 or 2

- Glyph name: uni0462	Contours detected: 9	Expected: 2

- Glyph name: uni0463	Contours detected: 8	Expected: 2

- Glyph name: uni0472	Contours detected: 13	Expected: 3

- Glyph name: uni0473	Contours detected: 9	Expected: 3

- Glyph name: uni0474	Contours detected: 13	Expected: 1

- Glyph name: uni0475	Contours detected: 9	Expected: 1

- Glyph name: Geupturn-cy	Contours detected: 8	Expected: 1

- Glyph name: geupturn-cy	Contours detected: 6	Expected: 1

- Glyph name: Gestroke-cy	Contours detected: 7	Expected: 1

- Glyph name: gestroke-cy	Contours detected: 5	Expected: 1

- Glyph name: Zhedescender-cy	Contours detected: 20	Expected: 1 or 2

- Glyph name: zhedescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: Kadescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: kadescender-cy	Contours detected: 10	Expected: 1 or 2

- Glyph name: Endescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: endescender-cy	Contours detected: 10	Expected: 1 or 2

- Glyph name: Ustraight-cy	Contours detected: 10	Expected: 1

- Glyph name: ustraight-cy	Contours detected: 11	Expected: 1

- Glyph name: Ustraightstroke-cy	Contours detected: 10	Expected: 1

- Glyph name: ustraightstroke-cy	Contours detected: 11	Expected: 1

- Glyph name: Hadescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: hadescender-cy	Contours detected: 10	Expected: 1 or 2

- Glyph name: Chedescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: chedescender-cy	Contours detected: 8	Expected: 1 or 2

- Glyph name: Shha-cy	Contours detected: 10	Expected: 1

- Glyph name: shha-cy	Contours detected: 12	Expected: 1

- Glyph name: Schwa-cy	Contours detected: 10	Expected: 2

- Glyph name: schwa-cy	Contours detected: 6	Expected: 2

- Glyph name: Imacron-cy	Contours detected: 16	Expected: 2

- Glyph name: imacron-cy	Contours detected: 12	Expected: 2

- Glyph name: Obarred-cy	Contours detected: 11	Expected: 3

- Glyph name: obarred-cy	Contours detected: 7	Expected: 3

- Glyph name: Umacron-cy	Contours detected: 12	Expected: 2

- Glyph name: umacron-cy	Contours detected: 13	Expected: 2

- Glyph name: baht	Contours detected: 11	Expected: 3 or 5

- Glyph name: Ddotbelow	Contours detected: 13	Expected: 3

- Glyph name: ddotbelow	Contours detected: 13	Expected: 3

- Glyph name: Dmacronbelow	Contours detected: 13	Expected: 3

- Glyph name: dmacronbelow	Contours detected: 13	Expected: 3

- Glyph name: Gmacron	Contours detected: 12	Expected: 2

- Glyph name: gmacron	Contours detected: 13	Expected: 3 or 4

- Glyph name: Hdotbelow	Contours detected: 14	Expected: 2

- Glyph name: hdotbelow	Contours detected: 13	Expected: 2

- Glyph name: Hbrevebelow	Contours detected: 14	Expected: 2

- Glyph name: hbrevebelow	Contours detected: 13	Expected: 2

- Glyph name: uni1E36	Contours detected: 8	Expected: 2

- Glyph name: uni1E37	Contours detected: 8	Expected: 2

- Glyph name: uni1E38	Contours detected: 9	Expected: 3

- Glyph name: uni1E39	Contours detected: 9	Expected: 3

- Glyph name: uni1E3A	Contours detected: 8	Expected: 2

- Glyph name: uni1E3B	Contours detected: 8	Expected: 2

- Glyph name: Macute	Contours detected: 18	Expected: 2

- Glyph name: macute	Contours detected: 15	Expected: 2

- Glyph name: uni1E42	Contours detected: 17	Expected: 2

- Glyph name: uni1E43	Contours detected: 14	Expected: 2

- Glyph name: Ndotaccent	Contours detected: 16	Expected: 2

- Glyph name: ndotaccent	Contours detected: 11	Expected: 2

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

- Glyph name: Sdotbelow	Contours detected: 10	Expected: 2

- Glyph name: sdotbelow	Contours detected: 6	Expected: 2

- Glyph name: Tdotbelow	Contours detected: 8	Expected: 2

- Glyph name: tdotbelow	Contours detected: 9	Expected: 2

- Glyph name: Tmacronbelow	Contours detected: 8	Expected: 2

- Glyph name: tmacronbelow	Contours detected: 9	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 13	Expected: 2

- Glyph name: Zdotbelow	Contours detected: 8	Expected: 2

- Glyph name: zdotbelow	Contours detected: 6	Expected: 2

- Glyph name: tdieresis	Contours detected: 10	Expected: 3

- Glyph name: Germandbls	Contours detected: 13	Expected: 1

- Glyph name: Adotbelow	Contours detected: 13	Expected: 3

- Glyph name: adotbelow	Contours detected: 7	Expected: 3

- Glyph name: Ahookabove	Contours detected: 14	Expected: 3

- Glyph name: ahookabove	Contours detected: 8	Expected: 3

- Glyph name: Acircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: acircumflexacute	Contours detected: 11	Expected: 4

- Glyph name: Acircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: acircumflexgrave	Contours detected: 11	Expected: 4

- Glyph name: Acircumflexhookabove	Contours detected: 13	Expected: 4

- Glyph name: acircumflexhookabove	Contours detected: 11	Expected: 4

- Glyph name: Acircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: acircumflextilde	Contours detected: 13	Expected: 4

- Glyph name: Acircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: acircumflexdotbelow	Contours detected: 10	Expected: 4

- Glyph name: Abreveacute	Contours detected: 13	Expected: 4

- Glyph name: abreveacute	Contours detected: 11	Expected: 4

- Glyph name: Abrevegrave	Contours detected: 13	Expected: 4

- Glyph name: abrevegrave	Contours detected: 11	Expected: 4

- Glyph name: Abrevehookabove	Contours detected: 13	Expected: 4

- Glyph name: abrevehookabove	Contours detected: 11	Expected: 4

- Glyph name: Abrevetilde	Contours detected: 15	Expected: 4

- Glyph name: abrevetilde	Contours detected: 13	Expected: 4

- Glyph name: Abrevedotbelow	Contours detected: 16	Expected: 4

- Glyph name: abrevedotbelow	Contours detected: 10	Expected: 4

- Glyph name: Edotbelow	Contours detected: 8	Expected: 2

- Glyph name: edotbelow	Contours detected: 7	Expected: 3

- Glyph name: Ehookabove	Contours detected: 9	Expected: 2

- Glyph name: ehookabove	Contours detected: 8	Expected: 3

- Glyph name: Etilde	Contours detected: 11	Expected: 2

- Glyph name: etilde	Contours detected: 10	Expected: 3

- Glyph name: Ecircumflexacute	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexacute	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflexgrave	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexgrave	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflexhookabove	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexhookabove	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflextilde	Contours detected: 12	Expected: 3

- Glyph name: ecircumflextilde	Contours detected: 13	Expected: 4

- Glyph name: Ecircumflexdotbelow	Contours detected: 11	Expected: 3

- Glyph name: ecircumflexdotbelow	Contours detected: 10	Expected: 4

- Glyph name: Ihookabove	Contours detected: 9	Expected: 2

- Glyph name: ihookabove	Contours detected: 7	Expected: 2

- Glyph name: Idotbelow	Contours detected: 8	Expected: 2

- Glyph name: idotbelow	Contours detected: 7	Expected: 3

- Glyph name: Odotbelow	Contours detected: 13	Expected: 3

- Glyph name: odotbelow	Contours detected: 9	Expected: 3

- Glyph name: Ohookabove	Contours detected: 14	Expected: 3

- Glyph name: ohookabove	Contours detected: 10	Expected: 3

- Glyph name: Ocircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflexhookabove	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexhookabove	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: ocircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: Ocircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: ocircumflexdotbelow	Contours detected: 12	Expected: 4

- Glyph name: Ohornacute	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohornacute	Contours detected: 13	Expected: 3

- Glyph name: Ohorngrave	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohorngrave	Contours detected: 13	Expected: 3

- Glyph name: Ohornhookabove	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohornhookabove	Contours detected: 13	Expected: 3

- Glyph name: Ohorntilde	Contours detected: 19	Expected: 3 or 4

- Glyph name: ohorntilde	Contours detected: 15	Expected: 3

- Glyph name: Ohorndotbelow	Contours detected: 16	Expected: 3 or 4

- Glyph name: ohorndotbelow	Contours detected: 12	Expected: 3

- Glyph name: Udotbelow	Contours detected: 14	Expected: 2

- Glyph name: udotbelow	Contours detected: 11	Expected: 2

- Glyph name: Uhookabove	Contours detected: 15	Expected: 2

- Glyph name: uhookabove	Contours detected: 12	Expected: 2

- Glyph name: Uhornacute	Contours detected: 18	Expected: 2

- Glyph name: uhornacute	Contours detected: 15	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 18	Expected: 2

- Glyph name: uhorngrave	Contours detected: 15	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 18	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 15	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 20	Expected: 2

- Glyph name: uhorntilde	Contours detected: 17	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 17	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 14	Expected: 2

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: ygrave	Contours detected: 14	Expected: 2

- Glyph name: Ydotbelow	Contours detected: 11	Expected: 2

- Glyph name: ydotbelow	Contours detected: 8	Expected: 2

- Glyph name: Yhookabove	Contours detected: 12	Expected: 2

- Glyph name: yhookabove	Contours detected: 14	Expected: 2

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

- Glyph name: nmod	Contours detected: 7	Expected: 1

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

- Glyph name: Eng	Contours detected: 14	Expected: 1

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

- Glyph name: Ibreve	Contours detected: 10	Expected: 2

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

- Glyph name: ibreve	Contours detected: 8	Expected: 2

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

- Glyph name: uni0162	Contours detected: 9	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 10	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 10	Expected: 2

- Glyph name: uni0251	Contours detected: 10	Expected: 2

- Glyph name: uni0259	Contours detected: 6	Expected: 2

- Glyph name: uni0261	Contours detected: 12	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni0394	Contours detected: 11	Expected: 2

- Glyph name: uni03A9	Contours detected: 13	Expected: 1

- Glyph name: uni03BC	Contours detected: 12	Expected: 1

- Glyph name: uni0400	Contours detected: 9	Expected: 2

- Glyph name: uni0403	Contours detected: 9	Expected: 2

- Glyph name: uni0405	Contours detected: 9	Expected: 1

- Glyph name: uni040C	Contours detected: 15	Expected: 2

- Glyph name: uni040D	Contours detected: 17	Expected: 2

- Glyph name: uni0450	Contours detected: 8	Expected: 3

- Glyph name: uni0453	Contours detected: 7	Expected: 2

- Glyph name: uni0455	Contours detected: 5	Expected: 1

- Glyph name: uni045C	Contours detected: 11	Expected: 2

- Glyph name: uni045D	Contours detected: 13	Expected: 2

- Glyph name: uni0462	Contours detected: 9	Expected: 2

- Glyph name: uni0463	Contours detected: 8	Expected: 2

- Glyph name: uni0472	Contours detected: 13	Expected: 3

- Glyph name: uni0473	Contours detected: 9	Expected: 3

- Glyph name: uni0474	Contours detected: 13	Expected: 1

- Glyph name: uni0475	Contours detected: 9	Expected: 1

- Glyph name: uni1E36	Contours detected: 8	Expected: 2

- Glyph name: uni1E37	Contours detected: 8	Expected: 2

- Glyph name: uni1E38	Contours detected: 9	Expected: 3

- Glyph name: uni1E39	Contours detected: 9	Expected: 3

- Glyph name: uni1E3A	Contours detected: 8	Expected: 2

- Glyph name: uni1E3B	Contours detected: 8	Expected: 2

- Glyph name: uni1E42	Contours detected: 17	Expected: 2

- Glyph name: uni1E43	Contours detected: 14	Expected: 2

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

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 13	Expected: 2

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: і̀ і̂ і̃ і̄ і̆ і̇ і̉ і̊ і̋ і̌ і̍ і̒ і̛̀ і̛́ і̛̂ і̛̃ і̛̄ і̛̆ і̛̇ і̛̉</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[8] MatrixSansScreenSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ä; both buffers returned adieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ë; both buffers returned edieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ï; both buffers returned idieresis.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ü; both buffers returned udieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ý; both buffers returned yacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: å; both buffers returned aring.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ã; both buffers returned atilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: æ; both buffers returned ae.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: œ; both buffers returned oe.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ñ; both buffers returned ntilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɓ; both buffers returned bhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɗ; both buffers returned dhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƙ; both buffers returned khook.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƴ; both buffers returned yhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ị; both buffers returned idotbelow.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṅ; both buffers returned ndotaccent.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ụ; both buffers returned udotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ā; both buffers returned amacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ē; both buffers returned emacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ī; both buffers returned imacron.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ū; both buffers returned umacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: Ibreve	Contours detected: 16	Expected: 2

- Glyph name: ibreve	Contours detected: 13	Expected: 2

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

- Glyph name: Eng	Contours detected: 16	Expected: 1

- Glyph name: eng	Contours detected: 14	Expected: 1

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: Obreve	Contours detected: 21	Expected: 3

- Glyph name: obreve	Contours detected: 17	Expected: 3

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

- Glyph name: Bhook	Contours detected: 20	Expected: 3

- Glyph name: Oopen	Contours detected: 13	Expected: 1

- Glyph name: Dhook	Contours detected: 17	Expected: 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: Eopen	Contours detected: 15	Expected: 1

- Glyph name: florin	Contours detected: 14	Expected: 1

- Glyph name: Khook	Contours detected: 14	Expected: 1

- Glyph name: khook	Contours detected: 13	Expected: 1

- Glyph name: Nhookleft	Contours detected: 19	Expected: 1

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: Yhook	Contours detected: 12	Expected: 1

- Glyph name: yhook	Contours detected: 18	Expected: 1

- Glyph name: Acaron	Contours detected: 19	Expected: 3

- Glyph name: acaron	Contours detected: 17	Expected: 3

- Glyph name: Icaron	Contours detected: 14	Expected: 2

- Glyph name: icaron	Contours detected: 11	Expected: 2

- Glyph name: Ocaron	Contours detected: 19	Expected: 3

- Glyph name: ocaron	Contours detected: 15	Expected: 3

- Glyph name: Ucaron	Contours detected: 18	Expected: 2

- Glyph name: ucaron	Contours detected: 15	Expected: 2

- Glyph name: Udieresismacron	Contours detected: 18	Expected: 4

- Glyph name: udieresismacron	Contours detected: 17	Expected: 4

- Glyph name: Udieresisacute	Contours detected: 15	Expected: 4

- Glyph name: udieresisacute	Contours detected: 16	Expected: 4

- Glyph name: Udieresiscaron	Contours detected: 16	Expected: 4

- Glyph name: udieresiscaron	Contours detected: 17	Expected: 4

- Glyph name: Udieresisgrave	Contours detected: 15	Expected: 4

- Glyph name: udieresisgrave	Contours detected: 16	Expected: 4

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Ngrave	Contours detected: 19	Expected: 2

- Glyph name: ngrave	Contours detected: 14	Expected: 2

- Glyph name: Scommaaccent	Contours detected: 17	Expected: 2

- Glyph name: scommaaccent	Contours detected: 15	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 14	Expected: 2

- Glyph name: Ymacron	Contours detected: 13	Expected: 2

- Glyph name: ymacron	Contours detected: 19	Expected: 2

- Glyph name: jdotless	Contours detected: 10	Expected: 1

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: nhookleft	Contours detected: 14	Expected: 1

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: apostrophemod	Contours detected: 3	Expected: 1

- Glyph name: ringhalfright	Contours detected: 3	Expected: 1

- Glyph name: ringhalfleft	Contours detected: 3	Expected: 1

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

- Glyph name: brevebelowcomb	Contours detected: 5	Expected: 1

- Glyph name: macronbelowcomb	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: uni0400	Contours detected: 20	Expected: 2

- Glyph name: Io-cy	Contours detected: 20	Expected: 3

- Glyph name: Dje-cy	Contours detected: 16	Expected: 1

- Glyph name: uni0403	Contours detected: 13	Expected: 2

- Glyph name: E-cy	Contours detected: 16	Expected: 1

- Glyph name: uni0405	Contours detected: 15	Expected: 1

- Glyph name: I-cy	Contours detected: 11	Expected: 1

- Glyph name: Yi-cy	Contours detected: 13	Expected: 3

- Glyph name: Je-cy	Contours detected: 11	Expected: 1

- Glyph name: Lje-cy	Contours detected: 20	Expected: 2

- Glyph name: Nje-cy	Contours detected: 22	Expected: 2

- Glyph name: Tshe-cy	Contours detected: 16	Expected: 1

- Glyph name: uni040C	Contours detected: 16	Expected: 2

- Glyph name: uni040D	Contours detected: 19	Expected: 2

- Glyph name: Ushort-cy	Contours detected: 21	Expected: 2

- Glyph name: Dzhe-cy	Contours detected: 18	Expected: 1

- Glyph name: A-cy	Contours detected: 16	Expected: 2

- Glyph name: Be-cy	Contours detected: 19	Expected: 2

- Glyph name: Ve-cy	Contours detected: 20	Expected: 3

- Glyph name: Ge-cy	Contours detected: 11	Expected: 1

- Glyph name: De-cy	Contours detected: 21	Expected: 2

- Glyph name: Ie-cy	Contours detected: 18	Expected: 1

- Glyph name: Zhe-cy	Contours detected: 21	Expected: 1

- Glyph name: Ze-cy	Contours detected: 15	Expected: 1

- Glyph name: Ii-cy	Contours detected: 17	Expected: 1

- Glyph name: Iishort-cy	Contours detected: 22	Expected: 2

- Glyph name: Ka-cy	Contours detected: 14	Expected: 1

- Glyph name: El-cy	Contours detected: 15	Expected: 1

- Glyph name: Em-cy	Contours detected: 18	Expected: 1

- Glyph name: En-cy	Contours detected: 17	Expected: 1

- Glyph name: O-cy	Contours detected: 16	Expected: 2

- Glyph name: Pe-cy	Contours detected: 17	Expected: 1

- Glyph name: Er-cy	Contours detected: 15	Expected: 1 or 2

- Glyph name: Es-cy	Contours detected: 13	Expected: 1

- Glyph name: Te-cy	Contours detected: 11	Expected: 1

- Glyph name: U-cy	Contours detected: 16	Expected: 1

- Glyph name: Ef-cy	Contours detected: 17	Expected: 3

- Glyph name: Ha-cy	Contours detected: 13	Expected: 1

- Glyph name: Tse-cy	Contours detected: 18	Expected: 1

- Glyph name: Che-cy	Contours detected: 13	Expected: 1

- Glyph name: Sha-cy	Contours detected: 23	Expected: 1

- Glyph name: Shcha-cy	Contours detected: 25	Expected: 1

- Glyph name: Hardsign-cy	Contours detected: 15	Expected: 2

- Glyph name: Yeru-cy	Contours detected: 20	Expected: 3

- Glyph name: Softsign-cy	Contours detected: 15	Expected: 2

- Glyph name: Ereversed-cy	Contours detected: 16	Expected: 1

- Glyph name: Yu-cy	Contours detected: 22	Expected: 2

- Glyph name: Ya-cy	Contours detected: 18	Expected: 2

- Glyph name: a-cy	Contours detected: 14	Expected: 2

- Glyph name: be-cy	Contours detected: 16	Expected: 2

- Glyph name: ve-cy	Contours detected: 16	Expected: 3

- Glyph name: ge-cy	Contours detected: 9	Expected: 1

- Glyph name: de-cy	Contours detected: 17	Expected: 2

- Glyph name: ie-cy	Contours detected: 14	Expected: 2

- Glyph name: zhe-cy	Contours detected: 15	Expected: 1

- Glyph name: ze-cy	Contours detected: 13	Expected: 1

- Glyph name: ii-cy	Contours detected: 13	Expected: 1

- Glyph name: iishort-cy	Contours detected: 18	Expected: 2

- Glyph name: ka-cy	Contours detected: 11	Expected: 1

- Glyph name: el-cy	Contours detected: 11	Expected: 1

- Glyph name: em-cy	Contours detected: 14	Expected: 1

- Glyph name: en-cy	Contours detected: 13	Expected: 1

- Glyph name: o-cy	Contours detected: 12	Expected: 2

- Glyph name: pe-cy	Contours detected: 13	Expected: 1

- Glyph name: er-cy	Contours detected: 16	Expected: 2

- Glyph name: es-cy	Contours detected: 11	Expected: 1

- Glyph name: te-cy	Contours detected: 9	Expected: 1

- Glyph name: u-cy	Contours detected: 16	Expected: 1

- Glyph name: ef-cy	Contours detected: 19	Expected: 3

- Glyph name: ha-cy	Contours detected: 9	Expected: 1

- Glyph name: tse-cy	Contours detected: 14	Expected: 1

- Glyph name: che-cy	Contours detected: 10	Expected: 1

- Glyph name: sha-cy	Contours detected: 17	Expected: 1

- Glyph name: shcha-cy	Contours detected: 19	Expected: 1

- Glyph name: hardsign-cy	Contours detected: 12	Expected: 2

- Glyph name: yeru-cy	Contours detected: 15	Expected: 3

- Glyph name: softsign-cy	Contours detected: 12	Expected: 2

- Glyph name: ereversed-cy	Contours detected: 14	Expected: 1

- Glyph name: yu-cy	Contours detected: 16	Expected: 2

- Glyph name: ya-cy	Contours detected: 14	Expected: 2

- Glyph name: uni0450	Contours detected: 16	Expected: 3

- Glyph name: io-cy	Contours detected: 16	Expected: 4

- Glyph name: dje-cy	Contours detected: 18	Expected: 1

- Glyph name: uni0453	Contours detected: 11	Expected: 2

- Glyph name: e-cy	Contours detected: 14	Expected: 1

- Glyph name: uni0455	Contours detected: 13	Expected: 1

- Glyph name: i-cy	Contours detected: 9	Expected: 2

- Glyph name: yi-cy	Contours detected: 10	Expected: 3

- Glyph name: je-cy	Contours detected: 11	Expected: 2

- Glyph name: lje-cy	Contours detected: 15	Expected: 2

- Glyph name: nje-cy	Contours detected: 17	Expected: 2

- Glyph name: tshe-cy	Contours detected: 16	Expected: 1

- Glyph name: uni045C	Contours detected: 13	Expected: 2

- Glyph name: uni045D	Contours detected: 15	Expected: 2

- Glyph name: ushort-cy	Contours detected: 21	Expected: 2

- Glyph name: dzhe-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0462	Contours detected: 17	Expected: 2

- Glyph name: uni0463	Contours detected: 14	Expected: 2

- Glyph name: uni0472	Contours detected: 17	Expected: 3

- Glyph name: uni0473	Contours detected: 13	Expected: 3

- Glyph name: uni0474	Contours detected: 14	Expected: 1

- Glyph name: uni0475	Contours detected: 10	Expected: 1

- Glyph name: Geupturn-cy	Contours detected: 12	Expected: 1

- Glyph name: geupturn-cy	Contours detected: 10	Expected: 1

- Glyph name: Gestroke-cy	Contours detected: 14	Expected: 1

- Glyph name: gestroke-cy	Contours detected: 12	Expected: 1

- Glyph name: Zhedescender-cy	Contours detected: 23	Expected: 1 or 2

- Glyph name: zhedescender-cy	Contours detected: 17	Expected: 1 or 2

- Glyph name: Kadescender-cy	Contours detected: 16	Expected: 1 or 2

- Glyph name: kadescender-cy	Contours detected: 12	Expected: 1 or 2

- Glyph name: Endescender-cy	Contours detected: 18	Expected: 1 or 2

- Glyph name: endescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: Ustraight-cy	Contours detected: 10	Expected: 1

- Glyph name: ustraight-cy	Contours detected: 11	Expected: 1

- Glyph name: Ustraightstroke-cy	Contours detected: 12	Expected: 1

- Glyph name: ustraightstroke-cy	Contours detected: 13	Expected: 1

- Glyph name: Hadescender-cy	Contours detected: 15	Expected: 1 or 2

- Glyph name: hadescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: Chedescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: chedescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: Shha-cy	Contours detected: 13	Expected: 1

- Glyph name: shha-cy	Contours detected: 14	Expected: 1

- Glyph name: Schwa-cy	Contours detected: 18	Expected: 2

- Glyph name: schwa-cy	Contours detected: 14	Expected: 2

- Glyph name: Imacron-cy	Contours detected: 20	Expected: 2

- Glyph name: imacron-cy	Contours detected: 16	Expected: 2

- Glyph name: Obarred-cy	Contours detected: 19	Expected: 3

- Glyph name: obarred-cy	Contours detected: 15	Expected: 3

- Glyph name: Umacron-cy	Contours detected: 19	Expected: 2

- Glyph name: umacron-cy	Contours detected: 19	Expected: 2

- Glyph name: baht	Contours detected: 20	Expected: 3 or 5

- Glyph name: Ddotbelow	Contours detected: 17	Expected: 3

- Glyph name: ddotbelow	Contours detected: 17	Expected: 3

- Glyph name: Dmacronbelow	Contours detected: 19	Expected: 3

- Glyph name: dmacronbelow	Contours detected: 19	Expected: 3

- Glyph name: Gmacron	Contours detected: 20	Expected: 2

- Glyph name: gmacron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Hdotbelow	Contours detected: 18	Expected: 2

- Glyph name: hdotbelow	Contours detected: 15	Expected: 2

- Glyph name: Hbrevebelow	Contours detected: 20	Expected: 2

- Glyph name: hbrevebelow	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: Macute	Contours detected: 20	Expected: 2

- Glyph name: macute	Contours detected: 16	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: Ndotaccent	Contours detected: 18	Expected: 2

- Glyph name: ndotaccent	Contours detected: 13	Expected: 2

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

- Glyph name: Sdotbelow	Contours detected: 16	Expected: 2

- Glyph name: sdotbelow	Contours detected: 14	Expected: 2

- Glyph name: Tdotbelow	Contours detected: 12	Expected: 2

- Glyph name: tdotbelow	Contours detected: 13	Expected: 2

- Glyph name: Tmacronbelow	Contours detected: 14	Expected: 2

- Glyph name: tmacronbelow	Contours detected: 15	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: Zdotbelow	Contours detected: 16	Expected: 2

- Glyph name: zdotbelow	Contours detected: 14	Expected: 2

- Glyph name: tdieresis	Contours detected: 14	Expected: 3

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

- Glyph name: nmod	Contours detected: 8	Expected: 1

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

- Glyph name: Eng	Contours detected: 16	Expected: 1

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

- Glyph name: Ibreve	Contours detected: 16	Expected: 2

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

- Glyph name: eng	Contours detected: 14	Expected: 1

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

- Glyph name: ibreve	Contours detected: 13	Expected: 2

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

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: uni0400	Contours detected: 20	Expected: 2

- Glyph name: uni0403	Contours detected: 13	Expected: 2

- Glyph name: uni0405	Contours detected: 15	Expected: 1

- Glyph name: uni040C	Contours detected: 16	Expected: 2

- Glyph name: uni040D	Contours detected: 19	Expected: 2

- Glyph name: uni0450	Contours detected: 16	Expected: 3

- Glyph name: uni0453	Contours detected: 11	Expected: 2

- Glyph name: uni0455	Contours detected: 13	Expected: 1

- Glyph name: uni045C	Contours detected: 13	Expected: 2

- Glyph name: uni045D	Contours detected: 15	Expected: 2

- Glyph name: uni0462	Contours detected: 17	Expected: 2

- Glyph name: uni0463	Contours detected: 14	Expected: 2

- Glyph name: uni0472	Contours detected: 17	Expected: 3

- Glyph name: uni0473	Contours detected: 13	Expected: 3

- Glyph name: uni0474	Contours detected: 14	Expected: 1

- Glyph name: uni0475	Contours detected: 10	Expected: 1

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

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

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: і̀ і̂ і̃ і̄ і̆ і̇ і̉ і̊ і̋ і̌ і̍ і̒ і̛̀ і̛́ і̛̂ і̛̃ і̛̄ і̛̆ і̛̇ і̛̉</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[8] MatrixSansRaster-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: Ibreve	Contours detected: 10	Expected: 2

- Glyph name: ibreve	Contours detected: 8	Expected: 2

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

- Glyph name: Eng	Contours detected: 14	Expected: 1

- Glyph name: eng	Contours detected: 12	Expected: 1

- Glyph name: Omacron	Contours detected: 13	Expected: 3

- Glyph name: omacron	Contours detected: 9	Expected: 3

- Glyph name: Obreve	Contours detected: 15	Expected: 3

- Glyph name: obreve	Contours detected: 11	Expected: 3

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

- Glyph name: Bhook	Contours detected: 13	Expected: 3

- Glyph name: Oopen	Contours detected: 9	Expected: 1

- Glyph name: Dhook	Contours detected: 14	Expected: 2

- Glyph name: uni018F	Contours detected: 10	Expected: 2

- Glyph name: Eopen	Contours detected: 9	Expected: 1

- Glyph name: florin	Contours detected: 10	Expected: 1

- Glyph name: Khook	Contours detected: 13	Expected: 1

- Glyph name: khook	Contours detected: 11	Expected: 1

- Glyph name: Nhookleft	Contours detected: 17	Expected: 1

- Glyph name: Ohorn	Contours detected: 15	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 11	Expected: 2

- Glyph name: Uhorn	Contours detected: 16	Expected: 1

- Glyph name: uhorn	Contours detected: 13	Expected: 1

- Glyph name: Yhook	Contours detected: 12	Expected: 1

- Glyph name: yhook	Contours detected: 14	Expected: 1

- Glyph name: Acaron	Contours detected: 15	Expected: 3

- Glyph name: acaron	Contours detected: 9	Expected: 3

- Glyph name: Icaron	Contours detected: 10	Expected: 2

- Glyph name: icaron	Contours detected: 8	Expected: 2

- Glyph name: Ocaron	Contours detected: 15	Expected: 3

- Glyph name: ocaron	Contours detected: 11	Expected: 3

- Glyph name: Ucaron	Contours detected: 16	Expected: 2

- Glyph name: ucaron	Contours detected: 13	Expected: 2

- Glyph name: Udieresismacron	Contours detected: 14	Expected: 4

- Glyph name: udieresismacron	Contours detected: 13	Expected: 4

- Glyph name: Udieresisacute	Contours detected: 13	Expected: 4

- Glyph name: udieresisacute	Contours detected: 14	Expected: 4

- Glyph name: Udieresiscaron	Contours detected: 14	Expected: 4

- Glyph name: udieresiscaron	Contours detected: 15	Expected: 4

- Glyph name: Udieresisgrave	Contours detected: 13	Expected: 4

- Glyph name: udieresisgrave	Contours detected: 14	Expected: 4

- Glyph name: Gcaron	Contours detected: 14	Expected: 2

- Glyph name: gcaron	Contours detected: 15	Expected: 3 or 4

- Glyph name: Ngrave	Contours detected: 17	Expected: 2

- Glyph name: ngrave	Contours detected: 12	Expected: 2

- Glyph name: Scommaaccent	Contours detected: 11	Expected: 2

- Glyph name: scommaaccent	Contours detected: 7	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 9	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 10	Expected: 2

- Glyph name: Ymacron	Contours detected: 11	Expected: 2

- Glyph name: ymacron	Contours detected: 13	Expected: 2

- Glyph name: jdotless	Contours detected: 8	Expected: 1

- Glyph name: uni0251	Contours detected: 10	Expected: 2

- Glyph name: uni0259	Contours detected: 6	Expected: 2

- Glyph name: uni0261	Contours detected: 12	Expected: 2

- Glyph name: nhookleft	Contours detected: 12	Expected: 1

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: apostrophemod	Contours detected: 3	Expected: 1

- Glyph name: ringhalfright	Contours detected: 3	Expected: 1

- Glyph name: ringhalfleft	Contours detected: 3	Expected: 1

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

- Glyph name: hookabovecomb	Contours detected: 2	Expected: 1

- Glyph name: ringcomb	Contours detected: 4	Expected: 2

- Glyph name: hungarumlautcomb	Contours detected: 4	Expected: 2

- Glyph name: caroncomb	Contours detected: 3	Expected: 1

- Glyph name: commaturnedabovecomb	Contours detected: 2	Expected: 1

- Glyph name: horncomb	Contours detected: 3	Expected: 1

- Glyph name: commaaccentcomb	Contours detected: 2	Expected: 1

- Glyph name: cedillacomb	Contours detected: 2	Expected: 1

- Glyph name: ogonekcomb	Contours detected: 2	Expected: 1

- Glyph name: brevebelowcomb	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 11	Expected: 2

- Glyph name: uni03A9	Contours detected: 13	Expected: 1

- Glyph name: uni03BC	Contours detected: 12	Expected: 1

- Glyph name: pi	Contours detected: 9	Expected: 1

- Glyph name: uni0400	Contours detected: 9	Expected: 2

- Glyph name: Io-cy	Contours detected: 9	Expected: 3

- Glyph name: Dje-cy	Contours detected: 10	Expected: 1

- Glyph name: uni0403	Contours detected: 9	Expected: 2

- Glyph name: E-cy	Contours detected: 9	Expected: 1

- Glyph name: uni0405	Contours detected: 9	Expected: 1

- Glyph name: I-cy	Contours detected: 7	Expected: 1

- Glyph name: Yi-cy	Contours detected: 9	Expected: 3

- Glyph name: Je-cy	Contours detected: 8	Expected: 1

- Glyph name: Lje-cy	Contours detected: 15	Expected: 2

- Glyph name: Nje-cy	Contours detected: 15	Expected: 2

- Glyph name: Tshe-cy	Contours detected: 10	Expected: 1

- Glyph name: uni040C	Contours detected: 15	Expected: 2

- Glyph name: uni040D	Contours detected: 17	Expected: 2

- Glyph name: Ushort-cy	Contours detected: 14	Expected: 2

- Glyph name: Dzhe-cy	Contours detected: 14	Expected: 1

- Glyph name: A-cy	Contours detected: 12	Expected: 2

- Glyph name: Be-cy	Contours detected: 9	Expected: 2

- Glyph name: Ve-cy	Contours detected: 11	Expected: 3

- Glyph name: Ge-cy	Contours detected: 7	Expected: 1

- Glyph name: De-cy	Contours detected: 14	Expected: 2

- Glyph name: Ie-cy	Contours detected: 7	Expected: 1

- Glyph name: Zhe-cy	Contours detected: 19	Expected: 1

- Glyph name: Ze-cy	Contours detected: 9	Expected: 1

- Glyph name: Ii-cy	Contours detected: 15	Expected: 1

- Glyph name: Iishort-cy	Contours detected: 18	Expected: 2

- Glyph name: Ka-cy	Contours detected: 13	Expected: 1

- Glyph name: El-cy	Contours detected: 13	Expected: 1

- Glyph name: Em-cy	Contours detected: 16	Expected: 1

- Glyph name: En-cy	Contours detected: 13	Expected: 1

- Glyph name: O-cy	Contours detected: 12	Expected: 2

- Glyph name: Pe-cy	Contours detected: 13	Expected: 1

- Glyph name: Er-cy	Contours detected: 9	Expected: 1 or 2

- Glyph name: Es-cy	Contours detected: 9	Expected: 1

- Glyph name: Te-cy	Contours detected: 7	Expected: 1

- Glyph name: U-cy	Contours detected: 11	Expected: 1

- Glyph name: Ef-cy	Contours detected: 13	Expected: 3

- Glyph name: Ha-cy	Contours detected: 13	Expected: 1

- Glyph name: Tse-cy	Contours detected: 14	Expected: 1

- Glyph name: Che-cy	Contours detected: 10	Expected: 1

- Glyph name: Sha-cy	Contours detected: 19	Expected: 1

- Glyph name: Shcha-cy	Contours detected: 20	Expected: 1

- Glyph name: Hardsign-cy	Contours detected: 9	Expected: 2

- Glyph name: Yeru-cy	Contours detected: 16	Expected: 3

- Glyph name: Softsign-cy	Contours detected: 9	Expected: 2

- Glyph name: Ereversed-cy	Contours detected: 9	Expected: 1

- Glyph name: Yu-cy	Contours detected: 18	Expected: 2

- Glyph name: Ya-cy	Contours detected: 12	Expected: 2

- Glyph name: a-cy	Contours detected: 6	Expected: 2

- Glyph name: be-cy	Contours detected: 9	Expected: 2

- Glyph name: ve-cy	Contours detected: 7	Expected: 3

- Glyph name: ge-cy	Contours detected: 5	Expected: 1

- Glyph name: de-cy	Contours detected: 10	Expected: 2

- Glyph name: ie-cy	Contours detected: 6	Expected: 2

- Glyph name: zhe-cy	Contours detected: 13	Expected: 1

- Glyph name: ze-cy	Contours detected: 5	Expected: 1

- Glyph name: ii-cy	Contours detected: 11	Expected: 1

- Glyph name: iishort-cy	Contours detected: 14	Expected: 2

- Glyph name: ka-cy	Contours detected: 9	Expected: 1

- Glyph name: el-cy	Contours detected: 9	Expected: 1

- Glyph name: em-cy	Contours detected: 12	Expected: 1

- Glyph name: en-cy	Contours detected: 9	Expected: 1

- Glyph name: o-cy	Contours detected: 8	Expected: 2

- Glyph name: pe-cy	Contours detected: 9	Expected: 1

- Glyph name: er-cy	Contours detected: 12	Expected: 2

- Glyph name: es-cy	Contours detected: 7	Expected: 1

- Glyph name: te-cy	Contours detected: 5	Expected: 1

- Glyph name: u-cy	Contours detected: 12	Expected: 1

- Glyph name: ef-cy	Contours detected: 15	Expected: 3

- Glyph name: ha-cy	Contours detected: 9	Expected: 1

- Glyph name: tse-cy	Contours detected: 10	Expected: 1

- Glyph name: che-cy	Contours detected: 7	Expected: 1

- Glyph name: sha-cy	Contours detected: 13	Expected: 1

- Glyph name: shcha-cy	Contours detected: 14	Expected: 1

- Glyph name: hardsign-cy	Contours detected: 6	Expected: 2

- Glyph name: yeru-cy	Contours detected: 11	Expected: 3

- Glyph name: softsign-cy	Contours detected: 6	Expected: 2

- Glyph name: ereversed-cy	Contours detected: 5	Expected: 1

- Glyph name: yu-cy	Contours detected: 12	Expected: 2

- Glyph name: ya-cy	Contours detected: 8	Expected: 2

- Glyph name: uni0450	Contours detected: 8	Expected: 3

- Glyph name: io-cy	Contours detected: 8	Expected: 4

- Glyph name: dje-cy	Contours detected: 13	Expected: 1

- Glyph name: uni0453	Contours detected: 7	Expected: 2

- Glyph name: e-cy	Contours detected: 5	Expected: 1

- Glyph name: uni0455	Contours detected: 5	Expected: 1

- Glyph name: i-cy	Contours detected: 6	Expected: 2

- Glyph name: yi-cy	Contours detected: 7	Expected: 3

- Glyph name: je-cy	Contours detected: 9	Expected: 2

- Glyph name: lje-cy	Contours detected: 10	Expected: 2

- Glyph name: nje-cy	Contours detected: 10	Expected: 2

- Glyph name: tshe-cy	Contours detected: 11	Expected: 1

- Glyph name: uni045C	Contours detected: 11	Expected: 2

- Glyph name: uni045D	Contours detected: 13	Expected: 2

- Glyph name: ushort-cy	Contours detected: 15	Expected: 2

- Glyph name: dzhe-cy	Contours detected: 10	Expected: 1 or 2

- Glyph name: uni0462	Contours detected: 9	Expected: 2

- Glyph name: uni0463	Contours detected: 8	Expected: 2

- Glyph name: uni0472	Contours detected: 13	Expected: 3

- Glyph name: uni0473	Contours detected: 9	Expected: 3

- Glyph name: uni0474	Contours detected: 13	Expected: 1

- Glyph name: uni0475	Contours detected: 9	Expected: 1

- Glyph name: Geupturn-cy	Contours detected: 8	Expected: 1

- Glyph name: geupturn-cy	Contours detected: 6	Expected: 1

- Glyph name: Gestroke-cy	Contours detected: 7	Expected: 1

- Glyph name: gestroke-cy	Contours detected: 5	Expected: 1

- Glyph name: Zhedescender-cy	Contours detected: 20	Expected: 1 or 2

- Glyph name: zhedescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: Kadescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: kadescender-cy	Contours detected: 10	Expected: 1 or 2

- Glyph name: Endescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: endescender-cy	Contours detected: 10	Expected: 1 or 2

- Glyph name: Ustraight-cy	Contours detected: 10	Expected: 1

- Glyph name: ustraight-cy	Contours detected: 11	Expected: 1

- Glyph name: Ustraightstroke-cy	Contours detected: 10	Expected: 1

- Glyph name: ustraightstroke-cy	Contours detected: 11	Expected: 1

- Glyph name: Hadescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: hadescender-cy	Contours detected: 10	Expected: 1 or 2

- Glyph name: Chedescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: chedescender-cy	Contours detected: 8	Expected: 1 or 2

- Glyph name: Shha-cy	Contours detected: 10	Expected: 1

- Glyph name: shha-cy	Contours detected: 12	Expected: 1

- Glyph name: Schwa-cy	Contours detected: 10	Expected: 2

- Glyph name: schwa-cy	Contours detected: 6	Expected: 2

- Glyph name: Imacron-cy	Contours detected: 16	Expected: 2

- Glyph name: imacron-cy	Contours detected: 12	Expected: 2

- Glyph name: Obarred-cy	Contours detected: 11	Expected: 3

- Glyph name: obarred-cy	Contours detected: 7	Expected: 3

- Glyph name: Umacron-cy	Contours detected: 12	Expected: 2

- Glyph name: umacron-cy	Contours detected: 13	Expected: 2

- Glyph name: baht	Contours detected: 11	Expected: 3 or 5

- Glyph name: Ddotbelow	Contours detected: 13	Expected: 3

- Glyph name: ddotbelow	Contours detected: 13	Expected: 3

- Glyph name: Dmacronbelow	Contours detected: 13	Expected: 3

- Glyph name: dmacronbelow	Contours detected: 13	Expected: 3

- Glyph name: Gmacron	Contours detected: 12	Expected: 2

- Glyph name: gmacron	Contours detected: 13	Expected: 3 or 4

- Glyph name: Hdotbelow	Contours detected: 14	Expected: 2

- Glyph name: hdotbelow	Contours detected: 13	Expected: 2

- Glyph name: Hbrevebelow	Contours detected: 14	Expected: 2

- Glyph name: hbrevebelow	Contours detected: 13	Expected: 2

- Glyph name: uni1E36	Contours detected: 8	Expected: 2

- Glyph name: uni1E37	Contours detected: 8	Expected: 2

- Glyph name: uni1E38	Contours detected: 9	Expected: 3

- Glyph name: uni1E39	Contours detected: 9	Expected: 3

- Glyph name: uni1E3A	Contours detected: 8	Expected: 2

- Glyph name: uni1E3B	Contours detected: 8	Expected: 2

- Glyph name: Macute	Contours detected: 18	Expected: 2

- Glyph name: macute	Contours detected: 15	Expected: 2

- Glyph name: uni1E42	Contours detected: 17	Expected: 2

- Glyph name: uni1E43	Contours detected: 14	Expected: 2

- Glyph name: Ndotaccent	Contours detected: 16	Expected: 2

- Glyph name: ndotaccent	Contours detected: 11	Expected: 2

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

- Glyph name: Sdotbelow	Contours detected: 10	Expected: 2

- Glyph name: sdotbelow	Contours detected: 6	Expected: 2

- Glyph name: Tdotbelow	Contours detected: 8	Expected: 2

- Glyph name: tdotbelow	Contours detected: 9	Expected: 2

- Glyph name: Tmacronbelow	Contours detected: 8	Expected: 2

- Glyph name: tmacronbelow	Contours detected: 9	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 13	Expected: 2

- Glyph name: Zdotbelow	Contours detected: 8	Expected: 2

- Glyph name: zdotbelow	Contours detected: 6	Expected: 2

- Glyph name: tdieresis	Contours detected: 10	Expected: 3

- Glyph name: Germandbls	Contours detected: 13	Expected: 1

- Glyph name: Adotbelow	Contours detected: 13	Expected: 3

- Glyph name: adotbelow	Contours detected: 7	Expected: 3

- Glyph name: Ahookabove	Contours detected: 14	Expected: 3

- Glyph name: ahookabove	Contours detected: 8	Expected: 3

- Glyph name: Acircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: acircumflexacute	Contours detected: 11	Expected: 4

- Glyph name: Acircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: acircumflexgrave	Contours detected: 11	Expected: 4

- Glyph name: Acircumflexhookabove	Contours detected: 13	Expected: 4

- Glyph name: acircumflexhookabove	Contours detected: 11	Expected: 4

- Glyph name: Acircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: acircumflextilde	Contours detected: 13	Expected: 4

- Glyph name: Acircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: acircumflexdotbelow	Contours detected: 10	Expected: 4

- Glyph name: Abreveacute	Contours detected: 13	Expected: 4

- Glyph name: abreveacute	Contours detected: 11	Expected: 4

- Glyph name: Abrevegrave	Contours detected: 13	Expected: 4

- Glyph name: abrevegrave	Contours detected: 11	Expected: 4

- Glyph name: Abrevehookabove	Contours detected: 13	Expected: 4

- Glyph name: abrevehookabove	Contours detected: 11	Expected: 4

- Glyph name: Abrevetilde	Contours detected: 15	Expected: 4

- Glyph name: abrevetilde	Contours detected: 13	Expected: 4

- Glyph name: Abrevedotbelow	Contours detected: 16	Expected: 4

- Glyph name: abrevedotbelow	Contours detected: 10	Expected: 4

- Glyph name: Edotbelow	Contours detected: 8	Expected: 2

- Glyph name: edotbelow	Contours detected: 7	Expected: 3

- Glyph name: Ehookabove	Contours detected: 9	Expected: 2

- Glyph name: ehookabove	Contours detected: 8	Expected: 3

- Glyph name: Etilde	Contours detected: 11	Expected: 2

- Glyph name: etilde	Contours detected: 10	Expected: 3

- Glyph name: Ecircumflexacute	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexacute	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflexgrave	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexgrave	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflexhookabove	Contours detected: 10	Expected: 3

- Glyph name: ecircumflexhookabove	Contours detected: 11	Expected: 4

- Glyph name: Ecircumflextilde	Contours detected: 12	Expected: 3

- Glyph name: ecircumflextilde	Contours detected: 13	Expected: 4

- Glyph name: Ecircumflexdotbelow	Contours detected: 11	Expected: 3

- Glyph name: ecircumflexdotbelow	Contours detected: 10	Expected: 4

- Glyph name: Ihookabove	Contours detected: 9	Expected: 2

- Glyph name: ihookabove	Contours detected: 7	Expected: 2

- Glyph name: Idotbelow	Contours detected: 8	Expected: 2

- Glyph name: idotbelow	Contours detected: 7	Expected: 3

- Glyph name: Odotbelow	Contours detected: 13	Expected: 3

- Glyph name: odotbelow	Contours detected: 9	Expected: 3

- Glyph name: Ohookabove	Contours detected: 14	Expected: 3

- Glyph name: ohookabove	Contours detected: 10	Expected: 3

- Glyph name: Ocircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexacute	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexgrave	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflexhookabove	Contours detected: 13	Expected: 4

- Glyph name: ocircumflexhookabove	Contours detected: 13	Expected: 4

- Glyph name: Ocircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: ocircumflextilde	Contours detected: 15	Expected: 4

- Glyph name: Ocircumflexdotbelow	Contours detected: 16	Expected: 4

- Glyph name: ocircumflexdotbelow	Contours detected: 12	Expected: 4

- Glyph name: Ohornacute	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohornacute	Contours detected: 13	Expected: 3

- Glyph name: Ohorngrave	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohorngrave	Contours detected: 13	Expected: 3

- Glyph name: Ohornhookabove	Contours detected: 17	Expected: 3 or 4

- Glyph name: ohornhookabove	Contours detected: 13	Expected: 3

- Glyph name: Ohorntilde	Contours detected: 19	Expected: 3 or 4

- Glyph name: ohorntilde	Contours detected: 15	Expected: 3

- Glyph name: Ohorndotbelow	Contours detected: 16	Expected: 3 or 4

- Glyph name: ohorndotbelow	Contours detected: 12	Expected: 3

- Glyph name: Udotbelow	Contours detected: 14	Expected: 2

- Glyph name: udotbelow	Contours detected: 11	Expected: 2

- Glyph name: Uhookabove	Contours detected: 15	Expected: 2

- Glyph name: uhookabove	Contours detected: 12	Expected: 2

- Glyph name: Uhornacute	Contours detected: 18	Expected: 2

- Glyph name: uhornacute	Contours detected: 15	Expected: 2

- Glyph name: Uhorngrave	Contours detected: 18	Expected: 2

- Glyph name: uhorngrave	Contours detected: 15	Expected: 2

- Glyph name: Uhornhookabove	Contours detected: 18	Expected: 2

- Glyph name: uhornhookabove	Contours detected: 15	Expected: 2

- Glyph name: Uhorntilde	Contours detected: 20	Expected: 2

- Glyph name: uhorntilde	Contours detected: 17	Expected: 2

- Glyph name: Uhorndotbelow	Contours detected: 17	Expected: 2

- Glyph name: uhorndotbelow	Contours detected: 14	Expected: 2

- Glyph name: Ygrave	Contours detected: 12	Expected: 2

- Glyph name: ygrave	Contours detected: 14	Expected: 2

- Glyph name: Ydotbelow	Contours detected: 11	Expected: 2

- Glyph name: ydotbelow	Contours detected: 8	Expected: 2

- Glyph name: Yhookabove	Contours detected: 12	Expected: 2

- Glyph name: yhookabove	Contours detected: 14	Expected: 2

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

- Glyph name: nmod	Contours detected: 7	Expected: 1

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

- Glyph name: Eng	Contours detected: 14	Expected: 1

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

- Glyph name: Ibreve	Contours detected: 10	Expected: 2

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

- Glyph name: ibreve	Contours detected: 8	Expected: 2

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

- Glyph name: uni0162	Contours detected: 9	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 10	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 10	Expected: 2

- Glyph name: uni0251	Contours detected: 10	Expected: 2

- Glyph name: uni0259	Contours detected: 6	Expected: 2

- Glyph name: uni0261	Contours detected: 12	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni0394	Contours detected: 11	Expected: 2

- Glyph name: uni03A9	Contours detected: 13	Expected: 1

- Glyph name: uni03BC	Contours detected: 12	Expected: 1

- Glyph name: uni0400	Contours detected: 9	Expected: 2

- Glyph name: uni0403	Contours detected: 9	Expected: 2

- Glyph name: uni0405	Contours detected: 9	Expected: 1

- Glyph name: uni040C	Contours detected: 15	Expected: 2

- Glyph name: uni040D	Contours detected: 17	Expected: 2

- Glyph name: uni0450	Contours detected: 8	Expected: 3

- Glyph name: uni0453	Contours detected: 7	Expected: 2

- Glyph name: uni0455	Contours detected: 5	Expected: 1

- Glyph name: uni045C	Contours detected: 11	Expected: 2

- Glyph name: uni045D	Contours detected: 13	Expected: 2

- Glyph name: uni0462	Contours detected: 9	Expected: 2

- Glyph name: uni0463	Contours detected: 8	Expected: 2

- Glyph name: uni0472	Contours detected: 13	Expected: 3

- Glyph name: uni0473	Contours detected: 9	Expected: 3

- Glyph name: uni0474	Contours detected: 13	Expected: 1

- Glyph name: uni0475	Contours detected: 9	Expected: 1

- Glyph name: uni1E36	Contours detected: 8	Expected: 2

- Glyph name: uni1E37	Contours detected: 8	Expected: 2

- Glyph name: uni1E38	Contours detected: 9	Expected: 3

- Glyph name: uni1E39	Contours detected: 9	Expected: 3

- Glyph name: uni1E3A	Contours detected: 8	Expected: 2

- Glyph name: uni1E3B	Contours detected: 8	Expected: 2

- Glyph name: uni1E42	Contours detected: 17	Expected: 2

- Glyph name: uni1E43	Contours detected: 14	Expected: 2

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

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 13	Expected: 2

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̛̇ i̛̊ i̛̋ i̛̍ i̛̒ i̤̇ i̤̊ i̤̋ i̤̍ i̤̒ i̦̇ i̦̊ i̦̋ i̦̍ i̦̒ i̧̇ i̧̊ i̧̋ i̧̍ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[8] MatrixSansScreen-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: Ibreve	Contours detected: 16	Expected: 2

- Glyph name: ibreve	Contours detected: 13	Expected: 2

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

- Glyph name: Eng	Contours detected: 16	Expected: 1

- Glyph name: eng	Contours detected: 14	Expected: 1

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: Obreve	Contours detected: 21	Expected: 3

- Glyph name: obreve	Contours detected: 17	Expected: 3

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

- Glyph name: Bhook	Contours detected: 20	Expected: 3

- Glyph name: Oopen	Contours detected: 13	Expected: 1

- Glyph name: Dhook	Contours detected: 17	Expected: 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: Eopen	Contours detected: 15	Expected: 1

- Glyph name: florin	Contours detected: 14	Expected: 1

- Glyph name: Khook	Contours detected: 14	Expected: 1

- Glyph name: khook	Contours detected: 13	Expected: 1

- Glyph name: Nhookleft	Contours detected: 19	Expected: 1

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: Yhook	Contours detected: 12	Expected: 1

- Glyph name: yhook	Contours detected: 18	Expected: 1

- Glyph name: Acaron	Contours detected: 19	Expected: 3

- Glyph name: acaron	Contours detected: 17	Expected: 3

- Glyph name: Icaron	Contours detected: 14	Expected: 2

- Glyph name: icaron	Contours detected: 11	Expected: 2

- Glyph name: Ocaron	Contours detected: 19	Expected: 3

- Glyph name: ocaron	Contours detected: 15	Expected: 3

- Glyph name: Ucaron	Contours detected: 18	Expected: 2

- Glyph name: ucaron	Contours detected: 15	Expected: 2

- Glyph name: Udieresismacron	Contours detected: 18	Expected: 4

- Glyph name: udieresismacron	Contours detected: 17	Expected: 4

- Glyph name: Udieresisacute	Contours detected: 15	Expected: 4

- Glyph name: udieresisacute	Contours detected: 16	Expected: 4

- Glyph name: Udieresiscaron	Contours detected: 16	Expected: 4

- Glyph name: udieresiscaron	Contours detected: 17	Expected: 4

- Glyph name: Udieresisgrave	Contours detected: 15	Expected: 4

- Glyph name: udieresisgrave	Contours detected: 16	Expected: 4

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Ngrave	Contours detected: 19	Expected: 2

- Glyph name: ngrave	Contours detected: 14	Expected: 2

- Glyph name: Scommaaccent	Contours detected: 17	Expected: 2

- Glyph name: scommaaccent	Contours detected: 15	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 14	Expected: 2

- Glyph name: Ymacron	Contours detected: 13	Expected: 2

- Glyph name: ymacron	Contours detected: 19	Expected: 2

- Glyph name: jdotless	Contours detected: 10	Expected: 1

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: nhookleft	Contours detected: 14	Expected: 1

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: apostrophemod	Contours detected: 3	Expected: 1

- Glyph name: ringhalfright	Contours detected: 3	Expected: 1

- Glyph name: ringhalfleft	Contours detected: 3	Expected: 1

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

- Glyph name: brevebelowcomb	Contours detected: 5	Expected: 1

- Glyph name: macronbelowcomb	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: uni0400	Contours detected: 20	Expected: 2

- Glyph name: Io-cy	Contours detected: 20	Expected: 3

- Glyph name: Dje-cy	Contours detected: 16	Expected: 1

- Glyph name: uni0403	Contours detected: 13	Expected: 2

- Glyph name: E-cy	Contours detected: 16	Expected: 1

- Glyph name: uni0405	Contours detected: 15	Expected: 1

- Glyph name: I-cy	Contours detected: 11	Expected: 1

- Glyph name: Yi-cy	Contours detected: 13	Expected: 3

- Glyph name: Je-cy	Contours detected: 11	Expected: 1

- Glyph name: Lje-cy	Contours detected: 20	Expected: 2

- Glyph name: Nje-cy	Contours detected: 22	Expected: 2

- Glyph name: Tshe-cy	Contours detected: 16	Expected: 1

- Glyph name: uni040C	Contours detected: 16	Expected: 2

- Glyph name: uni040D	Contours detected: 19	Expected: 2

- Glyph name: Ushort-cy	Contours detected: 21	Expected: 2

- Glyph name: Dzhe-cy	Contours detected: 18	Expected: 1

- Glyph name: A-cy	Contours detected: 16	Expected: 2

- Glyph name: Be-cy	Contours detected: 19	Expected: 2

- Glyph name: Ve-cy	Contours detected: 20	Expected: 3

- Glyph name: Ge-cy	Contours detected: 11	Expected: 1

- Glyph name: De-cy	Contours detected: 21	Expected: 2

- Glyph name: Ie-cy	Contours detected: 18	Expected: 1

- Glyph name: Zhe-cy	Contours detected: 21	Expected: 1

- Glyph name: Ze-cy	Contours detected: 15	Expected: 1

- Glyph name: Ii-cy	Contours detected: 17	Expected: 1

- Glyph name: Iishort-cy	Contours detected: 22	Expected: 2

- Glyph name: Ka-cy	Contours detected: 14	Expected: 1

- Glyph name: El-cy	Contours detected: 15	Expected: 1

- Glyph name: Em-cy	Contours detected: 18	Expected: 1

- Glyph name: En-cy	Contours detected: 17	Expected: 1

- Glyph name: O-cy	Contours detected: 16	Expected: 2

- Glyph name: Pe-cy	Contours detected: 17	Expected: 1

- Glyph name: Er-cy	Contours detected: 15	Expected: 1 or 2

- Glyph name: Es-cy	Contours detected: 13	Expected: 1

- Glyph name: Te-cy	Contours detected: 11	Expected: 1

- Glyph name: U-cy	Contours detected: 16	Expected: 1

- Glyph name: Ef-cy	Contours detected: 17	Expected: 3

- Glyph name: Ha-cy	Contours detected: 13	Expected: 1

- Glyph name: Tse-cy	Contours detected: 18	Expected: 1

- Glyph name: Che-cy	Contours detected: 13	Expected: 1

- Glyph name: Sha-cy	Contours detected: 23	Expected: 1

- Glyph name: Shcha-cy	Contours detected: 25	Expected: 1

- Glyph name: Hardsign-cy	Contours detected: 15	Expected: 2

- Glyph name: Yeru-cy	Contours detected: 20	Expected: 3

- Glyph name: Softsign-cy	Contours detected: 15	Expected: 2

- Glyph name: Ereversed-cy	Contours detected: 16	Expected: 1

- Glyph name: Yu-cy	Contours detected: 22	Expected: 2

- Glyph name: Ya-cy	Contours detected: 18	Expected: 2

- Glyph name: a-cy	Contours detected: 14	Expected: 2

- Glyph name: be-cy	Contours detected: 16	Expected: 2

- Glyph name: ve-cy	Contours detected: 16	Expected: 3

- Glyph name: ge-cy	Contours detected: 9	Expected: 1

- Glyph name: de-cy	Contours detected: 17	Expected: 2

- Glyph name: ie-cy	Contours detected: 14	Expected: 2

- Glyph name: zhe-cy	Contours detected: 15	Expected: 1

- Glyph name: ze-cy	Contours detected: 13	Expected: 1

- Glyph name: ii-cy	Contours detected: 13	Expected: 1

- Glyph name: iishort-cy	Contours detected: 18	Expected: 2

- Glyph name: ka-cy	Contours detected: 11	Expected: 1

- Glyph name: el-cy	Contours detected: 11	Expected: 1

- Glyph name: em-cy	Contours detected: 14	Expected: 1

- Glyph name: en-cy	Contours detected: 13	Expected: 1

- Glyph name: o-cy	Contours detected: 12	Expected: 2

- Glyph name: pe-cy	Contours detected: 13	Expected: 1

- Glyph name: er-cy	Contours detected: 16	Expected: 2

- Glyph name: es-cy	Contours detected: 11	Expected: 1

- Glyph name: te-cy	Contours detected: 9	Expected: 1

- Glyph name: u-cy	Contours detected: 16	Expected: 1

- Glyph name: ef-cy	Contours detected: 19	Expected: 3

- Glyph name: ha-cy	Contours detected: 9	Expected: 1

- Glyph name: tse-cy	Contours detected: 14	Expected: 1

- Glyph name: che-cy	Contours detected: 10	Expected: 1

- Glyph name: sha-cy	Contours detected: 17	Expected: 1

- Glyph name: shcha-cy	Contours detected: 19	Expected: 1

- Glyph name: hardsign-cy	Contours detected: 12	Expected: 2

- Glyph name: yeru-cy	Contours detected: 15	Expected: 3

- Glyph name: softsign-cy	Contours detected: 12	Expected: 2

- Glyph name: ereversed-cy	Contours detected: 14	Expected: 1

- Glyph name: yu-cy	Contours detected: 16	Expected: 2

- Glyph name: ya-cy	Contours detected: 14	Expected: 2

- Glyph name: uni0450	Contours detected: 16	Expected: 3

- Glyph name: io-cy	Contours detected: 16	Expected: 4

- Glyph name: dje-cy	Contours detected: 18	Expected: 1

- Glyph name: uni0453	Contours detected: 11	Expected: 2

- Glyph name: e-cy	Contours detected: 14	Expected: 1

- Glyph name: uni0455	Contours detected: 13	Expected: 1

- Glyph name: i-cy	Contours detected: 9	Expected: 2

- Glyph name: yi-cy	Contours detected: 10	Expected: 3

- Glyph name: je-cy	Contours detected: 11	Expected: 2

- Glyph name: lje-cy	Contours detected: 15	Expected: 2

- Glyph name: nje-cy	Contours detected: 17	Expected: 2

- Glyph name: tshe-cy	Contours detected: 16	Expected: 1

- Glyph name: uni045C	Contours detected: 13	Expected: 2

- Glyph name: uni045D	Contours detected: 15	Expected: 2

- Glyph name: ushort-cy	Contours detected: 21	Expected: 2

- Glyph name: dzhe-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0462	Contours detected: 17	Expected: 2

- Glyph name: uni0463	Contours detected: 14	Expected: 2

- Glyph name: uni0472	Contours detected: 17	Expected: 3

- Glyph name: uni0473	Contours detected: 13	Expected: 3

- Glyph name: uni0474	Contours detected: 14	Expected: 1

- Glyph name: uni0475	Contours detected: 10	Expected: 1

- Glyph name: Geupturn-cy	Contours detected: 12	Expected: 1

- Glyph name: geupturn-cy	Contours detected: 10	Expected: 1

- Glyph name: Gestroke-cy	Contours detected: 14	Expected: 1

- Glyph name: gestroke-cy	Contours detected: 12	Expected: 1

- Glyph name: Zhedescender-cy	Contours detected: 23	Expected: 1 or 2

- Glyph name: zhedescender-cy	Contours detected: 17	Expected: 1 or 2

- Glyph name: Kadescender-cy	Contours detected: 16	Expected: 1 or 2

- Glyph name: kadescender-cy	Contours detected: 12	Expected: 1 or 2

- Glyph name: Endescender-cy	Contours detected: 18	Expected: 1 or 2

- Glyph name: endescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: Ustraight-cy	Contours detected: 10	Expected: 1

- Glyph name: ustraight-cy	Contours detected: 11	Expected: 1

- Glyph name: Ustraightstroke-cy	Contours detected: 12	Expected: 1

- Glyph name: ustraightstroke-cy	Contours detected: 13	Expected: 1

- Glyph name: Hadescender-cy	Contours detected: 15	Expected: 1 or 2

- Glyph name: hadescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: Chedescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: chedescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: Shha-cy	Contours detected: 13	Expected: 1

- Glyph name: shha-cy	Contours detected: 14	Expected: 1

- Glyph name: Schwa-cy	Contours detected: 18	Expected: 2

- Glyph name: schwa-cy	Contours detected: 14	Expected: 2

- Glyph name: Imacron-cy	Contours detected: 20	Expected: 2

- Glyph name: imacron-cy	Contours detected: 16	Expected: 2

- Glyph name: Obarred-cy	Contours detected: 19	Expected: 3

- Glyph name: obarred-cy	Contours detected: 15	Expected: 3

- Glyph name: Umacron-cy	Contours detected: 19	Expected: 2

- Glyph name: umacron-cy	Contours detected: 19	Expected: 2

- Glyph name: baht	Contours detected: 20	Expected: 3 or 5

- Glyph name: Ddotbelow	Contours detected: 17	Expected: 3

- Glyph name: ddotbelow	Contours detected: 17	Expected: 3

- Glyph name: Dmacronbelow	Contours detected: 19	Expected: 3

- Glyph name: dmacronbelow	Contours detected: 19	Expected: 3

- Glyph name: Gmacron	Contours detected: 20	Expected: 2

- Glyph name: gmacron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Hdotbelow	Contours detected: 18	Expected: 2

- Glyph name: hdotbelow	Contours detected: 15	Expected: 2

- Glyph name: Hbrevebelow	Contours detected: 20	Expected: 2

- Glyph name: hbrevebelow	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: Macute	Contours detected: 20	Expected: 2

- Glyph name: macute	Contours detected: 16	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: Ndotaccent	Contours detected: 18	Expected: 2

- Glyph name: ndotaccent	Contours detected: 13	Expected: 2

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

- Glyph name: Sdotbelow	Contours detected: 16	Expected: 2

- Glyph name: sdotbelow	Contours detected: 14	Expected: 2

- Glyph name: Tdotbelow	Contours detected: 12	Expected: 2

- Glyph name: tdotbelow	Contours detected: 13	Expected: 2

- Glyph name: Tmacronbelow	Contours detected: 14	Expected: 2

- Glyph name: tmacronbelow	Contours detected: 15	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: Zdotbelow	Contours detected: 16	Expected: 2

- Glyph name: zdotbelow	Contours detected: 14	Expected: 2

- Glyph name: tdieresis	Contours detected: 14	Expected: 3

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

- Glyph name: nmod	Contours detected: 8	Expected: 1

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

- Glyph name: Eng	Contours detected: 16	Expected: 1

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

- Glyph name: Ibreve	Contours detected: 16	Expected: 2

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

- Glyph name: eng	Contours detected: 14	Expected: 1

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

- Glyph name: ibreve	Contours detected: 13	Expected: 2

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

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: uni0400	Contours detected: 20	Expected: 2

- Glyph name: uni0403	Contours detected: 13	Expected: 2

- Glyph name: uni0405	Contours detected: 15	Expected: 1

- Glyph name: uni040C	Contours detected: 16	Expected: 2

- Glyph name: uni040D	Contours detected: 19	Expected: 2

- Glyph name: uni0450	Contours detected: 16	Expected: 3

- Glyph name: uni0453	Contours detected: 11	Expected: 2

- Glyph name: uni0455	Contours detected: 13	Expected: 1

- Glyph name: uni045C	Contours detected: 13	Expected: 2

- Glyph name: uni045D	Contours detected: 15	Expected: 2

- Glyph name: uni0462	Contours detected: 17	Expected: 2

- Glyph name: uni0463	Contours detected: 14	Expected: 2

- Glyph name: uni0472	Contours detected: 17	Expected: 3

- Glyph name: uni0473	Contours detected: 13	Expected: 3

- Glyph name: uni0474	Contours detected: 14	Expected: 1

- Glyph name: uni0475	Contours detected: 10	Expected: 1

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

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

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̛̇ i̛̊ i̛̋ i̛̍ i̛̒ i̤̇ i̤̊ i̤̋ i̤̍ i̤̒ i̦̇ i̦̊ i̦̋ i̦̍ i̦̒ i̧̇ i̧̊ i̧̋ i̧̍ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[8] MatrixSansPrint-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: Ibreve	Contours detected: 16	Expected: 2

- Glyph name: ibreve	Contours detected: 13	Expected: 2

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

- Glyph name: Eng	Contours detected: 16	Expected: 1

- Glyph name: eng	Contours detected: 14	Expected: 1

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: Obreve	Contours detected: 21	Expected: 3

- Glyph name: obreve	Contours detected: 17	Expected: 3

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

- Glyph name: Bhook	Contours detected: 20	Expected: 3

- Glyph name: Oopen	Contours detected: 13	Expected: 1

- Glyph name: Dhook	Contours detected: 17	Expected: 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: Eopen	Contours detected: 15	Expected: 1

- Glyph name: florin	Contours detected: 14	Expected: 1

- Glyph name: Khook	Contours detected: 14	Expected: 1

- Glyph name: khook	Contours detected: 13	Expected: 1

- Glyph name: Nhookleft	Contours detected: 19	Expected: 1

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: Yhook	Contours detected: 12	Expected: 1

- Glyph name: yhook	Contours detected: 18	Expected: 1

- Glyph name: Acaron	Contours detected: 19	Expected: 3

- Glyph name: acaron	Contours detected: 17	Expected: 3

- Glyph name: Icaron	Contours detected: 14	Expected: 2

- Glyph name: icaron	Contours detected: 11	Expected: 2

- Glyph name: Ocaron	Contours detected: 19	Expected: 3

- Glyph name: ocaron	Contours detected: 15	Expected: 3

- Glyph name: Ucaron	Contours detected: 18	Expected: 2

- Glyph name: ucaron	Contours detected: 15	Expected: 2

- Glyph name: Udieresismacron	Contours detected: 18	Expected: 4

- Glyph name: udieresismacron	Contours detected: 17	Expected: 4

- Glyph name: Udieresisacute	Contours detected: 15	Expected: 4

- Glyph name: udieresisacute	Contours detected: 16	Expected: 4

- Glyph name: Udieresiscaron	Contours detected: 16	Expected: 4

- Glyph name: udieresiscaron	Contours detected: 17	Expected: 4

- Glyph name: Udieresisgrave	Contours detected: 15	Expected: 4

- Glyph name: udieresisgrave	Contours detected: 16	Expected: 4

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Ngrave	Contours detected: 19	Expected: 2

- Glyph name: ngrave	Contours detected: 14	Expected: 2

- Glyph name: Scommaaccent	Contours detected: 17	Expected: 2

- Glyph name: scommaaccent	Contours detected: 15	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 14	Expected: 2

- Glyph name: Ymacron	Contours detected: 13	Expected: 2

- Glyph name: ymacron	Contours detected: 19	Expected: 2

- Glyph name: jdotless	Contours detected: 10	Expected: 1

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: nhookleft	Contours detected: 14	Expected: 1

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: apostrophemod	Contours detected: 3	Expected: 1

- Glyph name: ringhalfright	Contours detected: 3	Expected: 1

- Glyph name: ringhalfleft	Contours detected: 3	Expected: 1

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

- Glyph name: brevebelowcomb	Contours detected: 5	Expected: 1

- Glyph name: macronbelowcomb	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: uni0400	Contours detected: 20	Expected: 2

- Glyph name: Io-cy	Contours detected: 20	Expected: 3

- Glyph name: Dje-cy	Contours detected: 16	Expected: 1

- Glyph name: uni0403	Contours detected: 13	Expected: 2

- Glyph name: E-cy	Contours detected: 16	Expected: 1

- Glyph name: uni0405	Contours detected: 15	Expected: 1

- Glyph name: I-cy	Contours detected: 11	Expected: 1

- Glyph name: Yi-cy	Contours detected: 13	Expected: 3

- Glyph name: Je-cy	Contours detected: 11	Expected: 1

- Glyph name: Lje-cy	Contours detected: 20	Expected: 2

- Glyph name: Nje-cy	Contours detected: 22	Expected: 2

- Glyph name: Tshe-cy	Contours detected: 16	Expected: 1

- Glyph name: uni040C	Contours detected: 16	Expected: 2

- Glyph name: uni040D	Contours detected: 19	Expected: 2

- Glyph name: Ushort-cy	Contours detected: 21	Expected: 2

- Glyph name: Dzhe-cy	Contours detected: 18	Expected: 1

- Glyph name: A-cy	Contours detected: 16	Expected: 2

- Glyph name: Be-cy	Contours detected: 19	Expected: 2

- Glyph name: Ve-cy	Contours detected: 20	Expected: 3

- Glyph name: Ge-cy	Contours detected: 11	Expected: 1

- Glyph name: De-cy	Contours detected: 21	Expected: 2

- Glyph name: Ie-cy	Contours detected: 18	Expected: 1

- Glyph name: Zhe-cy	Contours detected: 21	Expected: 1

- Glyph name: Ze-cy	Contours detected: 15	Expected: 1

- Glyph name: Ii-cy	Contours detected: 17	Expected: 1

- Glyph name: Iishort-cy	Contours detected: 22	Expected: 2

- Glyph name: Ka-cy	Contours detected: 14	Expected: 1

- Glyph name: El-cy	Contours detected: 15	Expected: 1

- Glyph name: Em-cy	Contours detected: 18	Expected: 1

- Glyph name: En-cy	Contours detected: 17	Expected: 1

- Glyph name: O-cy	Contours detected: 16	Expected: 2

- Glyph name: Pe-cy	Contours detected: 17	Expected: 1

- Glyph name: Er-cy	Contours detected: 15	Expected: 1 or 2

- Glyph name: Es-cy	Contours detected: 13	Expected: 1

- Glyph name: Te-cy	Contours detected: 11	Expected: 1

- Glyph name: U-cy	Contours detected: 16	Expected: 1

- Glyph name: Ef-cy	Contours detected: 17	Expected: 3

- Glyph name: Ha-cy	Contours detected: 13	Expected: 1

- Glyph name: Tse-cy	Contours detected: 18	Expected: 1

- Glyph name: Che-cy	Contours detected: 13	Expected: 1

- Glyph name: Sha-cy	Contours detected: 23	Expected: 1

- Glyph name: Shcha-cy	Contours detected: 25	Expected: 1

- Glyph name: Hardsign-cy	Contours detected: 15	Expected: 2

- Glyph name: Yeru-cy	Contours detected: 20	Expected: 3

- Glyph name: Softsign-cy	Contours detected: 15	Expected: 2

- Glyph name: Ereversed-cy	Contours detected: 16	Expected: 1

- Glyph name: Yu-cy	Contours detected: 22	Expected: 2

- Glyph name: Ya-cy	Contours detected: 18	Expected: 2

- Glyph name: a-cy	Contours detected: 14	Expected: 2

- Glyph name: be-cy	Contours detected: 16	Expected: 2

- Glyph name: ve-cy	Contours detected: 16	Expected: 3

- Glyph name: ge-cy	Contours detected: 9	Expected: 1

- Glyph name: de-cy	Contours detected: 17	Expected: 2

- Glyph name: ie-cy	Contours detected: 14	Expected: 2

- Glyph name: zhe-cy	Contours detected: 15	Expected: 1

- Glyph name: ze-cy	Contours detected: 13	Expected: 1

- Glyph name: ii-cy	Contours detected: 13	Expected: 1

- Glyph name: iishort-cy	Contours detected: 18	Expected: 2

- Glyph name: ka-cy	Contours detected: 11	Expected: 1

- Glyph name: el-cy	Contours detected: 11	Expected: 1

- Glyph name: em-cy	Contours detected: 14	Expected: 1

- Glyph name: en-cy	Contours detected: 13	Expected: 1

- Glyph name: o-cy	Contours detected: 12	Expected: 2

- Glyph name: pe-cy	Contours detected: 13	Expected: 1

- Glyph name: er-cy	Contours detected: 16	Expected: 2

- Glyph name: es-cy	Contours detected: 11	Expected: 1

- Glyph name: te-cy	Contours detected: 9	Expected: 1

- Glyph name: u-cy	Contours detected: 16	Expected: 1

- Glyph name: ef-cy	Contours detected: 19	Expected: 3

- Glyph name: ha-cy	Contours detected: 9	Expected: 1

- Glyph name: tse-cy	Contours detected: 14	Expected: 1

- Glyph name: che-cy	Contours detected: 10	Expected: 1

- Glyph name: sha-cy	Contours detected: 17	Expected: 1

- Glyph name: shcha-cy	Contours detected: 19	Expected: 1

- Glyph name: hardsign-cy	Contours detected: 12	Expected: 2

- Glyph name: yeru-cy	Contours detected: 15	Expected: 3

- Glyph name: softsign-cy	Contours detected: 12	Expected: 2

- Glyph name: ereversed-cy	Contours detected: 14	Expected: 1

- Glyph name: yu-cy	Contours detected: 16	Expected: 2

- Glyph name: ya-cy	Contours detected: 14	Expected: 2

- Glyph name: uni0450	Contours detected: 16	Expected: 3

- Glyph name: io-cy	Contours detected: 16	Expected: 4

- Glyph name: dje-cy	Contours detected: 18	Expected: 1

- Glyph name: uni0453	Contours detected: 11	Expected: 2

- Glyph name: e-cy	Contours detected: 14	Expected: 1

- Glyph name: uni0455	Contours detected: 13	Expected: 1

- Glyph name: i-cy	Contours detected: 9	Expected: 2

- Glyph name: yi-cy	Contours detected: 10	Expected: 3

- Glyph name: je-cy	Contours detected: 11	Expected: 2

- Glyph name: lje-cy	Contours detected: 15	Expected: 2

- Glyph name: nje-cy	Contours detected: 17	Expected: 2

- Glyph name: tshe-cy	Contours detected: 16	Expected: 1

- Glyph name: uni045C	Contours detected: 13	Expected: 2

- Glyph name: uni045D	Contours detected: 15	Expected: 2

- Glyph name: ushort-cy	Contours detected: 21	Expected: 2

- Glyph name: dzhe-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0462	Contours detected: 17	Expected: 2

- Glyph name: uni0463	Contours detected: 14	Expected: 2

- Glyph name: uni0472	Contours detected: 17	Expected: 3

- Glyph name: uni0473	Contours detected: 13	Expected: 3

- Glyph name: uni0474	Contours detected: 14	Expected: 1

- Glyph name: uni0475	Contours detected: 10	Expected: 1

- Glyph name: Geupturn-cy	Contours detected: 12	Expected: 1

- Glyph name: geupturn-cy	Contours detected: 10	Expected: 1

- Glyph name: Gestroke-cy	Contours detected: 14	Expected: 1

- Glyph name: gestroke-cy	Contours detected: 12	Expected: 1

- Glyph name: Zhedescender-cy	Contours detected: 23	Expected: 1 or 2

- Glyph name: zhedescender-cy	Contours detected: 17	Expected: 1 or 2

- Glyph name: Kadescender-cy	Contours detected: 16	Expected: 1 or 2

- Glyph name: kadescender-cy	Contours detected: 12	Expected: 1 or 2

- Glyph name: Endescender-cy	Contours detected: 18	Expected: 1 or 2

- Glyph name: endescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: Ustraight-cy	Contours detected: 10	Expected: 1

- Glyph name: ustraight-cy	Contours detected: 11	Expected: 1

- Glyph name: Ustraightstroke-cy	Contours detected: 12	Expected: 1

- Glyph name: ustraightstroke-cy	Contours detected: 13	Expected: 1

- Glyph name: Hadescender-cy	Contours detected: 15	Expected: 1 or 2

- Glyph name: hadescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: Chedescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: chedescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: Shha-cy	Contours detected: 13	Expected: 1

- Glyph name: shha-cy	Contours detected: 14	Expected: 1

- Glyph name: Schwa-cy	Contours detected: 18	Expected: 2

- Glyph name: schwa-cy	Contours detected: 14	Expected: 2

- Glyph name: Imacron-cy	Contours detected: 20	Expected: 2

- Glyph name: imacron-cy	Contours detected: 16	Expected: 2

- Glyph name: Obarred-cy	Contours detected: 19	Expected: 3

- Glyph name: obarred-cy	Contours detected: 15	Expected: 3

- Glyph name: Umacron-cy	Contours detected: 19	Expected: 2

- Glyph name: umacron-cy	Contours detected: 19	Expected: 2

- Glyph name: baht	Contours detected: 20	Expected: 3 or 5

- Glyph name: Ddotbelow	Contours detected: 17	Expected: 3

- Glyph name: ddotbelow	Contours detected: 17	Expected: 3

- Glyph name: Dmacronbelow	Contours detected: 19	Expected: 3

- Glyph name: dmacronbelow	Contours detected: 19	Expected: 3

- Glyph name: Gmacron	Contours detected: 20	Expected: 2

- Glyph name: gmacron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Hdotbelow	Contours detected: 18	Expected: 2

- Glyph name: hdotbelow	Contours detected: 15	Expected: 2

- Glyph name: Hbrevebelow	Contours detected: 20	Expected: 2

- Glyph name: hbrevebelow	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: Macute	Contours detected: 20	Expected: 2

- Glyph name: macute	Contours detected: 16	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: Ndotaccent	Contours detected: 18	Expected: 2

- Glyph name: ndotaccent	Contours detected: 13	Expected: 2

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

- Glyph name: Sdotbelow	Contours detected: 16	Expected: 2

- Glyph name: sdotbelow	Contours detected: 14	Expected: 2

- Glyph name: Tdotbelow	Contours detected: 12	Expected: 2

- Glyph name: tdotbelow	Contours detected: 13	Expected: 2

- Glyph name: Tmacronbelow	Contours detected: 14	Expected: 2

- Glyph name: tmacronbelow	Contours detected: 15	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: Zdotbelow	Contours detected: 16	Expected: 2

- Glyph name: zdotbelow	Contours detected: 14	Expected: 2

- Glyph name: tdieresis	Contours detected: 14	Expected: 3

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

- Glyph name: nmod	Contours detected: 8	Expected: 1

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

- Glyph name: Eng	Contours detected: 16	Expected: 1

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

- Glyph name: Ibreve	Contours detected: 16	Expected: 2

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

- Glyph name: eng	Contours detected: 14	Expected: 1

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

- Glyph name: ibreve	Contours detected: 13	Expected: 2

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

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: uni0400	Contours detected: 20	Expected: 2

- Glyph name: uni0403	Contours detected: 13	Expected: 2

- Glyph name: uni0405	Contours detected: 15	Expected: 1

- Glyph name: uni040C	Contours detected: 16	Expected: 2

- Glyph name: uni040D	Contours detected: 19	Expected: 2

- Glyph name: uni0450	Contours detected: 16	Expected: 3

- Glyph name: uni0453	Contours detected: 11	Expected: 2

- Glyph name: uni0455	Contours detected: 13	Expected: 1

- Glyph name: uni045C	Contours detected: 13	Expected: 2

- Glyph name: uni045D	Contours detected: 15	Expected: 2

- Glyph name: uni0462	Contours detected: 17	Expected: 2

- Glyph name: uni0463	Contours detected: 14	Expected: 2

- Glyph name: uni0472	Contours detected: 17	Expected: 3

- Glyph name: uni0473	Contours detected: 13	Expected: 3

- Glyph name: uni0474	Contours detected: 14	Expected: 1

- Glyph name: uni0475	Contours detected: 10	Expected: 1

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

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

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̛̇ i̛̊ i̛̋ i̛̍ i̛̒ i̤̇ i̤̊ i̤̋ i̤̍ i̤̒ i̦̇ i̦̊ i̦̋ i̦̍ i̦̒ i̧̇ i̧̊ i̧̋ i̧̍ i̧̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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

<details><summary>[8] MatrixSansPrintSC-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: A-cy, Be-cy, Che-cy, Chedescender-cy, De-cy, Dje-cy, Dzhe-cy, E-cy, Ef-cy, El-cy, Em-cy, En-cy, Endescender-cy, Er-cy, Ereversed-cy, Es-cy, Ge-cy, Gestroke-cy, Geupturn-cy, Ha-cy, Hadescender-cy, Hardsign-cy, I-cy, Ie-cy, Ii-cy, Iishort-cy, Imacron-cy, Io-cy, Je-cy, Ka-cy, Kadescender-cy, Lje-cy, Nje-cy, O-cy, Obarred-cy, Pe-cy, Schwa-cy, Sha-cy, Shcha-cy, Shha-cy, Softsign-cy, Te-cy, Tse-cy, Tshe-cy, U-cy, Umacron-cy, Ushort-cy, Ustraight-cy, Ustraightstroke-cy, Ve-cy, Ya-cy, Yeru-cy, Yi-cy, Yu-cy, Ze-cy, Zhe-cy, Zhedescender-cy, a-cy, be-cy, che-cy, chedescender-cy, de-cy, dje-cy, dzhe-cy, e-cy, ef-cy, el-cy, em-cy, en-cy, endescender-cy, er-cy, ereversed-cy, es-cy, ge-cy, gestroke-cy, geupturn-cy, ha-cy, hadescender-cy, hardsign-cy, i-cy, ie-cy, ii-cy, iishort-cy, imacron-cy, io-cy, je-cy, ka-cy, kadescender-cy, lje-cy, nje-cy, o-cy, obarred-cy, pe-cy, schwa-cy, sha-cy, shcha-cy, shha-cy, softsign-cy, te-cy, tse-cy, tshe-cy, u-cy, umacron-cy, ushort-cy, ustraight-cy, ustraightstroke-cy, ve-cy, ya-cy, yeru-cy, yi-cy, yu-cy, ze-cy, zhe-cy and zhedescender-cy</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">af_Latn (Afrikaans)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ä; both buffers returned adieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ë; both buffers returned edieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ï; both buffers returned idieresis.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ö; both buffers returned odieresis=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ü; both buffers returned udieresis.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ý; both buffers returned yacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: å; both buffers returned aring.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ã; both buffers returned atilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: æ; both buffers returned ae.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: œ; both buffers returned oe.sc=0+800</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ç; both buffers returned ccedilla=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ñ; both buffers returned ntilde.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">bm_Latn (Bambara)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dyu_Latn (Dyula)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɲ; both buffers returned nhookleft.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɔ; both buffers returned oopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ha_Latn (Hausa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɓ; both buffers returned bhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɗ; both buffers returned dhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƙ; both buffers returned khook.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ƴ; both buffers returned yhook.sc=0+700</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: â; both buffers returned acircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ê; both buffers returned ecircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: î; both buffers returned icircumflex.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ô; both buffers returned ocircumflex=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: û; both buffers returned ucircumflex.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">ig_Latn (Igbo)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ị; both buffers returned idotbelow.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṅ; both buffers returned ndotaccent.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ụ; both buffers returned udotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ā; both buffers returned amacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ē; both buffers returned emacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ī; both buffers returned imacron.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ō; both buffers returned omacron=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ū; both buffers returned umacron.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɛ; both buffers returned eopen=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ɵ; both buffers returned .notdef=0+601</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">lg_Latn (Ganda)</td>
<td align="left">The locl feature did not affect Eng</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ŋ; both buffers returned eng.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">om_Latn (Oromo)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">sw_Latn (Swahili)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">xh_Latn (Xhosa)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* 🔥 **FAIL** <p>GF_Latin_PriAfrican glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">yo_Latn (Yoruba)</td>
<td align="left">Requires Small-cap: a; both buffers returned a.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: á; both buffers returned aacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: à; both buffers returned agrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: b; both buffers returned b.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: d; both buffers returned d.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: e; both buffers returned e.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: é; both buffers returned eacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: è; both buffers returned egrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ẹ; both buffers returned edotbelow.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: f; both buffers returned f.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: g; both buffers returned g.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: h; both buffers returned h.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: i; both buffers returned i.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: í; both buffers returned iacute.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ì; both buffers returned igrave.sc=0+400</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: j; both buffers returned j.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: k; both buffers returned kgreenlandic=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: l; both buffers returned l.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: m; both buffers returned m.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ḿ; both buffers returned macute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: n; both buffers returned n.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ń; both buffers returned nacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ǹ; both buffers returned ngrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: o; both buffers returned o=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ó; both buffers returned oacute=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ò; both buffers returned ograve=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ọ; both buffers returned odotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: p; both buffers returned p.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: r; both buffers returned r.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: s; both buffers returned s=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ṣ; both buffers returned sdotbelow=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: t; both buffers returned t.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: u; both buffers returned u.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ú; both buffers returned uacute.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: ù; both buffers returned ugrave.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: w; both buffers returned w=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: y; both buffers returned y.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: c; both buffers returned c=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: q; both buffers returned q.sc=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: v; both buffers returned v=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: x; both buffers returned x=0+600</td>
</tr>
<tr>
<td align="left">^</td>
<td align="left">Requires Small-cap: z; both buffers returned z=0+600</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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

- Glyph name: Ibreve	Contours detected: 16	Expected: 2

- Glyph name: ibreve	Contours detected: 13	Expected: 2

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

- Glyph name: Eng	Contours detected: 16	Expected: 1

- Glyph name: eng	Contours detected: 14	Expected: 1

- Glyph name: Omacron	Contours detected: 19	Expected: 3

- Glyph name: omacron	Contours detected: 15	Expected: 3

- Glyph name: Obreve	Contours detected: 21	Expected: 3

- Glyph name: obreve	Contours detected: 17	Expected: 3

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

- Glyph name: Bhook	Contours detected: 20	Expected: 3

- Glyph name: Oopen	Contours detected: 13	Expected: 1

- Glyph name: Dhook	Contours detected: 17	Expected: 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: Eopen	Contours detected: 15	Expected: 1

- Glyph name: florin	Contours detected: 14	Expected: 1

- Glyph name: Khook	Contours detected: 14	Expected: 1

- Glyph name: khook	Contours detected: 13	Expected: 1

- Glyph name: Nhookleft	Contours detected: 19	Expected: 1

- Glyph name: Ohorn	Contours detected: 19	Expected: 2 or 3

- Glyph name: ohorn	Contours detected: 15	Expected: 2

- Glyph name: Uhorn	Contours detected: 18	Expected: 1

- Glyph name: uhorn	Contours detected: 15	Expected: 1

- Glyph name: Yhook	Contours detected: 12	Expected: 1

- Glyph name: yhook	Contours detected: 18	Expected: 1

- Glyph name: Acaron	Contours detected: 19	Expected: 3

- Glyph name: acaron	Contours detected: 17	Expected: 3

- Glyph name: Icaron	Contours detected: 14	Expected: 2

- Glyph name: icaron	Contours detected: 11	Expected: 2

- Glyph name: Ocaron	Contours detected: 19	Expected: 3

- Glyph name: ocaron	Contours detected: 15	Expected: 3

- Glyph name: Ucaron	Contours detected: 18	Expected: 2

- Glyph name: ucaron	Contours detected: 15	Expected: 2

- Glyph name: Udieresismacron	Contours detected: 18	Expected: 4

- Glyph name: udieresismacron	Contours detected: 17	Expected: 4

- Glyph name: Udieresisacute	Contours detected: 15	Expected: 4

- Glyph name: udieresisacute	Contours detected: 16	Expected: 4

- Glyph name: Udieresiscaron	Contours detected: 16	Expected: 4

- Glyph name: udieresiscaron	Contours detected: 17	Expected: 4

- Glyph name: Udieresisgrave	Contours detected: 15	Expected: 4

- Glyph name: udieresisgrave	Contours detected: 16	Expected: 4

- Glyph name: Gcaron	Contours detected: 20	Expected: 2

- Glyph name: gcaron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Ngrave	Contours detected: 19	Expected: 2

- Glyph name: ngrave	Contours detected: 14	Expected: 2

- Glyph name: Scommaaccent	Contours detected: 17	Expected: 2

- Glyph name: scommaaccent	Contours detected: 15	Expected: 2

- Glyph name: Tcommaaccent	Contours detected: 13	Expected: 2

- Glyph name: tcommaaccent	Contours detected: 14	Expected: 2

- Glyph name: Ymacron	Contours detected: 13	Expected: 2

- Glyph name: ymacron	Contours detected: 19	Expected: 2

- Glyph name: jdotless	Contours detected: 10	Expected: 1

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: nhookleft	Contours detected: 14	Expected: 1

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: apostrophemod	Contours detected: 3	Expected: 1

- Glyph name: ringhalfright	Contours detected: 3	Expected: 1

- Glyph name: ringhalfleft	Contours detected: 3	Expected: 1

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

- Glyph name: brevebelowcomb	Contours detected: 5	Expected: 1

- Glyph name: macronbelowcomb	Contours detected: 3	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: pi	Contours detected: 13	Expected: 1

- Glyph name: uni0400	Contours detected: 20	Expected: 2

- Glyph name: Io-cy	Contours detected: 20	Expected: 3

- Glyph name: Dje-cy	Contours detected: 16	Expected: 1

- Glyph name: uni0403	Contours detected: 13	Expected: 2

- Glyph name: E-cy	Contours detected: 16	Expected: 1

- Glyph name: uni0405	Contours detected: 15	Expected: 1

- Glyph name: I-cy	Contours detected: 11	Expected: 1

- Glyph name: Yi-cy	Contours detected: 13	Expected: 3

- Glyph name: Je-cy	Contours detected: 11	Expected: 1

- Glyph name: Lje-cy	Contours detected: 20	Expected: 2

- Glyph name: Nje-cy	Contours detected: 22	Expected: 2

- Glyph name: Tshe-cy	Contours detected: 16	Expected: 1

- Glyph name: uni040C	Contours detected: 16	Expected: 2

- Glyph name: uni040D	Contours detected: 19	Expected: 2

- Glyph name: Ushort-cy	Contours detected: 21	Expected: 2

- Glyph name: Dzhe-cy	Contours detected: 18	Expected: 1

- Glyph name: A-cy	Contours detected: 16	Expected: 2

- Glyph name: Be-cy	Contours detected: 19	Expected: 2

- Glyph name: Ve-cy	Contours detected: 20	Expected: 3

- Glyph name: Ge-cy	Contours detected: 11	Expected: 1

- Glyph name: De-cy	Contours detected: 21	Expected: 2

- Glyph name: Ie-cy	Contours detected: 18	Expected: 1

- Glyph name: Zhe-cy	Contours detected: 21	Expected: 1

- Glyph name: Ze-cy	Contours detected: 15	Expected: 1

- Glyph name: Ii-cy	Contours detected: 17	Expected: 1

- Glyph name: Iishort-cy	Contours detected: 22	Expected: 2

- Glyph name: Ka-cy	Contours detected: 14	Expected: 1

- Glyph name: El-cy	Contours detected: 15	Expected: 1

- Glyph name: Em-cy	Contours detected: 18	Expected: 1

- Glyph name: En-cy	Contours detected: 17	Expected: 1

- Glyph name: O-cy	Contours detected: 16	Expected: 2

- Glyph name: Pe-cy	Contours detected: 17	Expected: 1

- Glyph name: Er-cy	Contours detected: 15	Expected: 1 or 2

- Glyph name: Es-cy	Contours detected: 13	Expected: 1

- Glyph name: Te-cy	Contours detected: 11	Expected: 1

- Glyph name: U-cy	Contours detected: 16	Expected: 1

- Glyph name: Ef-cy	Contours detected: 17	Expected: 3

- Glyph name: Ha-cy	Contours detected: 13	Expected: 1

- Glyph name: Tse-cy	Contours detected: 18	Expected: 1

- Glyph name: Che-cy	Contours detected: 13	Expected: 1

- Glyph name: Sha-cy	Contours detected: 23	Expected: 1

- Glyph name: Shcha-cy	Contours detected: 25	Expected: 1

- Glyph name: Hardsign-cy	Contours detected: 15	Expected: 2

- Glyph name: Yeru-cy	Contours detected: 20	Expected: 3

- Glyph name: Softsign-cy	Contours detected: 15	Expected: 2

- Glyph name: Ereversed-cy	Contours detected: 16	Expected: 1

- Glyph name: Yu-cy	Contours detected: 22	Expected: 2

- Glyph name: Ya-cy	Contours detected: 18	Expected: 2

- Glyph name: a-cy	Contours detected: 14	Expected: 2

- Glyph name: be-cy	Contours detected: 16	Expected: 2

- Glyph name: ve-cy	Contours detected: 16	Expected: 3

- Glyph name: ge-cy	Contours detected: 9	Expected: 1

- Glyph name: de-cy	Contours detected: 17	Expected: 2

- Glyph name: ie-cy	Contours detected: 14	Expected: 2

- Glyph name: zhe-cy	Contours detected: 15	Expected: 1

- Glyph name: ze-cy	Contours detected: 13	Expected: 1

- Glyph name: ii-cy	Contours detected: 13	Expected: 1

- Glyph name: iishort-cy	Contours detected: 18	Expected: 2

- Glyph name: ka-cy	Contours detected: 11	Expected: 1

- Glyph name: el-cy	Contours detected: 11	Expected: 1

- Glyph name: em-cy	Contours detected: 14	Expected: 1

- Glyph name: en-cy	Contours detected: 13	Expected: 1

- Glyph name: o-cy	Contours detected: 12	Expected: 2

- Glyph name: pe-cy	Contours detected: 13	Expected: 1

- Glyph name: er-cy	Contours detected: 16	Expected: 2

- Glyph name: es-cy	Contours detected: 11	Expected: 1

- Glyph name: te-cy	Contours detected: 9	Expected: 1

- Glyph name: u-cy	Contours detected: 16	Expected: 1

- Glyph name: ef-cy	Contours detected: 19	Expected: 3

- Glyph name: ha-cy	Contours detected: 9	Expected: 1

- Glyph name: tse-cy	Contours detected: 14	Expected: 1

- Glyph name: che-cy	Contours detected: 10	Expected: 1

- Glyph name: sha-cy	Contours detected: 17	Expected: 1

- Glyph name: shcha-cy	Contours detected: 19	Expected: 1

- Glyph name: hardsign-cy	Contours detected: 12	Expected: 2

- Glyph name: yeru-cy	Contours detected: 15	Expected: 3

- Glyph name: softsign-cy	Contours detected: 12	Expected: 2

- Glyph name: ereversed-cy	Contours detected: 14	Expected: 1

- Glyph name: yu-cy	Contours detected: 16	Expected: 2

- Glyph name: ya-cy	Contours detected: 14	Expected: 2

- Glyph name: uni0450	Contours detected: 16	Expected: 3

- Glyph name: io-cy	Contours detected: 16	Expected: 4

- Glyph name: dje-cy	Contours detected: 18	Expected: 1

- Glyph name: uni0453	Contours detected: 11	Expected: 2

- Glyph name: e-cy	Contours detected: 14	Expected: 1

- Glyph name: uni0455	Contours detected: 13	Expected: 1

- Glyph name: i-cy	Contours detected: 9	Expected: 2

- Glyph name: yi-cy	Contours detected: 10	Expected: 3

- Glyph name: je-cy	Contours detected: 11	Expected: 2

- Glyph name: lje-cy	Contours detected: 15	Expected: 2

- Glyph name: nje-cy	Contours detected: 17	Expected: 2

- Glyph name: tshe-cy	Contours detected: 16	Expected: 1

- Glyph name: uni045C	Contours detected: 13	Expected: 2

- Glyph name: uni045D	Contours detected: 15	Expected: 2

- Glyph name: ushort-cy	Contours detected: 21	Expected: 2

- Glyph name: dzhe-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0462	Contours detected: 17	Expected: 2

- Glyph name: uni0463	Contours detected: 14	Expected: 2

- Glyph name: uni0472	Contours detected: 17	Expected: 3

- Glyph name: uni0473	Contours detected: 13	Expected: 3

- Glyph name: uni0474	Contours detected: 14	Expected: 1

- Glyph name: uni0475	Contours detected: 10	Expected: 1

- Glyph name: Geupturn-cy	Contours detected: 12	Expected: 1

- Glyph name: geupturn-cy	Contours detected: 10	Expected: 1

- Glyph name: Gestroke-cy	Contours detected: 14	Expected: 1

- Glyph name: gestroke-cy	Contours detected: 12	Expected: 1

- Glyph name: Zhedescender-cy	Contours detected: 23	Expected: 1 or 2

- Glyph name: zhedescender-cy	Contours detected: 17	Expected: 1 or 2

- Glyph name: Kadescender-cy	Contours detected: 16	Expected: 1 or 2

- Glyph name: kadescender-cy	Contours detected: 12	Expected: 1 or 2

- Glyph name: Endescender-cy	Contours detected: 18	Expected: 1 or 2

- Glyph name: endescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: Ustraight-cy	Contours detected: 10	Expected: 1

- Glyph name: ustraight-cy	Contours detected: 11	Expected: 1

- Glyph name: Ustraightstroke-cy	Contours detected: 12	Expected: 1

- Glyph name: ustraightstroke-cy	Contours detected: 13	Expected: 1

- Glyph name: Hadescender-cy	Contours detected: 15	Expected: 1 or 2

- Glyph name: hadescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: Chedescender-cy	Contours detected: 14	Expected: 1 or 2

- Glyph name: chedescender-cy	Contours detected: 11	Expected: 1 or 2

- Glyph name: Shha-cy	Contours detected: 13	Expected: 1

- Glyph name: shha-cy	Contours detected: 14	Expected: 1

- Glyph name: Schwa-cy	Contours detected: 18	Expected: 2

- Glyph name: schwa-cy	Contours detected: 14	Expected: 2

- Glyph name: Imacron-cy	Contours detected: 20	Expected: 2

- Glyph name: imacron-cy	Contours detected: 16	Expected: 2

- Glyph name: Obarred-cy	Contours detected: 19	Expected: 3

- Glyph name: obarred-cy	Contours detected: 15	Expected: 3

- Glyph name: Umacron-cy	Contours detected: 19	Expected: 2

- Glyph name: umacron-cy	Contours detected: 19	Expected: 2

- Glyph name: baht	Contours detected: 20	Expected: 3 or 5

- Glyph name: Ddotbelow	Contours detected: 17	Expected: 3

- Glyph name: ddotbelow	Contours detected: 17	Expected: 3

- Glyph name: Dmacronbelow	Contours detected: 19	Expected: 3

- Glyph name: dmacronbelow	Contours detected: 19	Expected: 3

- Glyph name: Gmacron	Contours detected: 20	Expected: 2

- Glyph name: gmacron	Contours detected: 21	Expected: 3 or 4

- Glyph name: Hdotbelow	Contours detected: 18	Expected: 2

- Glyph name: hdotbelow	Contours detected: 15	Expected: 2

- Glyph name: Hbrevebelow	Contours detected: 20	Expected: 2

- Glyph name: hbrevebelow	Contours detected: 17	Expected: 2

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: Macute	Contours detected: 20	Expected: 2

- Glyph name: macute	Contours detected: 16	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

- Glyph name: Ndotaccent	Contours detected: 18	Expected: 2

- Glyph name: ndotaccent	Contours detected: 13	Expected: 2

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

- Glyph name: Sdotbelow	Contours detected: 16	Expected: 2

- Glyph name: sdotbelow	Contours detected: 14	Expected: 2

- Glyph name: Tdotbelow	Contours detected: 12	Expected: 2

- Glyph name: tdotbelow	Contours detected: 13	Expected: 2

- Glyph name: Tmacronbelow	Contours detected: 14	Expected: 2

- Glyph name: tmacronbelow	Contours detected: 15	Expected: 2

- Glyph name: Wgrave	Contours detected: 19	Expected: 2

- Glyph name: wgrave	Contours detected: 15	Expected: 2

- Glyph name: Wacute	Contours detected: 19	Expected: 2

- Glyph name: wacute	Contours detected: 15	Expected: 2

- Glyph name: Wdieresis	Contours detected: 19	Expected: 3

- Glyph name: wdieresis	Contours detected: 15	Expected: 3

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

- Glyph name: Zdotbelow	Contours detected: 16	Expected: 2

- Glyph name: zdotbelow	Contours detected: 14	Expected: 2

- Glyph name: tdieresis	Contours detected: 14	Expected: 3

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

- Glyph name: nmod	Contours detected: 8	Expected: 1

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

- Glyph name: Eng	Contours detected: 16	Expected: 1

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

- Glyph name: Ibreve	Contours detected: 16	Expected: 2

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

- Glyph name: eng	Contours detected: 14	Expected: 1

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

- Glyph name: ibreve	Contours detected: 13	Expected: 2

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

- Glyph name: uni0162	Contours detected: 14	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 15	Expected: 1 or 2

- Glyph name: uni018F	Contours detected: 18	Expected: 2

- Glyph name: uni0251	Contours detected: 14	Expected: 2

- Glyph name: uni0259	Contours detected: 14	Expected: 2

- Glyph name: uni0261	Contours detected: 18	Expected: 2

- Glyph name: uni02BB	Contours detected: 3	Expected: 1

- Glyph name: uni02C8	Contours detected: 2	Expected: 1

- Glyph name: uni02C9	Contours detected: 3	Expected: 1

- Glyph name: uni02CA	Contours detected: 2	Expected: 1

- Glyph name: uni02CB	Contours detected: 2	Expected: 1

- Glyph name: uni02CC	Contours detected: 2	Expected: 1

- Glyph name: uni0394	Contours detected: 15	Expected: 2

- Glyph name: uni03A9	Contours detected: 17	Expected: 1

- Glyph name: uni03BC	Contours detected: 14	Expected: 1

- Glyph name: uni0400	Contours detected: 20	Expected: 2

- Glyph name: uni0403	Contours detected: 13	Expected: 2

- Glyph name: uni0405	Contours detected: 15	Expected: 1

- Glyph name: uni040C	Contours detected: 16	Expected: 2

- Glyph name: uni040D	Contours detected: 19	Expected: 2

- Glyph name: uni0450	Contours detected: 16	Expected: 3

- Glyph name: uni0453	Contours detected: 11	Expected: 2

- Glyph name: uni0455	Contours detected: 13	Expected: 1

- Glyph name: uni045C	Contours detected: 13	Expected: 2

- Glyph name: uni045D	Contours detected: 15	Expected: 2

- Glyph name: uni0462	Contours detected: 17	Expected: 2

- Glyph name: uni0463	Contours detected: 14	Expected: 2

- Glyph name: uni0472	Contours detected: 17	Expected: 3

- Glyph name: uni0473	Contours detected: 13	Expected: 3

- Glyph name: uni0474	Contours detected: 14	Expected: 1

- Glyph name: uni0475	Contours detected: 10	Expected: 1

- Glyph name: uni1E36	Contours detected: 12	Expected: 2

- Glyph name: uni1E37	Contours detected: 11	Expected: 2

- Glyph name: uni1E38	Contours detected: 15	Expected: 3

- Glyph name: uni1E39	Contours detected: 14	Expected: 3

- Glyph name: uni1E3A	Contours detected: 14	Expected: 2

- Glyph name: uni1E3B	Contours detected: 13	Expected: 2

- Glyph name: uni1E42	Contours detected: 19	Expected: 2

- Glyph name: uni1E43	Contours detected: 15	Expected: 2

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

- Glyph name: uni1E8E	Contours detected: 11	Expected: 2

- Glyph name: uni1E8F	Contours detected: 17	Expected: 2

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
greater, less, greaterequal, lessequal</p>
 [code: width-outliers]



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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, tifinagh, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, tifinagh, malayalam, coptic, math, canadian-aboriginal, tai-le, syriac, old-permic, hebrew, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, syriac, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: caucasian-albanian, gothic, tifinagh, thai, syriac, sunuwar, cherokee</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: arabic, armenian, lisu, coptic, syloti-nagri, cham, sora-sompeng, yi, sundanese, kharoshthi, hebrew, kaithi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: math, yi, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+23CF EJECT SYMBOL: try adding symbols</li>
<li>U+23E9 BLACK RIGHT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23EA BLACK LEFT-POINTING DOUBLE TRIANGLE: try adding symbols</li>
<li>U+23F8 DOUBLE VERTICAL BAR: try adding symbols</li>
<li>U+23F9 BLACK SQUARE FOR STOP: try adding symbols</li>
<li>U+23FA BLACK CIRCLE FOR RECORD: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: math, symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: devanagari, math, lao, old-permic, miao, bhaiksuki, sinhala, marchen, pahawh-hmong, limbu, hebrew, phags-pa, lepcha, balinese, syriac, elbasan, sundanese, wancho, gunjala-gondi, mahajani, masaram-gondi, sharada, thaana, warang-citi, hanunoo, siddham, newa, thai, syloti-nagri, saurashtra, duployan, brahmi, khojki, manichaean, tagbanwa, takri, gujarati, buginese, tai-tham, yi, tagalog, oriya, kayah-li, mende-kikakui, buhid, tamil, gurmukhi, myanmar, khudawadi, mongolian, batak, meetei-mayek, zanabazar-square, bengali, new-tai-lue, rejang, tirhuta, psalter-pahlavi, kharoshthi, osage, music, ahom, canadian-aboriginal, tai-le, nko, kaithi, javanese, adlam, modi, coptic, tibetan, caucasian-albanian, tifinagh, malayalam, telugu, tai-viet, hanifi-rohingya, khmer, armenian, chakma, sogdian, cham, kannada, dogra, soyombo, symbols, bassa-vah, grantha, mandaic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: і́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: і̀ і̂ і̃ і̄ і̆ і̇ і̉ і̊ і̋ і̌ і̍ і̒ і̛̀ і̛́ і̛̂ і̛̃ і̛̄ і̛̆ і̛̇ і̛̉</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Cicipu (Latn, 44,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Dan (Latn, 1,099,244 speakers), Ngbaka (Latn, 1,020,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Vute (Latn, 21,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Teke-Ebo (Latn, 260,000 speakers), Ma’di (Latn, 584,000 speakers), Igbo (Latn, 27,823,640 speakers), Basaa (Latn, 332,940 speakers), Yala (Latn, 200,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Kaska (Latn, 125 speakers), Sar (Latn, 500,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Gulay (Latn, 250,478 speakers), Fur (Latn, 1,230,163 speakers), Ekpeye (Latn, 226,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Lugbara (Latn, 2,200,000 speakers), Koonzime (Latn, 40,000 speakers), Ebira (Latn, 2,200,000 speakers), Zapotec (Latn, 490,000 speakers), Heiltsuk (Latn, 300 speakers), Mundani (Latn, 34,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Han (Latn, 6 speakers), Mfumte (Latn, 79,000 speakers), Aghem (Latn, 38,843 speakers), South Central Banda (Latn, 244,000 speakers), Navajo (Latn, 166,319 speakers).</p>
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




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 21 | 64 | 1153 | 81 | 1029 | 0 | 
| 0% | 0% | 1% | 3% | 49% | 3% | 44% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
