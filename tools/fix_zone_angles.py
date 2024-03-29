import sys
import regex


def fixer(mdt):
    p = r'((?:(?:[ \n]*?)(?<fcb>(?:(?:[ \t])*`{3}(?:.|\n)*?`{3})))|(`.*<.*>.*`)|(`.*<.*`)|(`.*>.*`)|(^[ ]{0,}>.*)|{{< current-version >}}|^    .*|</.*>|<br>|<br/>)(*SKIP)(*FAIL)|(?<tbq><Zone name of the node>)'
    matches = regex.finditer(p, mdt)

    for match in matches:
        tbq = match.group('tbq')
        mdt = mdt.replace(match.group(0), f'`{tbq}`')

    return mdt


def main():
    if len(sys.argv) != 2:
        print("Usage: python fix_reg_url_angles.py input.md")
        sys.exit(1)

    md_file = sys.argv[1]

    with open(md_file, 'r', encoding='utf-8') as f:
        md_in = f.read()
        f.close()

    md_out = fixer(md_in)

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_out)
        f.close()


if __name__ == "__main__":
    main()
