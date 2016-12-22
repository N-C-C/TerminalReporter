import os

import TerminalWriter


def test_column_generator():
    layout = TerminalWriter.column_generator([3, 3, 3])
    assert layout == "{: <3}{: <3}{: <3}\n"


def test_title_generator():
    title = TerminalWriter.title_generator("hello world", 15)
    expected_title = ""
    expected_title += "==========================\n"
    expected_title += "       hello world        \n"
    expected_title += "==========================\n"

    assert title == expected_title


def test_generate_report():
    data = [["hello", "world"],
            ["goodbye", "world"]]
    actual_report = TerminalWriter.generate_report(TerminalWriter.title_generator("hello world", 20),
                                                   TerminalWriter.column_generator([10, 10]).format("col1", "col2"),
                                                   TerminalWriter.column_generator([10, 10]),
                                                   data)
    expected_report = ""
    expected_report += "===============================\n"
    expected_report += "          hello world          \n"
    expected_report += "===============================\n"
    expected_report += "col1      col2      \n"
    expected_report += "=====================\n"
    expected_report += "\n"
    expected_report += "hello     world     \n"
    expected_report += "goodbye   world     \n"

    assert actual_report == expected_report


def test_display_report():
    expected_text = "Hello"
    test_file = "foo.txt"
    actual_text = ""
    TerminalWriter.display_report(expected_text, test_file)
    with open(test_file, "r") as in_file:
        actual_text = in_file.readline()
    os.remove(test_file)
    assert actual_text == expected_text + "\n"




