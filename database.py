
import sqlite3
from sqlite3 import Connection, Cursor
from typing import Self
from constants import *

connect: Connection
cursor: Cursor


class DBUser:
    def __init__(self, id: int):
        global cursor
        self.id = id

    def _check_id(self):
        assert self.id != None, "No ID specified!"

    def _db_getter(self, prop: str):
        global cursor
        self._check_id()
        res = cursor.execute(f"SELECT {prop} FROM users WHERE id=?;", (self.id,))
        fetch = res.fetchone()
        return fetch[0]
    
    def _db_setter(self, prop: str, val):
        global connect
        global cursor
        self._check_id()
        cursor.execute(f"UPDATE users SET {prop} = ? WHERE id = ?;", (val, self.id,))
        connect.commit()

    @property
    def discord_id(self):
        return self._db_getter("discord_id")
    @discord_id.setter
    def discord_id(self, val):
        self._db_setter("discord_id", val)

    @property
    def social_credit(self):
        return self._db_getter("social_credit")
    @social_credit.setter
    def social_credit(self, val):
        self._db_setter("social_credit", val)

    @property
    def execution_date(self):
        return self._db_getter("execution_date")
    @execution_date.setter
    def execution_date(self, val):
        self._db_setter("execution_date", val)

    @property
    def to_be_executed(self):
        return self._db_getter("to_be_executed")
    @to_be_executed.setter
    def to_be_executed(self, val):
        self._db_setter("to_be_executed", val)


class DB:
    def __init__(self):
        global connect
        global cursor
        connect = sqlite3.connect("main.db")
        cursor = connect.cursor()
        
        cursor.execute(USER_TABLE_STRUCTURE)
    
    def get_new_id(self) -> int:
        max_id = cursor.execute("SELECT MAX(id) FROM users").fetchone()
        new_id = 0
        try:
            new_id = max_id[0] + 1
        except TypeError:
            pass
        return new_id

    def get_user_by_discord_id(self, discord_id: int) -> DBUser:
        global connect
        global cursor
        res = cursor.execute("SELECT id FROM users WHERE discord_id=?;", (discord_id,))
        val = res.fetchone()
        user = None
        if val == None:
            new_id = self.get_new_id()

            cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?);", (new_id, discord_id, DEFAULT_CREDIT, 0, False,))
            user = DBUser(new_id)
            connect.commit()
        else:
            user = DBUser(val[0])
        
        return user

db = DB()