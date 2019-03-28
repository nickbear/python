# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:23:48 2019

@author: nickbear
"""
import string
def reverse(text):
    return text[::-1]s

def is_palindrome(text):
    text = text.lower()
    text = text.replace(' ','')
    for char in string.punctuation: #所有的标点字符
        text = text.replace(char,'')
    return text == reverse(text)

def main():
    something = input('Enter text:')
    if (is_palindrome(something)):
        print("Yes,'{0}' is a palindrome".format(something))
    else:
        print("No',{0}' is not a palindrome".format(something))

smain()