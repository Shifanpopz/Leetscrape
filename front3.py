import os
from tkinter import *
from PIL import Image, ImageTk
import pyperclip
def generate_count():
    sheet = entry_box.get()
    f = open("demofile.txt", "w")
    f.write(sheet)
    f.close()
    print("Generating count for sheet:", sheet)
    
    



def tutorial_window():
    tutorial = Toplevel()
    tutorial.title("Tutorial")
    tutorial.geometry("800x800")
    tutorial.config(bg='lightcyan')

    frame = Frame(tutorial, bd=10)
    frame.pack(pady=20)

    image1 = Image.open("image1.png")
    image1 = image1.resize((280, 280), Image.ANTIALIAS)
    image1_tk = ImageTk.PhotoImage(image1)

    image2 = Image.open("image2.png")
    image2 = image2.resize((280, 280), Image.ANTIALIAS)
    image2_tk = ImageTk.PhotoImage(image2)

    image3 = Image.open("image3.png")
    image3 = image3.resize((280, 280), Image.ANTIALIAS)
    image3_tk = ImageTk.PhotoImage(image3)

    image1_label = Label(frame, image=image1_tk)
    image2_label = Label(frame, image=image2_tk)
    image3_label = Label(frame, image=image3_tk)

    image1_label.grid(row=0, column=0)
    image2_label.grid(row=0, column=1)
    image3_label.grid(row=0, column=2)

    rules_label = Label(tutorial, text="1.Open the Google Sheet that you want to share.\n2.Click on Share in the top right corner.\n3.Enter the email address of the collaborator given below\n4.Choose the level of access you want to grant: Editor.\n5.Click the Send button.", font=("Courier", 14), bg="#D3D3D3", fg="black")
    rules_label.pack(pady=10)

    mail_id_var = StringVar()
    mail_id_var.set("contest-ranking-generation@contest-ranking-generation.iam.gserviceaccount.com")
    mail_id_entry = Entry(tutorial, textvariable=mail_id_var, font=("Times New Roman", 14), state="readonly")
    mail_id_entry.pack(pady=10)

    def copy_to_clipboard():
        pyperclip.copy(mail_id_var.get())

    copy_button = Button(tutorial, text="Copy to Clipboard", font=("Calibri", 14), command=copy_to_clipboard, bg="#4ca5e5", fg="#ffffff")
    copy_button.pack(pady=10)


    back_button = Button(tutorial, text="Back", font=("Verdana", 14), command=tutorial.destroy, bg="#16f3ff", fg="#1a1817")
    back_button.pack(pady=10)
    tutorial.mainloop()


root = Tk()
root.geometry("800x800")
root.config(bg="lightcyan")
root.title("Program Count Generator")

title_frame = Frame(root, bg="black", height=200)
title_frame.pack(fill=X, padx=5, pady=20)

title = Label(title_frame, text="Rank Generator", font=("Courier New", 50, "bold"), fg="white", bg="black")
title.pack(pady=20)

label = Label(root, text="Google Sheet Link:", font=("Verdana", 20, "bold"), bg="lightcyan")
label.pack(pady=20)

entry_frame = Frame(root, bg="lightcyan")
entry_frame.pack(pady=20)

entry_box = Entry(entry_frame, font=("Helvetica", 20), width=30, bg="lightblue")
entry_box.pack(side=LEFT, padx=20)

generate_button = Button(entry_frame, text="Generate Count", font=("Helvetica", 14), relief="groove", command=generate_count, bg="#00bfff", activebackground="#00bfff", activeforeground="white", width=15, height=1, cursor="hand2")
generate_button.pack(side=LEFT, padx=20)

rules = Label(root, text="Rules and Regulations:", font=("Verdana", 20, "bold"), bg="lightcyan")
rules.pack(pady=10)

#rules_img = Image.open("rules.png")
#rules_img = rules_img.resize((175,175), Image.ANTIALIAS)
#rules_img = ImageOps.expand(rules_img, border=0, fill='lightcyan')
#rules_img = ImageTk.PhotoImage(rules_img)
#rules_img_label = Label(root, image=rules_img)
#rules_img_label.pack(side=RIGHT, padx=30)

rules_text = Label(root, text="1.Read the Tutorial which is present below\n2.Copy the Google sheet link from your browser.\n3.Paste the link in the above text box.\n4.Ensure that the link is complete and properly formatted.\n5.Click the Generate Count button to save the link.", font=("Comic Sans MS", 14), bg="#D3D3D3", fg="black")
rules_text.pack(pady=10,padx=20)

tutorial_button = Button(root, text="Tutorial", font=("Verdana", 14), relief="groove", command=tutorial_window, bg="#00bfff", activebackground="#00bfff", activeforeground="white", width=15, height=1, cursor="hand2")
tutorial_button.pack(pady=10)




root.mainloop()
print('initizated')
os.system('python main.py')
print('Completed')