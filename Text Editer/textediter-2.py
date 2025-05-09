import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully!")

# Edit menu functions
def cut_text():
    text.event_generate("<<Cut>>")

def copy_text():
    text.event_generate("<<Copy>>")

def paste_text():
    text.event_generate("<<Paste>>")

def undo_text():
    try:
        text.edit_undo()
    except tk.TclError:
        pass

def redo_text():
    try:
        text.edit_redo()
    except tk.TclError:
        pass

def find_text():
    search_term = simpledialog.askstring("Find", "Enter text to find:")
    text.tag_remove("highlight", "1.0", tk.END)
    if search_term:
        start_pos = "1.0"
        while True:
            start_pos = text.search(search_term, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_term)}c"
            text.tag_add("highlight", start_pos, end_pos)
            start_pos = end_pos
        text.tag_config("highlight", background="yellow")

def replace_text():
    find_term = simpledialog.askstring("Replace", "Enter text to find:")
    replace_term = simpledialog.askstring("Replace", "Enter replacement text:")
    content = text.get("1.0", tk.END)
    new_content = content.replace(find_term, replace_term)
    text.delete("1.0", tk.END)
    text.insert("1.0", new_content)

def select_all():
    text.tag_add('sel', '1.0', 'end')

def toggle_word_wrap():
    current_wrap = text.cget('wrap')
    if current_wrap == 'none':
        text.config(wrap='word')
    else:
        text.config(wrap='none')

def change_font():
    font_name = simpledialog.askstring("Font", "Enter font name (e.g., Arial):")
    font_size = simpledialog.askinteger("Font Size", "Enter font size (e.g., 12):")
    if font_name and font_size:
        text.config(font=(font_name, font_size))

# Center the window on the screen
def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("Advanced Text Editor")

# Set default window size and make the window resizable
root.geometry("800x600")
root.minsize(600, 400)  # Minimum size of the window

# Create the menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=undo_text)
edit_menu.add_command(label="Redo", command=redo_text)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find_text)
edit_menu.add_command(label="Replace", command=replace_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

# Format menu
format_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Word Wrap", command=toggle_word_wrap)
format_menu.add_command(label="Font", command=change_font)

# Text widget
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), undo=True)
text.pack(expand=tk.YES, fill=tk.BOTH)

# Center the window on start
center_window(root)

root.mainloop()
