from flask import Flask, request, session, render_template
app = Flask(__name__)

@app.route('/input-form') 
def login_form_get():
    return render_template('input_form.html')

@app.route('/input_form', methods=['GET']) 
def input_form():
    user_input = request.args.get('user_input')
    
    if len(user_input) == 0 :
        return 'no {} '.format(user_input)
    
    return '{} printed.'.format(user_input)


if __name__ == '__main__':
    app.debug = True
    app.run()