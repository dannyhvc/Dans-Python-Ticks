def puts(num: int) -> None:
    print(bin(num))


def main():
    spam = 0b0000_0000_0000_0000_0000_0000_0000_1010
    eggs = 0b1010_1010_1010_1010_1010_1010_1010_1010
    ham = 0b1111111111
    operation = (eggs << spam) ^ ham
    puts(operation)
    print(operation)

if __name__ == "__main__":
    main()
