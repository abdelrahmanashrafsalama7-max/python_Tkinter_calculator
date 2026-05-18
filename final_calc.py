import tkinter as tk
from tkinter import messagebox
import math

class BaseCalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator Project")
        
        # ثبتنا الأبعاد هنا بشكل مريح جداً
        self.window.geometry("360x560")
        self.window.configure(bg="#202124")
        self.window.resizable(False, False)

        self.__text_data = "" 
        self.screen_value = tk.StringVar()
        self.init_screen()

    def get_text(self):
        return self.__text_data

    def set_text(self, value):
        self.__text_data = value

    def init_screen(self):
        
        screen_frame = tk.Frame(self.window, bg="#121212")
        screen_frame.place(x=15, y=20, width=330, height=90)

        screen = tk.Entry(
            screen_frame, 
            textvariable=self.screen_value, 
            font=("Arial", 28, "bold"), 
            bd=0, bg="#121212", fg="#FFFFFF", justify="right",
            insertbackground="#FFFFFF"
        )
        screen.place(x=10, y=20, width=310, height=50)

    def refresh_screen(self):
        self.screen_value.set(self.__text_data)


class MyCalculator(BaseCalculator):
    def __init__(self, window):
        super().__init__(window)
        self.init_buttons()

    def init_buttons(self):
        
        buttons_frame = tk.Frame(self.window, bg="#202124")
        buttons_frame.place(x=10, y=130, width=340, height=410)

        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['x²', 'x³', '√', '='],
            ['0', '.', '', '']
        ]

        for i in range(6):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.columnconfigure(j, weight=1)

        for r, row in enumerate(buttons):
            for c, item in enumerate(row):
                if item == '':
                    continue

                if item in ['/', '*', '-', '+', '=']:
                    bg_color = "#FF9500"
                    fg_color = "#FFFFFF"
                elif item in ['C', '(', ')', 'x²', 'x³', '√']:
                    bg_color = "#A5A5A5"
                    fg_color = "#000000"
                else:
                    bg_color = "#3A3A3C"
                    fg_color = "#FFFFFF"

                btn = tk.Button(
                    buttons_frame, text=item, font=("Arial", 16, "bold"), bd=0, 
                    bg=bg_color, fg=fg_color,
                    activebackground="#555555",
                    command=lambda val=item: self.handle_click(val)
                )
                
                if item == '0':
                    btn.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=3, pady=3)
                elif item == '.':
                    btn.grid(row=r, column=c+1, sticky="nsew", padx=3, pady=3)
                else:
                    btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

    def handle_click(self, value):
        current = self.get_text()

        if value == 'C':
            self.set_text("")
        elif value == 'x²':
            try:
                result = str(eval(current) ** 2)
                self.set_text(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
        elif value == 'x³':
            try:
                result = str(eval(current) ** 3)
                self.set_text(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
        elif value == '√':
            try:
                result = str(math.sqrt(eval(current)))
                self.set_text(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
        elif value == '=':
            try:
                result = str(eval(current))
                self.set_text(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.set_text("")
            except Exception:
                messagebox.showerror("Error", "Invalid equation")
                self.set_text("")
        else:
            self.set_text(current + str(value))
        
        self.refresh_screen()


if __name__ == "__main__":
    main_window = tk.Tk()
    app = MyCalculator(main_window)
    main_window.mainloop()