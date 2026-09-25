
"""Ejercicio Twitter: programación orientada a objetos y SQLite.

La base de datos se crea llamando a create_db() antes de usar las clases.
"""

import re
import sqlite3

DB_PATH = "test.db"


class TwitterError(Exception):
    """Excepción propia de la aplicación."""


def conectar_db(db_path: str = DB_PATH) -> sqlite3.Connection:
    """Abre una conexión con filas accesibles por nombre y claves ajenas activas."""
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def create_db(db_path: str = DB_PATH) -> None:
    """Crea las tablas necesarias en la base de datos indicada."""
    con = conectar_db(db_path)
    try:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                bio TEXT NOT NULL DEFAULT ''
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tweet (
                id INTEGER PRIMARY KEY,
                content TEXT NOT NULL DEFAULT '',
                user_id INTEGER NOT NULL,
                retweet_from INTEGER,
                FOREIGN KEY (user_id) REFERENCES user(id),
                FOREIGN KEY (retweet_from) REFERENCES tweet(id)
            )
        """)
        con.commit()
    finally:
        con.close()


class User:
    con = conectar_db()
    cur = con.cursor()

    def __init__(self, username: str, password: str, bio: str = '',
                 user_id: int = 0):
        self.username = username
        self.password = password
        self.bio = bio
        self.id = user_id
        self.logged = False

    def save(self) -> None:
        self.cur.execute(
            "INSERT INTO user (username, password, bio) VALUES (?, ?, ?)",
            (self.username, self.password, self.bio)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def login(self, password: str) -> None:
        self.cur.execute(
            "SELECT * FROM user WHERE username = ? AND password = ?",
            (self.username, password)
        )
        row = self.cur.fetchone()
        self.logged = row is not None
        if row is not None:
            self.id = row['id']
            self.username = row['username']
            self.password = row['password']
            self.bio = row['bio']

    def tweet(self, content: str) -> 'Tweet':
        if not self.logged:
            raise TwitterError(f"User {self.username} is not logged in!")
        if len(content) > 280:
            raise TwitterError("Tweet has more than 280 chars!")
        new_tweet = Tweet(content)
        new_tweet.save(self)
        return new_tweet

    def retweet(self, tweet_id: int) -> 'Tweet':
        if not self.logged:
            raise TwitterError(f"User {self.username} is not logged in!")
        Tweet.cur.execute("SELECT id FROM tweet WHERE id = ?", (tweet_id,))
        if Tweet.cur.fetchone() is None:
            raise TwitterError(f"Tweet with id {tweet_id} does not exist!")
        new_tweet = Tweet(retweet_from=tweet_id)
        new_tweet.save(self)
        return new_tweet

    @property
    def tweets(self):
        self.cur.execute("SELECT * FROM tweet WHERE user_id = ? ORDER BY id",(self.id,))
        rows = self.cur.fetchall()
        for row in rows:
            yield Tweet.from_db_row(row)

    def __repr__(self) -> str:
        return f"{self.username}: {self.bio}"

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> 'User':
        return cls(row['username'], row['password'], row['bio'], row['id'])


class Tweet:
    con = conectar_db()
    cur = con.cursor()

    def __init__(self, content: str = '', retweet_from: int = 0,
                 tweet_id: int = 0):
        self.retweet_from = retweet_from
        self.id = tweet_id
        self._content = '' if retweet_from else content

    @property
    def is_retweet(self) -> bool:
        return self.retweet_from != 0

    @property
    def content(self) -> str:
        if not self.is_retweet:
            return self._content

        # Recorre los retuits hasta encontrar el tweet original.
        current_id = self.retweet_from
        while True:
            self.cur.execute(
                "SELECT content, retweet_from FROM tweet WHERE id = ?",
                (current_id,)
            )
            row = self.cur.fetchone()
            if row is None:
                raise TwitterError(
                    f"Tweet with id {current_id} does not exist!"
                )
            if row['retweet_from'] is None:
                return row['content']
            current_id = row['retweet_from']

    def save(self, user: User) -> None:
        self.cur.execute(
            "INSERT INTO tweet (content, user_id, retweet_from) "
            "VALUES (?, ?, ?)",
            (self._content, user.id,
             self.retweet_from if self.is_retweet else None)
        )
        self.con.commit()
        self.id = self.cur.lastrowid

    def __repr__(self) -> str:
        prefix = "[RT] " if self.is_retweet else ""
        return f"{prefix}{self.content} (id={self.id})"

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> 'Tweet':
        return cls(row['content'], row['retweet_from'] or 0, row['id'])


class Twitter:
    con = conectar_db()
    cur = con.cursor()

    def add_user(self, username: str, password: str,
                 bio: str = '') -> User:
        patron = r'[@=][0-9]{2,4}[A-Za-z]{2,4}[!*]'
        if re.fullmatch(patron, password) is None:
            raise TwitterError("Password does not follow security rules!")
        user = User(username, password, bio)
        user.save()
        return user

    def get_user(self, user_id: int) -> User:
        self.cur.execute("SELECT * FROM user WHERE id = ?", (user_id,))
        row = self.cur.fetchone()
        if row is None:
            raise TwitterError(f"User with id {user_id} does not exist!")
        return User.from_db_row(row)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
