from tkinter import ttk
import tkinter as tk
# Creating tkinter my_w
my_w = tk.Tk()
my_w.geometry("300x280") 
my_w.title("www.plus2net.com")  
# Using treeview widget
trv = ttk.Treeview(my_w, selectmode ='browse')
trv.grid(row=0,column=0,padx=30,pady=20)

# column identifiers 
trv["columns"] = ("1", "2")
# Defining headings, other option is tree
trv['show'] = 'tree' 
# width of columns and alignment 
trv.column("#0", width = 80, anchor ='c')
trv.column("1", width = 10, anchor ='c')
trv.column("2", width = 100, anchor ='c')
# Headings  
# respective columns
trv.heading("#0", text ="Label",anchor='c')
trv.heading("1", text ="id")
trv.heading("2", text ="Name",anchor='c')

trv.insert("",'end',iid=1,text='First',values=(1,'n1-Alex'))
trv.insert("",'end',iid=2,text='second',values=(2,'n2-Ravi'))
trv.insert("",'end',iid=3,text='third',values=(3,'n3-Ronn'))
trv.insert("",'end',iid=4,text='third',values=(4,'n3-Ronn'))
trv.insert("",'end',iid=5,text='third',values=(5,'n3-Ronn'))
trv.insert("",'end',iid=6,text='third',values=(6,'n3-Ronn'))
trv.insert("",'end',iid=7,text='third',values=(7,'n3-Ronn'))
trv.insert("",'end',iid=8,text='third',values=(8,'n3-Ronn'))
trv.insert("",'end',iid=9,text='third',values=(9,'n3-Ronn'))
trv.insert("",'end',iid=10,text='third',values=(10,'n3-Ronn'))
trv.insert("",'end',iid=11,text='third',values=(11,'n3-Ronn'))


#hs = ttk.Scrollbar(my_w,orient="vertical", command=trv.yview)#H Scrollbar 
#trv.configure(xscrollcommand=hs.set)  # connect to Treeview
#hs.grid(row=0,column=1,sticky='ew')
vs = ttk.Scrollbar(my_w,orient="vertical", command=trv.yview)#V Scrollbar
trv.configure(yscrollcommand=vs.set)  # connect to Treeview
vs.grid(row=0,column=1,sticky='ns')


my_w.mainloop()
