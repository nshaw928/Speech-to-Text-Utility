import customtkinter
from customtkinter import filedialog
from baseFunctions import startTranscription, selectOutputFolder


# Create base GUI
app = customtkinter.CTk()
app.geometry("900x600")
app.title("Speech to Text Utility")

# Where to save the output text files
select_output_folder_button = customtkinter.CTkButton(app, text="Select Output Folder", command=selectOutputFolder)
select_output_folder_button.pack(padx=20, pady=20)

# Upload audio file


# Start
button = customtkinter.CTkButton(app, text='Start Transciption', command=startTranscription)
button.pack(padx=20, pady=20)

# Status Bar


# Start App
app.mainloop()