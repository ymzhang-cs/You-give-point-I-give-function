# -*- coding = utf-8 -*-
import tkinter as tk
import tkinter.font as tkFont
import sympy

# window information
root = tk.Tk()
root.title("You give point, I give function")
root.geometry("555x310")
# set font model
tnr_bold = tkFont.Font(family='Times New Roman', size=14, weight=tkFont.BOLD)
tnr = tkFont.Font(family=('Times New Roman'), size=15)
tnr_bold1 = tkFont.Font(size=18)
shs = tkFont.Font(family='Source Han Serif', size=15, weight=tkFont.BOLD)


# give point position tip
empty2 = tk.Label(root, text=" ")
empty2.grid(row=0)
empty2 = tk.Label(root, text=" ")
empty2.grid(row=1)
givePoint_Label = tk.Label(root, \
    text="Please input the position of points:\t", font=tnr_bold)
givePoint_Label.grid(row=1, column=1, columnspan=2)

# give point 1 block
point1 = tk.Label(root, text=r"Point 1", font=('Cambria', 15, "italic"))
point1.grid(row=1, column=3)
point1LeftParenthesis = tk.Label(root, text=r"(", font=tnr)
point1LeftParenthesis.grid(row=1, column=4)
point1EntryX = tk.Entry(root, bd='2px', font="Cambria", width=5)
point1EntryX.grid(row=1, column=5)
point1Comma = tk.Label(root, text=r",", font=('Cambria', 15, "italic"))
point1Comma.grid(row=1, column=6)
point1EntryY = tk.Entry(root, bd='2px', font="Cambria", width=5)
point1EntryY.grid(row=1, column=7)
point1RightParenthesis = tk.Label(root, text=r")", font=tnr)
point1RightParenthesis.grid(row=1, column=8)
# give point 2 block
point2 = tk.Label(root, text=r"Point 2", font=('Cambria', 15, "italic"))
point2.grid(row=2, column=3)
point2LeftParenthesis = tk.Label(root, text=r"(", font=tnr)
point2LeftParenthesis.grid(row=2, column=4)
point2EntryX = tk.Entry(root, bd='2px', font="Cambria", width=5)
point2EntryX.grid(row=2, column=5)
point2Comma = tk.Label(root, text=r",", font=('Cambria', 15, "italic"))
point2Comma.grid(row=2, column=6)
point2EntryY = tk.Entry(root, bd='2px', font="Cambria", width=5)
point2EntryY.grid(row=2, column=7)
point2RightParenthesis = tk.Label(root, text=r")", font=tnr)
point2RightParenthesis.grid(row=2, column=8)

