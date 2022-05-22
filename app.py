from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Order %r>' %self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/posts')
def posts():
    orders = Order.query.order_by(Order.date.desc()).all()
    return render_template("posts.html", orders=orders)


@app.route('/posts/<int:id>')
def post_detail(id):
    order = Order.query.get(id)
    return render_template("post_detail.html", order=order)


@app.route('/posts/<int:id>/delete')
def post_delete(id):
    order = Order.query.get_or_404(id)

    try:
        db.session.delete(order)
        db.session.commit()
        return redirect('/posts')
    except:
        return "Something went wrong :("


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    order = Order.query.get(id)
    if request.method == "POST":
        order.title = request.form['title']
        order.intro = request.form['intro']
        order.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "Something went wrong :("

    else:
        return render_template("post_update.html", order=order)


@app.route('/make-an-order', methods=['POST', 'GET'])
def make_order():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        order = Order(title=title, intro=intro, text=text)

        try:
            db.session.add(order)
            db.session.commit()
            return redirect('/posts')
        except:
            return "Something went wrong :("

    else:
        return render_template("make-an-order.html")


if __name__ == "__main__":
    app.run(debug=True)