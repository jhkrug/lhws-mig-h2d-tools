import sys
import regex


def i2f_cb(mdt):
    p = r'```(.|\n)*?```(*SKIP)(*FAIL)|(?P<icb>^(?:(?:[ ]{4}|\t).*(\R|$))+)'

    matches = regex.finditer(p, mdt, flags=regex.MULTILINE)

    offset = 0
    for match in matches:
        icb = match.group('icb')
        indented_lines = [line[4:] for line in icb.splitlines()]
        fcb = '```\n' + '\n'.join(indented_lines) + '\n```\n'
        start, end = match.span('icb')
        mdt = mdt[:start + offset] + fcb + mdt[end + offset:]
        offset += len(fcb) - len(icb)

    return mdt


def main():
    if len(sys.argv) != 2:
        print("Usage: python i2f_cb.py input.md")
        sys.exit(1)

    md_file = sys.argv[1]

    with open(md_file, 'r', encoding='utf-8') as f:
        md_in = f.read()
        f.close()

    md_out = i2f_cb(md_in)

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_out)
        f.close()


if __name__ == "__main__":
    main()
