from flask import Blueprint, jsonify, request
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")

geocode = Blueprint("geocode", __name__)


@geocode.route("/geocode/", methods=["POST"])
def geo():
    result = json.loads(request.data.decode("utf-8"))
    try:
        street_address = result["street_address"]
        city = result["city"]
        state = result["state"]
        zip_code = result["zip_code"]
    except:
        return "invalid address"
    location = geolocator.geocode(f"{street_address}, {city}, {state}, {zip_code}")
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
        return "latitude and longitude not provided"
    location = geolocator.reverse(f"{latitude}, {longitude}")
    return location.raw
