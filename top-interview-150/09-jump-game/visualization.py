import tkinter as tk
from tkinter import ttk
import time

class VisualizeCanJump:
    def __init__(self, root, nums):
        self.root = root
        self.root.title("Visualizar Algoritmo canJump")

        self.nums = nums
        self.n = len(nums)
        self.target = self.n - 1
        self.steps = []
        self.current_step = 0  # Inicializamos current_step aquí

        self.code = [
            "n = len(nums)",
            "target = n - 1",
            "for i in range(n-1, -1, -1):",
            "    max_jump = nums[i]",
            "    if i + max_jump >= target:",
            "        target = i",
            "return target == 0"
        ]

        self.setup_ui()
        self.create_steps()

    def setup_ui(self):
        self.code_text = tk.Text(self.root, width=50, height=15, font=("Consolas", 12))
        self.code_text.grid(row=0, column=0, padx=10, pady=10)

        self.array_label = tk.Label(self.root, text="Array: " + str(self.nums), font=("Consolas", 12))
        self.array_label.grid(row=1, column=0, padx=10, pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.grid(row=2, column=0, padx=10, pady=10)

        self.next_button = ttk.Button(self.buttons_frame, text="Next Step", command=self.next_step)
        self.next_button.grid(row=0, column=0, padx=5)

        self.reset_button = ttk.Button(self.buttons_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=1, padx=5)

        self.update_code_display()

    def update_code_display(self):
        self.code_text.delete(1.0, tk.END)
        for idx, line in enumerate(self.code):
            if self.current_step < len(self.steps) and self.steps[self.current_step][0] == idx:
                self.code_text.insert(tk.END, line + "\n", "highlight")
            else:
                self.code_text.insert(tk.END, line + "\n")

        self.code_text.tag_config("highlight", background="yellow")

    def create_steps(self):
        n = len(self.nums)
        target = n - 1
        self.steps.append((0, {"n": n}))
        self.steps.append((1, {"target": target}))

        for i in range(n-1, -1, -1):
            max_jump = self.nums[i]
            self.steps.append((2, {"i": i}))
            self.steps.append((3, {"max_jump": max_jump}))

            if i + max_jump >= target:
                self.steps.append((4, {"i": i, "max_jump": max_jump, "target": target}))
                target = i
                self.steps.append((5, {"target": target}))

        self.steps.append((6, {"target": target, "result": target == 0}))

    def next_step(self):
        if self.current_step < len(self.steps):
            step_info = self.steps[self.current_step][1]
            self.array_label.config(text=f"Array: {self.nums} | {step_info}")
            self.current_step += 1
            self.update_code_display()

    def reset(self):
        self.current_step = 0
        self.array_label.config(text="Array: " + str(self.nums))
        self.update_code_display()

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    root = tk.Tk()
    app = VisualizeCanJump(root, nums)
    root.mainloop()

