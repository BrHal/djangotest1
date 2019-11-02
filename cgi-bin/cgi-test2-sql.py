#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
From Book Django programming.

A simple cgi script.

"""

import sys
import codecs
import sqlite3
import cgi

form = cgi.FieldStorage()
service_id = str(form['service'].value)

db_connection = sqlite3.connect('db/djangotest.sqlite3')
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()
cursor.execute("SELECT name from Services where id=" + service_id)
row = cursor.fetchone()
service_name = str(row['name'])
cursor.execute("SELECT first_name, name, home_phone_number FROM Employees WHERE id_service="
               + service_id)
rows = cursor.fetchall()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print(
    """Content-Type: application/xhtml+xml; charset=utf-8

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
 <head>
  <title>eCarnet - Employés d'un service</title>
 </head>
 <body>
  <h1>Bienvenue sur l'eCarnet</h1>
  <h2>Employés du service <em>""" + service_name + """</em></h2>
   <ol>""")
for row in rows:
    print('   <li>'
          + row['first_name']
          + ' ' + row['name']
          + ' ' + row['home_phone_number']
          + '</li>')
print("""   </ol>
 </body>
 <footer>
  <a href="/cgi-bin/cgi-test-sql.py">Retour</a>
 </footer>
</html>
"""
      )
db_connection.close()
