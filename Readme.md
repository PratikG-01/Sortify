# Sortify - An Automated File Organizer (Python)

A clean, config-driven Python utility that automatically organizes files in a directory into structured folders based on file type — safely and efficiently.

---

##  Problem

Folders like **Downloads** quickly become cluttered with mixed file types.  
Manually organizing them is time-consuming and error-prone, especially when files share the same names.

---

##  Solution

This tool scans a target directory and:
- Categorizes files by extension
- Creates folders automatically
- Moves files safely without overwriting
- Keeps configuration separate from logic for easy customization

Designed to be simple, safe, and practical for real-world use.

---

##  Features

- Organizes files by type (Images, Documents, Videos, etc.)
- Config-driven behavior (`config.py`)
- Safe filename conflict handling (auto-renaming)
- Skips hidden files (optional)
- Clean CLI output
- No external dependencies

---

##  Tech Stack

- Python 3
- `pathlib`
- `shutil`
- Standard Libraries only

---

##  How to Run

1. Clone the repository

   git clone https://github.com/your-username/file-organizer.git

---

## Configuration

All behavior is controlled via config.py.
You can:

- Add or modify file categories

- Change the default target folder

- Enable/disable overwrite protection

- Control output verbosity

- No changes to core logic required.

---

##  License

This project is open-source and available under the MIT License.

---







