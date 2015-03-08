# -*- coding: utf-8 -*-

from jinja2 import Template
template = Template('Hello {{ name }}!')
template.render(name='John Doe')
print template