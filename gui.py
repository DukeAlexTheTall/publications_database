import tkinter as tk
import pandas as pd

authors_data = pd.read_csv('authors.csv')

def list_of_authors(data):
    listbox_authors.delete(0, 'end')
    auth_list = sorted(list(set(data.name)))
    for name in auth_list:
        listbox_authors.insert('end', name)

def list_of_publishings(data):
    auth_name_index = listbox_authors.curselection()
    if len(auth_name_index) > 0:
        auth_name = listbox_authors.get(auth_name_index)
        var_auth.set(auth_name)
        pub_list = sorted(list(set(data.publication_name.where(data['name']==auth_name)))[1:])
        listbox_publishings.delete(0, 'end')
        for publication in pub_list:
            listbox_publishings.insert('end', publication)

def get_publication_info(data):
    publ_name_index = listbox_publishings.curselection()
    if len(publ_name_index) > 0:
        publ_name = listbox_publishings.get(publ_name_index)
        publ_details = data.loc[data['publication_name'] == publ_name]
        details_frame.configure(text=publ_details)

window = tk.Tk()
window.title('Publications')

listbox_authors = tk.Listbox(master=window, selectbackground="yellow", height=20)
listbox_authors.grid(row=0, column=0, padx=1, columnspan=2, rowspan=3 ,sticky='WE')

listbox_publishings = tk.Listbox(master=window, selectbackground="yellow", height=10, width=50)
listbox_publishings.grid(row=0, column=2, padx=1, columnspan=2, sticky='NS')

bt_open_authors = tk.Button(window, text='List authors', command=lambda:list_of_authors(authors_data))
bt_open_authors.grid(row=3, column=0)

bt_open_publications = tk.Button(window, text='List publications', command=lambda:list_of_publishings(authors_data))
bt_open_publications.grid(row=3, column=1)

var_auth = tk.StringVar()
label_author_name = tk.Label(window, textvariable=var_auth)
label_author_name.grid(row=1, column=2, sticky='NW')

bt_publication_details = tk.Button(window, text='Show details', command=lambda:get_publication_info(authors_data))
bt_publication_details.grid(row=1, column=3, sticky='NE')

details_frame = tk.Label(window, relief='sunken')
details_frame.grid(row=2, column=2, columnspan=3, rowspan=2, padx=2, pady=2, sticky='WNES')

window.mainloop()
