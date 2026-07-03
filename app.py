import os
import cv2
import numpy as np
from PIL import Image
import gc  # RAM'i temizlemek için Çöp Toplayıcı (Garbage Collector) eklendi
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
VIDEO_FOLDER = 'static/videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['VIDEO_FOLDER'] = VIDEO_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)

def process_image_to_video(image_path, output_filename):
    img = cv2.imread(image_path)
    if img is None: 
        return False

    H, W = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 80, 50])
    upper_blue = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    blue_mask[:int(H * 0.45), :] = 0

    y_coords, x_coords = np.where(blue_mask > 0)
    if len(x_coords) == 0:
        return False 

    min_x = np.min(x_coords)
    max_x = np.max(x_coords)

    kernel = np.ones((4,4), np.uint8)
    dilated_mask = cv2.dilate(blue_mask, kernel, iterations=1)
    clean_bg = cv2.inpaint(img, dilated_mask, 3, cv2.INPAINT_TELEA)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    clean_bg_rgb = cv2.cvtColor(clean_bg, cv2.COLOR_BGR2RGB)

    pil_frames = []
    num_frames = 120 
    step = max(1, (max_x - min_x) // num_frames) 

    for current_x in range(min_x, max_x + step, step):
        frame = clean_bg_rgb.copy()
        
        reveal_mask = np.zeros_like(blue_mask)
        reveal_mask[:, :current_x] = blue_mask[:, :current_x]
        
        frame[reveal_mask > 0] = img_rgb[reveal_mask > 0]
        
        pil_img = Image.fromarray(frame)
        pil_img = pil_img.convert('P', palette=Image.ADAPTIVE, colors=128)
        pil_frames.append(pil_img)

        del frame
        del reveal_mask

    last_frame = pil_frames[-1]
    for _ in range(30):
        pil_frames.append(last_frame)

    gc.collect()

    output_path = os.path.join(app.config['VIDEO_FOLDER'], output_filename)
    
    pil_frames[0].save(
        output_path, 
        format='GIF',
        append_images=pil_frames[1:],
        save_all=True,
        duration=33, 
        loop=0,
        optimize=True
    )
    
    return output_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Dosya bulunamadı'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Dosya seçilmedi'}), 400
        
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        video_filename = f"animated_{filename.split('.')[0]}.gif"
        
        success = process_image_to_video(file_path, video_filename)
        
        if success:
            return jsonify({'video_url': f"/static/videos/{video_filename}"})
        else:
            return jsonify({'error': 'Grafik tespit edilemedi. Farklı bir görsel deneyin.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)