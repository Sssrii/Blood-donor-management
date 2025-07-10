


# import tkinter as tk
# from tkinter import messagebox, simpledialog
# import subprocess

# def register_donor():
#     name = name_entry.get()
#     age = age_entry.get()
#     blood = blood_entry.get()
#     location = location_entry.get()
#     pincode = pincode_entry.get()
#     phone = phone_entry.get()

#     if not (name and age and blood and location and pincode and phone):
#         messagebox.showerror("Error", "Please fill all fields")
#         return

#     try:
#         result = subprocess.run(
#             ["register.exe", name, age, blood, location, pincode, phone],
#             capture_output=True,
#             text=True
#         )
#         messagebox.showinfo("Result", result.stdout.strip())
#     except Exception as e:
#         messagebox.showerror("Error", f"Something went wrong: {e}")

# def show_all_donors():
#     try:
#         with open("donors.txt", "r") as file:
#             data = file.readlines()

#         if not data:
#             messagebox.showinfo("Donors", "No donors found.")
#             return

#         popup = tk.Toplevel(root)
#         popup.title("All Donors")
#         text = tk.Text(popup, wrap="word", width=70, height=20)
#         text.pack(padx=10, pady=10)

#         for line in data:
#             fields = line.strip().split(',')
#             if len(fields) >= 6:
#                 display = (
#                     f"Name: {fields[0]}, Age: {fields[1]}, Blood: {fields[2]}, "
#                     f"Location: {fields[3]}, Pincode: {fields[4]}, Phone: {fields[5]}\n"
#                 )
#                 text.insert(tk.END, display)
#     except FileNotFoundError:
#         messagebox.showerror("Error", "donors.txt file not found.")

# def search_by_blood_group():
#     bg = simpledialog.askstring("Search", "Enter Blood Group (e.g., A+, B-, O+):")
#     if not bg:
#         return

#     try:
#         with open("donors.txt", "r") as file:
#             data = file.readlines()

#         matches = []
#         for line in data:
#             fields = line.strip().split(',')
#             if len(fields) >= 3 and fields[2].upper() == bg.upper():
#                 matches.append(fields)

#         if not matches:
#             messagebox.showinfo("Result", f"No donors with blood group {bg}")
#             return

#         popup = tk.Toplevel(root)
#         popup.title(f"Donors with Blood Group {bg}")
#         text = tk.Text(popup, wrap="word", width=70, height=20)
#         text.pack(padx=10, pady=10)

#         for fields in matches:
#             display = (
#                 f"Name: {fields[0]}, Age: {fields[1]}, Blood: {fields[2]}, "
#                 f"Location: {fields[3]}, Pincode: {fields[4]}, Phone: {fields[5]}\n"
#             )
#             text.insert(tk.END, display)
#     except FileNotFoundError:
#         messagebox.showerror("Error", "donors.txt not found")

# def search_by_bg_and_location():
#     bg = simpledialog.askstring("Search", "Enter Blood Group:")
#     loc = simpledialog.askstring("Search", "Enter Location:")
#     if not (bg and loc):
#         return

#     try:
#         with open("donors.txt", "r") as file:
#             data = file.readlines()

#         matches = []
#         for line in data:
#             fields = line.strip().split(',')
#             if len(fields) >= 4 and fields[2].upper() == bg.upper() and fields[3].lower() == loc.lower():
#                 matches.append(fields)

#         if not matches:
#             messagebox.showinfo("Result", f"No donors with {bg} in {loc}")
#             return

#         popup = tk.Toplevel(root)
#         popup.title(f"Donors with {bg} in {loc}")
#         text = tk.Text(popup, wrap="word", width=70, height=20)
#         text.pack(padx=10, pady=10)

#         for fields in matches:
#             display = (
#                 f"Name: {fields[0]}, Age: {fields[1]}, Blood: {fields[2]}, "
#                 f"Location: {fields[3]}, Pincode: {fields[4]}, Phone: {fields[5]}\n"
#             )
#             text.insert(tk.END, display)
#     except FileNotFoundError:
#         messagebox.showerror("Error", "donors.txt not found")

# def find_nearest_donors():
#     try:
#         user_pin = simpledialog.askinteger("Nearest Donors", "Enter your Pincode:")
#         if not user_pin:
#             return

#         with open("donors.txt", "r") as file:
#             data = file.readlines()

#         donors = []
#         for line in data:
#             fields = line.strip().split(',')
#             if len(fields) >= 5:
#                 try:
#                     donor_pin = int(fields[4])
#                     distance = abs(user_pin - donor_pin)
#                     donors.append((distance, fields))
#                 except:
#                     continue

