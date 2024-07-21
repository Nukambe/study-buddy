import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("study_buddy.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def create_tables(self):
        self.query("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, subject TEXT, note TEXT)")
        saved_notes = self.query("SELECT * FROM notes")
        if not saved_notes:
            self.query("INSERT INTO notes (subject, note) VALUES ('Math', 'Math is fun')")
            self.query("INSERT INTO notes (subject, note) VALUES ('English', 'English is fun')")
            self.query("INSERT INTO notes (subject, note) VALUES ('Science', 'Science is fun')")
            self.query("INSERT INTO notes (subject, note) VALUES ('History', 'History is fun')")
        self.commit()

    def get_notes(self):
        return self.query("SELECT * FROM notes")

db = DB()
print("called db")
