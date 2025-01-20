# import requests
# response = requests.get("https://api.opendota.com/api/heroes")
#
# name = response.json()[0]["localized_name"]
# print(name)

import tkinter as tk
from tkinter import ttk
     

def main():
    root = tk.Tk()
    root.title("DOTA_HEROES")
    title = root.title()

    window_width = 600 
    window_height = 400 

    #Screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    #centre point 
    centre_x = int(screen_width/2 - window_width/2)
    centre_y = int(screen_height/2 - window_height/2)
    
    #set the position of the window
    root.geometry(f"{window_width}x{window_height}+{centre_x}+{centre_y}")
    
    root.columnconfigure(0,weight=1)
    
    input_frame, keyword_entry = create_input_frame(root)
    input_frame.grid(column=0, row=0)
    
    button_frame = create_button_frame(root, keyword_entry)
    button_frame.grid(column=1, row=0)
    
    root.mainloop()

def create_input_frame(container)->tuple[ttk.Frame, ttk.Entry]:
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    #Find Hero
    ttk.Label(frame, text="Hero Name").grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)
    return frame, keyword


def create_button_frame(container, keyword_entry)->ttk.Frame:
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    #search button
    ttk.Button(frame, text="Search", command=lambda: on_search(keyword_entry)).grid(column=0, row=0)
    return frame

def on_search(entry):
    print(entry.get())

if __name__ == "__main__":
    main()
