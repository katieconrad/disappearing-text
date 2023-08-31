import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

# Constants for widget padding
XPAD = 5
YPAD = 5


class Application:

    def __init__(self, master):

        # Set up the window
        self.master = master
        self.master.title("Don't Stop Writing!")
        self.master.minsize(width=1000, height=1000)
        self.master.config(padx=20, pady=20)
        self.after_function = None
        self.after_label = None

        # Display instructions
        self.text_frame = tk.Frame(self.master)
        self.text_frame.grid(column=0, row=0, columnspan=2, padx=XPAD, pady=YPAD)
        self.instructions = tk.Label(self.text_frame, wraplength=960, text="Write whatever you want in the box below. "
                                                                           "If you stop writing for 10 seconds, your "
                                                                           "work will disappear!")
        self.instructions.grid(column=0, row=0, padx=XPAD, pady=YPAD)

        # Create text entry field
        self.entry_frame = tk.Frame(self.master)
        self.entry_frame.grid(column=0, row=1, columnspan=2, padx=XPAD, pady=YPAD)
        self.entry = tk.Text(self.entry_frame, width=75, height=25)
        self.entry.grid(column=0, row=0, padx=XPAD, pady=XPAD)
        self.entry.focus_set()
        self.entry.bind('<Key>', self.handle_wait)

        # Display countdown timer and save button
        self.countdown_label = tk.Label(self.master, text="Time to deletion: 10")
        self.countdown_label.grid(column=0, row=2, padx=XPAD, pady=YPAD)
        self.save_button = ttk.Button(self.master, text="Save", command=self.save_text)
        self.save_button.grid(column=1, row=2, padx=XPAD, pady=YPAD)

    def handle_wait(self, event):
        """Starts countdown to deletion and countdown timer"""
        if self.after_function is not None:
            self.master.after_cancel(self.after_function)

        self.after_function = self.master.after(10000, self.stop)
        self.countdown(10)

    def stop(self):
        """Deletes contents of Text field"""
        self.entry.delete("1.0", "end")

    def countdown(self, time_remaining):
        """Displays and updates countdown timer"""
        if self.after_label is not None:
            self.master.after_cancel(self.after_label)
        self.countdown_label.config(text=f"Time to deletion: {time_remaining}")
        time_remaining -= 1
        if time_remaining >= 0:
            self.after_label = self.master.after(1000, self.countdown, time_remaining)

    def save_text(self):
        """Saves text as a .txt file"""
        text = self.entry.get("1.0", "end-1c")
        file_name = simpledialog.askstring(title="Filename", prompt="Enter a file name for your work.")
        with open(f"{file_name}.txt", "w") as file:
            file.write(text)
        messagebox.showinfo(message="Your text has been saved.")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.title("Don't Stop Writing!")
    root.minsize(width=500, height=500)
    root.config(padx=20, pady=20)
    root.mainloop()
