import tkinter as tk
from tkinter import messagebox
import random

quiz_data = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
]
random.shuffle(quiz_data)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)
        
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)
        
        self.buttons = []
        for _ in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=20, command=lambda b=_: self.check_answer(b))
            btn.pack(pady=5)
            self.buttons.append(btn)
        
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(quiz_data):
            q_data = quiz_data[self.current_question]
            self.question_label.config(text=q_data["question"])
            self.feedback_label.config(text="")
            for i, option in enumerate(q_data["options"]):
                self.buttons[i].config(text=option, command=lambda opt=option: self.check_answer(opt))
        else:
            messagebox.showinfo("Quiz Completed", f"Your Score: {self.score} / {len(quiz_data)}")
            self.root.quit()
    
    def check_answer(self, selected_option):
        correct_answer = quiz_data[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct! ✅", fg="green")
        else:
            self.feedback_label.config(text=f"Wrong! ❌ Correct answer: {correct_answer}", fg="red")
        self.root.after(1000, self.next_question)
    
    def next_question(self):
        self.current_question += 1
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
