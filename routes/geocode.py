from flask import Blueprint, jsonify, request
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")

geocode = Blueprint("geocode", __name__)


@geocode.route("/geocode/", methods=["POST"])
def geo():
    result = json.loads(request.data.decode("utf-8"))
    try:
        address = result["address"]
    except:
        return "address attribute not found"
    location = geolocator.geocode(f"{address}")
    return {
        "latitude": location.latitude,
        "longitude": location.longitude,
    }


@geocode.route("/reverse/", methods=["POST"])
def reverse():
    result = json.loads(request.data.decode("utf-8"))
    try:
        longitude = result["longitude"]
        latitude = result["latitude"]
    except:
        return "There was an error with your request"
    location = geolocator.reverse(f"{latitude}, {longitude}")
    return location.address
