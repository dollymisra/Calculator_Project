import tkinter as tk
import math




class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.expression = ""

        # Set background color
        self.root.configure(bg="#8a7ca8")
        self.root.title("Calculator")

        # Outer frame with padding and border
        # frame = tk.Frame(root, bd=10, relief=tk.RIDGE, bg="#b5d3cf")
        # frame.pack(padx=20, pady=20, fill='both', expand=True)
        outer_frame = tk.Frame(root, bd=6, relief=tk.SOLID, bg="#8a7ca8")  # Customize outer border color
        outer_frame.pack(padx=20, pady=20)
         
        frame = tk.Frame(outer_frame, bd=10, relief=tk.RIDGE, bg="#8a7ca8")  # Existing design
        frame.pack(padx=8, pady=8)
        # Display field
        self.display = tk.Entry(frame, font=('Roboto', 23, 'bold'), bd=10, relief=tk.GROOVE,
        justify='right', bg="#ffffff", fg="#333", highlightthickness=0, highlightbackground="#ffffff")

        # self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=15, ipadx=5, ipady=10)
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=20, sticky='nsew')
        self.create_buttons(frame)

    def click(self, value):
        if value == "CE":
            self.expression = ""
        elif value == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif value == "x²":
            self.expression += "**2"
        elif value == "√":
            self.expression += "math.sqrt("
        elif value == "π":
            self.expression += str(math.pi)
        elif value == "e":
            self.expression += str(math.e)
        elif value == "1/x":
            self.expression += "1/("
        elif value == "log":
            self.expression += "math.log10("
        elif value == "ln":
            self.expression += "math.log("
        elif value == "n!":
            try:
                self.expression = str(math.factorial(int(eval(self.expression))))
            except:
                self.expression = "Error"
        elif value == "%":
            try:
                self.expression = str(eval(self.expression) / 100)
            except:
                self.expression = "Error"
        elif value == "MC-":
            try:
                self.memory = eval(self.expression) 
                self.expression = ""
            except:
                self.expression = "Error" 

        elif value == "MC+":
            self.expression += str(self.memory)     
        elif value == "exp":
            self.expression += "math.exp("
        elif value == "|x|":
            self.expression += "abs("
        elif value == "x^y":
            self.expression += "**"
        elif value == "10^y":
            self.expression += "10**"
        
        elif value == "←":
            self.expression = self.expression[:-1]
        else:
            self.expression += str(value)

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def create_buttons(self, parent):
        buttons = [
            ['x²', 'π', 'e', 'CE', '←'],
            ['√', '1/x', '|x|', 'exp', '%'],
            ['(', ')', 'n!', 'log', 'ln'],
            ['x^y', '7', '8', '9', '/'],
            ['MC+', '4', '5', '6', '*'],
            ['MC-', '1', '2', '3', '-'],
            ['.', '0', '=', '+', '']
        ]

        row_start = 1
        for row in buttons:
            col = 0
            for btn in row:
                if btn != "":
                    is_equal = btn == "="
                    font = ('Roboto', 11, 'bold')
                    bg_color = "#e6d9f8" if is_equal else "white"
                    fg_color = "#000"

                    btn_kwargs = {
                        "text": btn,
                        "width": 6 if not is_equal else 14,
                        "height": 2,
                        "font": font,
                        "bg": bg_color,
                        "fg": fg_color,
                        "activebackground": "#e6d9f8",
                        "bd": 0,
                        "relief": tk.FLAT,
                        "command": lambda b=btn: self.click(b)
                    }

                    if is_equal:
                        tk.Button(parent, **btn_kwargs).grid(row=row_start, column=col, columnspan=2, padx=4, pady=4)
                        col += 1  # Skip next column for columnspan=2
                    else:
                        tk.Button(parent, **btn_kwargs).grid(row=row_start, column=col, sticky='nsew', padx=5, pady=4)

                col += 1
            row_start += 1

# Run the Calculator
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("485x570")
    app = ScientificCalculator(root)
    root.mainloop()
