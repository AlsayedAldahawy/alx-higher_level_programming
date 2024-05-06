#!/usr/bin/python3
append_after = __import__('100-append_after').append_after

filename = "file_0"
text_search = "c"
text_append = "Python is cool!\n"
append_after(filename, text_search, text_append)


# append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
