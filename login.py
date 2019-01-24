#!/usr/bin/env python3
import cgi
import cgitb
import os

from templates import login_page, secret_page, after_login_incorrect
from secret import username, password

cgitb.enable()

def print_base():
    print("Content-Type: text/html\n")
    print()
    print("<!doctype html>")
    print(login_page())

form = cgi.FieldStorage()
formUser = form.getvalue("username")
formPass = form.getvalue("password")

if (formUser == None):
    try:
        cookie_string = os.environ.get("HTTP_COOKIE")
        cookie_pairs = cookie_string.split(";")
        for pair in cookie_pairs:
            key, value = pair.split("=")
            if ("username" in key):
                formUser = value
            elif ("password" in key):
                formPass = value
    except:
        pass

if (formUser == username and formPass == password):
    print("Set-Cookie: username=%s" % (username))
    print("Set-Cookie: password=%s" % (password))
    print_base()
    print(secret_page(formUser, formPass))
elif (formUser != None and formPass != None):
    print_base()
    print(after_login_incorrect())