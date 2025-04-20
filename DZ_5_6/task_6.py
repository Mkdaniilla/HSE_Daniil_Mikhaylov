
import json

def parse_ics_to_json(ics_path, output_path):
    events = []
    current_event = {}
    inside_event = False

    with open(ics_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line == "BEGIN:VEVENT":
                inside_event = True
                current_event = {}
                continue

            if line == "END:VEVENT":
                inside_event = False
                if current_event.get("DTSTART", "").startswith("00010101"):
                    continue

                event_data = {
                    "start": current_event.get("DTSTART"),
                    "end": current_event.get("DTEND"),
                    "description": current_event.get("DESCRIPTION", ""),
                    "location": current_event.get("LOCATION", ""),
                    "case_number": ""
                }

                for line_desc in event_data["description"].splitlines():
                    if "дело" in line_desc.lower():
                        event_data["case_number"] = line_desc.strip()
                        break

                events.append(event_data)

            if inside_event and ":" in line:
                key, value = line.split(":", 1)
                current_event[key] = value

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    parse_ics_to_json("efrsb_calendar.ics", "court_dates.json")


