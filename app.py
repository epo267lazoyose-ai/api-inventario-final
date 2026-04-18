from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

devices = []
current_id = 1

def validar_device(data):
    campos = ["nombre", "tipo", "estado", "area"]
    for campo in campos:
        if campo not in data or not data[campo]:
            return False
    return True

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(devices), 200

@app.route('/devices/<int:id>', methods=['GET'])
def get_device(id):
    for device in devices:
        if device["id"] == id:
            return jsonify(device), 200
    return jsonify({"error": "No encontrado"}), 404

@app.route('/devices', methods=['POST'])
def create_device():
    global current_id
    data = request.get_json()

    if not validar_device(data):
        return jsonify({"error": "Datos incompletos"}), 400

    new_device = {
        "id": current_id,
        "nombre": data["nombre"],
        "tipo": data["tipo"],
        "estado": data["estado"],
        "area": data["area"],
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    devices.append(new_device)
    current_id += 1

    return jsonify(new_device), 201

@app.route('/devices/<int:id>', methods=['PUT'])
def update_device(id):
    data = request.get_json()

    if not validar_device(data):
        return jsonify({"error": "Datos incompletos"}), 400

    for device in devices:
        if device["id"] == id:
            device.update(data)
            return jsonify(device), 200

    return jsonify({"error": "No encontrado"}), 404

@app.route('/devices/<int:id>', methods=['DELETE'])
def delete_device(id):
    for device in devices:
        if device["id"] == id:
            devices.remove(device)
            return jsonify({"mensaje": "Eliminado"}), 200

    return jsonify({"error": "No encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)