import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
#This is Chatgpt take on Designing


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Material Verwaltung")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.conn = sqlite3.connect("material.db")
        self.cursor = self.conn.cursor()

        self.options = [
            'Kohte', 'SKohte', 'Jurtelang', 'Jurtekurz',
            'Großjurte', 'Gigajurte', 'HochkohteGroß'
        ]

        self.init_sq()
        self.clear_whole_db()
        self.init_sq()
        self.insert_essential_data()

        self.build_gui()

    def init_sq(self):
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Gesamt (mat TEXT, anzahl INTEGER)''')
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS Alle (name TEXT UNIQUE, anzahl INTEGER)''')

        for option in self.options:
            self.cursor.execute(f''' CREATE TABLE IF NOT EXISTS {option} (mat TEXT, anzahl INTEGER)''')
        self.conn.commit()

    def execute_command(self, text):
        self.cursor.execute(text)
        self.conn.commit()

    def clear_whole_db(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for table in tables:
            self.cursor.execute(f'DROP TABLE IF EXISTS {table[0]}')
        self.conn.commit()

    def insert_essential_data(self):
        # For clarity, add a single function to insert data per tent type
        def batch_insert(table, items):
            for mat, count in items:
                self.cursor.execute(f'INSERT INTO {table} (mat, anzahl) VALUES (?, ?)', (mat, count))

        batch_insert('Kohte', [
            ("Kohtenplane", 4), ("Lange Seile", 3), ("Heringe", 8),
            ("Kohtenabdeckplane", 1), ("Kohtenkreuzstange", 2)
        ])

        batch_insert('SKohte', [
            ("SKohtenplane", 4), ("Lange Seile", 3), ("Heringe", 8),
            ("SKohtenabdeckplane", 1), ("Kohtenkreuzstange", 2)
        ])

        batch_insert('Jurtelang', [
            ("12er Jurtendach", 1), ("6er Spinne", 1), ("Seitenplane 2M doppelt", 6),
            ("Seitenstange 2M", 12), ("Heringe", 12), ("Tampen", 15), ("Lange Seile", 3)
        ])

        batch_insert('Jurtekurz', [
            ("12er Jurtendach", 1), ("6er Spinne", 1), ("Seitenplane 1.6M", 12),
            ("Seitenstange 1.6M", 12), ("Heringe", 12), ("Tampen", 15), ("Lange Seile", 3)
        ])

        batch_insert('Großjurte', [
            ("16er Jurtendach", 1), ("8er Spinne", 1), ("Seitenplane 2M doppelt", 8),
            ("Seitenstange 2M", 16), ("Heringe", 16), ("Tampen", 20), ("Lange Seile", 3)
        ])

        batch_insert('Gigajurte', [
            ("18er Jurtendach (Giga)", 1), ("9er Spinne", 1), ("Seitenplane 2M doppelt", 9),
            ("Seitenstange 2M", 18), ("Heringe", 18), ("Tampen", 22), ("Lange Seile", 3)
        ])

        batch_insert('HochkohteGroß', [
            ("Kohtenplane", 4), ("Seitenplane 1.6M", 16), ("Lange Seile", 3),
            ("Seitenstange 3M", 8), ("Heringe", 8), ("Tampen", 8),
            ("Kohtenabdeckplane", 1), ("Kohtenkreuzstange", 2)
        ])

        self.conn.commit()

    def add_to_total(self, obj):
        if obj not in self.options:
            messagebox.showerror("Fehler", "Ungültiges Objekt")
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

        self.cursor.execute(
            "INSERT INTO Alle (name, anzahl) VALUES (?, ?) ON CONFLICT(name) DO UPDATE SET anzahl = anzahl + 1",
            (obj, 1)
        )
        self.conn.commit()
        self.update_output()

    def build_gui(self):
        frame_top = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        frame_top.pack()

        tk.Label(frame_top, text="Wähle ein Zelt:", font=("Helvetica", 14), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)

        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])
        dropdown = ttk.Combobox(frame_top, textvariable=self.selected_option, values=self.options, state="readonly", width=20)
        dropdown.pack(side=tk.LEFT, padx=10)

        tk.Button(frame_top, text="Hinzufügen", command=lambda: self.add_to_total(self.selected_option.get()), bg="#4CAF50", fg="white", padx=10).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_top, text="Beenden", command=self.root.quit, bg="#f44336", fg="white", padx=10).pack(side=tk.LEFT, padx=10)

        frame_bottom = tk.Frame(self.root, bg="#f0f0f0")
        frame_bottom.pack(fill=tk.BOTH, expand=True)

        self.text_gesamt = tk.Text(frame_bottom, width=40, height=20)
        self.text_gesamt.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_gesamt.insert(tk.END, "Gesamtmaterialien\n")

        self.text_alle = tk.Text(frame_bottom, width=40, height=20)
        self.text_alle.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_alle.insert(tk.END, "Objekte gezählt\n")

        self.update_output()

    def update_output(self):
        self.text_gesamt.delete("1.0", tk.END)
        self.text_gesamt.insert(tk.END, "Gesamtmaterialien\n\n")
        self.cursor.execute("SELECT * FROM Gesamt ORDER BY mat")
        for (name, anzahl) in self.cursor.fetchall():
            self.text_gesamt.insert(tk.END, f"{name}: {anzahl}\n")

        self.text_alle.delete("1.0", tk.END)
        self.text_alle.insert(tk.END, "Objekte gezählt\n\n")
        self.cursor.execute("SELECT * FROM Alle")
        for (name, anzahl) in self.cursor.fetchall():
            self.text_alle.insert(tk.END, f"{name}: {anzahl}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
