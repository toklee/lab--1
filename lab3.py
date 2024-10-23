import tkinter as tk
from chat import connector, reader,send_msg,read_msg
import threading
import time
from time import strftime
username='nn'
MSG_HEIGHT = 2
msg = []
msg_lbls = []
maxm=10

def init_gui():
    root = tk.Tk()
    return root
def init_input(fr_input,fr_list):
    txt_entry= tk.Entry(fr_input)
    label = tk.Label(text="name", bg='pink')
    name_entry = tk.Entry()
    name_entry.insert(0,username)
    def click(txt_entry):
        text=txt_entry.get()
        msg={
            'user':name_entry.get(),
            'text':text
        }
        send_msg(msg)
        add_label(text)
        print('meow')
    tk_bt = tk.Button(fr_input,bg='purple',text="send",command=lambda : click(txt_entry))
    txt_entry.pack(side=tk.LEFT,fill=tk.X, expand = True)
    tk_bt.pack(side=tk.LEFT)
    label.pack(side=tk.LEFT)
    name_entry.pack(side=tk.LEFT)
    style.configure("TButton", padding=6, relief="flat", background="#ccc")


def add_label(text):
    lbl_msg = tk.Label(fr_list_msg,text=text,height=MSG_HEIGHT, background = 'purple')
    lbl_msg.pack(anchor='ne',side=tk.TOP,padx=2,pady=2)
    msg_lbls.append(lbl_msg)
    if len(msg_lbls)>maxm:
        label=lbl_msg.pop(0)
        label.destroy()
def init_frames(root):
    fr_list_msg = tk.Frame(root)
    fr_input_msg = tk.Frame(root)
    fr_list_msg.pack(fill=tk.BOTH,expand=True)
    fr_input_msg.pack(fill=tk.X, side=tk.BOTTOM)

    lbl_grit = tk.Label(fr_list_msg,text="chatik",height=MSG_HEIGHT)
    lbl_grit.pack(side=tk.TOP)
    return fr_list_msg,fr_input_msg

if __name__=="__main__":
    root = init_gui()
    fr_list_msg, fr_input_msg = init_frames(root)
    th = threading.Thread(target=read_msg,args=(add_label, ))
    th.start()
    init_input(fr_input_msg,fr_list_msg)
    root.mainloop()