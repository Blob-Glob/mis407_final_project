import sqlite3

sqlite_file = 'inventory_system.sqlite'    # name of the sqlite database file



conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


#drop table if exists to avoid problems
c.execute("DROP TABLE IF EXISTS {v1}".format(v1="orders"))
# we can simply execute SQL using string literals as follows...
c.execute("CREATE TABLE IF NOT EXISTS orders (ID 'INTEGER' PRIMARY KEY AUTOINCREMENT, item_name 'TEXT', item_price 'REAL', item_quantity 'INTEGER')")
#insert values into table
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"socks"', item_price='"5.99"', item_quantity='"50"'))
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"blue hat"', item_price='"5.59"', item_quantity='"6"'))
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"red hat"', item_price='"49.50"', item_quantity='"10"'))
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"stress potato"', item_price='"45.99"', item_quantity='"43"'))
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"vintage table"', item_price='"15.99"', item_quantity='"4"'))
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"baby toy"', item_price='"55.99"', item_quantity='"4"'))
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"plush dog"', item_price='"95.99"', item_quantity='"9"'))
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"s"', item_price='"0.99"', item_quantity='"5"'))
c.execute('INSERT INTO {tn} VALUES ( NULL, {item_name}, {item_price}, {item_quantity})'.format(tn="orders", item_name='"socks"', item_price='"2.99"', item_quantity='"1"'))

#orders table
#item_upc, item_name, item_price,item quantity, date, customer_id
#inventory table
#item_upc, item_name, item_retail_price, item_wholesale_price, item_quantity, vendor_id

c.execute('SELECT item_name, item_price, item_quantity from orders')

rows = c.fetchall()

for row in rows:
    print(row)



#Here I make the inventory table
c.execute("DROP TABLE IF EXISTS {v1}".format(v1="inventory"))
c.execute("CREATE TABLE IF NOT EXISTS inventory (ID 'INTEGER' PRIMARY KEY AUTOINCREMENT, "
          "item_id 'INTEGER', "
          "item_name 'TEXT',"
          "retail_price 'FLOAT',"
          "buy_price 'FLOAT', "
          "item_quantity 'INTEGER', "
          "upc 'INTEGER', "
          "vendor_id 'INTEGER', "
          "num_item_sold 'INTEGER')")
c.execute('INSERT INTO {tn} VALUES ( NULL,'
          '{item_id}, '
          '{item_name}, '
          '{retail_price},'
          '{buy_price}, '
          '{item_quantity},'
          '{upc},'
          '{vendor_id}, '
          '{num_item_sold})'.format(tn="inventory",
                                      item_id='1',
                                      item_name='"fancy hat"',
                                      retail_price='5.99',
                                      buy_price='1.00',
                                      item_quantity='"50"',
                                      upc='72527273070',
                                      vendor_id='99',
                                      num_item_sold='50'))

c.execute('INSERT INTO {tn} VALUES ( NULL,'
          '{item_id}, '
          '{item_name}, '
          '{retail_price},'
          '{buy_price}, '
          '{item_quantity},'
          '{upc},'
          '{vendor_id}, '
          '{num_item_sold})'.format(tn="inventory",
                                      item_id='2',
                                      item_name='"taco pillow"',
                                      retail_price='25.99',
                                      buy_price='9.00',
                                      item_quantity='"66"',
                                      upc='72527273170',
                                      vendor_id='59',
                                      num_item_sold='484'))

c.execute('INSERT INTO {tn} VALUES ( NULL,'
          '{item_id}, '
          '{item_name}, '
          '{retail_price},'
          '{buy_price}, '
          '{item_quantity},'
          '{upc},'
          '{vendor_id}, '
          '{num_item_sold})'.format(tn="inventory",
                                      item_id='3',
                                      item_name='"signed photo of Guy Helmer"',
                                      retail_price='250.99',
                                      buy_price='1.00',
                                      item_quantity='"5"',
                                      upc='72528273170',
                                      vendor_id='1',
                                      num_item_sold='4'))



c.execute('SELECT * from inventory')
rows = c.fetchall()

for row in rows:
    print(row)


#drop table if exists to avoid problems
c.execute("DROP TABLE IF EXISTS {v1}".format(v1="customer_order"))
# we can simply execute SQL using string literals as follows...
c.execute("CREATE TABLE IF NOT EXISTS customer_order (ID 'INTEGER' PRIMARY KEY AUTOINCREMENT, "
          "item_id 'INTEGER',"
          "item_name 'TEXT', "
          "item_price 'FLOAT',"
          "item_quantity 'INTEGER',"
          "customer_id 'INTEGER',"
          "purchase_date 'DATE')")


c.execute('INSERT INTO {tn} VALUES ( NULL, {item_id},{item_name}, {item_price}, {item_quantity}, {customer_id}, {purchase_date})'
          .format(tn="customer_order",
                  item_id='"1"',
                  item_name='"fancy hat"',
                  item_price='"5.99"',
                  item_quantity='"5"',
                  customer_id='"2"',
                  purchase_date='"2018-12-04"'))

c.execute('INSERT INTO {tn} VALUES ( NULL, {item_id},{item_name}, {item_price}, {item_quantity}, {customer_id}, {purchase_date})'
          .format(tn="customer_order",
                  item_id='"2"',
                  item_name='"taco pillow"',
                  item_price='"25.99"',
                  item_quantity='"1"',
                  customer_id='"23"',
                  purchase_date='"2018-12-03"'))


c.execute('INSERT INTO {tn} VALUES ( NULL, {item_id},{item_name}, {item_price}, {item_quantity}, {customer_id}, {purchase_date})'
          .format(tn="customer_order",
                  item_id='"3"',
                  item_name='"signed photo of Guy Helmer"',
                  item_price='"250.99"',
                  item_quantity='"1"',
                  customer_id='"3"',
                  purchase_date='"2018-12-01"'))


c.execute('SELECT * from inventory')
rows = c.fetchall()

for row in rows:
    print(row)


conn.commit()
conn.close()