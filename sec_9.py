# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:38:01 2021

@author: Анастасия
"""
import random


def user_connection(username: str):
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"


def establish_connection(auth: bool = True):
    id = f"{random.randint(0, 100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"


def connection():
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))

    while len(connections) > 0:
        connection = random.choice(connections)

        try:
            yield next(connection)
        except StopIteration:
            del connections[connections.index(connection)]


def user_input(id):
    with open(f"./user_{id}.txt", "w") as file:
        msg = yield
        file.write(msg)


connections = []
ids = []

for i in connection():
    print(i)
    line = i.split()

    if line[0] == "auth":
        user_id = int(line[1])
        ids.append(user_id)
        connections.append(user_input(user_id))

    else:
        print("user is not logged in")