#!/usr/bin/env python3

import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))
with open("templates/service.json.jinja") as file:
    tmpl = env.parse(file.read())
tmpl_vars = jinja2.meta.find_undeclared_variables(tmpl)
print(tmpl_vars)
