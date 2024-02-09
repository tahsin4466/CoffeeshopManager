from flask import *
import sqlite3
import os
from random import randint

app = Flask(__name__)
secret = os.urandom(12)
app.config['SECRET_KEY'] = secret
adminAcc = {'email': 'admin@example.com', 'password': 'mysecurepassword'}

def changeBackground():
    return "go you"


@app.route("/", methods=["GET", "POST"])
def main():
    '''
    This is the root directory (main page users will see when they go to the URL) 
    IF the customer is logged in, this should redirect to the customerView.
    IF admin is logged in, this should redirect to the adminView.
    IF no one is logged in, then it should redirect to the customer login.
    Note that to log in as an admin you must use the /admin route'''
    if 'admin' in session:
        return redirect('/adminMenu')
    elif 'admin' in session:
        return redirect('/adminOrder')
    elif 'user' in session:
        return redirect('/customerView')
    else:
        return redirect('login')

@app.route('/bgdef')
def bgdef():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    return (bgurl)

@app.route('/admin', methods=["GET", "POST"])
# this is the admin login. You do not need to modify this code (unless you want to)
def adminLogin():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        # check to see that both were not empty
        if not email or not password:
            return redirect('admin')
        # check to see they match admin account
        if email == adminAcc['email'] and password == adminAcc['password']:
            session['logged_in']= True
            admin = adminAcc['email']
            session['admin'] = admin
            print('all tests passed. Trying to see page')
            return redirect('/adminMenu')
        else:
            return redirect('/')
    return render_template('adminLogin.html', bgurl=bgurl)


@app.route('/login', methods=["GET", "POST"])
# this is the customer login. You do not need to modify this code. 
def login():
    string = changeBackground()
    print(string)
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    if request.method=="POST":
        # get the form data
        email = request.form['email']
        password = request.form['password']
        # find the user that has this email
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        result = cursor.execute("SELECT * FROM customers WHERE email = ?", (email,)).fetchone()
        user=result[0]
        # check to see if user exists
        if user:
            # check to see that password matches
            if password == result[4]:
                # password matches, log user in to session
                session['logged_in'] = True
                # save the user id to the session variable called 'user' - this can be accessed elsewhere if needed
                session['user'] = user
                return redirect('/')
        return redirect('login')
    return render_template('customerLogin.html', bgurl=bgurl)

@app.route('/logout')
# this removes all session data, whether logged in as customer or admin
def logout():
    session.pop('user', None)
    session.pop('logged_in', None)
    session.pop('admin', None)
    return redirect('/')

@app.route('/customerView')
def customerView():
    if 'user' in session:
        # TO DO - customer view

        return render_template('customerView.html')
    else:
        return redirect('/')

@app.route('/adminOrder')
#route for the order screen
def adminOrder():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    #when connecting, if the admin is in session it will get all of the required info for order displaying
    if 'admin' in session:
        #connect to db
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        #execute SQL for the orderList to be displayed in the table
        orderList = cursor.execute("SELECT customers.firstName, customers.lastName, orders.timestamp, orders.paid, orders.orderTotal, orders.orderExtras, orders.orderLocation, items.name, orders.id FROM (((customers INNER JOIN orders ON orders.customerID = customers.id) INNER JOIN orderItems ON orderItems.orderID = orders.id) INNER JOIN items ON orderItems.itemID = items.id) ORDER BY orders.id ASC;").fetchall()
        #SQL statement that just gets the names for the items for the dropdown search. Because the orderList
        #SQL statement inner joins tables, this is here just to provide all the unique item names
        itemList = cursor.execute("SELECT name FROM items").fetchall()
        #print lists for error checking
        print(orderList)
        print(itemList)
        #return the template and assign each list with the jinja counterpart
        return render_template('adminOrder.html', orderList=orderList, itemList=itemList, bgurl=bgurl)
    else:
        return redirect('/admin')

