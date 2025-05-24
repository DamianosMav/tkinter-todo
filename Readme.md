# Python Tkinter To-Do List

A simple desktop To-Do List application built in Python with Tkinter.  
Enter up to 14 tasks, mark them complete with a strike-through effect, and save your list—persisted as JSON in your Documents folder.

---

## 📝 Features

- **Add / Remove Tasks**  
  Enter or clear up to 14 items in the list.  
- **Complete Tasks**  
  Check a box to toggle strike-through on any task.  
- **Save & Load**  
  • **Save** writes all current tasks to `~/Documents/Todo.json`.  
  • **Load** automatically reads `Todo.json` on startup.  
- **Clear All**  
  One-click “CLEAR” button removes all entries from the UI and JSON file.

---

## 🛠️ Technologies

- **Python 3.x**  
- **Tkinter** (built-in) for the GUI  
- **pathlib** & **json** for file I/O and persistence  

_No external packages required._

---

## 🚀 Getting Started

 **Clone this repository**  
   ```
   bash
   git clone https://github.com/DamianosMav/tkinter-todo.git
   cd tkinter-todo
   ```

## Run the app
    python todo.py


## ⚙️Configuration
    The app uses a constant save path at the top of todo.py

## 📄License
    This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


Built by Damianos Mav
Feel free to ⭐ the repo if you find it useful.