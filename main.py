import sqlite3


class App:
    def __init__(self):
        self.init_sq()
        self.clear_whole_db()
        self.init_sq()
        self.insert_essential_data()


    def init_sq(self):
        self.conn = sqlite3.connect("material.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Kohte (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS SKohte (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Jurtelang (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Jurtekurz (mat TEXT, anzahl INTEGER)''')
        self.conn.commit()

    def execute_command(self, text):
        #text = "'''" + text + "'''"
        print(text)
        self.cursor.execute(text)
        self.conn.commit()

    def clear_whole_db(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for table in tables:
            self.cursor.execute(f'DROP TABLE IF EXISTS {table[0]}')
        self.conn.commit()


    def insert_essential_data(self):
        self.execute_command('INSERT INTO Kohte (mat, anzahl) VALUES ("Kohtenplane", 4)')
        self.execute_command('INSERT INTO Kohte (mat, anzahl) VALUES ("Lange Seile", 3)')
        self.execute_command('INSERT INTO Kohte (mat, anzahl) VALUES ("Heringe", 8)')
        self.execute_command('INSERT INTO Kohte (mat, anzahl) VALUES ("Kohtenabdeckplane", 1)')
        self.execute_command('INSERT INTO Kohte (mat, anzahl) VALUES ("Kohtenkreuzstange", 2)')

        self.execute_command('INSERT INTO SKohte (mat, anzahl) VALUES ("SKohtenplane", 4)')
        self.execute_command('INSERT INTO SKohte (mat, anzahl) VALUES ("Lange Seile", 3)')
        self.execute_command('INSERT INTO SKohte (mat, anzahl) VALUES ("Heringe", 8)')
        self.execute_command('INSERT INTO SKohte (mat, anzahl) VALUES ("SKohtenabdeckplane", 1)')
        self.execute_command('INSERT INTO SKohte (mat, anzahl) VALUES ("Kohtenkreuzstange", 2)')


        self.execute_command('INSERT INTO Jurtelang (mat, anzahl) VALUES ("12er Jurtendach", 1)')
        self.execute_command('INSERT INTO Jurtelang (mat, anzahl) VALUES ("6er Spinne", 1)')
        self.execute_command('INSERT INTO Jurtelang (mat, anzahl) VALUES ("Seitenplane 2M doppelt", 6)')
        self.execute_command('INSERT INTO Jurtelang (mat, anzahl) VALUES ("Seitenstange 2M", 12)')
        self.execute_command('INSERT INTO Jurtelang (mat, anzahl) VALUES ("Heringe", 12)')
        self.execute_command('INSERT INTO Jurtelang (mat, anzahl) VALUES ("Tampen", 15)')





if __name__ == '__main__':
    app = App()