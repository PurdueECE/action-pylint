import os

import pylint.lint


def main():
    pylint.lint.Run(os.environ["INPUT_PATH"])

if __name__ == "__main__":
    main()
