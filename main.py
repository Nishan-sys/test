import tkinter
from tkinter import ttk

#main windows
main_window = tkinter.Tk() #define the window
main_window.title("නිව් ට්‍රේඩ් සෙන්ටර්") #main window title
main_window.geometry("500x400")

notebook = ttk.Notebook(main_window)

tab1 = tkinter.Frame(notebook)
tab2 = tkinter.Frame(notebook)
tab3 = tkinter.Frame(notebook)
tab4 = tkinter.Frame(notebook)
tab5 = tkinter.Frame(notebook)
tab6 = tkinter.Frame(notebook)


notebook.add(tab1,text="මිල දී ගැනීම්")
notebook.add(tab2,text="විකිණීම්")
notebook.add(tab3,text="ගැනුම්කරුවන්")
notebook.add(tab4,text="අයිතිකරුවන්")
notebook.add(tab5,text="Items")
notebook.add(tab6,text="Summary")

notebook.pack(expand=True,fill="both")

#-----------------start of farmers labels and entries
#Farmers name
name_label = tkinter.Label(tab4, text="අයිතිකරුගේ නම :")
name_label.grid(column=0,row=0)
name_entry = tkinter.Entry(tab4)
name_entry.grid(column=1,row=0)

#farmers short name
short_name_label = tkinter.Label(tab4, text="අයිතිකරුගේ කෙටි නම :")
short_name_label.grid(column=0,row=1)
short_name_entry = tkinter.Entry(tab4)
short_name_entry.grid(column=1,row=1)

#farmers nic

nic_label = tkinter.Label(tab4, text="අයිතිකරුගේ හැදුනුමිපත් අංකය :")
nic_label.grid(column=0,row=2)
nic_entry = tkinter.Entry(tab4)
nic_entry.grid(column=1,row=2)


#farmers telphone
tel1_label = tkinter.Label(tab4, text="අයිතිකරුගේ දුරකතන අංකය 1 :")
tel1_label.grid(column=0,row=3)
tel1_entry = tkinter.Entry(tab4)
tel1_entry.grid(column=1,row=3)


tel2_label = tkinter.Label(tab4, text="අයිතිකරුගේ දුරකතන අංකය 2 :")
tel2_label.grid(column=0,row=4)
tel2_entry = tkinter.Entry(tab4)
tel2_entry.grid(column=1,row=4)


tel3_label = tkinter.Label(tab4, text="අයිතිකරුගේ දුරකතන අංකය 3 :")
tel3_label.grid(column=0,row=5)
tel3_entry = tkinter.Entry(tab4)
tel3_entry.grid(column=1,row=5)

address_label = tkinter.Label(tab4,text="අයිතිකරුගේ ලිපිනය:")
address_label.grid(column=0,row=6)
address_entry = tkinter.Entry(tab4)
address_entry.grid(column=1,row=6)
#---------------end of farmers labes and entries

#-----------------start of buyers labels and entries
#Farmers name
name_label = tkinter.Label(tab3, text="ගැනුම්කරුගේ නම :")
name_label.grid(column=0,row=0)
name_entry = tkinter.Entry(tab3)
name_entry.grid(column=1,row=0)

#farmers short name
short_name_label = tkinter.Label(tab3, text="ගැනුම්කරුගේ කෙටි නම :")
short_name_label.grid(column=0,row=1)
short_name_entry = tkinter.Entry(tab3)
short_name_entry.grid(column=1,row=1)

#farmers nic

nic_label = tkinter.Label(tab3, text="ගැනුම්කරුගේ හැදුනුමිපත් අංකය :")
nic_label.grid(column=0,row=2)
nic_entry = tkinter.Entry(tab3)
nic_entry.grid(column=1,row=2)


#farmers telphone
tel1_label = tkinter.Label(tab3, text="ගැනුම්කරුගේ දුරකතන අංකය 1 :")
tel1_label.grid(column=0,row=3)
tel1_entry = tkinter.Entry(tab3)
tel1_entry.grid(column=1,row=3)


tel2_label = tkinter.Label(tab3, text="ගැනුම්කරුගේ දුරකතන අංකය 2 :")
tel2_label.grid(column=0,row=4)
tel2_entry = tkinter.Entry(tab3)
tel2_entry.grid(column=1,row=4)


tel3_label = tkinter.Label(tab3, text="ගැනුම්කරුගේ දුරකතන අංකය 3 :")
tel3_label.grid(column=0,row=5)
tel3_entry = tkinter.Entry(tab3)
tel3_entry.grid(column=1,row=5)

address_label = tkinter.Label(tab3,text="ගැනුම්කරුගේ ලිපිනය:")
address_label.grid(column=0,row=6)
address_entry = tkinter.Entry(tab3)
address_entry.grid(column=1,row=6)
#---------------end of buyers labes and entries

main_window.mainloop()