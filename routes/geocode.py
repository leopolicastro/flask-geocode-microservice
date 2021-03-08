from flask import Blueprint, jsonify, request
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")

geocode = Blueprint("geocode", __name__)


@geocode.route("/geocode/", methods=["POST"])
def geo():
    result = json.loads(request.data.decode("utf-8"))
    address = result["address"]
    location = geolocator.geocode(f"{address}")
    return {
        "latitude": location.latitude,
        "longitude": location.longitude,
    }