#         donors.sort(key=lambda x: x[0])

#         if not donors:
#             messagebox.showinfo("Result", "No donors found.")
#             return

#         popup = tk.Toplevel(root)
#         popup.title("Nearest Donors")
#         text = tk.Text(popup, wrap="word", width=70, height=20)
#         text.pack(padx=10, pady=10)

#         for distance, fields in donors:
#             display = (
#                 f"Name: {fields[0]}, Age: {fields[1]}, Blood: {fields[2]}, "
#                 f"Location: {fields[3]}, Pincode: {fields[4]}, Phone: {fields[5]}, Distance: {distance}\n"
#             )
#             text.insert(tk.END, display)
#     except FileNotFoundError:
#         messagebox.showerror("Error", "donors.txt not found")

# # GUI layout
# root = tk.Tk()
# root.title("Blood Donor Management")

# labels = ["Name", "Age", "Blood Group", "Location", "Pincode", "Phone"]
# entries = []

# for i, label in enumerate(labels):
#     tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
#     entry = tk.Entry(root)
#     entry.grid(row=i, column=1, padx=10, pady=5)
#     entries.append(entry)

# name_entry, age_entry, blood_entry, location_entry, pincode_entry, phone_entry = entries

# tk.Button(root, text="Register Donor", command=register_donor).grid(row=6, columnspan=2, pady=5)
# tk.Button(root, text="Show All Donors", command=show_all_donors).grid(row=7, columnspan=2, pady=5)
# tk.Button(root, text="Search by Blood Group", command=search_by_blood_group).grid(row=8, columnspan=2, pady=5)
# tk.Button(root, text="Search by BG + Location", command=search_by_bg_and_location).grid(row=9, columnspan=2, pady=5)
# tk.Button(root, text="Nearest Donors (Pincode)", command=find_nearest_donors).grid(row=10, columnspan=2, pady=5)

# root.mainloop()


import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess

# ---------------------- Function: Register Donor ----------------------
def register_donor():
    name = name_entry.get()
    age = age_entry.get()
    blood = blood_entry.get()
    location = location_entry.get()
    pincode = pincode_entry.get()
    phone = phone_entry.get()

    if not (name and age and blood and location and pincode and phone):
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        result = subprocess.run(
            ["register.exe", name, age, blood, location, pincode, phone],
            capture_output=True,
            text=True
        )
        messagebox.showinfo("Result", result.stdout.strip())
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# ---------------------- Function: Show All Donors ----------------------
def show_all_donors():
    try:
        with open("donors.txt", "r") as file:
            data = file.readlines()

        if not data:
            messagebox.showinfo("Donors", "No donors found.")
            return

        popup = tk.Toplevel(root)
        popup.title("All Donors")
        text = tk.Text(popup, wrap="word", width=70, height=20)
        text.pack(padx=10, pady=10)

        for line in data:
            fields = line.strip().split(',')
            if len(fields) >= 6:
                display = (
                    f"Name: {fields[0]}, Age: {fields[1]}, Blood: {fields[2]}, "
                    f"Location: {fields[3]}, Pincode: {fields[4]}, Phone: {fields[5]}\n"
                )
                text.insert(tk.END, display)
    except FileNotFoundError:
        messagebox.showerror("Error", "donors.txt file not found.")

# ---------------------- Function: Search by Blood Group ----------------------
def search_by_blood_group():
    bg = simpledialog.askstring("Search", "Enter Blood Group (e.g., A+, B-, O+):")
    if not bg:
        return

    try:
        with open("donors.txt", "r") as file:

            data = file.readlines()

        matches = []
        for line in data:
            fields = line.strip().split(',')
            if len(fields) >= 3 and fields[2].upper() == bg.upper():
                matches.append(fields)

        if not matches:
            messagebox.showinfo("Result", f"No donors with blood group {bg}")
            return

        popup = tk.Toplevel(root)
        popup.title(f"Donors with Blood Group {bg}")
        text = tk.Text(popup, wrap="word", width=70, height=20)
        text.pack(padx=10, pady=10)

        for fields in matches:
            display = (
                f"Name: {fields[0]}, Age: {fields[1]}, Blood: {fields[2]}, "
                f"Location: {fields[3]}, Pincode: {fields[4]}, Phone: {fields[5]}\n"
            )
            text.insert(tk.END, display)
    except FileNotFoundError:
        messagebox.showerror("Error", "donors.txt not found")

