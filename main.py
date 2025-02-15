from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/alert', methods=['GET'])
def get_alert():
    return jsonify({
        "alert": True,
    })

if __name__ == '__main__':
    app.run(debug=True)
