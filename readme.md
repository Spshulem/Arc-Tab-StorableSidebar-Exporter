StorableSidebar to CSV Conversion Tool for Arc Browser

Trying to get your tabs out of Arc browser? Search no more!

You can use this on the "StorableSidebar.json" files under "Application Support -> Arc -> StorableSidebar.xxx-xx-xx-xx-xx-xx-xxx.json" 

This tool reads a structured JSON file—like the one extracted from a sidebar configuration—and converts specific “item” entries into a CSV format. It includes logic to convert Apple Core Foundation timestamps into a human-readable date/time format.

Prerequisites
	•	Python 3.6 or above
	•	A JSON file containing the data you want to convert

Installation
	1.	Ensure you have Python 3.6+ installed.
	2.	(Optional) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows


	3.	No additional Python packages are required since this uses only the standard library.

Usage
	1.	Place your input JSON file (e.g. StorableSidebar.json) in the same directory as the Python script.
	2.	Update the json_file_path and output_csv_path variables in the script if needed, or leave them as defaults:

json_file_path = 'input.json' <- add file path here
output_csv_path = 'output.csv'


	3.	Run the Python script:

python convert.py


	4.	Once the script finishes, you will find the output CSV file (output.csv by default) in the same directory.

What It Does
	•	The script navigates through the JSON structure, specifically looking at sidebar.containers[].items[] objects.
	•	Each item that has an id field is treated as a row in the CSV.
	•	Fields extracted:
	•	id
	•	title
	•	parentID
	•	createdAt (converted from Apple Core Foundation timestamp to a human-readable UTC datetime)
	•	savedTitle
	•	savedURL
	•	savedMuteStatus

These fields are written as columns in the CSV.

Date Conversion Details

The createdAt field is assumed to be an Apple Core Foundation absolute time. This is a timestamp measured in seconds since January 1, 2001, UTC. To convert it to a standard UNIX timestamp (seconds since January 1, 1970, UTC), the script adds 978307200 seconds (the difference between the 2001 and 1970 epochs).

The resulting UNIX timestamp is then converted into a UTC datetime string using Python’s datetime module, resulting in a human-readable date/time in the format YYYY-MM-DD HH:MM:SS UTC.

If your timestamps have a different format, you may need to adjust the script accordingly.

Customization
	•	To add or remove fields, update the columns list and the extraction logic in the script.
	•	To change the date/time format, modify the strftime format string in the code (e.g., dt.strftime("%Y-%m-%d %H:%M:%S %Z")).

Example

Input JSON (partial):

{
  "sidebar": {
    "containers": [
      {
        "items": [
          {
            "id": "23789828-F49A-44AC-BD16-D3D61120CEF8",
            "title": null,
            "createdAt": 679034564.62281895,
            "parentID": "7C95EB81-9705-433C-A0F6-2CCFDD641F19",
            "data": {
              "tab": {
                "savedTitle": "Slack",
                "savedURL": "https://slack.com",
                "savedMuteStatus": "allowAudio"
              }
            }
          }
        ]
      }
    ]
  }
}

Output CSV (partial):

id,title,parentID,createdAt,savedTitle,savedURL,savedMuteStatus
23789828-F49A-44AC-BD16-D3D61120CEF8,,7C95EB81-9705-433C-A0F6-2CCFDD641F19,2024-04-11 12:34:56 UTC,Slack,https://slack.com,allowAudio

(The exact date/time will vary based on the timestamp and your system’s settings.)