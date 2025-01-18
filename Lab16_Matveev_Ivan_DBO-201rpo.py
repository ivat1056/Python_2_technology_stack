from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Добро пожаловать на главную страницу!"

@app.route("/about/")
def about():
    return "Это страница о нас."

@app.route("/services/")
def services():
    return """Наши услуги:
    <ul>
        <li>Консалтинг</li>
        <li>Разработка</li>
        <li>Поддержка</li>
    </ul>
    """

@app.route("/services/<string:n>/")
def specific_service(n):
    services_mapping = {
        "consulting": "Консалтинг",
        "development": "Разработка",
        "support": "Поддержка"
    }
    service = services_mapping.get(n.lower())
    if service:
        return f"Наши услуги: {service}"
    else:
        return "Услуга не найдена!", 404

if __name__ == "__main__":
    app.run(debug=True)
