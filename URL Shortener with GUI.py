#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pyshorteners
from tkinter import *

window = Tk()
window.title("URL Shortener")

def shrink():
    shortener=pyshorteners.Shortener()
    res=shortener.tinyurl.short(e1.get())
    label_text.set(res)



label_text=StringVar();
Label(window, text="Enter Your URL:").grid(row=0, sticky=W)
Label(window, text="Shortened URL:").grid(row=3, sticky=W)
result = Label(window, text="", textvariable=label_text).grid(row=3,column=1, sticky=W)
 
e1 = Entry(window, width = 50)

shortener=pyshorteners.Shortener()
e1.grid(row=0, column=1)
 
b = Button(window, text="Shorten", command=shrink)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

window.mainloop()

