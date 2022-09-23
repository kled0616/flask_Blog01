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
    return 'hello world99'

if __name__ == '__main__':
    app.run()