
```
A fenced code block. Leave alone.
With a few lines.

{{< current-version >}}

```

Plain text {{< current-version>}}. Both need to be
hard-coded or some other variable scheme.
Whether in a code block or not.

`<angles>` in plain text need to be back-ticked.
<angles> in plain text need to be back-ticked.

Characters '<', '>', need to be transformed to `&lt;` and `&gt;`.

Character sequences '<=' and '=>' need to be transformed to ≤ and ≥.

    ```
        A fenced code block. It ss
        indented. Leave alone.
        With a few lines.

    ```

Plain text

    bog standard
    multi line
    indented code block. Transform to fenced.


     This is only separated from the icb by white
     space. So, still a part of that icb.

Plain text





Previously, a few blank lines. Not an icb.

{{< figure alt="alt text" src="url" >}}
needs to be changed to
![alt text](url)

<http://example.com>
changed to http://example.com

1. list

    This is not an icb.

        But this is an icb!
        another line


        still continuing that icb!

    more text at this level is not an icb.


Back to plain text

    And a bog standard
    icb.

Plain text.

1. list
    1. list

            icb