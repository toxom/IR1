import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    
    # Create a label with the text "test"
    label = tk.Label(root, text="test")
    
    # Pack the label into the window
    label.pack()
    
    # Run the Tkinter event loop
    root.mainloop()

if name == "__main__":
    main()