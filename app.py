from flask import Flask, render_template_string, request, redirect, url_for

# Define the commission grid with percentages
commission_grid = {
    "Wireless Services": {
        "Postpaid": 0.35,
        "Prepaid": 0.20,
        "HUG Migration": 0.14,
        "Brand Migration (Bell to Virgin)": 0.05,
    },
    "Extra Services": {
        "Prepaid Auto Top-Up": 5,
        "Applecare": 2,
        "Lost/Stolen Loaner": 7.5,  # Average of 5/10
    },
    "Residential Services": {
        "Fibe TV - Starter": 12,
        "Fibe TV - Good": 30,
        "Fibe TV - Better": 40,
        "Fibe TV - Best": 50,
        "Aliant TV": 35,
        "Fibe Migration": 35,
        "Internet - Aliant Fibe/DSL": 20,
        "Internet Migration": 5,
        "Home Phone": 10,
        "Long Distance": 2,
    },
}

# Initialize Flask app
app = Flask(__name__)

# Initialize global variables to store cumulative total and sales history
total_commission = 0
total_extra_earnings = 0
sales_history = []
extra_earnings_history = []

# HTML template with a modern, clean UI
html_template = """
<!doctype html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Bell Commission Tracker</title>
    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\">
    <style>
        body {
            background-color: #f9fafb;
            font-family: 'Arial', sans-serif;
        }
        .card {
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .btn-primary {
            background-color: #0055A4;
            border: none;
            border-radius: 8px;
        }
        .btn-primary:hover {
            background-color: #003B73;
        }
        .btn-warning {
            background-color: #FFC72C;
            border: none;
            border-radius: 8px;
        }
        .btn-danger {
            background-color: #DA291C;
            border: none;
            border-radius: 8px;
        }
        .total-display {
            font-size: 1.5rem;
            font-weight: bold;
            color: #264653;
        }
        .list-group-item {
            border: none;
            background-color: #e9ecef;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        h1, h2, h3 {
            color: #264653;
        }
    </style>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const saleTypeDropdown = document.getElementById("sale_type");
            const saleAmountInput = document.getElementById("sale_amount");

            saleTypeDropdown.addEventListener("change", function() {
                const selectedType = saleTypeDropdown.value;
                const residentialServices = {
                    "Fibe TV - Starter": 12,
                    "Fibe TV - Good": 30,
                    "Fibe TV - Better": 40,
                    "Fibe TV - Best": 50,
                    "Aliant TV": 35,
                    "Fibe Migration": 35,
                    "Internet - Aliant Fibe/DSL": 20,
                    "Internet Migration": 5,
                    "Home Phone": 10,
                    "Long Distance": 2
                };

                const extraServices = {
                    "Prepaid Auto Top-Up": 5,
                    "Applecare": 2,
                    "Lost/Stolen Loaner": 7.5
                };

                if (residentialServices[selectedType]) {
                    saleAmountInput.value = residentialServices[selectedType];
                } else if (extraServices[selectedType]) {
                    saleAmountInput.value = extraServices[selectedType];
                } else {
                    saleAmountInput.value = "";
                }
            });
        });
    </script>
</head>
<body>
    <div class=\"container py-5\">
        <h1 class=\"text-center mb-4\">Bell Commission Tracker</h1>
        <div class=\"card\">
            <div class=\"card-body\">
                <form method=\"POST\" action=\"/add_sale\">
                    <div class=\"mb-3\">
                        <label for=\"sale_type\" class=\"form-label\">Select Sale Type:</label>
                        <select name=\"sale_type\" id=\"sale_type\" class=\"form-select\">
                            {% for category, items in commission_grid.items() %}
                                <optgroup label=\"{{ category }}\">
                                    {% for sale, commission in items.items() %}
                                        <option value=\"{{ sale }}\">{{ sale }} - Commission: {{ commission }}</option>
                                    {% endfor %}
                                </optgroup>
                            {% endfor %}
                            <option value=\"Accessories\">Accessories - Commission: 9%</option>
                            <option value=\"SPC\">SPC (Smartphone Care) - Commission: 30%</option>
                        </select>
                    </div>
                    <div class=\"mb-3\">
                        <label for=\"sale_amount\" class=\"form-label\">Enter Sale Amount (CAD):</label>
                        <input type=\"number\" name=\"sale_amount\" id=\"sale_amount\" class=\"form-control\" step=\"0.01\" required>
                    </div>
                    <button type=\"submit\" class=\"btn btn-primary w-100\">Add Sale</button>
                </form>
            </div>
        </div>

        <div class=\"card\">
            <div class=\"card-body\">
                <h2 class=\"total-display\">Running Total: {{ total | round(2) }} CAD</h2>
                <h3 class=\"h5 mt-3\">Sales History:</h3>
                <ul class=\"list-group\">
                    {% for sale in sales_history %}
                        <li class=\"list-group-item\">{{ sale }}</li>
                    {% endfor %}
                </ul>
            </div>
        </div>

        <div class=\"card\">
            <div class=\"card-body\">
                <form method=\"POST\" action=\"/add_extra_earning\">
                    <div class=\"mb-3\">
                        <label for=\"extra_earning\" class=\"form-label\">Enter Extra Earnings (CAD):</label>
                        <input type=\"number\" name=\"extra_earning\" id=\"extra_earning\" class=\"form-control\" step=\"0.01\" required>
                    </div>
                    <button type=\"submit\" class=\"btn btn-primary w-100\">Add Extra Earning</button>
                </form>
            </div>
        </div>

        <div class=\"card\">
            <div class=\"card-body\">
                <h2 class=\"total-display\">Total Extra Earnings: {{ total_extra | round(2) }} CAD</h2>
                <h3 class=\"h5 mt-3\">Extra Earnings History:</h3>
                <ul class=\"list-group\">
                    {% for extra in extra_earnings_history %}
                        <li class=\"list-group-item\">{{ extra }}</li>
                    {% endfor %}
                </ul>
            </div>
        </div>

        <div class=\"d-flex justify-content-between\">
            <form method=\"POST\" action=\"/undo_last\">
                <button type=\"submit\" class=\"btn btn-warning\">Undo Last Entry</button>
            </form>
            <form method=\"POST\" action=\"/reset_total\">
                <button type=\"submit\" class=\"btn btn-danger\">Clear All Entries</button>
            </form>
        </div>
    </div>

    <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js\"></script>
</body>
</html>
"""

