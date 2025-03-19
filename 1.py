import webbrowser
import os
from flask import Flask, request, jsonify
import base64

from PIL import Image
import io
from flask_cors import CORS  # 导入 CORS
# HTML 文件的路径
html_file_path = "camera.html"  # 替换为你的 HTML 文件名

# 确保 HTML 文件存在
if not os.path.exists(html_file_path):
    print(f"错误：HTML 文件 '{html_file_path}' 不存在。")
else:
    # 使用默认浏览器打开 HTML 文件
    webbrowser.open("file://" + os.path.abspath(html_file_path))
    print(f"已在浏览器中打开 '{html_file_path}'。 请手动点击'拍照并上传'按钮。")


app = Flask(__name__)
CORS(app)  # 在此处启用 CORS

# 设置保存图片的文件夹
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from flask import Flask, request, jsonify
import base64
import os
from PIL import Image
import io
from flask_cors import CORS  # 导入 CORS

app = Flask(__name__)
CORS(app)  # 在此处启用 CORS

# 设置保存图片的文件夹
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 确保上传文件夹存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        data = request.get_json()
        image_data = data['image']

        image_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(image_data)

        image = Image.open(io.BytesIO(image_bytes))

        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image_' + str(int(time.time())) + '.png')

        image.save(filename, 'PNG')

        return jsonify({'message': 'Image uploaded successfully!', 'filename': filename}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import time
    app.run(debug=True)