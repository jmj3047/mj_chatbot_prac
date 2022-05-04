from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000에 가면 함수 실행
def root_world():
    result = 'root world'
    return result

@app.route('/hello') #127.0.0.1:5000/hello 를 가면 실행
def hello_world():
    result = 'hello world'
    return result

@app.route('/users/<user_id>') 
#동적 변수를 사용하여 URI 접속
# <동적변수>를 뷰함수의 인자로 사용
# <동적 변수> 다음에 /를 넣으면 안됨
def user_id(userid):
    result = 'user_id = ' + userid
    return result

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

# url_for(): 함수를 호출하는 URI를 반환
# redirect(): 다른 route 경로 이동(다른 페이지 이동)

if __name__ == '__main__':
    app.debug = True
    app.run()