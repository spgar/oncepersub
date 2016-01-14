import sqlite3

class OncePerSub:
    def __init__(self, filename):
        self.sql = sqlite3.connect(filename)
        self.cursor = self.sql.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS handledsubmissions(id TEXT)')

    def isHandled(self, submission):
        self.cursor.execute('SELECT * FROM handledsubmissions WHERE ID=?', [submission.id])
        if self.cursor.fetchone():
            return True
        return False

    def handle(self, submission):
        self.cursor.execute('INSERT INTO handledsubmissions VALUES(?)', [submission.id])
        self.sql.commit()