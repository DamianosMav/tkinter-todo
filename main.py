import json
import tkinter as tk
from tkinter import font
from pathlib import Path

class ToDo:
    def __init__(self, root):
        # Set up root window
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Define save path for storing tasks
        self.path = Path.home() / "Documents" / "Todo.json"

        # Define fonts (normal and strike-through for completed tasks)
        self.font_normal = font.Font(family="Helvetica", size=8)
        self.font_strike = font.Font(family="Helvetica", size=8, overstrike=1)

        # Initialize lists to store task entry data and checkbox states
        self.entries = []  # List of (StringVar, Entry)
        self.checks = []   # List of IntVar (checkbox states)

        num_of_entries = 14  # Maximum number of task rows

        # Create Entry and Checkbutton widgets for each task
        for i in range(num_of_entries):
            entry_var = tk.StringVar()    # StringVar to hold entry text
            check_var = tk.IntVar()       # IntVar to hold checkbox state (0 or 1)

            # Create entry field for the task
            entry = tk.Entry(self.root, width=40, textvariable=entry_var, font=self.font_normal)
            # Create checkbox to toggle strike-through effect
            check_button = tk.Checkbutton(
                self.root,
                variable=check_var,
                command=lambda e=entry, v=check_var: self.toggle_font(e, v)
            )

            # Place the widgets in the grid
            entry.grid(row=i, column=0, padx=5, columnspan=2)
            check_button.grid(row=i, column=2)

            # Save references for later use
            self.entries.append((entry_var, entry))
            self.checks.append(check_var)

        # Load any previously saved entries from file
        saved = self.load_entries(self.path)
        for (stringvar, _), text in zip(self.entries, saved):
            stringvar.set(text)

        # Create and place Save and Clear buttons
        save_button = tk.Button(self.root, text="SAVE", background="green", command=self.save_entries)
        clear_button = tk.Button(self.root, text="CLEAR", background="red", command=self.clear_entries)

        # Place buttons below the entries
        save_button.grid(row=num_of_entries + 1, column=1, columnspan=2, sticky="se", padx=35, pady=5)
        clear_button.grid(row=num_of_entries + 1, column=0, columnspan=2, sticky="sw", padx=15, pady=5)

    def toggle_font(self, entry, var):
        """Toggle font style between normal and strike-through based on checkbox state."""
        entry.config(font=self.font_strike if var.get() else self.font_normal)

    def clear_entries(self):
        """Clear all entry fields and delete saved JSON file content."""
        for stringvar, _ in self.entries:
            stringvar.set("")  # Clear entry from UI

        self.path.write_text("")  # Clear saved file

    def save_entries(self):
        """Save all current task text values into a JSON file."""
        # Create a dictionary: {index: task_text}
        entries_dict = {i: var.get() for i, (var, _) in enumerate(self.entries)}
        # Save as JSON to file
        self.path.write_text(json.dumps(entries_dict))

    def load_entries(self, file_path):
        """Load previously saved entries from JSON file."""
        file_path = Path(file_path)

        # If file doesn't exist or is empty, return empty list
        if not file_path.exists():
            return []

        content = file_path.read_text().strip()
        if not content:
            return []

        # Return list of task strings
        return list(json.loads(content).values())

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDo(root)
    root.mainloop()
