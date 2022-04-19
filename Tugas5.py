import tkinter

main_window =tkinter.Tk()

def eventombol():
    label2 = tkinter.Label(main_window,text='TEKAN')
    label2.pack()

label = tkinter.Label(main_window, text='Hai I PUPUT')

tombol = tkinter.Button(main_window, text='ini tombol', command = eventombol)
label.pack()
tombol.pack()
main_window.mainloop()
