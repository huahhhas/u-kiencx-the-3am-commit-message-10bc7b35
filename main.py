"""The 3AM Commit Message — one line, written to /output/entry.txt."""

LINE = "fix: the bug was in the code I wrote at 2am to fix the bug I wrote at 1am"


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
