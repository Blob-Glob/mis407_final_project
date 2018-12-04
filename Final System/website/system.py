import json
from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure

app = Flask(__name__)

# name of the sqlite database file
# name of the table to be queried
sqlite_file = 'inventory_system.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

df = pd.read_sql_query("select * from inventory;", conn)
df2 = pd.read_sql_query("select * from customer_order ;", conn)


@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['password']
    if user == 'admin' and password == 'p':
        return render_template("home.html", user=user)
    return render_template("login.html", content="Invalid ")

@app.route('/login', methods=['GET'])
def login_page():
    return render_template("login.html")


@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html")

def create_figure():
    item_name = df["item_name"]
    item_quantity = df["item_quantity"]

    item_quantity_graph = figure(x_range=item_name, plot_height=250, title="Items on Hand",
                                 toolbar_location=None, tools="")

    item_quantity_graph.vbar(x=item_name, top=item_quantity, width=0.9)

    item_quantity_graph.xgrid.grid_line_color = None
    item_quantity_graph.y_range.start = 0

    return item_quantity_graph

@app.route('/analytics')
def analytics():
    return render_template("analytics.html")

@app.route('/orders', methods=['GET'])
def orders():
    con = sqlite3.connect(sqlite_file)
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM orders")

    rows = cur.fetchall()
    con.close()
    return render_template("orders.html", rows=rows)

@app.route('/order', methods=['DELETE'])
def delete():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    id = json.loads(request.data)['id']
    c.execute('DELETE FROM {tn} WHERE ID = {id}'.format(tn="orders", id=id))
    conn.commit()
    conn.close()
    return "OK"


@app.route('/addrec', methods=['POST', 'PUT'])
def addrec():
    if request.method == 'POST':
        nm = request.form['nm']
        price = request.form['price']
        quantity = request.form['quan']

        conn = sqlite3.connect(sqlite_file)
        cur = conn.cursor()
        query = 'INSERT INTO {tn} VALUES (NULL, "{name}", {price}, {quantity})'.format(tn="orders",
                                                                                       name=nm,
                                                                                       price=price,
                                                                                       quantity=quantity)
        cur.execute(query)
        conn.commit()
        conn.close()
    return redirect('/orders')

@app.route('/inventory', methods=['GET'])
def inventory():
    con = sqlite3.connect(sqlite_file)
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM inventory")

    rows = cur.fetchall()
    con.close()
    return render_template("inventory.html",  rows=rows)

@app.route('/inventory', methods=['DELETE'])
def delete1():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    id = json.loads(request.data)['id']
    c.execute('DELETE FROM {tn} WHERE ID = {id}'.format(tn="inventory", id=id))
    conn.commit()
    conn.close()
    return "OK"

@app.route('/addinv', methods=['POST', 'PUT'])
def addinv():
    if request.method == 'POST':
        item_id = request.form['item_id']
        nm = request.form['nm']
        rprice = request.form['rprice']
        bprice = request.form['bprice']
        quantity = request.form['quantity']
        upc = request.form['upc']
        vid = request.form['vid']
        numsold = request.form['numsold']



        conn = sqlite3.connect(sqlite_file)
        cur = conn.cursor()


        query = 'INSERT INTO {tn} VALUES ( NULL,' \
        '{item_id}, ' \
        '"{item_name}", ' \
        '{retail_price},' \
        '{buy_price}, ' \
        '{item_quantity},' \
        '{upc},' \
        '{vendor_id}, ' \
        '{num_item_sold})'.format(tn="inventory",
                                  item_id=item_id,
                                  item_name=nm,
                                  retail_price=rprice,
                                  buy_price=bprice,
                                  item_quantity=quantity,
                                  upc=upc,
                                  vendor_id=vid,
                                  num_item_sold=numsold)
        print(query)

        cur.execute(query)
        conn.commit()
        conn.close()
    return redirect('/orders')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
