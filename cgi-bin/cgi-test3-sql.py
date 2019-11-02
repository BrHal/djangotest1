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
id_service = str(form['service'].value)
name = str(form['name'].value)
first_name = str(form['first_name'].value)
registration_number = str(form['registration_number'].value)
home_phone_number = str(form['home_phone_number'].value)

db_connection = sqlite3.connect('db/djangotest.sqlite3')
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()
cursor.execute("INSERT INTO Employees (registration_number, first_name, name, home_phone_number, id_service)"
               + " VALUES (?,?,?,?,?)", (registration_number, first_name, name, home_phone_number, id_service))
db_connection.commit()
db_connection.close()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print(
    """Content-Type: application/xhtml+xml; charset=utf-8

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
 <head>
  <title>eCarnet - Ajout d'employé</title>
  <link href="/css/topcoat-desktop-light.min.css" rel="stylesheet"/>
 </head>
 <body>""")
print("  <h1>Ajout de l'employé <em>" + first_name + " " + name + "</em></h1>")
print("  <p>" + first_name + " " + name + " a bien été ajouté dans la base de données</p>")
print(""" </body>
 <footer>
  <a href="/cgi-bin/cgi-test-sql.py">Retour</a>
 </footer>
</html>
"""
      )
