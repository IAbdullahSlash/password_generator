Password Generator
A secure and customizable password generator built with Python and customtkinter for a modern GUI. Generate strong passwords with options for length, character types, and more.

Demo (Replace with actual screenshot)

Features
Customizable Passwords: Choose between:

Mixed case (recommended)

Uppercase only

Lowercase only

Numbers only

Symbols only

Password Length: 4, 6, 8, or 16 characters.

Strength Meter: Visual feedback on password strength (Weak/Good/Strong/Secure).

Dark/Light Mode: Toggle between themes.

One-Click Copy: Copy generated passwords to clipboard instantly.

Installation
Prerequisites:

Python 3.6+

Pip (Python package manager)

Install dependencies:

bash
pip install customtkinter pyperclip
Run the application:

bash
python MyPro.py
Usage
Select Alphabet Type (e.g., mixed, uppercase).

Select Symbol Type (e.g., mixed, numbers only).

Choose Password Length (4–16 digits).

Click Generate to create a password.

Click Copy to save it to your clipboard.

Code Structure
gen(): Handles password generation based on user selections.

mode(): Toggles between dark/light themes.

copybutt(): Copies the password to the clipboard.

GUI: Built with customtkinter for a sleek, modern interface.

Screenshots
(Add actual screenshots here)

Main Window

Light Mode Example

Strength Indicator

Contributing
Pull requests are welcome! For major changes, open an issue first.
