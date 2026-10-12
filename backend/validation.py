SEVERITIES = {"LOW", "MEDIUM", "HIGH"}

def validate_incident(data):
    title = str(data.get("title", "")).strip()
    severity = data.get("severity")
    if not title:
        raise ValueError("title required")
    if severity not in SEVERITIES:
        raise ValueError("bad severity")
    return {"title": title, "severity": severity}
