from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        # Get form data
        number1 = request.form.get("var_1", type=int, default=0)
        number2 = request.form.get("var_2", type=int, default=0)
        operation = request.form.get("operation")

        # Perform the calculation
        if operation == "Addition":
            result = number1 + number2
        elif operation == "Subtraction":
            result = number1 - number2
        elif operation == "Multiplication":
            result = number1 * number2
        elif operation == "Division":
            result = number1 / number2
        else:
            result = None

        return render_template("calculator.html", result=result)

    # If it's a GET request (initial load), render the template
    return render_template("calculator.html", result=None)


if __name__ == "__main__":
    app.run(debug=True)
