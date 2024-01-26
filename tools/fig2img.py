import sys
import regex


def fig2img(mdt):
    p = r'{{<\s+figure\s+(?:(?:(?:alt="(?P<alt>.+?)")\s+)?src="(?P<src>.+?)"(?:\s+alt="(?P<alt2>.+?)")?)?\s*>}}'

    matches = regex.finditer(p, mdt)

    for match in matches:
        alt = match.group('alt') or match.group('alt2') or 'images'
        src = match.group('src')
        mdt = mdt.replace(match.group(0), f'![{alt}]({src})')

    return mdt


def main():
    if len(sys.argv) != 2:
        print("Usage: python fig2img.py input.md")
        sys.exit(1)

    md_file = sys.argv[1]

    with open(md_file, 'r', encoding='utf-8') as f:
        md_in = f.read()
        f.close()

    md_out = fig2img(md_in)

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_out)
        f.close()


if __name__ == "__main__":
    main()
