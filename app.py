#import flas module
from flask import Flask, jsonify
import json
app = Flask(__name__)
@app.route('/')
def my_info():
    about = {
        'name': 'Roseline DANGAZELA',
        'github': 'https://github.com/LynneDC',
       'Gender': 'Female',
    }
    return jsonify(about)


if __name__ == '__main__':

    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    