import tkinter as tk
from tkinter import scrolledtext
from tkinter import scrolledtext, messagebox
from datetime import datetime
import subprocess
import os

def git_push():
    try:
        # Navigate to the repository directory (replace 'path/to/repo' with the actual path)
        repo_path = '/Users/jamielaguerta/Desktop/Website/jalaguerta.github.io'
        os.chdir(repo_path)
        
        # Add the file to the staging area
        subprocess.check_call(['git', 'add', 'blog.html'])
        
        # Commit the change
        commit_message = "Update blog content"
        subprocess.check_call(['git', 'commit', '-m', commit_message])
        
        # Push the change
        subprocess.check_call(['git', 'push', 'origin', 'main'])
        print("Changes pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("Failed to push changes to GitHub:", e)


def post_content():
    title = title_entry.get()
    body = body_text.get("1.0", tk.END).strip()  # .strip() to remove trailing newline
    date_str = datetime.now().strftime("%B %d, %Y %H:%M:%S")

    
    # Define the file paths
    html_file_path = '/Users/jamielaguerta/Desktop/Website/jalaguerta.github.io/blog.html'  
    
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

    git_push()

        # Show a popup message
    messagebox.showinfo("Content Posted", "Your content has been posted!")
    
    print("Content posted!")
    
    # Close the Tkinter window
    root.destroy()

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
body_text = scrolledtext.ScrolledText(root, width=100, height=10)
body_text.pack()

# Create the post button
post_button = tk.Button(root, text="Post", command=post_content)
post_button.pack()

# Run the Tkinter event loop
root.mainloop()
