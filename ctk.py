import sqlite3
import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("680x580")
        self.title("Materialplaner")


        self.options = ['Kohte', 'SKohte', 'Jurtelang', 'Jurtekurz', 'Großjurte', 'Gigajurte', 'HochkohteGroß', 'Hochkohteklein']
        self.init_sq()
        self.clear_whole_db()
        self.init_sq()
        self.insert_essential_data()
        self.createGUI()


    def createGUI(self,):
        self.optionmenu = ctk.CTkOptionMenu(self, values=self.options)
        self.optionmenu.set(self.options[0])
        self.optionmenu.grid(row=0, column=0, pady=10)

        self.buttonADD = ctk.CTkButton(self, text="ADD to List", command=self.add_to_total)
        self.buttonADD.grid(row=0, column=1, pady=10)

        self.textMats = ctk.CTkTextbox(self, width=300, height=500)
        self.textMats.grid(row=1, column=0, padx=20, pady=10)

        self.textobj = ctk.CTkTextbox(self, width=300, height=500)
        self.textobj.grid(row=1, column=1, padx=20, pady=10)


    def init_sq(self):
        self.conn = sqlite3.connect("material.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Kohte (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS SKohte (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Jurtelang (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Jurtekurz (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Großjurte (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Gigajurte (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS HochkohteGroß (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Hochkohteklein (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Gesamt (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Alle (name TEXT UNIQUE, anzahl INTEGER)''')

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
        self.execute_command('INSERT INTO Jurtelang (mat, anzahl) VALUES ("Lange Seile", 3)')

        self.execute_command('INSERT INTO Jurtekurz (mat, anzahl) VALUES ("12er Jurtendach", 1)')
        self.execute_command('INSERT INTO Jurtekurz (mat, anzahl) VALUES ("6er Spinne", 1)')
        self.execute_command('INSERT INTO Jurtekurz (mat, anzahl) VALUES ("Seitenplane 1.6M", 12)')
        self.execute_command('INSERT INTO Jurtekurz (mat, anzahl) VALUES ("Seitenstange 1.6M", 12)')
        self.execute_command('INSERT INTO Jurtekurz (mat, anzahl) VALUES ("Heringe", 12)')
        self.execute_command('INSERT INTO Jurtekurz (mat, anzahl) VALUES ("Tampen", 15)')
        self.execute_command('INSERT INTO Jurtekurz (mat, anzahl) VALUES ("Lange Seile", 3)')

        self.execute_command('INSERT INTO Großjurte (mat, anzahl) VALUES ("16er Jurtendach", 1)')
        self.execute_command('INSERT INTO Großjurte (mat, anzahl) VALUES ("8er Spinne", 1)')
        self.execute_command('INSERT INTO Großjurte (mat, anzahl) VALUES ("Seitenplane 2M doppelt", 8)')
        self.execute_command('INSERT INTO Großjurte (mat, anzahl) VALUES ("Seitenstange 2M", 16)')
        self.execute_command('INSERT INTO Großjurte (mat, anzahl) VALUES ("Heringe", 16)')
        self.execute_command('INSERT INTO Großjurte (mat, anzahl) VALUES ("Tampen", 20)')
        self.execute_command('INSERT INTO Großjurte (mat, anzahl) VALUES ("Lange Seile", 3)')

        self.execute_command('INSERT INTO Gigajurte (mat, anzahl) VALUES ("18er Jurtendach (Giga)", 1)')
        self.execute_command('INSERT INTO Gigajurte (mat, anzahl) VALUES ("9er Spinne", 1)')
        self.execute_command('INSERT INTO Gigajurte (mat, anzahl) VALUES ("Seitenplane 2M doppelt", 9)')
        self.execute_command('INSERT INTO Gigajurte (mat, anzahl) VALUES ("Seitenstange 2M", 18)')
        self.execute_command('INSERT INTO Gigajurte (mat, anzahl) VALUES ("Heringe", 18)')
        self.execute_command('INSERT INTO Gigajurte (mat, anzahl) VALUES ("Tampen", 22)')
        self.execute_command('INSERT INTO Gigajurte (mat, anzahl) VALUES ("Lange Seile", 3)')

        self.execute_command('INSERT INTO HochkohteGroß (mat, anzahl) VALUES ("Kohtenplane", 4)')
        self.execute_command('INSERT INTO HochkohteGroß (mat, anzahl) VALUES ("Seitenplane 1.6M", 16)')
        self.execute_command('INSERT INTO HochkohteGroß (mat, anzahl) VALUES ("Lange Seile", 3)')
        self.execute_command('INSERT INTO HochkohteGroß (mat, anzahl) VALUES ("Seitenstange 3M", 8)')
        self.execute_command('INSERT INTO HochkohteGroß (mat, anzahl) VALUES ("Heringe", 8)')
        self.execute_command('INSERT INTO HochkohteGroß (mat, anzahl) VALUES ("Tampen", 8)')
        self.execute_command('INSERT INTO HochkohteGroß (mat, anzahl) VALUES ("Kohtenabdeckplane", 1)')
        self.execute_command('INSERT INTO HochkohteGroß (mat, anzahl) VALUES ("Kohtenkreuzstange", 2)')

        self.execute_command('INSERT INTO Hochkohteklein (mat, anzahl) VALUES ("Kohtenplane", 4)')
        self.execute_command('INSERT INTO Hochkohteklein(mat, anzahl) VALUES ("Seitenplane 2M doppelt", 8)')
        self.execute_command('INSERT INTO Hochkohteklein(mat, anzahl) VALUES ("Lange Seile", 3)')
        self.execute_command('INSERT INTO Hochkohteklein(mat, anzahl) VALUES ("Seitenstange 2M", 8)')
        self.execute_command('INSERT INTO Hochkohteklein(mat, anzahl) VALUES ("Heringe", 8)')
        self.execute_command('INSERT INTO Hochkohteklein(mat, anzahl) VALUES ("Tampen", 8)')
        self.execute_command('INSERT INTO Hochkohteklein(mat, anzahl) VALUES ("Kohtenabdeckplane", 1)')
        self.execute_command('INSERT INTO Hochkohteklein(mat, anzahl) VALUES ("Kohtenkreuzstange", 2)')


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

    def add_to_total(self):
        obj = self.optionmenu.get()
        if obj not in self.options:
            print('Object not valid') ################################### CHANGE
            return

        self.cursor.execute(f"SELECT mat, anzahl FROM {obj}")
        rows = self.cursor.fetchall()

        for mat, anzahl in rows:
            self.cursor.execute("SELECT anzahl FROM Gesamt WHERE mat = ?", (mat,))
            result = self.cursor.fetchone()



            if result:
                new_ges = result[0] + anzahl
                self.cursor.execute("UPDATE Gesamt SET anzahl = ? WHERE mat = ?", (new_ges, mat))

            else:
                self.cursor.execute("INSERT INTO Gesamt (mat, anzahl) VALUES (?, ?)", (mat, anzahl))

        self.cursor.execute("INSERT INTO Alle (name, anzahl) VALUES (?, ?) ON CONFLICT(name) DO UPDATE SET anzahl = anzahl + 1", (obj, 1))
        self.conn.commit()
        print(f"Added materials from {obj} to Gesamt.") ##########################CHANGE
        self.return_data_obj()
        self.return_data_mats()

    def return_data_mats(self): ##############
        self.textMats.delete("1.0", ctk.END)
        self.execute_command('SELECT * FROM Gesamt ORDER BY mat')

        data = self.cursor.fetchall()

        for (name, anzahl) in data:
            self.textMats.insert(ctk.END, f'{name}: {anzahl}\n')
            print(f'{name} : {anzahl}')


    def return_data_obj(self):
        self.textobj.delete("1.0", ctk.END)
        self.execute_command('SELECT * FROM Alle')
        data = self.cursor.fetchall()
        for (name, anzahl) in data:
            self.textobj.insert(ctk.END, f'{name}: {anzahl}\n')
            print(f'{name} : {anzahl}')






if __name__ == '__main__':
    app = App()
    app.mainloop()