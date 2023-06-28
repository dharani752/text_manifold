import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack()

# Add a Tab to the Notebook widget
tab1 = tk.Frame(notebook)
notebook.add(tab1, text="Tab 1")

# Change the height of the Notebook widget
notebook.configure(height=100)
tab_control.add(tab1, text=f'<font size="6">{"Home":^60s}</font>')

root.mainloop()