@app.route('/adminMenu')
#route for the menu / summary screen
def adminMenu():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    #when connecting, if the admin is in session it will retrieve all required data for the screen
    if 'admin' in session:
        #connect to the database
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        #menuList compiles all items and their info for display as a menu
        menuList = cursor.execute("SELECT name, category, price, totalQty, id, itemProfit FROM items ORDER BY totalQty DESC").fetchall()
        profitableList = cursor.execute("SELECT name, itemProfit FROM items ORDER BY itemProfit DESC").fetchall()
        #customerList is for the retrieval of all customer names inner joined with their orders. This is
        #for the best customer and no. of unpaid customers. It uses the exact same query as orderList to ensure consistency
        customerList = cursor.execute("SELECT customers.firstName, customers.lastName, orders.orderTotal, orders.paid FROM customers INNER JOIN orders ON customers.id = orders.customerID ORDER BY orders.orderTotal DESC;").fetchall()
        #expenseList to display all expenses 
        expenseList = cursor.execute("SELECT id, name, amount, information FROM expenses ORDER BY amount DESC").fetchall()
        #print both lists for error checking
        print(menuList)
        print(customerList)
        #in each of these next 8 lines, certain items from tuples are organised into lists for easier sorting
        #the first one organises all order payments
        totalPriceList = [lis[2] for lis in menuList]
        #organises all quanitities of items for summation
        totalQtyList = [lis[3] for lis in menuList]
        print(totalQtyList)
        #organises all items in order of qtySold for best sellers
        sellerList = [lis[0] for lis in menuList]
        #organised all items for profit calculations to be zipped
        profitList = [lis[5] for lis in menuList]
        profitableItemsList = [lis[0] for lis in profitableList]
        #organises all expense values to be summed
        expensesList = [lis[2] for lis in expenseList]
        #retrieves the first name, last name of each customer from each order sorted by the highest total paid
        bestCustomerListFname = [lis[0] for lis in customerList]
        bestCustomerListLname = [lis[1] for lis in customerList]
        bestCustomerTotalList = [lis[2] for lis in customerList]
        #organises all order status' as "yes" or "no" to determine who has not paid
        unpaidCustomersList = [lis[3] for lis in customerList]
        #these next five simply require one value from the organised list. Their SQL statements pre-sort them on a certain value (e.g. totalQty)
        #this retrieves the best seller (first in the list as sorted by highest qty)
        bestseller = sellerList[0]
        #retrieves worst seller (last value)
        worstseller = sellerList[-1]
        #retrieves the first and last name alongside the total of the highest paying order
        bestcustomerfname = bestCustomerListFname[0]
        bestcustomerlname = bestCustomerListLname[0]
        bestcustomertotal = bestCustomerTotalList[0]
        #the next five statistics involve sums; the sum of all quantities, the sum of all payments, the sum of all profits, sum of food expenses and other expenses
        #loop through all expense values per item for a total profit value before zipping into tuples
        totalexpenses = 0
        totalexpensesindex = 0
        for i in expensesList:
            totalexpenses = int(totalexpenses) + int(expensesList[int(totalexpensesindex)])
            totalexpensesindex = totalexpensesindex + 1
        totalexpenses = round((totalexpenses), 2)
        print(totalexpenses)
       
        foodexpenses = 0
        foodexpensesindex = 0
        for i in menuList:
            foodexpenses = foodexpenses + (((totalPriceList[int(foodexpensesindex)])-(profitList[int(foodexpensesindex)])) * totalQtyList[int(foodexpensesindex)])
            foodexpensesindex = foodexpensesindex + 1
        foodexpenses = round((foodexpenses), 2)
        print(foodexpenses)
        #totalprice is being added here, with the total set to 0 and the index set to 0 (first value)
        totalprice = 0
        priceindex = 0
        #loops through all items in the totalPriceList
        for i in totalPriceList:
            #adds new price of item to the total using the priceindex
            totalprice = totalprice + (totalPriceList[int(priceindex)]*totalQtyList[int(priceindex)])
            #priceindex is increased by one to retrieve the next value upon looping
            priceindex = priceindex + 1 
        #prints totalprice (error checking)
        totalprice = round((totalprice), 2)
        print(totalprice)
        #same thing happens here for quantity. It is the exact same logic but with different data and variables
        totalqty = 0
        qtyindex = 0
        for i in totalQtyList:
            totalqty = totalqty + totalQtyList[int(qtyindex)]
            qtyindex = qtyindex + 1 
        print(totalqty)
        #the second last requires the multiplication of total profits by their quantities sold for a profit summation
        #declare a list to hold all total profit values per item and an index
        profitsList = []
        profitsindex = 0
        #loop through all items in the profitList (list with individual profits per item)
        for i in profitList:
            #adds an items total profit by multiplying its profit value with the quantity sold
            profitsList.append(profitList[int(profitsindex)]*totalQtyList[int(profitsindex)])
            #profit is increased by one to retrieve the next value upon looping
            profitsindex = profitsindex + 1 
        #loop through all profit values per item for a total profit value before zipping into tuples
        totalprofits = 0
        totalprofitsindex = 0
        for i in profitList:
            totalprofits = totalprofits + profitsList[int(totalprofitsindex)]
            totalprofitsindex = totalprofitsindex + 1
        totalprofits = round((totalprofits), 2)
        print(totalprofits)
        profitableitem = profitableItemsList[0]
        #zip together all profits together with their respective item names to be displayed in the graph
        profitsList = list(zip(profitsList, sellerList))
        #print the final list (error checking)
        print(profitsList)
        #the final statistic sums all people who have not paid, or adds the number of "No"'s in the list
        #sets the sum and index to 0
        totalunpaid = 0
        unpaidindex = 0
        #loops through all values in the list
        for i in unpaidCustomersList:
            #a temporary variable holds the item ("Yes" or "No")
            unpaidvar = unpaidCustomersList[int(unpaidindex)]
            #if that item says "No", it is added to the tally
            if unpaidvar == "No":
                totalunpaid = totalunpaid + 1
            #if it doesn't say no (says "Yes"), nothing is added
            else:
                pass
            #index rises by one to read next value
            unpaidindex = unpaidindex + 1
        #print final value (error checking)
        print(totalunpaid)
        netprofit = float((totalprice)-(float(totalexpenses)+float(foodexpenses)))
        netprofit = round((netprofit), 2)
        sumexpenses = float(foodexpenses+totalexpenses)
    if 'admin' in session:
        #return the template to adminMenu.html with all the statistics, the menuList and the itemList
        return render_template('adminMenu.html', menuList=menuList, totalprice=totalprice, totalqty=totalqty, bestseller=bestseller, worstseller=worstseller, bestcustomerfname=bestcustomerfname, bestcustomerlname=bestcustomerlname, bestcustomertotal=bestcustomertotal, totalunpaid=totalunpaid, expenseList=expenseList, profitsList=profitsList, totalprofits=totalprofits, totalexpenses=totalexpenses, foodexpenses=foodexpenses, netprofit=netprofit, profitableitem=profitableitem, sumexpenses=sumexpenses, bgurl=bgurl)
    else:
        return redirect('/admin')

