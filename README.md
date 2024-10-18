# Text-to-Image-Generator
This project is a Text to Image Generator app using the Stable Diffusion v1.4 model from Hugging Face. It features a simple GUI built with tkinter and customtkinter, allowing users to input text prompts and generate images. The app supports CUDA for faster processing and saves generated images locally for viewing.
## Features

- Simple user interface for entering text prompts.
- Integration with Stable Diffusion for text-to-image generation.
- Display generated image directly in the app.
- Saves generated image to local storage.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/text-to-image-generator.git
   cd text-to-image-generator

2. Install the required dependencies:

   ```bash
   Copy code
   pip install -r requirements.txt

3. Make sure you have access to the Hugging Face model and set your authentication token in the authtoken.py file:
   
   ```python
   # authtoken.py
   auth_token = "your_huggingface_auth_token"

## Usage
1. Run the app
2. Enter your text prompt in the input field and click "Generate" to generate an image.
3. The generated image will be displayed within the app, and saved as generatedimage.png in the current directory.

## Requirements
You can install all dependencies using the provided requirements.txt.

## Notes
- Ensure that you have a GPU and CUDA installed to run Stable Diffusion effectively.
- The Hugging Face CompVis/stable-diffusion-v1-4 model is required for this project, and you must set up an access token to 
  use it.

## License
This project is licensed under the MIT License.
   


   
