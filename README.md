## lhws-mig-h2d-tools

Longhorn website migration, Hugo -> Docusaurus


Apply these steps in order to provide the required fixes. The ordering helps by fixing things that might complicate further steps.

1. Uses of `<br>` changed to `<br/>`
1. Isolated instances of `<`, `>`, `>=`, and `<=` changed to `&lt;`, `&gt;`, utf-8 equivalents, ≤ and ≥.
1. Change `{{< current-version >}}` to whatever the solution is, it's needed before the next steps as some are inside links or code blocks.
1. Image includes `{{< figure .... >}}` to be changed to `![]()` format. (fig2img.py)
1. Indented code blocks changed to fenced code blocks. (i2f_cb.py)
1. `` `<http://example.com>` `` changed to `http://example.com`
1. `<text>` changed to `` `<text>` `` but only after the previous step.
