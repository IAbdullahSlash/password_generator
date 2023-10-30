import customtkinter as ctk
import random
import pyperclip

ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title('Password Generater')
window.geometry('400x500')

uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lowercase = 'qwertyuiopasdfghjklzxcvbnm'
digits = '0123456789'
symbols = '*/~!@#$%^&*\;?><'

def gen():  
  pasentry.delete(0, 'end')
  alphaselection = fcomdo.get()
  symbolselection = symbolcombo.get()
  digitselection = degitcombo.get()
  if alphaselection== 'mixed (recommended)' and symbolselection=='mixed (recommended)':
    upper , lower, nums, syms = True, True, True, True
    all = ""
    if upper:
      all += uppercase
    if lower:
      all += lowercase
    if nums:
      all += digits
    if syms:
      all += symbols
    for i in range(1):
      password = "".join(random.sample(all, 16))
    pasentry.insert(0, password)  
    if digitselection=='4 digit':
      pasentry.delete(4, 'end')
      progressbar_1.set(0.2)
      progressbar_1.configure(progress_color='#FF0000')
      status.configure(text='weak')
    elif digitselection=='6 digit':
      pasentry.delete(6, 'end')
      progressbar_1.set(0.5)
      progressbar_1.configure(progress_color='#F8A005')
      status.configure(text='good')
    elif digitselection=='8 digit':
      pasentry.delete(8, 'end')
      progressbar_1.set(0.8)
      progressbar_1.configure(progress_color='#E6E919')
      status.configure(text='strong')
    elif digitselection=='16 digit':
      progressbar_1.set(1)
      progressbar_1.configure(progress_color='#26C916')
      status.configure(text='secure')
  elif alphaselection=='lower case only':
    upper, lower, nums, syms = False, True, False, False
    all = ""
    if upper: 
      all += uppercase
    if lower:
      all += lowercase
    if nums:
      all += digits
    if syms:
      all += symbols
    for i in range(1):
      password = "".join(random.sample(all, 16))
    pasentry.insert(0, password)
    if digitselection=='4 digit':
      pasentry.delete(4, 'end')
      progressbar_1.set(0.2)
      progressbar_1.configure(progress_color='#FF0000')
      status.configure(text='weak')
    elif digitselection=='6 digit':
      pasentry.delete(6, 'end')
      progressbar_1.set(0.5)
      progressbar_1.configure(progress_color='#F8A005')
      status.configure(text='good')
    elif digitselection=='8 digit':
      pasentry.delete(8, 'end')
      progressbar_1.set(0.8)
      progressbar_1.configure(progress_color='#E6E919')
      status.configure(text='strong')
    elif digitselection=='16 digit':
      progressbar_1.set(1)
      progressbar_1.configure(progress_color='#26C916')
      status.configure(text='secure')
  elif alphaselection=='Upper case only':
    upper, lower, nums, syms = True, False, False, False
    all = ""
    if upper:
      all += uppercase
    if lower:
      all += lowercase
    if nums:
      all += digits
    if syms:
      all += symbols
    for i in range(1):
      password = "".join(random.sample(all, 16))
    pasentry.insert(0, password)
    if digitselection=='4 digit':
      pasentry.delete(4, 'end')
      progressbar_1.set(0.2)
      progressbar_1.configure(progress_color='#FF0000')
      status.configure(text='weak')
    elif digitselection=='6 digit':
      pasentry.delete(6, 'end')
      progressbar_1.set(0.5)
      progressbar_1.configure(progress_color='#F8A005')
      status.configure(text='good')
    elif digitselection=='8 digit':
      pasentry.delete(8, 'end')
      progressbar_1.set(0.8)
      progressbar_1.configure(progress_color='#E6E919')
      status.configure(text='strong')
    elif digitselection=='16 digit':
      progressbar_1.set(1)
      progressbar_1.configure(progress_color='#26C916')
      status.configure(text='secure')
  elif symbolselection=='numbers only':
    upper , lower, nums, syms = False, False, True, False
    all = ""
    if nums:
      all += digits
    for i in range(1):
      password = "".join(random.sample(all, 9))
    pasentry.insert(0, password)
    if digitselection=='4 digit':
      pasentry.delete(4, 'end')
      progressbar_1.set(0.2)
      progressbar_1.configure(progress_color='#FF0000')
      status.configure(text='weak')
    elif digitselection=='6 digit':
      pasentry.delete(6, 'end')
      progressbar_1.set(0.5)
      progressbar_1.configure(progress_color='#F8A005')
      status.configure(text='good')
    elif digitselection=='8 digit':
      pasentry.delete(8, 'end')
      progressbar_1.set(0.8)
      progressbar_1.configure(progress_color='#E6E919')
      status.configure(text='strong')
    elif digitselection=='16 digit':
      progressbar_1.set(1)
      progressbar_1.configure(progress_color='#26C916')
      status.configure(text='secure')
  elif symbolselection=='symbols only':
    upper , lower, nums, syms = False, False, False, True
    all = ""
    if syms:
      all += symbols
    for i in range(1):
      password = "".join(random.sample(all, 16))
    pasentry.insert(0, password)
    if digitselection=='4 digit':
      pasentry.delete(4, 'end')
      progressbar_1.set(0.2)
      progressbar_1.configure(progress_color='#FF0000')
      status.configure(text='weak')
    elif digitselection=='6 digit':
      pasentry.delete(6, 'end')
      progressbar_1.set(0.5)
      progressbar_1.configure(progress_color='#F8A005')
      status.configure(text='good')
    elif digitselection=='8 digit':
      pasentry.delete(8, 'end')
      progressbar_1.set(0.8)
      progressbar_1.configure(progress_color='#E6E919')
      status.configure(text='strong')
    elif digitselection=='16 digit':
      progressbar_1.set(1)
      progressbar_1.configure(progress_color='#26C916')
      status.configure(text='secure')  

