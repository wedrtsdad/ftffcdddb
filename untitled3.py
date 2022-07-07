from tkinter import *
root=Tk()
root.title("popup")
root.geometry("600x600")

l1= Label(root)

array1= ["1","20","300"]

array2= [["1000","20000","300000"],["1000000","20000000","300000000"]]

array3= [[["1000000000","20000000000","300000000000"],["1000000000000","20000000000000","300000000000000"],["1000000000000000","20000000000000000","300000000000000000"]]]

def r1():
    l1["text"]= "Earning in 1 year :" + str(array1[0]) +"\n"+ "Earning in 2 year :" + str(array2[1][0]) +"\n"+ "Earning in 3 year :"+ str(array3[0][2][2])

btn= Button(root, text="show me the earning according to years", command=r1)
btn.place(relx=0.5 , rely=0.5 , anchor=CENTER)
l1.place(relx= 0.5 , rely= 0.6 , anchor=CENTER)

root.mainloop()
