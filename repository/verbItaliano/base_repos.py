import psycopg2


class PostgreDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='ce9oip7r5bp6e2.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com',
            database='d7c4rijg9fgt78',
            user='uffl13ltqt73r7',
            port='5432',
            password='pb4eae479a11a1f12660956bc4dae9dadbf1846f87176f0f81006e1c458217ed0'
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
