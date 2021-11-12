import psycopg2


class PostgreDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='ec2-54-73-110-26.eu-west-1.compute.amazonaws.com',
            database='djs348j1mlldt',
            user='mhjwehpsnygovo',
            port='5432',
            password='45bb40f50f6b24e466ac36270fc2ecdedae29b03382b120a1b1af335ec273f4a'
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
