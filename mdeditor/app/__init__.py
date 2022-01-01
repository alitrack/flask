from  hashlib import md5
from pathlib import Path
from flask import Flask,request,jsonify,render_template
import os
app = Flask(__name__)
app.config.from_object('config')
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect(app)
@app.route("/")
def index():
    return render_template("index.html")

@csrf.exempt
@app.route('/vditor/uploads/',methods=['POST'])
def vditor_uploads():
    """
    支持黏贴、拖拽和点击图片上传
    """

    images_upload = request.files.get('file[]', None)

    img = images_upload.stream.read()
    digest=md5(img).hexdigest()
    suffix = Path(images_upload.filename).suffix
    images_name = f'{digest}{suffix}'
    image_full_name = os.path.join(app.config['IMG_UPLOAD_FOLDER'], images_name)


    if not Path(image_full_name).exists():
        with open(image_full_name,"wb") as f :
            f.write(img)
    image_full_path = os.path.join(app.config['IMG_UPLOAD_URL'], images_name)
    return jsonify(
                            {
                    "msg": "Success!",
                    "code": 0,
                    "data": {
                    "errFiles": [],
                    "succMap": {
                        images_upload.filename: image_full_path,
                        }
                    }
                }
        ),200

@csrf.exempt
@app.route('/vditor/save/',methods=['POST'])
def vditor_save():
    """"
    markdown 保存
    json格式
    """
    data = request.json
    print(data['fname'])
    print(data['content'])
    # 保存代码省略
    
    return jsonify({"msg":0}),200