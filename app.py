# Libraries for building GUI 
import tkinter as tk
import customtkinter as ctk

# Machine Learning libraries 
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Libraries for processing image 
from PIL import ImageTk

# private modules 
from authtoken import auth_token

# Create app user interface
app = tk.Tk()
app.geometry("532x632")
app.title("Text to Image app")
app.configure(bg='black')
ctk.set_appearance_mode("dark")

# Create input box on the user interface
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 15), text_color="white", fg_color="black")
prompt.place(x=10, y=10)

# Create a placeholder to show the generated image
img_placeholder = ctk.CTkLabel(master=app, height=512, width=512, text="")
img_placeholder.place(x=10, y=110)

# Download stable diffusion model from hugging face 
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
stable_diffusion_model = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 
stable_diffusion_model.to(device)

# Generate image from text
def generate():
    """ This function generates an image from text using stable diffusion"""
    with autocast(device): 
        output = stable_diffusion_model(prompt.get(), guidance_scale=8.5)
    
    # Extract the generated image from the output
    image = output.images[0]
    
    # Save the generated image
    image.save('generatedimage.png')
    
    # Display the generated image on the user interface
    img = ImageTk.PhotoImage(image)
    img_placeholder.configure(image=img)

# Button to trigger image generation
trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 15), text_color="black", fg_color="white", command=generate)
trigger.configure(text="Generate")
trigger.place(x=206, y=60)

# Run the app
app.mainloop()
