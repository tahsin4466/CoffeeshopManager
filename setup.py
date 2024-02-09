import sqlite3

db = sqlite3.connect('coffeeshop.db')
cursor = db.cursor()
# create the table for coffeeshop products (items)
cursor.execute(''' CREATE TABLE IF NOT EXISTS items (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL,
    price NUMERIC,
    category TEXT);''')
# add a few starter items into the table
cursor.execute("INSERT INTO items (name, price, category) VALUES ('Choc Mud Cake', 3.00, 'Cake')")
cursor.execute("INSERT INTO items (name, price, category) VALUES ('Chicken Avocado & cheese Open Grill Focaccia', 4.00, 'Savoury')")
cursor.execute("INSERT INTO items (name, price, category) VALUES ('Flat White', 2.00, 'Hot Drinks')")
db.commit()

# create a table to hold customers
cursor.execute(''' CREATE TABLE IF NOT EXISTS customers (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    firstName VARCHAR(150) NOT NULL,
    lastName VARCHAR(150) NOT NULL,
    location VARCHAR(100),
    email VARCHAR(150) NOT NULL,
    password VARCHAR(100) NOT NULL);''')
# add a few starter customers
cursor.execute("INSERT INTO customers (firstName, lastName, location, email, password) VALUES ('Mickey', 'Mouse', 'Staff Building', 'mickey@disney.com', 'minniedabesteva')")
cursor.execute("INSERT INTO customers (firstName, lastName, location, email, password) VALUES ('Scooby', 'Doo', 'PAC', 'scooby@snacks.com', 'wheresmyscoobysnacksat')")
cursor.execute("INSERT INTO customers (firstName, lastName, location, email, password) VALUES ('Diana', 'Prince', 'Pick Up', 'wonderwoman@DC.com', 'howdidbrucegetmyemail')")
db.commit()

# create a table for orders. Note that the order total will not be known until products have been added
# on delete cascade means that if the customer is deleted, their orders should also be deleted
cursor.execute(''' CREATE TABLE IF NOT EXISTS orders (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    customerID INTEGER NOT NULL,
    paid INTEGER DEFAULT 0,
    orderTotal NUMERIC,
    FOREIGN KEY (customerID)
        REFERENCES customers (id)
        ON DELETE CASCADE
        );''')
# add a few starter orders. There are three so they should have id's 1, 2, 3
cursor.execute("INSERT INTO orders (timestamp, customerID) VALUES ('2020-08-08 09:14:09.396005', 1)")
cursor.execute("INSERT INTO orders (timestamp, customerID) VALUES ('2020-08-07 09:15:06.634349', 2)")
cursor.execute("INSERT INTO orders (timestamp, customerID) VALUES ('2020-08-07 09:15:42.834529', 2)")
db.commit()

# this is a junction table for ordered items. No primary keys - just foreign keys for items and orderIDs
cursor.execute(''' CREATE TABLE IF NOT EXISTS orderItems (
    itemID INTEGER NOT NULL,
    qty INTEGER NOT NULL,
    orderID INTEGER NOT NULL,
    CONSTRAINT fk_column
    FOREIGN KEY (itemID)
        REFERENCES items (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_column
    FOREIGN KEY (orderID)
        REFERENCES orders(id)
        ON DELETE CASCADE
        );''')
# some sample order data
cursor.execute("INSERT INTO orderItems (itemID, qty, orderID) VALUES (1,1,1)")
cursor.execute("INSERT INTO orderItems (itemID, qty, orderID) VALUES (2,1,1)")
cursor.execute("INSERT INTO orderItems (itemID, qty, orderID) VALUES (3,1,2)")
cursor.execute("INSERT INTO orderItems (itemID, qty, orderID) VALUES (3,1,3)")
cursor.execute("INSERT INTO orderItems (itemID, qty, orderID) VALUES (1,2,3)")

db.commit()


# update price in orders table
results = cursor.execute("SELECT * FROM items INNER JOIN orderItems ON items.ID = orderItems.itemID WHERE orderID = 1").fetchall()
# price is at index 2, qty at index 5
total = 0
for result in results:
    total += (result[2] * result[5])
# update the orders table with this total
cursor.execute("UPDATE orders SET orderTotal = ? WHERE id = 1 ", (total,))
db.commit()

# update price in orders table
results = cursor.execute("SELECT * FROM items INNER JOIN orderItems ON items.ID = orderItems.itemID WHERE orderID = 2").fetchall()
# price is at index 2, qty at index 5
total = 0
for result in results:
    total += (result[2] * result[5])
# update the orders table with this total
cursor.execute("UPDATE orders SET orderTotal = ? WHERE id = 2 ", (total,))
db.commit()

# update price in orders table
results = cursor.execute("SELECT * FROM items INNER JOIN orderItems ON items.ID = orderItems.itemID WHERE orderID = 3").fetchall()
# price is at index 2, qty at index 5
total = 0
for result in results:
    total += (result[2] * result[5])
# update the orders table with this total
cursor.execute("UPDATE orders SET orderTotal = ? WHERE id = 3 ", (total,))
db.commit()
    

# close connection to database
db.close()
