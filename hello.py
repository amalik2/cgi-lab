#!/usr/bin/env python3
import cgi
import cgitb
import os
import json

cgitb.enable()

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
#print(os.environ)

env_json = {}
for key, value in os.environ.items():
    env_json[key] = value
print(json.dumps(env_json))

print("<h2>" + os.environ.get("QUERY_STRING") + "</h2>")
print("<h2>" + os.environ.get("HTTP_USER_AGENT") + "</h2>")