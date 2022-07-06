from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
root = Tk()  
root.geometry("900x600") 
root.title("Multi GUI Maker")

gui_elements = ["Label", "Button", "ComboBox"]
dropdown = ttk.Combobox(root, state = "readonly", values = gui_elements)
dropdown.pack()

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createLabel(self):
        label = Label(root, text = "You have created this Label using class", fg = "green")
        label.pack()
        
    def createButton(self):
        button = Button(root, text = "Button", command = self.message)
        button.pack(padx = 20, pady = 10)
        
    def createDropdown(self):
        values = [1,2,3,4,5]
        class_dropdown = ttk.Combobox(root, state = "readonly", values = values)
        class_dropdown.pack()
        
    def choose(self):
        global dropdown
        elements = dropdown.get()
        if (elements == "Label"):
            self.createLabel()
            
        elif (elements == "Button"):
            self.createButton()
            
        elif (elements == "ComboBox"):
            self.createDropdown()
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class") 
        
obj_of_CreateElements = CreateElements()

btn = Button(root, text ="Create Elements", command = obj_of_CreateElements.choose) 
btn.pack(padx=20, pady = 10) 

root.mainloop()