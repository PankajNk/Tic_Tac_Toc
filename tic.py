from tkinter import *
import tkinter.messagebox 

#rot window initialization
tk = Tk()
tk.title("Tic Tac Toe")


bclick=True  #start with X make false to change to "O"
count=0   #count the total button 

# disable button after input 
def disableButton():
	button1.configure(state=DISABLED)
	button2.configure(state=DISABLED)
	button3.configure(state=DISABLED)
	button4.configure(state=DISABLED)
	button5.configure(state=DISABLED)
	button6.configure(state=DISABLED)
	button7.configure(state=DISABLED)
	button8.configure(state=DISABLED)
	button9.configure(state=DISABLED)
	
	
	#pass

#function to check button clicked or not 
def btnClick(buttons):
	global bclick, count
	if buttons["text"] == " " and bclick == True:#check blank & X
		buttons["text"] = "X"  #insert X
		bclick = False    #change to O
		checkForWin()     #will give the Wineer
		count += 1


	elif buttons["text"] == " " and bclick == False:
		buttons["text"] = "O"
		bclick = True
		checkForWin()
		count += 1
	else:
		tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def checkForWin():
	if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):#row
		button1.configure(bg="red")
		button2.configure(bg="red")
		button3.configure(bg="red")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," X is Winner ")
		Reset()
	elif(button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' ):
		button4.configure(bg="red")
		button5.configure(bg="red")
		button6.configure(bg="red")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," X is Winner ")
		Reset()
	elif(button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X'):
		button7.configure(bg="red")
		button8.configure(bg="red")
		button9.configure(bg="red")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," X is Winner ")
		Reset()

	elif(button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):#daigonal
		button1.configure(bg="red")
		button5.configure(bg="red")
		button9.configure(bg="red")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," X is Winner ")
		Reset()
	elif(button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
		button3.configure(bg="red")
		button5.configure(bg="red")
		button7.configure(bg="red")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," X is Winner ")
		Reset()
	
	elif(button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
		#column
		button1.configure(bg="red")
		button4.configure(bg="red")
		button7.configure(bg="red")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," X is Winner ")
		Reset()
	elif(button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
		button2.configure(bg="red")
		button5.configure(bg="red")
		button8.configure(bg="red")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," X is Winner ")
		Reset()
	elif(button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
		button3.configure(bg="red")
		button6.configure(bg="red")
		button9.configure(bg="red")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," X is Winner ")
		Reset()


		
	#for player 2	
	elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'):#row
		button1.configure(bg="blue")
		button2.configure(bg="blue")
		button3.configure(bg="blue")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," O is Winner ")
		Reset()
	elif(button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' ):
		button4.configure(bg="blue")
		button5.configure(bg="blue")
		button6.configure(bg="blue")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," O is Winner ")
		Reset()
	elif(button7['text'] =='O' and button8['text'] == 'O' and button9['text'] == 'O'):
		button7.configure(bg="blue")
		button8.configure(bg="blue")
		button9.configure(bg="blue")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," O is Winner ")
		Reset()

	elif(button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'):#daigonal
		button1.configure(bg="blue")
		button5.configure(bg="blue")
		button9.configure(bg="blue")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," O is Winner ")
		Reset()
	elif(button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
		button3.configure(bg="blue")
		button5.configure(bg="blue")
		button7.configure(bg="blue")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," O is Winner ")
		Reset()
	
	elif(button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'):
		#column
		button1.configure(bg="blue")
		button4.configure(bg="blue")
		button7.configure(bg="blue")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," O is Winner ")
		Reset()
	elif(button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'):
		button2.configure(bg="blue")
		button5.configure(bg="blue")
		button8.configure(bg="blue")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," O is Winner ")
		Reset()
	elif(button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
		button3.configure(bg="blue")
		button6.configure(bg="blue")
		button9.configure(bg="blue")
		disableButton()
		tkinter.messagebox.showinfo("Tic-Tac-Toe"," O is Winner ")
		Reset()
	
	elif(count == 8):
		button1.configure(bg="yellow")
		button2.configure(bg="yellow")
		button3.configure(bg="yellow")
		button4.configure(bg="yellow")
		button5.configure(bg="yellow")
		button6.configure(bg="yellow")
		button7.configure(bg="yellow")
		button8.configure(bg="yellow")
		button9.configure(bg="yellow")
		
		tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
		Reset()


# to reset the Game 
def Reset():
	
	button1['text']=" "
	button2['text']=" "
	button3['text']=" "
	button4['text']=" "
	button5['text']=" "
	button6['text']=" "
	button7['text']=" "
	button8['text']=" "
	button9['text']=" "
	button1.configure(bg="gray",state=NORMAL)
	button2.configure(bg="gray",state=NORMAL)
	button3.configure(bg="gray",state=NORMAL)
	button4.configure(bg="gray",state=NORMAL)
	button5.configure(bg="gray",state=NORMAL)
	button6.configure(bg="gray",state=NORMAL)
	button7.configure(bg="gray",state=NORMAL)
	button8.configure(bg="gray",state=NORMAL)
	button9.configure(bg="gray",state=NORMAL)

	global bclick,count
	if bclick == True or bclick == False:
		bclick= True
		count=0
	
	

def Quit():
	tk.destroy()



label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)
label = Label( tk, text=" X ", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=1)
label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)	
label = Label( tk, text=" Y ", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=1)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

btnreset = Button(tk, text='RESET', font=('Times 20 bold',10), bg='white', fg='black', height=1, width=5, command=Reset)
btnreset.grid(row=1, column=2)

btnquit = Button(tk, text='QUIT', font=('Times 20 bold',10), bg='white', fg='black', height=1, width=5, command=Quit)
btnquit.grid(row=2, column=2)

tk.mainloop()