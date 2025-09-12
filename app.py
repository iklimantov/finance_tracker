# app.py
from flask import Flask, render_template, request, redirect, url_for, abort
from models import db, Expense
import datetime

app = Flask(__name__)

# Конфигурация БД (файл finance.db в корне проекта)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Инициализируем SQLAlchemy
db.init_app(app)

@app.route("/")
def index():
    category = request.args.get("category", type=str)
    start_date = request.args.get("start_date", type=str)
    end_date = request.args.get("end_date", type=str)

    query = Expense.query.order_by(Expense.date.desc())

    if category:
        query = query.filter(Expense.category == category)

    if start_date:
        try:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            query = query.filter(Expense.date >= start)
        except ValueError:
            pass

    if end_date:
        try:
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            query = query.filter(Expense.date <= end)
        except ValueError:
            pass

    expenses = query.all()
    total = sum(e.amount for e in expenses)

    categories = db.session.query(Expense.category).distinct().all()
    categories = [c[0] for c in categories]

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        categories=categories,
        selected=category,
        start_date=start_date,
        end_date=end_date,
    )


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            category = request.form["category"].strip()
            date_str = request.form.get("date")
            if date_str:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            else:
                date = datetime.date.today()
            description = request.form.get("description") or None

            new = Expense(amount=amount, category=category, date=date, description=description)
            db.session.add(new)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            # В каркасе просто возвращаем ошибку 400; позже можно показать сообщение в UI
            abort(400, description=str(e))
    else:
        today = datetime.date.today().isoformat()
        return render_template("add_expense.html", today=today)

@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Создаём таблицы при первом запуске
    with app.app_context():
        db.create_all()
    app.run(debug=True)
