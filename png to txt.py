from PIL import Image
import os

def binary_text(binary_data):
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        text += chr(int(byte, 2))
    return text

def decode_frames(frames_folder):
    binary = ""
    for filename in sorted(os.listdir(frames_folder)):
        if filename.endswith(".png"):
            img = Image.open(os.path.join(frames_folder, filename))
            pixels = img.load()

            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    r, g, b = pixels[i, j]
                    red_binary = '1' if r > 0 else '0'
                    green_binary = '1' if g > 0 else '0'
                    binary += red_binary + green_binary

    return binary

if __name__ == "__main__":
    frames_folder = 'WHERE YOUR FRAMES ARE STORED'

    binary_content = decode_frames(frames_folder)
    decoded_text = binary_text(binary_content)

    outputfp = 'WHERE YOU WANT TO PUT YOUR TEXT'

    with open(outputfp, 'w', encoding='utf-8') as file:
        file.write(decoded_text)

    print(f"Decoded text saved to: {outputfp}")
