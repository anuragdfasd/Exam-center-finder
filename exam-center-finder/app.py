from flask import Flask, request, render_template

app = Flask(__name__)

centers = {
    "Baneshwor Multiple Campus, Shantinagar, Baneshwor": {
        "range": (1, 650),
        "code": 280,
        "map_url": "https://maps.app.goo.gl/zED9j2i9sKRTbohG8"
    },
    "Himalayan College, Koteshwor, Kathmandu": {
        "range": (651, 938),
        "code": 750,
        "map_url": "https://maps.app.goo.gl/Hg1iUfo3gQn7Uoan9"
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    map_url = ""

    if request.method == "POST":
        symbol_no = request.form.get("symbol_no", "").strip()

        if not symbol_no.isdigit() or len(symbol_no) != 9 or not symbol_no.startswith("500370"):
            message = "❌ Invalid Symbol Number! Must be 9 digits and start with '500370'."
        else:
            last_three_digits = int(symbol_no[-3:])
            for center, details in centers.items():
                if details["range"][0] <= last_three_digits <= details["range"][1]:
                    message = f"📌 Exam Center: {center} (Code: {details['code']})"
                    map_url = details["map_url"]
                    break
            else:
                message = "❌ Symbol number not in the valid range."

    return render_template("index.html", message=message, map_url=map_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
