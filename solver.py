import tkinter as tk
import cmath

class QuadraticSolverApp:
    """
    An enterprise-grade, object-oriented GUI application 
    built with Tkinter featuring exhaustive validation mechanics.
    """
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Quadratic Equation Solver")
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        
        
        self.COLOR_BG = "#EAEFFE"       
        self.COLOR_CARD = "#FFFFFF"     
        self.COLOR_PRIMARY = "#4D56DF"  
        self.COLOR_TEXT = "#222222"     
        self.COLOR_ERROR = "#D32F2F"    
        
        self.root.configure(bg=self.COLOR_BG)
        

        self._build_header_section()
        self._build_form_section()
        self._build_action_buttons()
        self._build_output_display()

    def _build_header_section(self) -> None:
        """Renders the top title block and equation format."""
        title_label = tk.Label(
            self.root, text="Quadratic Equation Solver", 
            font=("Arial", 16, "bold"), fg="#3B4CCA", bg=self.COLOR_BG
        )
        title_label.pack(pady=(20, 2))

        formula_label = tk.Label(
            self.root, text="ax² + bx + c = 0", 
            font=("Arial", 11, "italic"), fg="#555555", bg=self.COLOR_BG
        )
        formula_label.pack(pady=(0, 15))

    def _build_form_section(self) -> None:
        """Constructs the container card and grid layout input boxes."""
        self.form_frame = tk.Frame(self.root, bg=self.COLOR_CARD, padx=25, pady=20)
        self.form_frame.pack(padx=25, fill="x")
        
        self._create_field_row("Coefficient a:", 0)
        self.entry_a = self._get_last_entry()
        
        self._create_field_row("Coefficient b:", 1)
        self.entry_b = self._get_last_entry()
        
        self._create_field_row("Coefficient c:", 2)
        self.entry_c = self._get_last_entry()
        
        self.form_frame.columnconfigure(1, weight=1)

    def _create_field_row(self, label_text: str, row_index: int) -> None:
        """Helper to cleanly anchor grid fields to the UI grid hierarchy."""
        lbl = tk.Label(self.form_frame, text=label_text, font=("Arial", 11), bg=self.COLOR_CARD)
        lbl.grid(row=row_index, column=0, sticky="w", pady=8)
        
        entry = tk.Entry(self.form_frame, font=("Arial", 11), bd=1, relief="solid")
        entry.grid(row=row_index, column=1, padx=(15, 0), sticky="ew", ipady=3)
        entry.insert(0, "0.0")

    def _get_last_entry(self) -> tk.Entry:
        """Extracts the most recently registered Entry object inside the frame grid."""
        return [widget for widget in self.form_frame.winfo_children() if isinstance(widget, tk.Entry)][-1]

    def _build_action_buttons(self) -> None:
        """Generates side-by-side executable command buttons."""
        btn_frame = tk.Frame(self.root, bg=self.COLOR_BG)
        btn_frame.pack(fill="x", padx=25, pady=20)

        self.btn_solve = tk.Button(
            btn_frame, text="Solve Equation", font=("Arial", 11, "bold"), 
            bg=self.COLOR_PRIMARY, fg="white", bd=0, height=2,
            activebackground="#3B4CCA", activeforeground="white",
            command=self.calculate_roots
        )
        self.btn_solve.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.btn_reset = tk.Button(
            btn_frame, text="Reset", font=("Arial", 11, "bold"), 
            bg=self.COLOR_PRIMARY, fg="white", bd=0, height=2,
            activebackground="#3B4CCA", activeforeground="white",
            command=self.clear_fields
        )
        self.btn_reset.pack(side="right", fill="x", expand=True, padx=(10, 0))

    def _build_output_display(self) -> None:
        """Allocates visual area for numerical root answers and internal errors."""
        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 11, "bold"), 
            fg=self.COLOR_TEXT, bg=self.COLOR_BG, justify="center"
        )
        self.result_label.pack(pady=10)

    def _validate_numeric_input(self, raw_value: str, field_name: str) -> float:
        """
        Validates whether the raw string input is a valid real number.
        Throws a specific ValueError with descriptive context if check fails.
        """
        
        cleaned = raw_value.strip()
        
        
        if not cleaned:
            raise ValueError(f"Field '{field_name}' cannot be left blank.")
            
        try:
            return float(cleaned)
        except ValueError:
        
            raise ValueError(f"Invalid characters in '{field_name}'.\nPlease enter numeric values only.")

    def calculate_roots(self) -> None:
        """Validates input thoroughly, then processes algebraic root computations."""
        try:
            
            a = self._validate_numeric_input(self.entry_a.get(), "Coefficient a")
            b = self._validate_numeric_input(self.entry_b.get(), "Coefficient b")
            c = self._validate_numeric_input(self.entry_c.get(), "Coefficient c")
            
            
            if a == 0:
                self.result_label.config(text="Mathematical Error:\n'Coefficient a' cannot be zero.", fg=self.COLOR_ERROR)
                return
                
            
            discriminant = (b ** 2) - (4 * a * c)
            
            
            if discriminant > 0:
                x1 = (-b + cmath.sqrt(discriminant).real) / (2 * a)
                x2 = (-b - cmath.sqrt(discriminant).real) / (2 * a)
                display_output = f"The roots are real and distinct\nx1 = {x1:.2f}\nx2 = {x2:.2f}"
                
            
            elif discriminant == 0:
                x = -b / (2 * a)
                display_output = f"The roots are real and repeated\nx = {x:.2f} twice"
                
        
            else:
                x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
                x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
                
                sign1 = "+" if x1.imag >= 0 else "-"
                sign2 = "+" if x2.imag >= 0 else "-"
                display_output = (
                    f"The roots are real and complex\n"
                    f"x1 = {x1.real:.2f} {sign1} {abs(x1.imag):.2f}j\n"
                    f"x2 = {x2.real:.2f} {sign2} {abs(x2.imag):.2f}j"
                )
                
            
            self.result_label.config(text=display_output, fg=self.COLOR_TEXT)
            
        except ValueError as runtime_error:
            # Trap any invalid string formats and display directly inside the window
            self.result_label.config(text=str(runtime_error), fg=self.COLOR_ERROR)

    def clear_fields(self) -> None:
        """Clears calculations and reinitializes inputs to placeholder defaults."""
        for entry in (self.entry_a, self.entry_b, self.entry_c):
            entry.delete(0, tk.END)
            entry.insert(0, "0.0")
        self.result_label.config(text="")


if __name__ == "__main__":
    app_window = tk.Tk()
    app_instance = QuadraticSolverApp(app_window)
    app_window.mainloop()