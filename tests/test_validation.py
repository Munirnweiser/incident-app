import pytest
from backend.validation import validate_incident

def test_valid_incident_is_cleaned():
    result = validate_incident({"title": "  Feed down ", "severity": "HIGH"})
    assert result == {"title": "Feed down", "severity": "HIGH"}

def test_empty_title_is_rejected():
    with pytest.raises(ValueError):
        validate_incident({"title": "   ", "severity": "LOW"})

def test_unknown_severity_is_rejected():
    with pytest.raises(ValueError):
        validate_incident({"title": "Feed down", "severity": "URGENT"})
