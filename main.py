import io
import os
from contextlib import redirect_stdout

import pylint.lint
from actions_toolkit import core


def main():
    path = core.get_input('path')
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            pylint.lint.Run([path])
    except SystemExit as exit:
        if exit.code != os.EX_OK:
            core.error(f.getvalue())
        else:
            core.info(f.getvalue())
    except:
        core.set_failed('An unknown error occurred.')


if __name__ == "__main__":
    main()
