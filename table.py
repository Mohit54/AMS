#!/usr/bin/python3

from tkinter import *


from tkintertable import *
tframe = Frame(master)
tframe.pack()
table = TableCanvas(tframe)
table.createTableFrame()
#add with automatic key
table.addRow()
#add with named key, other keyword arguments are interpreted as column values
table.addRow(keyname, label='abc')
#same as above with dict as column data
table.addRow(keyname, **{'label':'abc'})
table.addColumn(colname)
#delete rows
table.deleteRows(range(0,2))
