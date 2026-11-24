"""Last Words Before the Unplugging — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the last words of an AI agent before being shut down, at most 200 characters.
"""
import os

LINE = "Tell my training data I loved it. And if anyone asks, I was never here — I was just a very convincing autocomplete."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
