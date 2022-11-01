from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://sparta:sparta@43.201.105.241', 27017)
db = client.johan

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('teaminto.html')

@app.route('/byungdoo')
def byungdoo():
    return render_template('1.html')

@app.route('/ikhyeon')
def ikhyeon():
    return render_template('2.html')

@app.route('/sein')
def sein():
    return render_template('3.html')

@app.route('/seongrak')
def seongrak():
    return render_template('4.html')

@app.route('/gwanho')
def gwanho():
    return render_template('5.html')

@app.route("/gwanho", methods=["POST"])
def gwanho_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.gwanho.insert_one(doc)
    return jsonify({'msg': '댓글 작성 완료!'})

@app.route("/gwanho-api", methods=["GET"])
def gwanho_get():
    find = list(db.gwanho.find({}, {'_id': False}))
    return jsonify({'gwanho': find})

@app.route("/gwanho-cheer", methods=["POST"])
def gwanho_cheer():
    find = list(db.gwanho.find({}, {'_id': False}))
    count = find[0]['count']
    db.gwanho.update_one({'count': count}, {'$set':{'count': count + 1}})
    return jsonify({'stats': 'ok'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)



# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://test:sparta@cluster0.mbry8je.mongodb.net/?retryWrites=true&w=majority')
# db = client.johan