from tkinter import *

raiz = Tk()
fr1 = Frame()
fr1.pack()

fr1.config(width = "200", height = "200", bg = "blue");
fr1.pack(fill = "both" , side = "left")

fr2 = Frame()
fr2.config (width = "300", height = "400", bg = "black");
fr2.pack(fill = "both", side = "bottom")

fr3 = Frame()
fr3.config (width = "300", height = "400", bg = "yellow");
fr2.pack(fill = "both", side = "right")

raiz.mainloop()
