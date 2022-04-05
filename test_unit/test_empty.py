import os
import sys
from unittest import mock
from main import main

@mock.patch.dict(os.environ, {
    "INPUT_PATH": "test_data/empty"
    })
def test_empty():
    main()