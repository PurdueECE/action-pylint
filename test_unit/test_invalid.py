import os
from unittest import mock
from main import main

@mock.patch.dict(os.environ, {
    "INPUT_PATH": "../test_data/invalid"
    })
def test_invalid():
    main()