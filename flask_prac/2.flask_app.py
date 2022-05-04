from flask import Flask, request, session, render_template
app = Flask(__name__)

@app.route('/login_form_get') 
def login_form_get():
    return render_template('login/login_form_get.html')

@app.route('/login_get_proc', methods=['GET']) 
def login_get_proc():
    user_id = request.args.get('user_id')
    user_pwd = request.args.get('user_pwd')
    
    if len(user_id) == 0 or len(user_pwd) == 0:
        return 'no {} or {}'.format(user_id, user_pwd)
    
    return 'welcome {}'.format(user_id)


if __name__ == '__main__':
    app.debug = True
    app.run()