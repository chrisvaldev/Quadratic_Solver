import tkinter as tk
from tkinter import messagebox
import cmath

class QuadraticSolverApp:
    """
    A professional, object-oriented GUI application 
    built with Tkinter to solve quadratic equations.
    """
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Quadratic Equation Solver")
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        
        # Define uniform color palette (Premium UI Aesthetics)
        self.COLOR_BG = "#EAEFFE"       # Light blue canvas
        self.COLOR_CARD = "#FFFFFF"     # Container background
        self.COLOR_PRIMARY = "#4D56DF"  # Royal blue buttons
        self.COLOR_TEXT = "#222222"     # Crisp text color
        
        self.root.configure(bg=self.COLOR_BG)
        
        # Initialize UI Components
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
        # Clean white card frame wrapper
        self.form_frame = tk.Frame(self.root, bg=self.COLOR_CARD, padx=25, pady=20)
        self.form_frame.pack(padx=25, fill="x")
        
        # Coefficient 'a' Input Field
        self._create_field_row("Coefficient a:", 0)
        self.entry_a = self._get_last_entry()
        
        # Coefficient 'b' Input Field
        self._create_field_row("Coefficient b:", 1)
        self.entry_b = self._get_last_entry()
        
        # Coefficient 'c' Input Field
        self._create_field_row("Coefficient c:", 2)
        self.entry_c = self._get_last_entry()
        
        # Configure input column weight to look identical to mockups
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

        # Solve Call-to-Action
        self.btn_solve = tk.Button(
            btn_frame, text="Solve Equation", font=("Arial", 11, "bold"), 
            bg=self.COLOR_PRIMARY, fg="white", bd=0, height=2,
            activebackground="#3B4CCA", activeforeground="white",
            command=self.calculate_roots
        )
        self.btn_solve.pack(side="left", fill="x", expand=True, padx=(0, 10))

        # Reset Form Call-to-Action
        self.btn_reset = tk.Button(
            btn_frame, text="Reset", font=("Arial", 11, "bold"), 
            bg=self.COLOR_PRIMARY, fg="white", bd=0, height=2,
            activebackground="#3B4CCA", activeforeground="white",
            command=self.clear_fields
        )
        self.btn_reset.pack(side="right", fill="x", expand=True, padx=(10, 0))

    def _build_output_display(self) -> None:
        """Allocates visual area for numerical root answers."""
        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 11, "bold"), 
            fg=self.COLOR_TEXT, bg=self.COLOR_BG, justify="center"
        )
        self.result_label.pack(pady=10)

    def calculate_roots(self) -> None:
        """Processes algebraic calculations for real/distinct, repeated, and complex inputs."""
        try:
            # Typecasting validation checks
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())
            
            # Form mathematical boundary guards
            if a == 0:
                messagebox.showerror("Mathematical Error", "The value of 'a' cannot be zero in a quadratic equation.")
                return
                
            # Discriminant: d = b^2 - 4ac
            discriminant = (b ** 2) - (4 * a * c)
            
            # Outcome 1: Real and Distinct Roots
            if discriminant > 0:
                x1 = (-b + cmath.sqrt(discriminant).real) / (2 * a)
                x2 = (-b - cmath.sqrt(discriminant).real) / (2 * a)
                display_output = f"The roots are real and distinct\nx1 = {x1:.2f}\nx2 = {x2:.2f}"
                
            # Outcome 2: Real and Repeated Roots
            elif discriminant == 0:
                x = -b / (2 * a)
                display_output = f"The roots are real and repeated\nx = {x:.2f} twice"
                
            # Outcome 3: Complex / Imaginary Roots (Hard Challenge Variant)
            else:
                x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
                x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
                
                # Format string to output clean signs without double operators (+ -)
                sign1 = "+" if x1.imag >= 0 else "-"
                sign2 = "+" if x2.imag >= 0 else "-"
                display_output = (
                    f"The roots are real and complex\n"
                    f"x1 = {x1.real:.2f} {sign1} {abs(x1.imag):.2f}j\n"
                    f"x2 = {x2.real:.2f} {sign2} {abs(x2.imag):.2f}j"
                )
                
            self.result_label.config(text=display_output)
            
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input detected. Please enter valid real numeric digits.")

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