import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def select_csv():
    csv_file_path.set(filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")]))
    if csv_file_path.get():
        messagebox.showinfo("File Selected", f"Selected file: {csv_file_path.get()}")

def convert_to_excel():
    if not csv_file_path.get():
        messagebox.showerror("Error", "Please select a CSV file first!")
        return

    try:
        data = pd.read_csv(csv_file_path.get())
        excel_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if excel_file_path:
            data.to_excel(excel_file_path, index=False)
            messagebox.showinfo("Success", f"File converted and saved to: {excel_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("CSV to Excel Converter")
root.geometry("400x200")

csv_file_path = tk.StringVar()

tk.Label(root, text="Select a CSV file:").pack(pady=10)
tk.Entry(root, textvariable=csv_file_path, width=50, state="readonly").pack(pady=5)
tk.Button(root, text="Browse", command=select_csv).pack(pady=5)

tk.Button(root, text="Convert to Excel", command=convert_to_excel).pack(pady=20)

root.mainloop()
