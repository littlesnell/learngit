from flask import request,Flask
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'hello!'
	searchword = request.args.get('user', '')
	return user
	searchword = request.args.get('key', '')
	return key
    else:
        return 'error!'
	

if __name__ == '__main__':
    app.run(host="0.0.0.0")
