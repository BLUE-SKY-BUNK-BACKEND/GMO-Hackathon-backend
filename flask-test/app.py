# coding: utf-8

from flask import Flask, jsonify, request
import os
import requests

# 追記
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

app = Flask(__name__)

host="127.0.0.1"
port= 4000



@app.route('/')
def hello_world():
    # ぐるナビAPIの撮ってきたデータ
    # URL = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    # API_KEY = "3c2f3b5a9fde3c4c"
    # params = {
    #     "key": API_KEY,
    #     "keyword": "沖縄",
    #     "format": "json"
    # }
    # res = requests.get(URL, params)
    # result = res.json()
    # items = result["results"]["shop"]
    
    # ichibarのAPIのデータ
    # URL2 = "https://api.gmo-aozora.com/ganb/api/simulator/personal/v1/accounts/transactions&dateFrom=2021-07-30"
    URL2 = 'https://api.sunabar.gmo-aozora.com/personal/v1/accounts/'
    header = {
        'accept': 'application/json',
        'charset': 'UTF-8',
        'x-access-token': 'NWY3NjFhYTUyYTI4NzJmMDY2N2JlODUx',
    }
        # "x-access-token": "M2ZlMTYxMGYxOTU1YjkzYTJkNWQ0NDQ4"  ｓｎｂｒにじ支店（302）
    res2 = requests.get(URL2, header)
    
    if res2.status_code == 200:
        result2 = res2.json()
    else:
        result2 = res2.json()["errorMessage"]
    
    # return jsonify({'message': 'Hello world !!!!!!!!',
                    # "GMO" : res2.status_code,
                    # "あおぞらGMO Hackasonのデータ" : result2
                    # })
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://info.finance.yahoo.co.jp/fx/')
    usd_jpy = driver.find_element(By.ID, 'USDJPY_top_bid').text
    driver.quit()
    return usd_jpy


db_data = [
    {'title': 'タイトル1', 'body': '本文one'},
    {'title': 'タイトル2', 'body': '本文two'},
    {'title': 'タイトル3', 'body': '本文three'},
    {'title': 'タイトル4', 'body': '本文4'},
    {'title': 'タイトル5', 'body': '本文5'},
]

app.config['JSON_AS_ASCII'] = False 

@app.route('/posts', methods=['GET'])
def get_all_posts():
    limit = request.args['limit']
    return jsonify(db_data[:int(limit)])


@app.route('/post/<id>', methods=['GET'])
def get_post(id):
    return jsonify(db_data[int(id)])

# POST処理
@app.route('/post/add', methods=['POST'])
def create_post():
    post = request.json
    db_data.append(post)
    return jsonify(db_data)


# PUT処理 更新
# $ curl -X PUT -H "Content-Type: application/json" -d '{"title":"投稿修正", "body":"修正済み投稿です"}' localhost:4000/post/update/1
# idが1番のものを削除
@app.route('/post/update/<id>', methods=['PUT'])
def update_post(id):
    post = request.json
    db_data[int(id)] = post
    return jsonify(db_data)


# DELETE処理 削除
# $ curl -X DELETE localhost:5000/post/delete/1
# idが1の内容を削除
@app.route('/post/delete/<id>', methods=['DELETE'])
def delete_post(id):
    db_data.pop(int(id))
    return jsonify(db_data)



if __name__ == "__main__":
    app.run(host=host, port=int(os.environ.get("PORT", 4000)), debug=True)

