from flask import Flask, render_template

app = Flask(__name__)

PHONE_DISPLAY = "+91 98142 43611"
PHONE_LINK = "+9198142 43611"
WHATSAPP_LINK = "https://wa.me/919814243611?text=Hi%20Gurlal%20Singh%2C%20I%20want%20to%20book%20a%20car."

CARS = [
    {
        "name": "Innova Crysta",
        "image": "innova.jpg",

        "services": [
            {
                "title": "Majha Punjab ↔ Delhi Round Trip",
                "price": "₹15,000"
            },

            {
                "title": "One Way",
                "price": "₹10,000"
            },

            {
                "title": "Himachal Tour",
                "price": "₹5,000/day"
            },
        ],
    },

    {
        "name": "Kia Carens",
        "image": "Kia.jpg",

        "services": [
            {
                "title": "Round Trip",
                "price": "₹13,000"
            },

            {
                "title": "One Way",
                "price": "₹9,000"
            },
        ],
    },

    {
        "name": "Scorpio",
        "image": "scorpio.jpg",

        "services": [
            {
                "title": "Self Drive",
                "price": "₹2,500/day"
            },

            {
                "title": "Monthly Rental",
                "price": "₹2,000/day"
            },
        ],
    },

    {
        "name": "Fortuner",
        "image": "fortuner.jpg",

        "services": [
            {
                "title": "Self Drive",
                "price": "₹5,000/day"
            },
        ],
    },

    {
        "name": "Wedding Fortuner",
        "image": "fortuner-wedding.jpg",

        "services": [
            {
                "title": "Local Doli",
                "price": "₹9,000"
            },

            {
                "title": "Outside Doli",
                "price": "₹13,000"
            },
        ],
    },

    {
        "name": "Sedan",
        "image": "Sedan.jpg",

        "services": [
            {
                "title": "Round Trip",
                "price": "₹10,000"
            },

            {
                "title": "One Way",
                "price": "₹7,000"
            },
        ],
    },
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        cars=CARS,
        phone_display=PHONE_DISPLAY,
        phone_link=PHONE_LINK,
        whatsapp_link=WHATSAPP_LINK,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
