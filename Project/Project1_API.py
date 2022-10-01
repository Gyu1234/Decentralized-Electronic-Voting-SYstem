from flask import Flask, jsonify, request

app = Flask(__name__)

chain = []
cnt = 0

@app.route('/list', methods=['GET'])
def vote_list():
    return jsonify(chain)


@app.route('/open', methods=['POST'])
def vote_open():
    try:
        global cnt
        data = request.get_json()
        block1 = {

            'type': 'open',
            'data': {
                'id': str(cnt),
                'question': data['question'],
                'options': data['options']
            }
        }
        chain.append(block1)
        cnt += 1
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'fail'})

@app.route('/vote', methods=['POST'])
def vote():
    try:
        data = request.get_json()
        block2 = {
            'type': 'vote',
            'data': {
                'id': '0',
                'vote': data['vote']
            }
        }
        chain.append(block2)
        return jsonify({'status':'success'})
    except:
        return jsonify({'status': 'fail'})

app.run()
