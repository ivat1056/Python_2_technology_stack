from flask import Flask

app = Flask(__name__)

@app.route("/square/<int:n>")
def square(n):
    result = n ** 2
    return f"Квадрат числа {n} равен {result}."

@app.route("/length/<string:stroka>")
def length(stroka):
    result = len(stroka)
    return f"Длина строки \"{stroka}\" равна {result}."

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    result = num1 + num2
    return f"Сумма {num1} и {num2} равна {result}."

@app.route("/error/")
def error():
    result = 1 / 0
    return f"Результат: {result}"

if __name__ == "__main__":
    app.run(debug=True)
