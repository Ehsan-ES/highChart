from flask import Flask, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route('/home')
def project():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    payload = {}
    headers = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        if response.status_code != 200:
            return({"status": f"{response.status_code}" , "error": "PROBLEM IS EXISTS!!!}"})
        # print(jsonify(response.json()))
        return jsonify(response.json())

    except requests.exceptions.HTTPError as req_err:
        return ({"error": f"PROBLEM EXISTS {req_err}"})
    except requests.exceptions.RequestException as e:
        return ({"error": f"PROBLEM EXISTS {e}"})
   
if __name__ == '__main__':
    app.run(debug=True)
