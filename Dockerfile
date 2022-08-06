FROM paddlepaddle/paddle:2.3.1-gpu-cuda11.2-cudnn8
WORKDIR /paddle
RUN pip install "paddleocr>=2.0.1" -i https://mirror.baidu.com/pypi/simple
RUN pip install "flask"
ADD . /paddle
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000