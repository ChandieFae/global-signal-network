import json
import csv
from pathlib import Path

# Paths
json_path = Path("../signals/phase-1.json")
csv_path = Path("../signals/phase-2.csv")
output_path = Path("../web/output_map.html")

# Load JSON signals
with open(json_path, "r", encoding="utf-8") as f:
    signals = json.load(f)

# Load CSV signals and add them
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        signals.append({
            "name": row["name"],
            "latitude": float(row["latitude"]),
            "longitude": float(row["longitude"]),
            "timezone": row.get("timezone", ""),
            "description": row.get("description", "")
        })

# Start HTML output
html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Global Signal Map</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <style>
    body { margin: 0; padding: 0; }
    #map { height: 100vh; width: 100%; }
  </style>
</head>
<body>
  <div id="map"></div>

  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>
    const map = L.map('map').setView([20, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

"""

# Add markers
marker_script = ""
for point in signals:
    name = point["name"].replace('"', "'")
    lat = point["latitude"]
    lon = point["longitude"]
    desc = point.get("description", "").replace('"', "'")
    popup = f"<strong>{name}</strong><br>{desc}"
    marker_script += f'L.marker([{lat}, {lon}]).addTo(map).bindPopup("{popup}");\n'

# End HTML
html_end = """
  </script>
</body>
</html>
"""

# Write final file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_start + marker_script + html_end)

print(f"✅ Map generated: {output_path.resolve()}")

