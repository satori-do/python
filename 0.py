#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print ("") # Just empty output

#-----------------------------------------------------------------------------
print ("\nHello World!!!")
print ('Hello World!!!\n')

print ('"Hello" World!!!')
print ("'Hello' World!!!\n")

print ("\"Hello\" World!!!") #;lghk\srh\
print ("\"Hello\"\nWorld!!!\n")

#-----------------------------------------------------------------------------
# int
number = 5

# float
fnumber = 5.7

# string
name = "Eternity"

# bool
status = True

print ( "\n",number )

print ("\nIt is a", number*2/2 + fnumber, name+"\n") # Concatenation, looks like to braid the braids...

print ("Hello my name is "+name+". I'm " + str(number)+" years old." ) # Type casting

#-----------------------------------------------------------------------------

name = input( "Input your name: " )
age = input( "Input your age: " )

print ( "Hello " + name + "!" )
print ( "You have a " + age + " years. It's great!" )
