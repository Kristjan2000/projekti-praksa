import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation = text_result.get(1.0, "end").strip()
    

    if symbol == "(":
       
        if calculation and (calculation[-1].isdigit() or calculation[-1] == ")"):
            calculation += "*"  
    
    calculation += str(symbol) 
    text_result.delete(1.0, "end") 
    text_result.insert(1.0, calculation) 

def evaluate_calculation():
    global calculation
    try:
        calculation = text_result.get(1.0, "end").strip()
        calculation = str(round(eval(calculation),2))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Nau šlo")
    pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

    pass

def delete_last_character():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    
    pass
def handle_opening_bracket():
    global calculation
    calculation = text_result.get(1.0, "end").strip()
    
   
    if calculation and (calculation[-1].isdigit() or calculation[-1] == ")"):
        calculation += "*"
    
   
    text_result.delete(1.0, "end") 
    text_result.insert(1.0, calculation) 
    pass

def validate_keypress(event):
    allowed_keys = "0123456789+-*/()."
    if event.keysym == "BackSpace":
        return

    if event.char not in allowed_keys:
        return "break" 
    pass

def handle_enter_key(event):
    evaluate_calculation()
    return "break"
    pass

root = tk.Tk()
root.geometry("300x300")

root.title("Kalkulator")
root.configure(bg="black")

text_result = tk.Text(root, bg="green", height=2, width=19, font=("Times New Roman", 24))
text_result.grid(columnspan=5)
text_result.bind("<Return>", lambda event: (evaluate_calculation(), "break"))
text_result.bind("(", lambda event: (handle_opening_bracket(), "break"))
text_result.bind("<Key>", lambda event: validate_keypress(event))
text_result.bind("<Return>", handle_enter_key)


bt1 = tk.Button(root, text="1", bg="green", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
bt1.grid(row=2, column=0)
bt2 = tk.Button(root, text="2", bg="green", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
bt2.grid(row=2, column=1)
bt3 = tk.Button(root, text="3", bg="green", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
bt3.grid(row=2, column=2)
bt4 = tk.Button(root, text="4", bg="green", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
bt4.grid(row=3, column=0)
bt5 = tk.Button(root, text="5", bg="green", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
bt5.grid(row=3, column=1)
bt6 = tk.Button(root, text="6", bg="green", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
bt6.grid(row=3, column=2)
bt7 = tk.Button(root, text="7", bg="green", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
bt7.grid(row=4, column=0)
bt8 = tk.Button(root, text="8", bg="green", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
bt8.grid(row=4, column=1)
bt9 =tk.Button(root, text="9", bg="green", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
bt9.grid(row=4, column=2)
bt0 =tk.Button(root, text="0", bg="green", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
bt0.grid(row=5, column=1)
bt_plus = tk.Button(root, text="+", bg="purple", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
bt_plus.grid(row=2, column=3)
bt_minus = tk.Button(root, text="-", bg="purple", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
bt_minus.grid(row=3, column=3)
bt_mult = tk.Button(root, text="*", bg="purple", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
bt_mult.grid(row=4, column=3)
bt_deljenje = tk.Button(root, text="/", bg="purple", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
bt_deljenje.grid(row=5, column=3)
bt_delete = tk.Button(root, text="C", bg="red", command=clear_field, width=5, font=("Arial", 14))
bt_delete.grid(row=5, column=0)
bt_jeenako = tk.Button(root, text="=", bg="white", command=evaluate_calculation, width=5, font=("Arial", 14))
bt_jeenako.grid(row=6, column=3)
bt_backspace = tk.Button(root, text="CE", bg="red", command=lambda: delete_last_character(), width=5, font=("Arial", 14))
bt_backspace.grid(row=5, column=2)
bt_oklepaj = tk.Button(root, text="(", bg="purple", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
bt_oklepaj.grid(row=6, column=1)
bt_zaklepaj = tk.Button(root, text=")", bg="purple", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
bt_zaklepaj.grid(row=6, column=2)



root.mainloop()