# ---------------------- Function: Search by BG + Location ----------------------
def search_by_bg_and_location():
    bg = simpledialog.askstring("Search", "Enter Blood Group:")
    loc = simpledialog.askstring("Search", "Enter Location:")
    if not (bg and loc):
        return

    try:
        with open("donors.txt", "r") as file:
            data = file.readlines()

        matches = []
        for line in data:
            fields = line.strip().split(',')
            if len(fields) >= 4 and fields[2].upper() == bg.upper() and fields[3].lower() == loc.lower():
                matches.append(fields)

        if not matches:
            messagebox.showinfo("Result", f"No donors with {bg} in {loc}")
            return

        popup = tk.Toplevel(root)
        popup.title(f"Donors with {bg} in {loc}")
        text = tk.Text(popup, wrap="word", width=70, height=20)
        text.pack(padx=10, pady=10)

        for fields in matches:
            display = (
                f"Name: {fields[0]}, Age: {fields[1]}, Blood: {fields[2]}, "
                f"Location: {fields[3]}, Pincode: {fields[4]}, Phone: {fields[5]}\n"
            )
            text.insert(tk.END, display)
    except FileNotFoundError:
        messagebox.showerror("Error", "donors.txt not found")

# ---------------------- Function: Find Nearest Donors ----------------------
def find_nearest_donors():
    try:
        user_pin = simpledialog.askinteger("Nearest Donors", "Enter your Pincode:")
        if not user_pin:
            return

        with open("donors.txt", "r") as file:
            data = file.readlines()

        donors = []
        for line in data:
            fields = line.strip().split(',')
            if len(fields) >= 5:
                try:
                    donor_pin = int(fields[4])
                    distance = abs(user_pin - donor_pin)
                    donors.append((distance, fields))
                except:
                    continue

        donors.sort(key=lambda x: x[0])

        if not donors:
            messagebox.showinfo("Result", "No donors found.")
            return

        popup = tk.Toplevel(root)
        popup.title("Nearest Donors")
        text = tk.Text(popup, wrap="word", width=70, height=20)
        text.pack(padx=10, pady=10)

        for distance, fields in donors:
            display = (
                f"Name: {fields[0]}, Age: {fields[1]}, Blood: {fields[2]}, "
                f"Location: {fields[3]}, Pincode: {fields[4]}, Phone: {fields[5]}, Distance: {distance}\n"
            )
            text.insert(tk.END, display)
    except FileNotFoundError:
        messagebox.showerror("Error", "donors.txt not found")

# ---------------------- GUI Layout and Design ----------------------
root = tk.Tk()
root.title("🩸 Blood Donor Management System")
root.geometry("450x600")
root.configure(bg="#e3f2fd")  # Light blue background

font_label = ("Segoe UI", 10)
font_entry = ("Segoe UI", 10)
font_button = ("Segoe UI", 10, "bold")
btn_color = "#1976D2"
btn_fg = "#ffffff"

# --- App Title ---
tk.Label(root, text="Blood Donor Management", font=("Segoe UI", 16, "bold"),
         bg="#e3f2fd", fg="#0d47a1", pady=10).pack()

# --- Main Form Frame ---
form_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, bd=2, relief="groove")
form_frame.pack(pady=10, padx=20, fill="both", expand=True)

# --- Input Fields ---
labels = ["Name", "Age", "Blood Group", "Location", "Pincode", "Phone"]
entries = []

for i, label in enumerate(labels):
    tk.Label(form_frame, text=label, font=font_label, bg="#ffffff").grid(row=i, column=0, sticky="w", pady=5)
    entry = tk.Entry(form_frame, font=font_entry, width=25)
    entry.grid(row=i, column=1, pady=5, padx=10)
    entries.append(entry)

name_entry, age_entry, blood_entry, location_entry, pincode_entry, phone_entry = entries

# --- Buttons Section ---
btn_frame = tk.Frame(form_frame, bg="#ffffff")
btn_frame.grid(row=7, columnspan=2, pady=20)

tk.Button(btn_frame, text="Register Donor", font=font_button, bg=btn_color, fg=btn_fg,
          command=register_donor, width=25).pack(pady=5)

tk.Button(btn_frame, text="Show All Donors", font=font_button, bg=btn_color, fg=btn_fg,
          command=show_all_donors, width=25).pack(pady=5)

tk.Button(btn_frame, text="Search by Blood Group", font=font_button, bg=btn_color, fg=btn_fg,
          command=search_by_blood_group, width=25).pack(pady=5)

tk.Button(btn_frame, text="Search by BG + Location", font=font_button, bg=btn_color, fg=btn_fg,
          command=search_by_bg_and_location, width=25).pack(pady=5)

tk.Button(btn_frame, text="Nearest Donors (Pincode)", font=font_button, bg=btn_color, fg=btn_fg,
          command=find_nearest_donors, width=25).pack(pady=5)

root.mainloop()