dark_mode = True
def mode():
  global dark_mode
  if dark_mode:
    ctk.set_appearance_mode("light")
  else:
    ctk.set_appearance_mode("dark")
  dark_mode = not dark_mode 

def copybutt():
  password = pasentry.get()
  if password:
    pyperclip.copy(password)
    copiedmess.configure(text='Copied successfully!')
  else:
    copiedmess.configure(text='Try again!')

headlabel = ctk.CTkLabel(window, text='Password Generator', font=('Arial', 30))
headlabel.pack(pady=60)

frame = ctk.CTkFrame(window)
frame.pack()

degitlabel = ctk.CTkLabel(frame, text='Number of digits:')
degitlabel.grid(row=3, column=0, pady=3, columnspan=2)

digitlist = ['4 digit','6 digit', '8 digit', '16 digit']
degitcombo = ctk.CTkComboBox(frame, values=digitlist)
degitcombo.grid(row=4, column=0, pady=10, columnspan=2)

pasentry = ctk.CTkEntry(frame, width=200)
pasentry.insert(0, 'password')
pasentry.grid(row=5, column=0, columnspan=2, pady=10, padx=20)

genbutton = ctk.CTkButton(frame, text='Generate', command=gen, cursor='hand2', width=300)
genbutton.grid(row=8, column=0, pady=10, columnspan=2)

alphalabel = ctk.CTkLabel(frame, text='Alphabets:')
alphalabel.grid(row=0, column=0, pady=5)

alphalist = ['mixed (recommended)', 'Upper case only', 'lower case only']
fcomdo = ctk.CTkComboBox(frame, values=alphalist)
fcomdo.set(alphalist[0])
fcomdo.grid(row=1, column=0, pady=10, padx=10)

symbolslabel = ctk.CTkLabel(frame, text='Symbols:')
symbolslabel.grid(row=0, column=1, padx=5)

symbollist = ['mixed (recommended)', 'numbers only', 'symbols only']
symbolcombo = ctk.CTkComboBox(frame, values=symbollist)
symbolcombo.set(symbollist[0])
symbolcombo.grid(row=1, column=1, pady=10, padx=10)

themebutton = ctk.CTkSwitch(frame, text='Mode', command=mode)
themebutton.grid(row=9, column=0, pady=10)

copbutton = ctk.CTkButton(frame, text='Copy', width=50, cursor='hand2', command=copybutt)
copbutton.place(x=265, y=178)

copiedmess = ctk.CTkLabel(frame, text='')
copiedmess.grid(row=7, column=0, columnspan=2, pady=10)

progressbar_1 = ctk.CTkProgressBar(frame)
progressbar_1.place(x=60, y=218)
progressbar_1.set(0)

status = ctk.CTkLabel(frame, text='')
status.place(x=273, y=208)

window.mainloop()
