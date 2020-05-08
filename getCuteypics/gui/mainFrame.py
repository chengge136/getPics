import tkinter as tk
import threading
import tkinter.messagebox
from gui.GetLinks import GetLinks

window=tk.Tk()
window.title('批量获取图片链接')
window.geometry('580x460')


def new_thred():
    if len(entry_link.get().strip()) == 0:
        print('请粘贴网页链接')
        tk.messagebox.showwarning('错误', '请粘贴网页链接')
    else:
        def start_verify(tx, cs, entry_link,window):
            getlink = GetLinks()
            getlink.get_links(tx, cs, entry_link,window)



        print('正确')
        btn.config(state=tk.DISABLED)
        th = threading.Thread(target=start_verify, args=(text, canvas, entry_link.get().strip(), window))
        th.setDaemon(True)  # 守护线程
        th.start()

var_entry_link=tk.StringVar()
tk.Label(window, text='粘贴写真的链接：', ).place(x=20, y=20)
entry_link = tk.Entry(window, textvariable=var_entry_link, width=30)
entry_link.place(x=20, y=60)
btn = tk.Button(window,bg='#ADD8E6',text='获取', width=15, height=2, command=new_thred)
btn.place(x=300,y=60)

tk.Label(window, text='执行进度:', ).place(x=20, y=120)
canvas = tk.Canvas(window, width=465, height=22, bg="white")
canvas.place(x=80, y=120)

tk.Label(window,text='获取的图片链接',).place(x=20,y=160)
text = tk.Text(window, height=16, width=70)
text.place(x=20,y=200)

window.mainloop()