@app.route('/delete/<int:id>')
#app route for deleting an item from the menu. The id is provided by the jinja route
def delete(id):
    #connects to the database
    db = sqlite3.connect('coffeeshop.db')
    cursor = db.cursor()
    #prints the id of the item to be deleted (error checking)
    print(id)
    #updates the menuList to delete the item with the given id. ? are used to protect against SQL injection
    cursor.execute("DELETE FROM items WHERE id=?", (id,)).fetchall()
    #commits results and closes database
    db.commit()
    db.close()
    #redirects to /adminMenu root to retrieve the menuList again and to refresh the page
    if 'admin' in session:
        return redirect('/adminMenu')
    else:
        return redirect('/admin')

@app.route('/update/<status>/<int:id>')
#app route to update the status of an order. The id of the order and the current status are given
def update(status, id):
    #connects to the database
    db = sqlite3.connect('coffeeshop.db')
    cursor = db.cursor()
    #if the current status is yes, the admin is assumed to be undoing the confirmation. It sets the status back to "No"
    if status == "Yes":
        cursor.execute("UPDATE orders SET paid ='No' WHERE id=?", (id,)).fetchall()
    #if not "Yes", the order at id is update to "Yes" to confirm payment
    else:
        cursor.execute("UPDATE orders SET paid='Yes' WHERE id=?", (id,)).fetchall()
    #commits the data and closes the database
    db.commit()
    db.close()
    #redirects to /adminOrder to retrieve orderList and reload the page
    if 'admin' in session:
        return redirect('/adminOrder')
    else:
        return redirect('/admin')

@app.route('/adminMenuInsert', methods=["GET", "POST"])
#app route to insert new items into the menu. Uses POST requests
def adminMenuInsert():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    #when the method is called via a POST request...
    if request.method == "POST":
        #temporary variables store the jinja variable values for injection into the SQL statement. These variables outline
        #the fields for the menu, except the id as that autoincrements
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        profit = request.form['profit']
        #connects to the database
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        #inserts new items into the database through the temporary variables
        cursor.execute("INSERT INTO items(name, price, category, totalQty, itemProfit) VALUES (?, ?, ?, 0, ?)", (name, price, category,profit)).fetchall()
        #commits the values and closes the database
        db.commit()
        db.close
     
    #loads the webpage if the admin is in session
    if 'admin' in session:
        return render_template('adminMenuInsert.html', bgurl=bgurl)
    else:
        return redirect('/admin')

#performs same functionality as inserting, except the id is given by the field select
@app.route('/adminMenuUpdate', methods=["GET", "POST"])
def adminMenuUpdate():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    if request.method == "POST":
        name = request.form['nameu']
        price = request.form['priceu']
        category = request.form['categoryu']
        idu = request.form['idu']
        profitu = request.form['profitu']
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        cursor.execute("UPDATE items SET name=?, price=?, category=?, itemProfit=? WHERE id=?", (name, price, category, idu, profitu)).fetchall()
        db.commit()
        db.close
   
    if 'admin' in session:
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        idList = cursor.execute("SELECT id FROM items").fetchall()
        print(idList)
        return render_template('adminMenuUpdate.html', idList=idList, bgurl=bgurl)
    else:
        return redirect('/admin')


