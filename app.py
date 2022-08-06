import json
from os import remove, mkdir, path, getenv
from uuid import uuid1
from flask import Flask, request
from paddleocr import PaddleOCR

# config
lang = getenv('PADDLE_LANG', 'en')
use_angle_cls = bool(getenv("USE_ANGLE_CLS"))
upload_folder = './upload/'
use_gpu = bool(getenv("USE_GPU"))

# app
app = Flask(__name__)

paddle = PaddleOCR(
    use_angle_cls=use_angle_cls,
    lang=lang,
    use_gpu=use_gpu,
    precision='fp32',
    use_tensorrt=False
)

if not path.exists(upload_folder):
    mkdir(upload_folder)

@app.route("/api/rec", methods=['POST'])
def rec():
    f = request.files['pic']
    path = upload_folder + str(uuid1())
    f.save(path)
    result = paddle.ocr(path)
    remove(path)
    return json.dumps(result)
