from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])


@app.route('/search/<q>/<page>')
def search(q):
    """
    :parameter

    q 用户输入的查询词(关键字或是 isbn)
    page 页数

    :return:
    """
    isbn_or_key = 'key'
    if len(q)== 13 and q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key


if __name__ == '__main__':
    app.run()