# create function
kandb = tk.StringVar()
press = 0
yest = ""
def generate():
    global press
    global yest
    press = press + 1
    try:
        error
    except:
        error_exists = False
    else:
        error_exists = True

    if error_exists == False:
        error = "0"
    # get the input number
    p1x = float(point1EntryX.get())
    p1y = float(point1EntryY.get())
    p2x = float(point2EntryX.get())
    p2y = float(point2EntryY.get())
    # tell sympy that we need to get k and b
    k = sympy.symbols("k")
    b = sympy.symbols("b")
    # get the k and b
    try:
        mathResult = sympy.solve([p1x*k+b-p1y, p2x*k+b-p2y], [k, b])
    except IndexError:
        error = "IE"
        yest = "Error"
    except:
        error = "Unknown"
        yest = "Error"
    # simplify output
    kandbNum = str(mathResult).strip("{").strip("}")
    # print to the consolo
    print(kandbNum)
    # give k1 and b1 the value of k and b
    try:
        k1 = kandbNum.split("k: ")[1].split(", b")[0]
        b1 = kandbNum.split("b: ")[1]
    except IndexError:
        error = "IE"
        yest = "Error"
    except:
        error = "Unknown"
        yest = "Error"
    # further simplify output
    try:
        if ".00000000000000" in k1:
            k1 = k1.strip("0").strip(".")
        else:
            k1 = k1.strip("0")
        if ".00000000000000" in b1:
            b1 = b1.strip("0").strip(".")
        elif b1 == "0.0":
            b1 = "0"
        else:
            b1 = b1.strip("0")
        if k1[0] == ".":
            k1 = "0"+k1
        if b1[0] == ".":
            b1 = "0"+b1
        k1 = k1.strip(".")
        b1 = b1.strip(".")
        #print to the consolo
        print("k={}\nb={}".format(k1,b1))
        #print to the the textbox
        if k1 == "1":
            k1 = ""
        elif k1 == "-1":
            k1 = "-"
    except:
        print(error)
    if error == "IE":
        result.delete('1.0', tk.END)
        result.insert(tk.END, "Value Error! \
May because your 2 points' Xs are the same.")
    elif error == "Unknown":
        result.delete('1.0', tk.END)
        result.insert(tk.END, "Unknown Error!")
    elif b1 == "0":
        result.delete('1.0', tk.END)
        if k1 == "0":
            print("k=0!!")
            result.insert(tk.END, "y = 0")
            yest = "y = 0"
        else:
            result.insert(tk.END, "y = {0}x".format(k1))
            yest = "y = {0}x".format(k1)
    elif b1[0] == "-":
        result.delete('1.0', tk.END)
        if k1 == "0":
            print("k=0!!")
            result.insert(tk.END, "y = {0}".format(b1))
            yest = "y = {0}".format(b1)
        else:
            result.insert(tk.END, "y = {0}x{1}".format(k1, b1))
            yest = "y = {0}x{1}".format(k1, b1)
    else:
        result.delete('1.0', tk.END)
        if k1 == "0":
            print("k=0!!")
            result.insert(tk.END, "y = {0}".format(b1))
            yest = "y = {0}".format(b1)
        else:
            result.insert(tk.END, "y = {0}x+{1}".format(k1, b1))
            yest = "y = {0}x+{1}".format(k1, b1)
    if error == "0":
        historyBox.insert(0, yest)
    else:
        error = "0"
def copySelection_comma():
    copy = historyBox.curselection()
    copyList = list(copy)
    print(copyList)
    strg = ""
    for item in copyList:
        strg = strg + historyBox.get(int(item)) + ", "
    strg = strg.strip(", ")
    print(strg)
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(strg)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()
def copySelection_enter():
    copy = historyBox.curselection()
    copyList = list(copy)
    print(copyList)
    strg = ""
    for item in copyList:
        strg = strg + historyBox.get(int(item)) + "\n"
    strg = strg.strip("\n")
    print(strg)
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(strg)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

def cleanHistory():
    historyBox.delete(0, tk.END)

def removeSelection():
    sel = historyBox.curselection()
    selList = list(sel)
    print(selList)
    for item in selList:
        historyBox.delete(item)
# generate button
generateButton = tk.Button(root, text="Generate", height=1, width=15, \
                    bd=3, bg="#ffffff", fg="#000000", font=tnr_bold1, \
                           command=generate, borderwidth=2, relief="raised")
generateButton.grid(row=3, column=3, columnspan=6)

# output
result = tk.Text(root, bd=3, font=('Times New Roman', 20, 'italic'), \
                 height=7, width=18, borderwidth=2, relief="ridge")
result.grid(row=4, column=3, rowspan=3, columnspan=6)

# history
historyTip = tk.Label(root, text=r"History⬇", font=shs)
historyTip.grid(row=2, column=1, columnspan=2)
historyBox = tk.Listbox(root, selectmode=tk.MULTIPLE)
historyBox.grid(row=3, column=1, columnspan=2, rowspan=2)
copyButton_Comma = tk.Button(root, text="Copy with Comma", \
                             command = copySelection_comma)
copyButton_Comma.grid(row=5, column=1)
copyButton_n = tk.Button(root, text="Copy with Enter", \
                         command = copySelection_enter)
copyButton_n.grid(row=5, column=2)
copyButton_Comma = tk.Button(root, text="Clean History", \
                             command = cleanHistory)
copyButton_Comma.grid(row=6, column=1)
copyButton_n = tk.Button(root, text="Remove Selection", \
                         command = removeSelection)
copyButton_n.grid(row=6, column=2)


root.mainloop()
