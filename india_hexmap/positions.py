"""
Grid coordinates for the India hex map.

Coordinates are in abstract (col, row) grid units — not pixels — so the
layout stays correct at any rendering size. Row increases downward.
Half-integer columns encode the row-to-row horizontal offset that makes
pointy-top hexagons interlock with no gaps (see plot.py for the geometry).
"""

POSITIONS = {
    "JK": (3.0, 0),
    "PB": (2.5, 1), "HP": (3.5, 1),
    "HR": (3.0, 2), "UT": (4.0, 2), "AR": (9.0, 2),
    "RJ": (2.5, 3), "DL": (3.5, 3), "UP": (4.5, 3), "BR": (5.5, 3),
    "SK": (6.5, 3), "AS": (7.5, 3), "NL": (8.5, 3),
    "GJ": (2.0, 4), "MP": (3.0, 4), "CT": (4.0, 4), "JH": (5.0, 4),
    "WB": (6.0, 4), "ML": (7.0, 4), "MN": (8.0, 4),
    "MH": (2.5, 5), "TG": (3.5, 5), "OR": (5.5, 5), "TR": (6.5, 5), "MZ": (7.5, 5),
    "GA": (3.0, 6), "AP": (4.0, 6),
    "KA": (3.5, 7), "AN": (6.0, 7),
    "LD": (1.0, 8), "KL": (3.0, 8), "TN": (4.0, 8),
    "CH": (6.0, 9), "DN": (7.0, 9), "DD": (8.0, 9), "PY": (9.0, 9),
}

NAMES = {
    "JK": "Jammu & Kashmir", "PB": "Punjab", "HP": "Himachal Pradesh",
    "HR": "Haryana", "UT": "Uttarakhand", "AR": "Arunachal Pradesh",
    "RJ": "Rajasthan", "DL": "Delhi", "UP": "Uttar Pradesh", "BR": "Bihar",
    "SK": "Sikkim", "AS": "Assam", "NL": "Nagaland",
    "GJ": "Gujarat", "MP": "Madhya Pradesh", "CT": "Chhattisgarh",
    "JH": "Jharkhand", "WB": "West Bengal", "ML": "Meghalaya", "MN": "Manipur",
    "MH": "Maharashtra", "TG": "Telangana", "OR": "Odisha", "TR": "Tripura", "MZ": "Mizoram",
    "GA": "Goa", "AP": "Andhra Pradesh",
    "KA": "Karnataka", "AN": "Andaman & Nicobar",
    "LD": "Lakshadweep", "KL": "Kerala", "TN": "Tamil Nadu",
    "CH": "Chandigarh", "DN": "Dadra & Nagar Haveli", "DD": "Daman & Diu", "PY": "Puducherry",
}
