#35th github projeect --> Character Frequency
print('----------Character Frequency----------')
from collections import Counter


def main():
    text = input("Enter text: ").strip()

    if not text:
        print("Nothing entered.")
        return

    counts = Counter(text.lower())
    total = sum(counts.values())

    for char, count in sorted(counts.items()):
        print(f"'{char}': {count}")
    print(f"Total characters: {total}")



main()