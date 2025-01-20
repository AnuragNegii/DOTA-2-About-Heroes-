# import requests
# response = requests.get("https://api.opendota.com/api/heroes")
#
# name = response.json()[0]["localized_name"]
# print(name)

import tkinter as tk
from tkinter import ttk
     

root = tk.Tk()
root.title("DOTA_HEROES")
title = root.title()

window_width = 1980
window_height = 1080

#Screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#centre point 
centre_x = int(screen_width/2 - window_width/2)
centre_y = int(screen_height/2 - window_height/2)

#set the position of the window
root.geometry(f"{window_width}x{window_height}+{centre_x}+{centre_y}")

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()
 
frame = ttk.Frame(root)
frame.pack(fill= "both", expand=True, padx=10, pady=10)
search_bar = ttk.Entry(frame)
search_bar.pack(ipadx= 20, ipady=5,expand=True, anchor="center", pady = 10)

# search_button = ttk.Button(root, text="Search", command=lambda: root.quit())
# search_button.pack(ipadx= 5, 
#                    ipady= 5,
#                    expand=True)
print(title)
# message = tk.Label(root, text="DOTA, World")
# message.pack()
root.mainloop()
