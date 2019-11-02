#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
From Book Django programming.

A simple cgi script.

"""

import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print(
    """Content-Type: application/xhtml+xml; charset=utf-8

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
 <head>
  <title>eCarnet - Home</title>
  <link href="/css/topcoat-desktop-light.min.css" rel="stylesheet"/>
 </head>
 <body>
  <h1>Bienvenue sur l'eCarnet</h1>
  <h2>Employés</h2>
   <ol>
    <li>Aude Heurdepet</li>
    <li>Bill de Foix</li>
    <li>Yvan Skivol</li>
   </ol>
 </body>
 <footer>
  <a href="/welcome.html">Retour</a>
 </footer>
</html>
    """
)
