from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient(
    'mongodb+srv://test:sparta@cluster0.njfgeoe.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile = ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('indexx.html')

@app.route("/walk", methods=["POST"])
def web_walk_post():
    user_id_receive = request.form['user_id_receive']
    title_receive = request.form['title_receive']
    review_receive = request.form['review_receive']
    img_receive = request.form['img_receive']
    category_receive = request.form['category_receive']

    walk_list = list(db.walk.find({}, {'_id':False}))
    count = len(walk_list) +1

    doc={
        'post_id': count,
        'user_id':user_id_receive,
        'title':title_receive,
        'review':review_receive,
        'img':img_receive,
        'category':category_receive
    }
    db.walk.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})

@app.route("/walk", methods=["GET"])
def web_walk_get():
    walk_list = list(db.walk.find({}, {'_id':False}))

    return jsonify({'walks': walk_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)