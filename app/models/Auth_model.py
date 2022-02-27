#!/usr/bin/python
# -*- coding: utf-8 -*-
from app.config import create_conn

class AuthModel():
    def __init__(self):
        pass

    def getUser(_id):
        mysql = create_conn();cur = mysql.cursor()
        cur.execute(f"SELECT * FROM users")
        users = cur.fetchall()
        x = []
        for user in users:
            x.append(user)

        cur.close();mysql.close()

        return user


authmodel=AuthModel()