#!/usr/bin/env python
# -*- coding: utf-8 -*-

# generate a password with length "passlen" with no duplicate characters in the password

# import random
#
# s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 8
# p =  "".join(random.sample(s,passlen ))
# print p

# import string
# import random
#
# def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
# 	return ''.join(random.choice(chars) for _ in range(size))
#
# print(pw_gen(int(input('How many characters in your password?'))))

import string
import random

def pw_gen(size = 16, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

from argparse import ArgumentParser

parser = ArgumentParser(add_help=True, description='About script...')
parser.add_argument('-u', '--user', help='User to ... (default: %(default)s)', default='user')
parser.add_argument('-p', '--password', help='Password for ...', default=(pw_gen()))
args = parser.parse_args()

print "\n This output for ...:"

print "SMTH TO '"+args.user+"'@'%'IDENTIFIED BY '"+args.password+"' ;"
