import tkinter as tk
import random
import string
root=tk.Tk()
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:  # negative ya zero length ko handle karna
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Enter a positive number")
            return
    except ValueError:  # agar user number na dale
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Enter a valid number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0,password)

root.title("Password Generate")
root.geometry("400x500")
root.config(bg="white")

titel = tk.Label(root, text="Password Generate", font=("Arial", 18, "bold"))
titel.pack()
length_label = tk.Label(root, text="Enter Password Length", font=("Arial", 18))
length_label.pack()
length_entry = tk.Entry(root, font=("Arial", 18), justify="center")
length_entry.pack()

# Generate button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=generate_password
)
generate_btn.pack(pady=10)

# Result
result_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=30)
result_entry.pack(pady=5)
root.mainloop()

