import math
import pytest
import os

@pytest.fixture
def testtwo_fixt():
    f1 = "file1.txt"
    f2 = "file2.txt"
    out = "output.txt"

    with open(f1, 'w') as file1:
        file1.write("a ||")

    with open(f2, 'w') as file2:
        file2.write("|| b")

    yield f1, f2, out

    for file_path in [f1, f2, out]:
        if os.path.exists(file_path):
            os.remove(file_path)

def merge_and_write(file1, file2, output):
    try:
        with open(file1, 'r') as f1:
            data1 = f1.read().strip()

        with open(file2, 'r') as f2:
            data2 = f2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output, 'w') as out:
            out.write(merged_data)

        with open(output, 'r') as out:
            data = out.read()
        return data
    except FileNotFoundError:
        return "Error not found ^)"

def test_merge_and_write(testtwo_fixt):
    f1, f2, out = testtwo_fixt

    expected_data = "a || || b"
    assert merge_and_write(f1, f2, out) == expected_data

def test_file_not_found():
    f1 = "not.txt"
    f2 = "file2.txt"
    out = "output.txt"

    assert merge_and_write(f1, f2, out) == "Error not found ^)"
