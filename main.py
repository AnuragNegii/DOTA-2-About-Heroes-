import requests
import tkinter as tk
from tkinter import ttk
     

def main():
    response = requests.get("https://api.opendota.com/api/heroes")
    list_of_heroes= response.json()
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

    text_frame, text_widget = create_text_frame(root)
    text_frame.grid(column=0, row=1, sticky="nsew")
    
    button_frame = create_button_frame(root, keyword_entry, list_of_heroes, text_widget)
    button_frame.grid(column=1, row=0)

    root.rowconfigure(1, weight=1)
    
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

def create_button_frame(container, keyword_entry, list_of_heroes, text_widget)->ttk.Frame:
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    #search button
    ttk.Button(frame, text="Search", command=lambda: on_search(keyword_entry, list_of_heroes, text_widget)).grid(column=0, row=0)
    return frame

def create_text_frame(container):
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    text = tk.Text(frame, height=8, wrap="word")
    text.grid(column=0, row=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text.yview)
    scrollbar.grid(column=1, row=0, sticky="ns")
    text.configure(yscrollcommand=scrollbar.set)
    return frame, text
 
def on_search(entry, list_of_heroes, text_widget):
    search = entry.get().lower()
    text_widget.delete("1.0", tk.END)
    hero_details = {} 
    for hero in list_of_heroes:
        if hero["localized_name"].lower() == search:
            hero_details = f"Hero Name: {hero['localized_name']}\n" \
                           f"Primary Attribute: {hero['primary_attr']}\n" \
                           f"Attack Type: {hero['attack_type']}\n" \
                           f"Roles: {', '.join(hero['roles'])}\n"
            text_widget.insert(tk.END, hero_details)
            return
    print("NOT Found")

if __name__ == "__main__":
    main()
