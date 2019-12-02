import re

re_MARKER = re.compile(r"\((\d+)x(\d+)\)")


def decompressed_length(text, version, return_text=False):
    pos = 0
    text_length = 0
    decompressed_text = []
    while pos < len(text):
        result = re_MARKER.search(text, pos)
        if result:
            no_chars = int(result.group(1))
            no_repeat = int(result.group(2))
            text_length += result.start() - pos
            decompressed = text[result.end():result.end() + no_chars]

            if return_text:
                decompressed_text.append(text[pos:result.start()])
                decompressed_text.append(decompressed * no_repeat)

            if version == 1:
                text_length += len(decompressed) * no_repeat
            else:
                text_length += decompressed_length(decompressed, version) * no_repeat
            pos = result.end() + no_chars
        else:
            if return_text:
                decompressed_text.append(text[pos:])
            text_length += len(text) - pos
            pos = len(text)
    if return_text:
        return "".join(decompressed_text)
    return text_length


if __name__ == '__main__':
    with open('../../../data/2016/input.9.txt', 'r') as fh:
        text = fh.readlines()[0].strip()
    print("Decompressed length:", decompressed_length(text, 1))
    print("Decompressed length v2:", decompressed_length(text, 2))
