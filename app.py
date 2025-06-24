import os
from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    file = request.files['image']
    input_image = Image.open(file.stream).convert("RGBA")
    output = remove(input_image)
    byte_io = io.BytesIO()
    output.save(byte_io, format='PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')

@app.route('/')
def home():
    return 'Background Remover is live!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # ← THIS LINE IS IMPORTANT
    app.run(host='0.0.0.0', port=port)
