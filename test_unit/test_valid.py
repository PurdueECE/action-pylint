import os
from unittest import mock
from main import main

@mock.patch.dict(os.environ, {
    "INPUT_PATH": "../test_data/valid"
    })
def test_valid():
    main()