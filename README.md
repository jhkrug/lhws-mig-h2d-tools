## lhws-mig-h2d-tools

Longhorn website migration, Hugo -> Docusaurus

Apply these steps in order to provide the required fixes. The ordering helps by
fixing things that might complicate further steps.

1. Uses of `<br>` changed to `<br/>`. 48 occurrences.

1. Isolated instances of `<`, `>`, `>=`, and `<=` changed to `&lt;`, `&gt;`,
utf-8 equivalents, ≤ and ≥. About 32 occurrences.

1. Change `{{< current-version >}}` to whatever the solution is, it's needed
before the next steps as some are inside links or code blocks. The interim
solution is to replace all occurrences with the hardcoded value corresponding to
the directory. There are currently 948 occurrences, 932 are
`v{{< current-version>}}`.
The remaining 16 appear to be internal links in very early versions.

1. Image includes `{{< figure .... >}}` to be changed to `![]()` format. (fig2img.py). 826 occurrences.

1. Indented code blocks changed to fenced code blocks. (i2f_cb.py). Indented
code blocks are painful. What ends an indented code block? It appears that a new
line is not always regarded as being the end of a code block if the line after
that is indented. Or the new lines follow a list. Or possibly something else.
So, searching for indented code blocks is giving a lot of false positives. Will
the false positives all have to be manual edits to resolve? Look in
`outputs/icb.txt`.

1. `` `<http://example.com>` `` to be changed to `http://example.com`

1. `<text>` changed to `` `<text>` `` but only after the previous step.

1. Some weird multi backticks in `outputs/too-many-backticks`.

Still need to check lists, bulleted and numbered and table rendering.

