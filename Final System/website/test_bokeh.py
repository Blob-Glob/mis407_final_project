import sqlite3
import pandas as pd
from bokeh.io import show, output_file
from bokeh.plotting import figure
import numpy as np


output_file("analytics.html")
sqlite_file = 'inventory_system.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

df = pd.read_sql_query("select * from inventory;", conn)
df2 = pd.read_sql_query("select * from customer_order ;", conn)


# #items on hand
# item_name = df["item_name"]
# item_quantity = df["item_quantity"]
#
# item_quantity_graph = figure(x_range=item_name, plot_height=250, title="Items on Hand",
#            toolbar_location=None, tools="")
#
# item_quantity_graph.vbar(x=item_name, top=item_quantity, width=0.9)
#
# item_quantity_graph.xgrid.grid_line_color = None
# item_quantity_graph.y_range.start = 0

# show(item_quantity_graph)

#items sold
item = df2["item_name"]
date = df2["purchase_date"]
quantity = df2["item_quantity"]
sales = df2["item_price"]
sales_cash = sales*quantity
# output_file("line.html")
#
# order_graph = figure(x_range=date, plot_height=250, title="Items on Hand",
#            toolbar_location=None, tools="")
#
# order_graph.vbar(x=date, top=quantity*sales, width=0.9)
#
# order_graph.xgrid.grid_line_color = None
# order_graph.y_range.start = 0
#
# show(order_graph)
XArray= date.as_matrix(columns=None)
YArray= sales_cash.as_matrix(columns=None)
print(type(YArray))
# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(XArray, YArray, legend="Temp.", line_width=2)

# show the results
show(p)


print(type(sales))
print(type(sales))

# print(item)
# print(date)
# print(quantity)
