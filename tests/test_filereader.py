import pytest
import pathlib
from rtframework.utils.filereader import read

def test_read_text_file():
    expected = "Hello World!\nExtra"
    cwd = pathlib.Path.cwd()
    test_file = cwd / "tests" / "mockfile.txt"
    decoded_file = read(test_file)
    assert(expected == decoded_file)
