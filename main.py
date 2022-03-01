import os

import pylint.lint


def main():
    path = os.environ["INPUT_PATH"]
    pylint.lint.Run([path])

if __name__ == "__main__":
    main()
