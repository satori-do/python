#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

choice = None

def ask(prompt, pattern=r'^(?i)(y(es)?|no?)$'):
# def ask(prompt, pattern=r'^(?i)(y(es)?|no?)$'):

    choice = ''
    while not re.match(pattern, choice):
        choice = input(prompt)
    return choice.lower()

choice = (ask('Proceed? (y/n): '))
if choice and choice.lower()[0] != "y":
    raise Error("Cancelling due to user request")
else:
    print ("YES!!!")
