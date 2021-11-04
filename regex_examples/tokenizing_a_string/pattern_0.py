import re


def main():
    pattern = re.compile(
        r"(\[START\])|"
        r"(\[PUSH\])|"
        r"(\[ADD\])|"
        r"(\[SUB\])|"
        r"(\[[0-9]+(.)??[0-9]*\])|"
        r"(\[POP\])|"
        r"(\[FINISH\])")

    spam = pattern.findall("[PUSH][1000][PUSH][3645][POP][FINISH]")
    eggs = [next(filter(bool, local)) for local in spam]
    print(eggs)


if __name__ == "__main__":
    main()
