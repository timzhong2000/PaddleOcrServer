# PaddleOcr Restful Server

## 构建镜像

```
docker build -t paddleocr:v1 .
```

## 启动以及配置

### 环境变量说明

| 环境变量      | 描述                         | 取值                 | 留空行为                  |
| ------------- | ---------------------------- | -------------------- | ------------------------- |
| USE_GPU       | 强制开启 GPU 模式(CUDA only) | 任意非空值           | 自动判断是否可以 GPU 加速 |
| USE_ANGLE_CLS | 开启文本方向分类器           | 任意非空值           | 关闭方向分类器            |
| PADDLE_LANG   | 识别语言                     | 详细见下面的语种缩写 | 英语和中文                |

### example

- 强制 GPU 模式
- 开启文本方向分类器
- 语种为日本语

```
docker run -d --gpus=all -e USE_GPU=1 -e USE_ANGLE_CLS=1 -e PADDLE_LANG=japan -p 5000:5000 paddleocr:v1
```

## API

- Method: POST
- URL: /api/rec
- Request Body (form-data):

| key | type   |
| --- | ------ |
| pic | `File` |

- Response:

```
[
  [
    [
      [665.0,79.0],
      [1566.0,77.0],
      [1566.0,128.0],
      [665.0,130.0]
    ], // 矩形坐标
    [
      "helloworld",
      0.9479010105133057
    ] // ocr结果和置信度
  ],
  ...
]
```

## Paddle 支持语种及缩写

[来自 PaddleOcr Github](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_ch/multi_languages.md)

| 语种                  | 描述                | 缩写        |     | 语种         | 描述         | 缩写 |
| --------------------- | ------------------- | ----------- | --- | ------------ | ------------ | ---- |
| 中文                  | chinese and english | ch          |     | 保加利亚文   | Bulgarian    | bg   |
| 英文                  | english             | en          |     | 乌克兰文     | Ukranian     | uk   |
| 法文                  | french              | fr          |     | 白俄罗斯文   | Belarusian   | be   |
| 德文                  | german              | german      |     | 泰卢固文     | Telugu       | te   |
| 日文                  | japan               | japan       |     | 阿巴扎文     | Abaza        | abq  |
| 韩文                  | korean              | korean      |     | 泰米尔文     | Tamil        | ta   |
| 中文繁体              | chinese traditional | chinese_cht |     | 南非荷兰文   | Afrikaans    | af   |
| 意大利文              | Italian             | it          |     | 阿塞拜疆文   | Azerbaijani  | az   |
| 西班牙文              | Spanish             | es          |     | 波斯尼亚文   | Bosnian      | bs   |
| 葡萄牙文              | Portuguese          | pt          |     | 捷克文       | Czech        | cs   |
| 俄罗斯文              | Russia              | ru          |     | 威尔士文     | Welsh        | cy   |
| 阿拉伯文              | Arabic              | ar          |     | 丹麦文       | Danish       | da   |
| 印地文                | Hindi               | hi          |     | 爱沙尼亚文   | Estonian     | et   |
| 维吾尔                | Uyghur              | ug          |     | 爱尔兰文     | Irish        | ga   |
| 波斯文                | Persian             | fa          |     | 克罗地亚文   | Croatian     | hr   |
| 乌尔都文              | Urdu                | ur          |     | 匈牙利文     | Hungarian    | hu   |
| 塞尔维亚文（latin)    | Serbian(latin)      | rs_latin    |     | 印尼文       | Indonesian   | id   |
| 欧西坦文              | Occitan             | oc          |     | 冰岛文       | Icelandic    | is   |
| 马拉地文              | Marathi             | mr          |     | 库尔德文     | Kurdish      | ku   |
| 尼泊尔文              | Nepali              | ne          |     | 立陶宛文     | Lithuanian   | lt   |
| 塞尔维亚文（cyrillic) | Serbian(cyrillic)   | rs_cyrillic |     | 拉脱维亚文   | Latvian      | lv   |
| 毛利文                | Maori               | mi          |     | 达尔瓦文     | Dargwa       | dar  |
| 马来文                | Malay               | ms          |     | 因古什文     | Ingush       | inh  |
| 马耳他文              | Maltese             | mt          |     | 拉克文       | Lak          | lbe  |
| 荷兰文                | Dutch               | nl          |     | 莱兹甘文     | Lezghian     | lez  |
| 挪威文                | Norwegian           | no          |     | 塔巴萨兰文   | Tabassaran   | tab  |
| 波兰文                | Polish              | pl          |     | 比尔哈文     | Bihari       | bh   |
| 罗马尼亚文            | Romanian            | ro          |     | 迈蒂利文     | Maithili     | mai  |
| 斯洛伐克文            | Slovak              | sk          |     | 昂加文       | Angika       | ang  |
| 斯洛文尼亚文          | Slovenian           | sl          |     | 孟加拉文     | Bhojpuri     | bho  |
| 阿尔巴尼亚文          | Albanian            | sq          |     | 摩揭陀文     | Magahi       | mah  |
| 瑞典文                | Swedish             | sv          |     | 那格浦尔文   | Nagpur       | sck  |
| 西瓦希里文            | Swahili             | sw          |     | 尼瓦尔文     | Newari       | new  |
| 塔加洛文              | Tagalog             | tl          |     | 保加利亚文   | Goan Konkani | gom  |
| 土耳其文              | Turkish             | tr          |     | 沙特阿拉伯文 | Saudi Arabia | sa   |
| 乌兹别克文            | Uzbek               | uz          |     | 阿瓦尔文     | Avar         | ava  |
| 越南文                | Vietnamese          | vi          |     | 阿瓦尔文     | Avar         | ava  |
| 蒙古文                | Mongolian           | mn          |     | 阿迪赫文     | Adyghe       | ady  |
