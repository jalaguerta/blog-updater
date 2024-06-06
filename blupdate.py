import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from datetime import datetime
import subprocess
import shutil
import os

image_uploaded = False
image_name = ""

def git_push():
    try:
        # Navigate to the repository directory (replace 'path/to/repo' with the actual path)
        repo_path = '/Users/jamielaguerta/Desktop/Website/jalaguerta.github.io'
        os.chdir(repo_path)
        
        # Add the file to the staging area
        subprocess.check_call(['git', 'add', '.'])
        
        # Commit the change
        commit_message = "Update blog content"
        subprocess.check_call(['git', 'commit', '-m', commit_message])
        
        # Push the change
        subprocess.check_call(['git', 'push', 'origin', 'main'])
        print("Changes pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("Failed to push changes to GitHub:", e)

def upload_image():
    global image_name, image_uploaded
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if not file_path:
        return

    # Copy the image file to the specified folder
    target_folder = '/Users/jamielaguerta/Desktop/Website/jalaguerta.github.io/images'
    image_name = os.path.basename(file_path)
    new_image_path = os.path.join(target_folder, image_name)
    if os.path.exists(new_image_path):
        #do nothing, this is if we want to use an image that is alr in the target directory
        pass
    else:
        shutil.copy(file_path, new_image_path)
    image_uploaded = True
    

    messagebox.showinfo("Image Selected", "Image slected and copied successfully!")


def post_content():
    global image_uploaded, image_name
    title = title_entry.get()
    body = body_text.get("1.0", tk.END).strip()  # .strip() to remove trailing newline
    date_str = datetime.now().strftime("%B %d, %Y %H:%M:%S")

    
    # Define the file paths
    html_file_path = '/Users/jamielaguerta/Desktop/Website/jalaguerta.github.io/blog.html'  
    
    # Read the existing HTML content
    with open(html_file_path, 'r', encoding='utf-8') as file:
        original_content = file.read()

    # Create the new section
    new_section = f'<div class="content-container">\n\t<h2>{date_str} - {title}</h2>\n\t<p>{body}</p>\n'
        # Insert the image if uploaded
    if  (image_uploaded):
        print (image_name)
        new_section += f'\t<img src="/images/{image_name}" alt="{title} Image" class="blog-pic">\n</div>'
        # Reset image upload flag and path
        image_uploaded = False
        image_name = ""
    else:  
        new_section += "</div>\n"
    
    


    # Insert the new section after the <h1>Technical Blog</h1>
    updated_content = original_content.replace('<h1>Technical Blog</h1>', f'<h1>Technical Blog</h1>\n{new_section}')
    
    # Write the updated HTML content back to the file
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    git_push()

        # Show a popup message
    messagebox.showinfo("Content Posted", "Your content has been posted!")
    
    print("Content posted!")

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
body_text = scrolledtext.ScrolledText(root, width=50, height=10)
body_text.pack()

# Create the upload button
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Create the post button
post_button = tk.Button(root, text="Post", command=post_content)
post_button.pack()

# Run the Tkinter event loop
root.mainloop()


