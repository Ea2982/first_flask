from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Hello, World!',
        header='Welcome',
        text='TODO'
    )
@app.route('/99-bottles')
def bottles():
    return render_template(
        'bottles.html',
        title='bottles1'
    )
@app.route('/echo')
def echo():
    print(request.path)
    return request.path
@app.route('/args', methods=['GET'])
def args():
    return render_template(
        'args.html',
        a=list(request.args.values())
    )
@app.route(('/div/<int:n1>/<int:n2>'))
def div(n1, n2):
    return str(n1 / n2)
if __name__ == '__main__':
    app.run()
