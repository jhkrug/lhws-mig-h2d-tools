Apply these steps in order

1. Uses of `<br>` changed to `<br/>`
1. Isolated instances of `<`, `>`, `>=`, and `<=` changed to `&lt;`, `&gt;`, utf-8 equivalents, ≤ and ≥.
1. Change `{{< current-version >}}` to whatever the solution is.
1. Image includes `{{< figure .... >}}` to be changed to `![]()` format. (fig2img.py)
1. Indented code blocks changed to fenced code blocks. (i2f_cb.py)
1. `` `<http://example.com>` `` changed to `http://example.com`
1. `<text>` changed to `` `<text>` `` but only after the previous step.
