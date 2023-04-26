import psycopg2


class PostgreDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='ec2-52-210-44-5.eu-west-1.compute.amazonaws.com',
            database='d5cgs2efbk9f55',
            user='pzenbabrskuqkz',
            port='5432',
            password='f7cd719b111c1d5f8fc7c313482967c457bb855de1cc6619648b22624172a21a'
        )
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def queryParams(self, query, params):
        self.cur.execute(query, params)
        self.conn.commit()

    def fetchOne(self):
        return self.cur.fetchone()

    def fetchAll(self):
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
