import math
import sys
import main
import sqlite3
BASE = 62

UPPERCASE_OFFSET = 55
LOWERCASE_OFFSET = 61
DIGIT_OFFSET = 48


def true_ord(char):
    if char.isdigit():
        return ord(char) - DIGIT_OFFSET
    elif 'A' <= char <= 'Z':
        return ord(char) - UPPERCASE_OFFSET
    elif 'a' <= char <= 'z':
        return ord(char) - LOWERCASE_OFFSET
    else:
        raise ValueError("%s is not a valid character" % char)


def true_chr(integer):
    if integer < 10:
        return chr(integer + DIGIT_OFFSET)
    elif 10 <= integer <= 35:
        return chr(integer + UPPERCASE_OFFSET)
    elif 36 <= integer < 62:
        return chr(integer + LOWERCASE_OFFSET)
    else:
        raise ValueError(
            "%d is not a valid integer in the range of base %d" % (integer, BASE))


def dehydrate(integer):

    if integer == 0:
        return '0'

    string = ""
    while integer > 0:
        remainder = integer % BASE
        string = true_chr(remainder) + string
        integer = int(integer//BASE)
    return string


def undo(user_input):
    original_link = ''
    for i in ascii_list:
        original_link += chr(i)
    return original_link



#? This function gets fed a link in string form, shortens it, adds it to the database and sends it out.
def start(user_input):
    global ascii_list

    def convert(user_input):
        global ascii_list
        ascii_list = []
        new_url = ''
        for i in str(user_input):
            ascii_list.append(ord(i))
            new_url += str(ord(i))

        # Connect to database

        return new_url
    conn = sqlite3.connect("urls.db")
    cur = conn.cursor()

    cur.execute(
        f"INSERT INTO urltable VALUES('{user_input}', '{dehydrate(int(convert(user_input)))[1:10:1]}')")
    conn.commit()
    cur.close()

    return dehydrate(int(convert(user_input)))[1:10:1], main.new_stuff(int(convert(user_input)[1:10:1]))
