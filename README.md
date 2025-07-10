# Blood Donor Management System (C++ + Python GUI)

This project is a real-life Blood Donor Management System built using C++ for core logic and data storage, and Python (Tkinter) for a user-friendly graphical interface.

It helps users register as donors, search for donors by blood group or location, and find the nearest available donors based on pincode.

![image](https://github.com/user-attachments/assets/54aac693-0771-4a1a-936d-d6ee054c1a19)


---

## Features

- Register new blood donors
- Search donors by:
  - Blood Group (e.g., A+, O-)
  - Blood Group + Location
  - Nearest donors using Pincode
- Display all registered donors
- Data saved in `donors.txt` using file handling

---

## Tech Stack

| Language/Tool | Usage |
|---------------|--------|
| C++           | Core logic and file storage |
| Python        | GUI (Tkinter) |
| Tkinter       | Interface elements (buttons, forms, popups) |
| VS Code       | Code editor |
| Git & GitHub  | Version control and hosting |


---

## Project Structure

```
├── blood_donation.cpp        # Full-feature C++ console logic
├── register.cpp              # C++ file to register donor (used with GUI)
├── register.exe              # Compiled .exe for GUI to call
├── donor_gui.py              # Python GUI using Tkinter
├── donors.txt                # Text file where all donor data is stored
├── README.md                 # You’re reading this
```

---

## How to Run

### Requirements

- Python installed (version 3.6 or higher recommended)
- Compile the C++ files to executables using:
  ```
  g++ register.cpp -o register.exe
  g++ blood_donation.cpp -o blood_donation.exe
  ```

## Then run the GUI:

python donor_gui.py


---

**Real-World Use Case**

- Hospitals or individuals in need of blood can quickly find suitable donors.
- Donors can be filtered by location and proximity using pincode logic.

