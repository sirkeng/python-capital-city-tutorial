import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to calculate the area of a rectangle
def calculate_area():
    try:
        width = float(simpledialog.askstring("Input", "Enter width:"))
        height = float(simpledialog.askstring("Input", "Enter height:"))
        area = width * height
        messagebox.showinfo("Area Calculator", f"The area of the rectangle is: {int(area)}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for width and height")

def main_program():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    while True:
        calculate_area()
        retry = messagebox.askyesno("Retry", "Do you want to calculate another area?")
        if not retry:
            messagebox.showinfo("Thanks", "Thank you for using the program. Goodbye!")
            root.destroy()
            break

# Run the main program
if __name__ == "__main__":
    main_program()
