# Final Project for CS50P

# Project Name: Rich Or Not?

#### Video Demo: <->

#### Description:

From a Singapore Financial Firm providing Insurance brokerage services, it could be potentially useful to determine the potential affluence or net-worth of a prospective client. We intend to do this purely with their residential data , as this is meant as a gauge and not as an actual indicator of their wealth.

Context:
Housing is mainly in Housing Development Boards (HDB), which is a form of public housing. All other types of housing is considered private housing (e.g. Condominium, Landed, Bunaglows, etc).

Although in reality, HDB properties also differ greatly from area to area, with some prime area properties being significantly more expensive than other areas. However, for simplicity, for the purposes of this project - we will be simply attemptiny to identify and classify purely based on public vs private housing.

Proposed Method:
Make use of OneMaps API - national map of Singapore Land Authority (SLA).

## API(s) used:

1. https://www.onemap.gov.sg/api/common/elastic/search?searchVal={postal_code}&returnGeom=N&getAddrDetails=Y - OneMap API

## Raw Data Output from OneMap API:

{'found': 1, 'totalNumPages': 1, 'pageNum': 1, 'results': [{'SEARCHVAL': 'PARC OLYMPIA', 'BLK_NO': '62', 'ROAD_NAME': 'FLORA DRIVE', 'BUILDING': 'PARC OLYMPIA', 'ADDRESS': '62 FLORA DRIVE PARC OLYMPIA SINGAPORE 506859', 'POSTAL': '506859'}]}

- Dictonary
- Found : Important for further down filtering , for found > 1
- Results : Most Important - Key data all lies here.

## Test Cases of some postal codes:

1. "506859" - Parc Olympia, Condominium
   Results:
   {'SEARCHVAL': 'PARC OLYMPIA', 'BLK_NO': '62', 'ROAD_NAME': 'FLORA DRIVE', 'BUILDING': 'PARC OLYMPIA', 'ADDRESS': '62 FLORA DRIVE PARC OLYMPIA SINGAPORE 506859', 'POSTAL': '506859'}

Present: Blk_No, Building

2. "467360" - Bedok Mall, Shopping Mall
   Results:
   {'SEARCHVAL': 'BEDOK INTEGRATED TRANSPORT HUB', 'BLK_NO': '311', 'ROAD_NAME': 'NEW UPPER CHANGI ROAD', 'BUILDING': 'BEDOK INTEGRATED TRANSPORT HUB', 'ADDRESS': '311 NEW UPPER CHANGI ROAD BEDOK INTEGRATED TRANSPORT HUB SINGAPORE 467360', 'POSTAL': '467360'}

Present: Blk_No, Building

3. "409575" - Richfield Industrial Centre
   Results:
   {'SEARCHVAL': 'RICHFIELD INDUSTRIAL CENTRE', 'BLK_NO': '122', 'ROAD_NAME': 'EUNOS AVENUE 7', 'BUILDING': 'RICHFIELD INDUSTRIAL CENTRE', 'ADDRESS': '122 EUNOS AVENUE 7 RICHFIELD INDUSTRIAL CENTRE SINGAPORE 409575', 'POSTAL': '409575'}

Present: Blk_No, Building

4. "398577" - 53 Lor 24A Geylang
   Results: {'SEARCHVAL': '53 LORONG 24A GEYLANG SINGAPORE 398577', 'BLK_NO': '53', 'ROAD_NAME': 'LORONG 24A GEYLANG', 'BUILDING': 'NIL', 'ADDRESS': '53 LORONG 24A GEYLANG SINGAPORE 398577', 'POSTAL': '398577'}

Present: Blk_No
Not Present: Building

5. "397691" - Singapore Indoor Stadium:
   Results: {'SEARCHVAL': 'SINGAPORE INDOOR STADIUM', 'BLK_NO': '2', 'ROAD_NAME': 'STADIUM WALK', 'BUILDING': 'SINGAPORE INDOOR STADIUM', 'ADDRESS': '2 STADIUM WALK SINGAPORE INDOOR STADIUM SINGAPORE 397691', 'POSTAL': '397691'}

Present: Building
Not Present: Blk_No

6. "269943" - 20 Astrid Hill - Good Class Bungalow Area:
   Results: {"SEARCHVAL": "20 ASTRID HILL SINGAPORE 269943", "BLK_NO": "20", "ROAD_NAME": "ASTRID HILL", "ADDRESS": "20 ASTRID HILL SINGAPORE 269943", "POSTAL": "269943"}

Present: Blk_No
Not Present: Building

## Preliminary Observations:

1. HDB has no building name(s).
2. Condominiums has a building name.
3. Office addresses has multiple building name(s).

## Limitations:

1. Lack of differentiation between landed property and HDB currently as both sets of results share similar structure when queried from OneMap API.

## Future Work and Development:

1. Address limitation #1 - have some better way to differentiate between clients staying in HDB vs in Landed property, as affluence could be significantly different.
2. A possible rudimentary way - to hardcode all of the landed property areas in Singapore and have a logic check against this hard-coded list.
3. Limitation of above solution - may not be future-proof.