# Route to handle the main page
@app.route("/", methods=["GET"])
def commission_tracker():
    global total_commission, total_extra_earnings, sales_history, extra_earnings_history
    return render_template_string(
        html_template, commission_grid=commission_grid, total=total_commission + total_extra_earnings, total_extra=total_extra_earnings, sales_history=sales_history, extra_earnings_history=extra_earnings_history
    )

# Route to handle adding a sale
@app.route("/add_sale", methods=["POST"])
def add_sale():
    global total_commission, sales_history
    sale_type = request.form["sale_type"]
    sale_amount = float(request.form["sale_amount"])

    if sale_type == "Accessories":
        earned = sale_amount * 0.09
    elif sale_type == "SPC":
        earned = sale_amount * 0.30
    elif sale_type in commission_grid["Residential Services"]:
        earned = commission_grid["Residential Services"][sale_type]
    elif sale_type in commission_grid["Extra Services"]:
        earned = commission_grid["Extra Services"][sale_type]
    else:
        for category, items in commission_grid.items():
            if sale_type in items:
                earned = sale_amount * items[sale_type]
                break

    total_commission += earned
    sales_history.append(f"{sale_type} - ${sale_amount:.2f} - Commission Earned: ${earned:.2f}")

    return redirect(url_for("commission_tracker"))

# Route to handle adding extra earnings
@app.route("/add_extra_earning", methods=["POST"])
def add_extra_earning():
    global total_extra_earnings, extra_earnings_history
    extra_earning = float(request.form["extra_earning"])
    total_extra_earnings += extra_earning
    extra_earnings_history.append(f"Extra Earning - ${extra_earning:.2f}")
    return redirect(url_for("commission_tracker"))

# Route to handle undoing the last sale
@app.route("/undo_last", methods=["POST"])
def undo_last():
    global total_commission, sales_history
    if sales_history:
        last_entry = sales_history.pop()
        earned = float(last_entry.split("Commission Earned: $")[-1])
        total_commission -= earned
    return redirect(url_for("commission_tracker"))

# Route to handle resetting the total
@app.route("/reset_total", methods=["POST"])
def reset_total():
    global total_commission, total_extra_earnings, sales_history, extra_earnings_history
    total_commission = 0
    total_extra_earnings = 0
    sales_history = []
    extra_earnings_history = []
    return redirect(url_for("commission_tracker"))
