from flask import Flask, url_for, render_template

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
        title='bottles'

    )


if __name__ == '__main__':
    app.run()
