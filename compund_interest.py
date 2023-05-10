from tkinter import *
# function to clear all the entry boxes
def clear_all():
    initial_field.delete(0,END)
    interest_rate.delete(0,END)
    time_field.delete(0,END)
    compund_field.delete(0,END)
    initial_field.focus_set()

# a function to calculate the compound interest
def calculate_ci():
        initial_value=int(initial_field.get())
        rate= float(interest_rate.get())
        time=int(time_field.get())
        compund_interest= initial_value* (pow((1 + rate / 100), time))
        compund_field.insert(10,compund_interest)

# modifying the GUI
if __name__ == "__main__" :
    CI= Tk()
    CI.configure(bg='cyan2')
    CI.geometry("400x250")
    CI.title("compund interest calculator")

# setting up the labels for the entry boxes
label1=Label(CI, text="initial amount: ",fg='black', bg='green2')
label2=Label(CI,text="Rate (%): ",fg='black', bg='green2')
label3=Label(CI, text="Time (years): ", fg='black', bg='green2')
label4=Label(CI,text="compound interest: ", fg='black', bg='green2')
 # placing the labels   
label1.grid(row = 1, column = 0, padx = 10, pady = 10)
label2.grid(row = 2, column = 0, padx = 10, pady = 10)
label3.grid(row = 3, column = 0, padx = 10, pady = 10)
label4.grid(row = 5, column = 0, padx = 10, pady = 10)
# setting up the boxes to be Entry
initial_field= Entry(CI)
interest_rate=Entry(CI)
time_field=Entry(CI)
compund_field=Entry (CI)

#placing the entry boxes
initial_field.grid(row = 1, column = 1, padx = 10, pady = 10)
interest_rate.grid(row = 2, column = 1, padx = 10, pady = 10)
time_field.grid(row = 3, column = 1, padx = 10, pady = 10)
compund_field.grid(row = 5, column = 1, padx = 10, pady = 10)
#seeting up the buttons for clear and submit
button1=Button(CI, text="submit", fg='black', bg='green2',command= calculate_ci )
button2=Button (CI, text="clear", fg='black', bg='green2',command= clear_all)
# setting the places for the buttons
button1.grid(row = 4, column = 1, pady = 10)
button2.grid(row = 6, column = 1, pady = 10)

# Start the GUI
CI.mainloop()


        

