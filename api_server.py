from flask import Flask, request, jsonify
import hashlib
import uuid

app = Flask(__name__)

# Simulate facility storage
FACILITIES = {}

# GET Facility by phone - generates unique facility if new
@app.route("/facility", methods=["GET"])
def get_facility():
    phone = request.args.get("phone")
    if not phone:
        return jsonify({"error": "Phone number required"}), 400

    if phone not in FACILITIES:
        # Generate unique Facility ID based on phone
        facility_id = "FAC" + hashlib.sha256(phone.encode()).hexdigest()[:8].upper()
        FACILITIES[phone] = {
            "facility_id": facility_id,
            "name": f"Facility for {phone}"
        }

    return jsonify(FACILITIES[phone])

# POST new Shift
@app.route("/shifts", methods=["POST"])
def post_shift():
    data = request.json
    required_fields = ["facility_id", "date", "time"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    shift_id = "SHIFT" + str(uuid.uuid4())[:8].upper()

    return jsonify({
        "success": True,
        "shift_id": shift_id,
        "message": "Shift created successfully"
    })


