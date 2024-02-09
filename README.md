# CoffeeshopManager

## Overview
This is a simple web application built as a restaurant management system. It contains two sides - a client and admin side. On the client side, users can see the menu and send in order requests. On the admin side, the admin can get live analytics and data on customer orders, as well as the ability to update menus.

This project was built using a Flask backend and an HTML/CSS/JS front-end with Bootstrap 4. It was made as part of a school assignment, specifically 11 DSO FA3. It has not been updated since, and is only here for archiving.

## Installation
Make sure you have the latest version of Python installed (preferabbly 3.12+).

This project requires Flask - a back-end framework for creating web applications. Using pip, run:

```
pip install flask
```

Make sure to have flask configured to:
 - Target the file `app.py`
 - Media/static folder set to `static`
 - Templates folder set to `templates`
   
Then, download this repository. Run the file `setup.py` to initialize the sqlite3 database. Then, run `app.py`. You will see a localhost IP pop up in the terminal. Press the link to open the application in your browser.

If you encounter an internal server error, clear the `database.db` file and run `setup.py` again.

NOTE: This is an archive of a project completed in 2020. It is no longer maintained.

