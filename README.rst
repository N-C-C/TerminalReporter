=====================
  Terminal Reporter
=====================
-----
About
-----
Terminal Reporter is a lightweight console report formatting tool for tabular data.  It can either write to a file or to the terminal (via stdout).

-----
Getting Started
-----
Importing the module:
>>> import TerminalWriter
Creating a title:

>>> import TerminalWriter
Creating a title:

>>> import writer
Creating a title:
>>> print(writer.title_generator("Sample Title", 10))
======================
     Sample Title
======================
Creating the layout for the columns, in this case both columns have a width of 10:
>>> writer.column_generator([10, 10])
'{: <10}{: <10}\n'
Also use the column_generator with format to create a column header:
>>> writer.column_generator([10, 10]).format("column1", "column2")
'column1   column2   \n'
Generating a report is using a combination of the functions mentioned about and a list of lists:
>>> data = [["hello", "world"],
...         ["goodbye", "world"]]
>>> report = writer.generate_report(writer.title_generator("hello world", 20),
...                                        writer.column_generator([10, 10]).format("col1", "col2"),
...                                        writer.column_generator([10, 10]),
...                                        data)
>>> print(report)
===============================
          hello world
===============================
col1      col2
=====================

hello     world
goodbye   world

If you want to save a report to disk, specify file_name for the display_report or leave it set to None (the default) to write it out to the console:
>>> writer.display_report(report, file_name=None)
===============================
          hello world
===============================
col1      col2
=====================

hello     world
goodbye   world
