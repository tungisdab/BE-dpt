from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Cho phép tất cả các nguồn

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file:
        img = Image.open(file.stream)
        
        # Xử lý ảnh tại đây, ví dụ chuyển ảnh thành chuỗi
        # Đây là phần bạn cần thay đổi theo yêu cầu xử lý ảnh của bạn
        result_string = f"Processed image size: kkk {img.size}"
        
        return jsonify({'result': result_string})
    return jsonify({'error': 'No file uploaded'}), 400

if __name__ == '__main__':
    app.run(debug=True)
