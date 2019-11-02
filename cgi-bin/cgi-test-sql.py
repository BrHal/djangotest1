#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
From Book Django programming.

A simple cgi script.

"""

import sys
import codecs
import sqlite3

db_connection = sqlite3.connect('db/djangotest.sqlite3')
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()
cursor.execute("SELECT first_name, name, home_phone_number FROM Employees")
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
  <title>eCarnet - Employés</title>
  <link href="/css/topcoat-desktop-light.min.css" rel="stylesheet"/>
 </head>
 <body>
  <h1>Bienvenue sur l'eCarnet</h1>
  <h2>Employés</h2>
   <ol>""")
for row in rows:
    print('   <li>'
          + row['first_name']
          + ' ' + row['name']
          + ' ' + row['home_phone_number']
          + '</li>')
print("""   </ol>
  <h2>Employés par service</h2>
  <form action="cgi-test2-sql.py" method="get">
   <p>
    <select name="service">""")
cursor.execute("SELECT id, name from Services")
rows = cursor.fetchall()
for row in rows:
    print('     <option value="' + str(row['id']) + '">' + row['name'] + '</option>')
print(
    """    </select>
    <input type="submit" value="Lister"/>
   </p>
  </form>""")
print("""  <h2>Ajouter un nouvel employé</h2>
  <form action="cgi-test3-sql.py" method="get">
   <p>Prénom : <input type="text" name="first_name"/></p>
   <p>Nom : <input type="text" name="name"/></p>
   <p>Matricule : <input type="text" name="registration_number"/></p>
   <p>Tél. fixe : <input type="text" name="home_phone_number"/></p>
   <p>Service : <select name="service">""")
for row in rows:
    print('     <option value="' + str(row['id']) + '">' + row['name'] + '</option>')

print("""    </select>
   </p>
   <p><input type="submit" value="Ajouter"/></p>
  </form>
 </body>
 <footer>
  <a href="/welcome.html">Retour</a>
 </footer>
</html>
"""
)
db_connection.close()
