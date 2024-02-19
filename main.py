import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import os

def post_content():
    title = title_entry.get()
    body = body_text.get("1.0", tk.END).strip()  # .strip() to remove trailing newline
    date_str = datetime.now().strftime("%B %d, %Y")
    
    # Define the file paths
    html_file_path = '/Users/jamielaguerta/Desktop/Website/jalaguerta.github.io/blog.html'  # Replace with the correct path to your HTML file
    
    # Read the existing HTML content
    with open(html_file_path, 'r', encoding='utf-8') as file:
        original_content = file.read()

    # Create the new section
    new_section = f"<div>\n\t<h2>{date_str} - {title}</h2>\n\t<p>{body}</p>\n</div>\n"
    
    # Insert the new section after the <h1>Technical Blog</h1>
    updated_content = original_content.replace('<h1>Technical Blog</h1>', f'<h1>Technical Blog</h1>\n{new_section}')
    
    # Write the updated HTML content back to the file
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print("Content posted!")

# Create the main window
root = tk.Tk()
root.title("Blog Content Updater")

# Create the title entry
title_label = tk.Label(root, text="Title:")
title_label.pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

# Create the body text area
body_label = tk.Label(root, text="Body:")
body_label.pack()
body_text = scrolledtext.ScrolledText(root, width=60, height=10)
body_text.pack()

# Create the post button
post_button = tk.Button(root, text="Post", command=post_content)
post_button.pack()

# Run the Tkinter event loop
root.mainloop()