@app.route('/adminOrderSearch', methods=["GET", "POST"])
#app route for searching by name in the order list
def adminOrderSearch():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    #when the method is called via a POST request...
    if request.method == "POST":
        #stores the search query as a temporary value 
        ordername = request.form['ordername']
        #connects to the database
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        #searches all orders in the orginal orderList SQL statement, with a WHERE clause filtering by
        #the search query. SQL injection attacks are protected against with the ?
        orderList = cursor.execute("SELECT customers.firstName, customers.lastName, orders.timestamp, orders.paid, orders.orderTotal, orders.orderExtras, orders.orderLocation, items.name, orders.id FROM (((customers INNER JOIN orders ON orders.customerID = customers.id) INNER JOIN orderItems ON orderItems.orderID = orders.id) INNER JOIN items ON orderItems.itemID = items.id) WHERE customers.firstName=? ORDER BY orders.id ASC;", (ordername,)).fetchall()
        #the item list is refreshed to ensure the dropdown works after reidrect
        itemList = cursor.execute("SELECT name FROM items").fetchall()
    #returns the user back to the admin order page with the two lists and the constrained order list if admin is in session
    if 'admin' in session:
        return render_template('adminOrder.html', orderList = orderList, itemList=itemList, bgurl=bgurl)
    else:
        return redirect('/admin')

#performs the exact same functionality as the name search, except the given search query is pre-determined throgh
#the selection fields
@app.route('/adminItemSearch', methods=["GET", "POST"])
def adminItemSearch():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    if request.method == "POST":
        itemsearch = request.form['itemsearch']
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        orderList = cursor.execute("SELECT customers.firstName, customers.lastName, orders.timestamp, orders.paid, orders.orderTotal, orders.orderExtras, orders.orderLocation, items.name, orders.id FROM (((customers INNER JOIN orders ON orders.customerID = customers.id) INNER JOIN orderItems ON orderItems.orderID = orders.id) INNER JOIN items ON orderItems.itemID = items.id) WHERE items.name=? ORDER BY orders.id ASC;", (itemsearch,)).fetchall()
        itemList = cursor.execute("SELECT name FROM items").fetchall()
    if 'admin' in session:
        return render_template('adminOrder.html', orderList = orderList, itemList=itemList, bgurl=bgurl)
    else:
        return redirect('/admin')

@app.route('/deleteExpense/<int:id>')
#app route for deleting an expense from the menu. The id is provided by the jinja route
def deleteExpense(id):
    #connects to the database
    db = sqlite3.connect('coffeeshop.db')
    cursor = db.cursor()
    #prints the id of the expense to be deleted (error checking)
    print(id)
    #updates the expenseList to delete the item with the given id. ? are used to protect against SQL injection
    cursor.execute("DELETE FROM expenses WHERE id=?", (id,)).fetchall()
    #commits results and closes database
    db.commit()
    db.close()
    #redirects to /adminMenu root to retrieve the menuList again and to refresh the page
    if 'admin' in session:
        return redirect('/adminMenu')
    else:
        return redirect('/admin')

@app.route('/adminExpense', methods=["GET", "POST"])
#app route to insert new items into the expenses. Uses POST requests
def adminExpense():
    bgurl = ""
    backgroundvar = randint(1,5)
    print(backgroundvar)
    if backgroundvar == 1:
        bgurl = "https://images.unsplash.com/photo-1555118367-93f01e18660f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80"
    elif backgroundvar == 2:
        bgurl = "https://i.pinimg.com/originals/e6/a8/4e/e6a84e02efd60d6da7d650c8a7170dd9.jpg"
    elif backgroundvar == 3:
        bgurl = "https://i.ytimg.com/vi/h2zkV-l_TbY/maxresdefault.jpg"
    elif backgroundvar == 4:
        bgurl = "https://www.parisperfect.com/blog/wp-content/uploads/2019/04/Everything-You-Want-To-Know-About-the-Cafe-Terraces-in-Paris-by-Paris-Perfect4.jpg"
    else:
        bgurl = "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9"
    #when the method is called via a POST request...
    if request.method == "POST":
        #temporary variables store the jinja variable values for injection into the SQL statement. These variables outline
        #the fields for the exepnse, except the id as that autoincrements
        name = request.form['name']
        amount = request.form['amount']
        information = request.form['information']
        #connects to the database
        db = sqlite3.connect('coffeeshop.db')
        cursor = db.cursor()
        #inserts new items into the database through the temporary variables
        cursor.execute("INSERT INTO expenses(name, amount, information) VALUES (?, ?, ?)", (name, amount, information,)).fetchall()
        #commits the values and closes the database
        db.commit()
        db.close

    if 'admin' in session:
        return render_template('adminExpense.html', bgurl=bgurl)
    else:
        return redirect('/admin')
#run the app, ensuring debugging is on
app.run(debug=True)