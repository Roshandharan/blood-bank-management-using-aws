from flask import Blueprint, jsonify, request
from backend.models import Donor, db

bp = Blueprint('donors', __name__, url_prefix='/donors')

@bp.route('/')
def get_donors():
    donors = Donor.query.all()
    return jsonify([{"id": d.id, "name": d.name, "blood_type": d.blood_type} for d in donors])

@bp.route('/add', methods=['POST'])
def add_donor():
    data = request.json
    new_donor = Donor(name=data['name'], blood_type=data['blood_type'])
    db.session.add(new_donor)
    db.session.commit()
    return jsonify({"message": "Donor added successfully"})
