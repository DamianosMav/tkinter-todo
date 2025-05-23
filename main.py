import tkinter as tk
from tkinter import font

from pathlib import Path
import json

#Setting the path to the documents folder and toso.jsoin file
SAVE_PATH = Path.home() / "Documents" / "Todo.json"

# Fonts
font_normal = font.Font(family="Helvetica", size=8)
font_strike = font.Font(family="Helvetica", size=8, overstrike=1)

# Toggles strike-through
def toggle_font(entry, var):
    entry.config(font=font_strike if var.get() else font_normal)

# Clears all the entries the user saved
def clear_entries(stringvars):
    for entry, _ in stringvars:
        entry.set("") # Clears it from the UI

    SAVE_PATH.write_text("") # Clears it from the json file

# Saves the entries
def save_entries(entries = []):
    entriesDictionary = {i: entry.get() for i, (entry, _) in enumerate(entries)}

    SAVE_PATH.write_text(json.dumps(entriesDictionary))

# Loads all the entries
def load_entries(file_path):
    file_path = Path(file_path)
    
    if not file_path.exists():
        return []
    
    text = file_path.read_text().strip()

    if not text:
        return []
    
    return list(json.loads(text).values())
        
def run_app():
    #Setting up the app, screen size and font
    app = tk.Tk(screenName=None, baseName=None, useTk=1)
    app.title("To-Do List")
    app.geometry("300x400")
    app.resizable(False, False)

    

    entries = [] # will hold (StringVar, Entry)
    checks  = [] # will hold IntVar for each checkbox

    num_of_enties = 14

    # Create's entries and checkboxes from the provided variable 
    for i in range(num_of_enties):
        entry_string_var = tk.StringVar()
        entryCheckVar = tk.IntVar()

        entry = tk.Entry(app, width=40, textvariable=entry_string_var, font=font_normal)
        check_button  = tk.Checkbutton(app, variable=entryCheckVar, command=lambda e=entry, v=entryCheckVar: toggle_font(e, v))

        entry.grid(row=i, column=0, padx=5, columnspan=2)
        check_button .grid(row=i, column=2)

        entries.append((entry_string_var, entry))
        checks.append(entryCheckVar)

    # Load any saved tasks
    saved = load_entries(SAVE_PATH)
    for (stringvar, _), text in zip(entries, saved):
        stringvar.set(text)

    # UI Buttons for saving and clearing
    save_button = tk.Button(app, text="SAVE", background="green")
    clear_button = tk.Button(app, text="CLEAR", background="red")

    rows = num_of_enties + 1
    clear_button.grid(row= rows, column=0 , columnspan= 2, sticky="sw", padx= 15, pady= 5)
    save_button.grid(row= rows, column= 1, columnspan= 2, sticky="se", padx= 35, pady= 5)

    # Button logic
    clear_button.config(command=lambda: clear_entries(entries))
    save_button.config(command=lambda: save_entries(entries))




    app.mainloop()

if __name__ == "__main__":
    run_app()




