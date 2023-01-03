"""
Custom API based website
Show stock market data based on symbol
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from dotenv.main import DotEnv
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
import requests

dot = DotEnv(".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = dot.get("SECRET_KEY")
Bootstrap(app)


# form
class MyForm(FlaskForm):
    symbol = StringField(
        validators=[DataRequired(), Length(1, 10)],
        render_kw={"placeholder": "Type Symbol of company e.g. TSLA"})


def get_stock_data(symbol):
    """
    Get stock data based on symbol
    :param symbol:
    :return:
    """
    params = {
        'access_key': dot.get("ACCESS_KEY"),
        'symbols': symbol,
    }
    api_result = requests.get(f'http://api.marketstack.com/v1/eod/latest', params)
    api_response = api_result.json()
    return api_response


@app.route("/", methods=["GET", "POST"])
def home():
    form = MyForm()
    stock_data = ""
    error_data = ""
    if form.validate_on_submit():
        symbol = form.symbol.data.upper()
        stock_data = get_stock_data(symbol)

        if stock_data.get("data"):
            stock_data = stock_data["data"]
        else:
            error_data = stock_data["error"]
            stock_data = ""

    return render_template("index.html", form=form, stock_data=stock_data, error_data=error_data)


if __name__ == "__main__":
    app.run(debug=True)
