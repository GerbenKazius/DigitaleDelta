from flask import Flask, jsonify, request
from database import get_session
from models import Reference, Result, Observation

app = Flask(__name__)

@app.route("/references", methods=["GET"])
def get_references():
    session = get_session()
    references = session.query(Reference).all()
    return jsonify([r.to_dict() for r in references])

@app.route("/results", methods=["GET"])
def get_results():
    session = get_session()
    results = session.query(Result).all()
    return jsonify([r.to_dict() for r in results])

@app.route("/observations", methods=["GET"])
def get_observations():
    session = get_session()
    observations = session.query(Observation).all()
    return jsonify([o.to_dict() for o in observations])
