import mysql.connector
from mysql.connector import errorcode
from lib import *

_settings = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "web_shop",
}

cnx = mysql.connector.connect(**_settings)
cursor = cnx.cursor()

def connect():
    log("load", "Connecting to database...")
    try:
        cnx = mysql.connector.connect(**_settings)
        Create_tables(cnx, cursor)
        log("scss", "Connection to database successful")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            log("err", "Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            log("err", "Database does not exist yet")
        else:
            log("err", err)

def Create_tables(cnx, cursor):
    log("load", "Creating tables...")
    try:
        with open("database.sql", "r") as file:
            sql = file.read()
            cursor.execute(sql, multi=True)
            cnx.commit()
        log("scss", "Tables created successfully")
    except mysql.connector.Error as err:
        log("err", err)

def Register(user):
    username = user.username
    email = user.email
    password = user.password

    checkEmail = "SELECT * FROM users WHERE email = %s"
    cursor.execute(checkEmail, (email,))
    result = cursor.fetchall()

    if len(result) > 0:
        log("err", "Email already exists")
        return False
    else:
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, email, password))
        cnx.commit()
        log("scss", "User registered successfully")
        return True

def Login(user):
    username = user.username
    password = user.password

    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchall()

    if len(result) > 0:
        log("scss", "Login successful")
        return True, result[0]
    else:
        log("err", "Login failed")
        return False

def Get_users():
    sql = "SELECT users.id,username,email,users_types.label AS `type` FROM users INNER JOIN users_types ON users.user_type = users_types.id"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def Get_user(id):
    sql = "SELECT users.id,username,email,users_types.label AS `type` FROM users INNER JOIN users_types ON users.user_type = users_types.id WHERE users.id = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchall()
    return result

def Update_user(user):
    id = user.id
    username = user.username
    email = user.email

    sql = "UPDATE users SET username = %s, email = %s WHERE id = %s"
    cursor.execute(sql, (username, email, id))
    cnx.commit()
    log("scss", "User updated successfully")

def Change_password(user):
    id = user.id
    password = user.password

    sql = "UPDATE users SET password = %s WHERE id = %s"
    cursor.execute(sql, (password, id))
    cnx.commit()
    log("scss", "Password changed successfully")

def Get_user_types():
    sql = "SELECT id,label FROM users_types"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def Get_products():
    sql = "SELECT products.id,products.name,products.description,products.price,catalog.label AS `catalog` FROM products INNER JOIN catalog ON products.catalog = catalog.id WHERE products.`status` = 1 ORDER BY products.name ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def Get_products_by_catalog(catalog):
    sql = "SELECT products.id,products.name,products.price,catalog.label AS `catalog` FROM products INNER JOIN catalog ON products.catalog = catalog.id WHERE products.`status` = 1 AND catalog.id = %s ORDER BY products.name ASC"
    cursor.execute(sql, (catalog,))
    result = cursor.fetchall()
    return result

def Get_products_ocults():
    sql = "SELECT products.id,products.name,products.price,catalog.label AS `catalog` FROM products INNER JOIN catalog ON products.catalog = catalog.id WHERE products.`status` = 0 ORDER BY products.name ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def Get_product(id):
    sql = "SELECT products.id,products.name,products.description,products.price,catalog.label AS `catalog` FROM products INNER JOIN catalog ON products.catalog = catalog.id WHERE products.id = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    return result

def Update_product(product):
    id = product.id
    name = product.name
    description = product.description
    price = product.price
    catalog = product.category

    sql = "UPDATE products SET name = %s, description = %s, price = %s, catalog = %s WHERE id = %s"
    cursor.execute(sql, (name, description, price, catalog, id))
    cnx.commit()
    log("scss", "Product updated successfully")

def Get_catalog():
    sql = "SELECT id,label FROM catalog"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def Delete_product(id):
    sql = "UPDATE products SET status = 0 WHERE id = %s"
    cursor.execute(sql, (id,))
    cnx.commit()
    log("scss", "Product deleted successfully")

def Insert_product(product):
    name = product.name
    description = product.description
    price = product.price
    catalog = product.category

    sql = "INSERT INTO products (name, description, price, catalog) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, description, price, catalog))
    cnx.commit()
    log("scss", "Product added successfully")

def Create_invoice(user_id, cart):
    sql = "INSERT INTO invoice_header (user_id) VALUES (%s)"
    cursor.execute(sql, (user_id,))
    cnx.commit()
    log("scss", "Invoice created successfully")

    sql = "SELECT id FROM invoice_header WHERE user_id = %s ORDER BY id DESC LIMIT 1"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchall()
    invoice_id = result[0][0]
    line = 0
    for item in cart:
        line += 1
        sql = "INSERT INTO invoice_detail (id_invoice, id_line, id_product, quantity) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (invoice_id, line, item[0], item[5]))
        cnx.commit()
    log("scss", "Invoice detail created successfully")

def Get_invoices_by_user(user_id):
    sql = "SELECT id,`time` FROM invoice_header WHERE user_id = %s ORDER BY id DESC"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchall()
    return result

def Get_invoice_by_id(id):
    sql = "SELECT invoice_header.id,invoice_header.`time`,invoice_detail.id_line,invoice_detail.quantity,users.username,users.email,products.name,products.price FROM invoice_header INNER JOIN invoice_detail ON invoice_header.id = invoice_detail.id_invoice INNER JOIN users ON invoice_header.user_id = users.id INNER JOIN products ON invoice_detail.id_product = products.id WHERE invoice_header.id = %s ORDER BY invoice_detail.id_line ASC "
    cursor.execute(sql, (id,))
    result = cursor.fetchall()
    return result

def Get_total_facturation():
    sql = "SELECT SUM(quantity * products.price) AS facturation FROM invoice_detail INNER JOIN products ON invoice_detail.id_product = products.id"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def Get_total_facturation_by_product(product_id):
    sql = "SELECT nvl(SUM(quantity * products.price), 0) AS facturation FROM invoice_detail INNER JOIN products ON invoice_detail.id_product = products.id WHERE products.id = %s"
    cursor.execute(sql, (product_id,))
    result = cursor.fetchone()
    return result