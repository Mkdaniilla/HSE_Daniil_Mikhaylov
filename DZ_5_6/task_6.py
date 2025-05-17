import json
from datetime import datetime

def parse_ics_to_json(ics_path, output_path):
    events = []
    with open(ics_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    current_event = {}
    for line in lines:
        if line == "BEGIN:VEVENT":
            current_event = {}
        elif line.startswith("DTSTART"):
            current_event["start_raw"] = line.split(":", 1)[1]
        elif line.startswith("DTEND"):
            current_event["end_raw"] = line.split(":", 1)[1]
        elif line.startswith("DESCRIPTION"):
            current_event["description"] = line.split(":", 1)[1]
        elif line.startswith("LOCATION"):
            current_event["location"] = line.split(":", 1)[1]
        elif line == "END:VEVENT":

            if current_event.get("start_raw", "").startswith("00010101"):
                continue


            start = current_event.get("start_raw", "")
            end = current_event.get("end_raw", "")
            start_iso = parse_dt(start)
            end_iso = parse_dt(end)

            event_data = {
                "start": start_iso,
                "end": end_iso,
                "description": current_event.get("description", ""),
                "location": current_event.get("location", ""),
                "case_number": extract_case_number(current_event.get("description", ""))
            }

            events.append(event_data)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

def parse_dt(dt_str):
    try:
        return datetime.strptime(dt_str, "%Y%m%dT%H%M%S").isoformat()
    except Exception:
        return ""

def extract_case_number(desc):
    for line in desc.splitlines():
        if "дело" in line.lower():
            return line.strip()
    return ""

if __name__ == "__main__":
    parse_ics_to_json("efrsb_calendar.ics", "court_dates.json")

