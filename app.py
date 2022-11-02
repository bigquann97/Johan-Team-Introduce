from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://sparta:sparta@43.201.105.241', 27017)
db = client.johan

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/teaminto')
def team():
    return render_template('teaminto.html')

@app.route('/bung')
def byeongdoo():
    return render_template('1.html')

@app.route('/ikhyeon')
def ikhyeon():
    return render_template('2.html')

@app.route('/sein')
def sein():
    return render_template('3.html')

@app.route('/seong')
def seongrock():
    return render_template('4.html')

@app.route('/quan')
def gwanho():
    return render_template('5.html')

@app.route("/api/gwanho", methods=["POST"])
def gwanho_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.gwanho.insert_one(doc)
    return jsonify({'msg': '댓글 작성 완료!'})

@app.route("/api/gwanho", methods=["GET"])
def gwanho_get():
    find = list(db.gwanho.find({}, {'_id': False}))
    return jsonify({'gwanho': find})

@app.route("/api/gwanho/like", methods=["POST"])
def gwanho_cheer():
    find = list(db.gwanho.find({}, {'_id': False}))
    count = find[0]['count']
    db.gwanho.update_one({'count': count}, {'$set':{'count': count + 1}})
    return jsonify({'stats': 'ok'})

'''''''''''''''''''''
성락 소개페이지 API 시작
'''''''''''''''''''''
@app.route("/api/seongrock/comment", methods=["POST"])
def seong_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    index_receive = request.form['index']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'index' : index_receive,
    }
    db.seong.insert_one(doc)
    return jsonify({'msg': '댓글 작성 완료'})

@app.route("/api/seongrock/comment", methods=["GET"])
def seong_get():
    find = list(db.seong.find({}, {'_id': False}))
    print(find)
    return jsonify({'seongrock': find})

@app.route("/api/seongrock/comment", methods=["DELETE"])
def seong_delete_comment():
    index_receive = request.form['target']
    print(index_receive)
    db.seong.delete_one({"index" : index_receive})
    return jsonify({'msg' : '댓글 삭제 완료'})


'''테스트 버전 실행할따마다 db비우기'''
def clear():
    db.seong.delete_many({})
    return

clear()
'''''''''''''''''''''
성락 소개페이지 API 끝
'''''''''''''''''''''


'''''''세인영역'''''''''
@app.route("/api/sein", methods=["POST"])
def sein_comment_post():
    name_receive = request.form['id_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.sein.insert_one(doc)
    return jsonify({'msg': '댓글 작성 완료!'})

@app.route("/api/sein", methods=["GET"])
def sein_get():
    find = list(db.sein.find({}, {'_id': False}))
    return jsonify({'sein_comment': find})

@app.route("/api/sein/like", methods=["POST"])
def sein_like_post():
    find = list(db.seinlike.find({},{',_id' : False}).sort('like', -1))

    if not find:
        db.seinlike.insert_one({'current_like' : 1})
    else:
        like = find[0]['current_like']
        new_like = like + 1
        db.seinlike.update_one({'current_like': like}, {'$set': {'current_like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})

@app.route("/api/sein/like", methods=["GET"])
def sein_like_get():
    find = list(db.seinlike.find({},{',_id' : False}).sort('like', -1))
    return jsonify({'sein_like_get' : find[0]['current_like']})
'''''''세인 영역 끝'''''''''


@app.route("/api/ikhyeon", methods=["POST"])
def ikhyeon_post():
    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']
    doc = {
        'comment':comment_receive,
        'name':name_receive
    }
    db.ikhyeon.insert_one(doc)
    return jsonify({'msg':'업로드 완료!'})

@app.route("/api/ikhyeon", methods=["GET"])
def ikhyeon_get():
    ikhyeon_list = list(db.ikhyeon.find({}, {'_id': False}))
    return jsonify({'ikhyeon':ikhyeon_list})

'''
@app.route("/gwanho-cheer", methods=["POST"])
def gwanho_cheer():
    find = list(db.gwanho.find({}, {'_id': False}))
    count = find[0]['count']
    db.gwanho.update_one({'count': count}, {'$set':{'count': count + 1}})
    return jsonify({'stats': 'ok'})
'''




if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)



# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://test:sparta@cluster0.mbry8je.mongodb.net/?retryWrites=true&w=majority')
# db = client.johan
