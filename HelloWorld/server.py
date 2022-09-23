from flask import Flask,request

app = Flask(__name__)
# # app = Flask("my-custom-app", static_folder="path1",template_folder="path2")
# @app.route('/')
# def hello_world():
#     # return 'Hello world'
#     # return request.args.__str__()
#     r = request.args.get('info')
#     if r==None:
#         # do something
#         return ''
#     return r

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

#     # app.run()
#     # app.run(debug=True)
#     # app.run(host='0.0.0.0', port=80, debug=True)

@app.route('/')
def hello_world():
    return 'hello world'

# @app.route('/register', methods=['GET', 'POST']) 同時支援
@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    # print(request.stream.read()) # 不要用，否则下面的form取不到数据
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    return 'welcome'



if __name__ == '__main__':
    app.run(port=5000, debug=True)