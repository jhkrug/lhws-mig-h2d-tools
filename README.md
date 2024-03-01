## lhws-mig-h2d-tools

Longhorn website migration, Hugo -> Docusaurus

Apply these steps in order to provide the required fixes. The ordering helps by
fixing things that might complicate further steps.

1. Uses of `<br>` changed to `<br/>`. 48 occurrences.

1. Isolated instances of `<`, `>`, `>=`, and `<=` changed to `&lt;`, `&gt;`,
utf-8 equivalents, ≤ and ≥. About 32 occurrences. `<=` and `>=` can be automated.

1. Lots of instances of the `>` prefix type admonitions, needs replacing with Docusaurus admonitions.
Or maybe just ignore them until after the migration and then clean them up.

1. Change `{{< current-version >}}` to whatever the solution is, it's needed
before the next steps as some are inside links or code blocks. The interim
solution is to replace all occurrences with the hardcoded value corresponding to
the directory. There are currently 948 occurrences, 932 are
`v{{< current-version>}}`.
The remaining 16 appear to be internal links in very early versions.

    What options are there?

    - Replace all occurrences with hard-code strings based on the directory path.
    This is easy.
    Creating a new versioned_docs would be a little harder than it currently is.
    Presumably a directory is copied to create the new version.
    All occurrences of the old version number would have to be replaced with the new version number.
    I would expect that there will be occurrences where this would be unwise.
    - Have the version number in the front-matter in each markdown file.
    This can then be referenced as `{frontMatter.docVersion}`, for example.
    Doesn't work in markdown code blocks.
    Does work in HTML `<code>` blocks but that creates another set of problems. It's mostly OK for inline blocks but multiline fenced blocks would be a pain, lots of `<br/>`s needed and syntax coloring is not possible (I think).
    Anyway, use of HTML in markdown is to be discouraged,
    - Searching indicates there are some under-the-hood ways in which it may be possible to do this in Docusaurus.
    I currently have insufficient knowledge to suggest a solution.
    - Introduce a macro processor, such a `m4` to do the job the handlebars templating was doing.
    It's possibly a good solution. So, replace all `{{< current-version >}}` with for example `lhv_CurrentVersion_lhv`. Then a `m4` command

      `m4 -D lhv_CurrentVersion_lhv='1.2.3' <filename>`

    does the job. It's how to integrate this with CI pipelines and the current build tools.
    - Aha! Preprocessor in `docusaurus.config.js` works! Something like this:

    ```javascript
    markdown: {
      preprocessor: ({filePath, fileContent}) => {
        // The regex extracts a version number that is being used as a part of
        // directory name. The assumption is that versions numbers are
        // '/n.n.n/' format. There must be at least one number.
        // Valid examples: /1/ /1.1/, /123.456.789/, /1.2.3.4.5.6/
        // Invalid: /1.2-dev/, /1.2rc3/
        // Trying to keep it simple for our use case in Longhorn.
        const regex = /\/(?<vno>(?:[0-9]{1,}\.{0,1})*)\//gm;
        var fp = filePath;
        var fc = fileContent;
        var cCV = '2.3.4';
        for (const match of fp.matchAll(regex)) {
          fc = fc.replace(/{{< current-version >}}/g, `${match.groups.vno}`);
        }
        // The next line ensures that any use of {{< current-version >}}
        // outside a versioned directory will be replaced with the default
        // cCV (currentCurrentVersion). If the next line is commented out then
        // the build fails if it finds any such. Which might be what you
        // need.
        fc = fc.replace(/{{< current-version >}}/g, cCV);
        fc = fc.replace(/lhv_fp_lhv/g, fp);
        return fc;
      },
    },
    ```
    - Also, angle brackets in indented code blocks don't work. The icb must be changed to a fenced code block.
    - Lot's of weird internal errors generated in examples.md files. Fix by surrounding by ``. Can be automated? Need to fix in the versioned_docs to see if they work.
    - Need `slug: /` in `what-is-longhorn.md`.
    - Will need lots of `_category_.json` to be inserted to make for a clean and ordered sidebar. These can be automated.

    The best current solution would be to use the Docusaurus preprocessor facility.

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
Do we need to avoid any 'valid' HTML in the markdown?

1. Some weird multi backticks in `outputs/too-many-backticks`.

1. Frontmatter `weight:` corresponds to `sidebar_position:` in Docusaurus.

Still need to check lists, bulleted and numbered and table rendering. No real problems anticipated.

## Versioned docs

This is going to be difficult.
For each versioned_docs subdirectory a versioned_sidebars sidebars.js needs to exist.
As far as I know that versioned_sidebars/version-sidebar.js file can only be generated by the standard process for creating a versioned_docs cut. i.e. `yarn docusaurus docs:version 1.1.1`.
I think this means that each existing version of the Longhorn docs will have to be copied to the Docusaurus docs directory,
all fixed for build, necessary ordering and `_category_.json` files in place,
 and then the docs:version command tagging done to generate the versioned_docs and the versioned_sidebar file.

## Important steps

- Get some PR's raised to fix the easy things like:
  - figures includes to standard markdown
  -

## Other things

- Google Analytics


## LH internal links

../something -> ./something
../../something > ../../something - so stays the same