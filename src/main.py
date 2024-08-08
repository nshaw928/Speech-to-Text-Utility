import customtkinter
from baseFunctions import startTranscription


# Create base GUI
app = customtkinter.CTk()
app.geometry("900x600")
app.title("Speech to Text Utility")

# Where to save the output text files


# Upload audio file


# Start
button = customtkinter.CTkButton(app, text='Start Transciption', command=startTranscription)
button.pack(padx=20, pady=20)

# Status Bar


# Start App
app.mainloop()