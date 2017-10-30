import pyperclip
#melt bulk of keywords into strings with specifyed length

raw = pyperclip.paste().lower()
raw = raw.replace(",", " ")
raw = " ".join(raw.split())

def split_to_len(raw, length):
    lines = [[],[],[],[],[]]
    words = sorted(set(raw.split(" ")), key=raw.split(" ").index)
    line_index = 0
    out = ""
    for w in words:
        if len(out + w) <= length:
            out = out + w + " "
        else:
            lines[line_index] = out[0:-1]
            out = w + " "
            line_index += 1
        lines[line_index] = out[0:-1]

    for l in lines:
        print(l)

split_to_len(raw, 1000)

