from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@sparta.t6tojb3.mongodb.net/sparta?retryWrites=true&w=majority',
                     tlsCAFile=ca)

db = client.dbsparta


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/detail/artistSong?xxnm=14945151', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#songlist-box > div.music-list-wrap > table > tbody > tr')

for music in musics:
        image = music.select_one('td > a > img')['src']
        title = music.select_one('td.info > a.title.ellipsis')['title']
        album = music.select_one('td.info > a.albumtitle.ellipsis').text

        doc = {
            'image': image,
            'title': title,
            'album': album
        }
        db.musics.insert_one(doc)

@app.route("/api/music", methods=["GET"])
def music_get():
    find = list(db.musics.find({}, {'_id': False}))
    return jsonify({'musics': find})

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/teaminto')
def team():
    return render_template('teaminto.html')


@app.route('/byeongdoo')
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

@app.route('/kimjohan')
def kimjohan():
    return render_template('6.html')


@app.route("/api/gwanho", methods=["POST"])
def gwanho_comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.gwanho.insert_one(doc)
    return jsonify({'msg': '?????? ?????? ??????!'})


@app.route("/api/gwanho", methods=["GET"])
def gwanho_get():
    find = list(db.gwanho.find({}, {'_id': False}))
    return jsonify({'gwanho': find})


@app.route("/api/gwanho/like", methods=["POST"])
def gwanho_cheer():
    find = list(db.gwanho.find({}, {'_id': False}))
    count = find[0]['count']
    db.gwanho.update_one({'count': count}, {'$set': {'count': count + 1}})
    return jsonify({'stats': 'ok'})


'''''''''''''''''''''
?????? ??????????????? API ??????
'''''''''''''''''''''


@app.route("/api/seongrock/comment", methods=["POST"])
def post_seong_comment():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    index_receive = request.form['index']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'index': index_receive,
        'current_like': 0,
    }
    db.seong.insert_one(doc)
    return jsonify({'msg': '?????? ?????? ??????'})


@app.route("/api/seongrock/comment", methods=["GET"])
def get_seong_comment():
    find = list(db.seong.find({}, {'_id': False}))
    print(find)
    return jsonify({'seongrock': find})


@app.route("/api/seongrock/comment", methods=["DELETE"])
def delete_seong_comment():
    index_receive = request.form['target']
    print(index_receive)
    db.seong.delete_one({"index": index_receive})
    return jsonify({'msg': '?????? ?????? ??????'})


@app.route("/api/seongrock/comment/like", methods=["POST"])
def plus_seong_comment_like():
    index_receive = request.form['target']

    find = db.seong.find_one({"index": index_receive})
    like = find['current_like']
    new_like = like + 1
    db.seong.update_one({'index': index_receive}, {'$set': {'current_like': new_like}})

    return jsonify({'msg': '????????? ??????!'})


'''????????? ?????? ?????????????????? db?????????''''''
def clear():
    db.seong.delete_many({})
    return

clear()
?????? ??????????????? API ???
'''''''''''''''''''''

'''''''????????????'''''''''


@app.route("/api/sein", methods=["POST"])
def sein_comment_post():
    name_receive = request.form['id_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.sein.insert_one(doc)
    return jsonify({'msg': '?????? ?????? ??????!'})


@app.route("/api/sein", methods=["GET"])
def sein_get():
    find = list(db.sein.find({}, {'_id': False}))
    return jsonify({'sein_comment': find})


@app.route("/api/sein/like", methods=["POST"])
def sein_like_post():
    find = list(db.seinlike.find({}, {',_id': False}).sort('like', -1))

    if not find:
        db.seinlike.insert_one({'current_like': 1})
    else:
        like = find[0]['current_like']
        new_like = like + 1
        db.seinlike.update_one({'current_like': like}, {'$set': {'current_like': new_like}})

    return jsonify({'msg': '????????? ??????!'})


@app.route("/api/sein/like", methods=["GET"])
def sein_like_get():
    find = list(db.seinlike.find({}, {',_id': False}).sort('like', -1))
    return jsonify({'sein_like_get': find[0]['current_like']})


'''''''?????? ?????? ???'''''''''


@app.route("/api/ikhyeon", methods=["POST"])
def ikhyeon_post():
    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']
    doc = {
        'comment': comment_receive,
        'name': name_receive
    }
    db.ikhyeon.insert_one(doc)
    return jsonify({'msg': '????????? ??????!'})


@app.route("/api/ikhyeon", methods=["GET"])
def ikhyeon_get():
    ikhyeon_list = list(db.ikhyeon.find({}, {'_id': False}))
    return jsonify({'ikhyeon': ikhyeon_list})


# ?????? ??????######################

@app.route("/api/byeongdoo", methods=["POST"])
def byeongdoo_save_comment():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.byeongdoo.insert_one(doc)
    return jsonify({'msg': '?????? ??????'})


@app.route("/api/byeongdoo", methods=["GET"])
def byeongdoo_get():
    find = list(db.byeongdoo.find({}, {'_id': False}))
    return jsonify({'byeongdoo': find})


@app.route("/api/byeongdoo/like", methods=["POST"])
def byeongdoo_add_like():
    find = list(db.byeongdoolike.find({}, {',_id': False}).sort('like', -1))

    if not find:
        db.byeongdoolike.insert_one({'like_count': 1})
    else:
        like = find[0]['like_count']
        new_like = like + 1
        db.byeongdoolike.update_one({'like_count': like}, {'$set': {'like_count': new_like}})

    return jsonify({'msg': '????????? ??????'})


@app.route("/api/byeongdoo/like", methods=["GET"])
def byeongdoo_get_like():
    find = list(db.byeongdoolike.find({}, {',_id': False}).sort('like', -1))

    like = find[0]['like_count']

    return jsonify({'byeongdoolike': like})


# ?????? ??? #######################
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
