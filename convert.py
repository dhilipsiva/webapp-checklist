#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# Copyright © dhilipsiva
#

'''
    File name: convert.py
    Version: 0.1
    Author: dhilipsiva <dhilipsiva@gmail.com>
    Date created: 2015-03-15
'''
__author__ = "dhilipsiva"
__status__ = "development"

"""
Just a script to convert StackOverflow link format to GH link format
"""

import re

with open("README.md", "r") as f:
    content = f.read()

split_texts = re.split("\s[\[(0-9)+\]]+:\s", content)

for i, link in enumerate(split_texts):
    link = "(%s)" % link.replace("\n", "").replace(" ", "")
    content = content.replace("[%d]" % i, link, 1)

with open("README.md", "w") as f:
    f.write(content)
