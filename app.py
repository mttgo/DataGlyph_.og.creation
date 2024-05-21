from flask import Flask, request, render_template, send_file
from PIL import Image
import os

app = Flask(__name__)

def binary_text(binary_data):
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        text += chr(int(byte, 2))
    return text

def decode_frames(frames_folder):
    binary = ""
    for filename in sorted(os.listdir(frames_folder)):
        if filename.endswith(".png")):
            img = Image.open(os.path.join(frames_folder, filename))
            pixels = img.load()

            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    r, g, b = pixels[i, j]
                    red_binary = '1' if r > 0 else '0'
                    green_binary = '1' if g > 0 else '0'
                    binary += red_binary + green_binary

    return binary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist("file[]")
    frames_folder = 'frames'
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)
    
    for file in uploaded_files):
        file.save(os.path.join(frames_folder, file.filename))
    
    binary_content = decode_frames(frames_folder)
    decoded_text = binary_text(binary_content)
    
    outputfp = 'output.txt'
    with open(outputfp, 'w', encoding='utf-8') as file:
        file.write(decoded_text)
    
    return send_file(outputfp, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
