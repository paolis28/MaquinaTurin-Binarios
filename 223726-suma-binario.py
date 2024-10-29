import tkinter as tk
from tkinter import messagebox

class MaquinaTuring:
    # Definición del valor inicial del cabezal
    def __init__(self, tape):
        self.tape = list(tape)
        self.head = 0
        self.state = 'q0'
        self.result = 2
    
    def step(self):
        transiciones = {
            'q0': {'1': ('q1', '1', 'R')},  
            'q1': {'0': ('q2', '0', 'R')}, 
            'q2': {'=': ('q3', '=', 'R'), '0': ('q2', '0', 'R'), '1': ('q2', '1', 'R')},  
            'q3': {'0': ('q3', '0', 'R'), '1': ('q3', '1', 'R'), 'B': ('qF', 'B', 'R')} 
        }
        
        current_symbol = self.tape[self.head]
        
        if self.state in transiciones and current_symbol in transiciones[self.state]:
            estado_nuevo, escribir_simbolo, mover_transaccion = transiciones[self.state][current_symbol]
            self.tape[self.head] = escribir_simbolo
            self.state = estado_nuevo
            
            if mover_transaccion == 'R':
                self.head += 1
            elif mover_transaccion == 'L':
                self.head -= 1
                
            if self.state == 'q3' and current_symbol == '1':
                self.result += 1
                
    def run(self):
        while self.state != 'qF':
            if self.head < 0 or self.head >= len(self.tape):
                break
            self.step()
        return self.result
    
class InterfazMaquina:
    def __init__(self, root):
        self.root = root
        self.root.title("MAQUINA DE TURING - SUMA DE BINARIOS")
        self.root.configure(bg="#003366") 
        self.root.geometry("400x300")  
        
        self.label = tk.Label(root, text="Ingresa un número binario", bg="#003366", fg="white", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.input_entry = tk.Entry(root, bg="#006699", fg="white", font=("Arial", 12))
        self.input_entry.pack(pady=10, padx=20)
        
        self.calculate_bt = tk.Button(root, text="Calcular", command=self.calculate_sum, bg="#005580", fg="white", font=("Arial", 10))
        self.calculate_bt.pack(pady=10)
        
        self.result_label_decimal = tk.Label(root, text="", bg="#003366", fg="white", font=("Arial", 12))
        self.result_label_decimal.pack(pady=10)
        
        self.result_label_binario = tk.Label(root, text="", bg="#003366", fg="white", font=("Arial", 12))
        self.result_label_binario.pack(pady=10)

    def calculate_sum(self):
        binary_input = self.input_entry.get()
        if not all(c in '01' for c in binary_input):
            messagebox.showerror("Error", "Ingresa solo números binarios (0 y 1)")
            return
        
        tape_input = "10=" + binary_input + "B"
        maquinaTuring = MaquinaTuring(tape_input)
        result = maquinaTuring.run()
        
        self.result_label_decimal.config(text=f"El resultado de la suma es (Decimal): {result}")
        result_binario = bin(result)[2:] 
        self.result_label_binario.config(text=f"El resultado de la suma es (Binario): {result_binario}")
        
root = tk.Tk()
app = InterfazMaquina(root)
root.mainloop()
