from tkinter import *
# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk
 
window = Tk()
window.geometry("240x300")
window.title("Welcome to stack and queue app")

def stackopt():

	stackwindow = Tk()
	stackwindow.geometry("200x200")
	stackwindow.title("Stack")
	stack = []
	def push():
		pushwindow = Tk()
		pushwindow.geometry("300x300")
		pushwindow.title("PUSH")
		if (len(stack) < 10):

			input = StringVar()
			e = Entry(pushwindow)
			e.pack()
			
			def submit():
				i = e.get()
				stack.append(i)
				pushwindow.destroy()
			b4 = Button(pushwindow , text = "Submit" ,  fg = "red" , command = submit  )
			b4.pack()
			pushwindow.mainloop()
		else :
			l1 = Message(pushwindow , text = "stack is overflow");
			l1.pack()
			def exit():
				pushwindow.destroy()
			b5 = Button(pushwindow , text = "EXIT" , command = exit )
			b5.pack()
			pushwindow.mainloop()
	def pop() : 
		if (len(stack) > 0):
			stack.pop()
		else :
			popwindow = Tk()
			popwindow.geometry("300x300")
			popwindow.title("POP")
			l1 = Message(popwindow , text = "stack is overflow" , relief = RAISED);
			l1.config(bg = 'red')
			l1.pack()
			def exit():
				 popwindow.destroy()
			b6 = Button(popwindow , text = "EXIT" , command = exit )
			b6.pack()
			popwindow.mainloop()
			
			
	def show():
		showwindow = Tk()
		showwindow.geometry("150x150")
		showwindow.title("SHOW")
		l = Message(showwindow , text = stack)
		l.pack()
		showwindow.mainloop()
	sb1 = Button(stackwindow ,text = "push" ,  fg = "red" , command = push)
	sb2 = Button(stackwindow ,text = "pop" ,  fg = "red" , command = pop)
	sb3 = Button(stackwindow ,text = "show" ,  fg = "red" , command = show)
	sb1.pack()
	sb2.pack()
	sb3.pack()

	stackwindow.mainloop()
	
	
def queueopt():

	queuewindow = Tk()
	queuewindow.geometry("300x300")
	queuewindow.title("Queue")
	queue = []
	def push1():
		qpushwindow = Tk()
		qpushwindow.geometry("250x250")
		qpushwindow.title("PUSH")
		if (len(queue) < 10):

			input = StringVar()
			f = Entry(qpushwindow )
			f.pack()
			
			def submit1():
				j = f.get()
				queue.append(j)
				qpushwindow.destroy()
			b4 = Button(qpushwindow , text = "Submit" ,  fg = "red" , command = submit1  )
			b4.pack()
			qpushwindow.mainloop()
		else :
			l1 = Message(qpushwindow , text = "QUEUE is overflow");
			l1.pack()
			def exit1():
				qpushwindow.destroy()
			b5 = Button(qpushwindow , text = "EXIT" , command = exit1 )
			b5.pack()
			qpushwindow.mainloop()

	def pop1() : 
		if (len(queue) > 0):
			queue.pop(0)
		else :
			qpopwindow = Tk()
			qpopwindow.geometry("300x300")
			qpopwindow.title("Q POP")
			l1 = Message(qpopwindow , text = "QUEUE is underflow" , relief = RAISED);
			l1.config(bg = 'red')
			l1.pack()
			def exit1():
				 qpopwindow.destroy()
			b6 = Button(qpopwindow , text = "EXIT" , command = exit1 )
			b6.pack()
			qpopwindow.mainloop()
			
			
	def show1():
		qshowwindow = Tk()
		qshowwindow.geometry("150x150")
		qshowwindow.title("Q SHOW")
		l = Message(qshowwindow , text = queue)
		l.pack()
		qshowwindow.mainloop()
	sb1 = Button(queuewindow ,text = "q push" ,  fg = "red" , command = push1)
	sb2 = Button(queuewindow ,text = "q pop" ,  fg = "red" , command = pop1)
	sb3 = Button(queuewindow ,text = "q show" ,  fg = "red" , command = show1)
	sb1.pack()
	sb2.pack()
	sb3.pack()

	queuewindow.mainloop()



lbl = Label(window, text="choose one")
b1 = Button(window ,text = "STACK",  fg = "red" , command = stackopt)
b2 = Button(window ,text = "QUEUE" ,  fg = "red" , command = queueopt)
lbl.pack()
b1.pack()
b2.pack()
window.mainloop()

