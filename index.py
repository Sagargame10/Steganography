from tkinter import *
from tkinter import ttk
from steganography import *

def enable(childList1, childList2):
    for child in childList1:
        child.configure(state='active')
    for child in childList2:
        child.configure(state='disabled')

def disable(childList1 , childList2):
    for child in childList1:
        child.configure(state='disabled')
    for child in childList2:
        child.configure(state='active')

def main():
    root = Tk()
    root.title('Steganography')
    root.configure(background='#240090')

    startingFrame = ttk.LabelFrame(root, padding=(10,10,10,10))
    startingFrame.grid(column=0, row = 0 , padx=10, pady=10)
    Label(startingFrame,text='Steganography',font='Helvetica 12 bold underline').pack()

    # Frame Containing Options : Embed / Extract
    frame = ttk.LabelFrame(root, padding=(15,15,15,15))
    frame.grid(column=0, row=1, padx=10, pady=10)
    v = IntVar()
    v.set(1)
    Radiobutton(frame, text='Embed File', variable=v, value=1 , command=lambda: enable(frame1.winfo_children(),frame2.winfo_children())).grid(row=0,column=0, padx=10, pady=10)
    Radiobutton(frame, text='Extract File', variable=v, value=2 ,command = lambda:disable(frame1.winfo_children(),frame2.winfo_children())).grid(row=0,column=1, padx=10, pady=10)

    # ==========================================================================================================

    #Creates top frame : FRAME 1 i.e Embed Frame
    frame1 = ttk.LabelFrame(root, padding=(15,15,15,15))
    frame1.grid(column=0, row=2, padx=10, pady=10)

    Label(frame1,text='  Embed File:',font='Helvetica 12 bold').grid(row=0 , column=0, padx=5, pady=5)
    Label(frame1, text='Path for the resultant image : ').grid(row=1, padx=5, pady=5)
    Label(frame1, text='Path for the source image : ').grid(row=2, padx=5, pady=5)
    Label(frame1, text='Path for the file to be embedd :').grid(row=3, padx=5, pady=5)
    entry1 = ttk.Entry(frame1, width = 35)
    entry2 = ttk.Entry(frame1, width = 35)
    entry3 = ttk.Entry(frame1, width = 35)
    entry1.grid(row=1, column=1, padx=5, pady=5)
    entry2.grid(row=2, column=1, padx=5, pady=5)
    entry3.grid(row=3, column=1, padx=5, pady=5)

    button1 = ttk.Button(frame1, text="Start Embedding" , command = lambda : embed(entry1.get(), entry2.get() , entry3.get()))
    button1.grid(row=4 ,padx=5,pady=5)

    # ==========================================================================================================

    #Creates bottom frame : FRAME 2 i.e Extract Frame
    frame2 = ttk.LabelFrame(root, padding=(15,15,15,15))
    frame2.grid(column=0, row=3, padx=10, pady=10)

    Label(frame2,text='Extract File',font='Helvetica 12 bold').grid(row=0 , column=0, padx=5, pady=5)
    Label(frame2, text='Target image : ').grid(row=1, padx=5, pady=5)
    Label(frame2, text='Path for extracted file :').grid(row=2, padx=5, pady=5)
    e1 = ttk.Entry(frame2, width = 35)
    e2 = ttk.Entry(frame2, width = 35)
    e1.grid(row=1, column=1, padx=5, pady=5)
    e2.grid(row=2, column=1, padx=5, pady=5)

    target_image = e1.get()
    save_in_folder = e2.get()

    button1 = ttk.Button(frame2, text="Start Extraction" , command = lambda : extract(e1.get(),e2.get()))
    button1.grid(row=4 ,padx=5,pady=5)

    for child in frame2.winfo_children():
        child.configure(state='disable')

    root.mainloop()

if __name__ == '__main__':
    main()
