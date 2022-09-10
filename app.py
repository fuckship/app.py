from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.gt6lkab.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():


    return render_template('index.html')


@app.route("/homework2", methods=["POST"])
def homework_post():
    다불러 = list(db.homework2.find({}, {'_id': False}))

    이름 = request.form['이름']
    댓글 = request.form['댓글']

    count = len(다불러) + 1

    doc = {

        'name' : 이름,
        'comment' : 댓글,
        'number' : count




    }

    db.homework2.insert_one(doc)


    return jsonify({'msg': '저장완료!'})




@app.route("/homework2", methods=["GET"])
def homework_get():
    all_users = list(db.homework2.find({}, {'_id': False}))


    return jsonify({ '불러온정보': all_users})

@app.route("/delet", methods=["POST"])
def delet_post():
    이거맞냐 = request.form['give']

    맞네 = int(이거맞냐)

    db.homework2.delete_one({'number': 맞네})


    print(맞네)
    return jsonify({'msg': '삭제완료완료'})








if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
