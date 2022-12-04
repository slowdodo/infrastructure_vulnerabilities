import json
import mysql.connector
import requests
import sys

# Set the API endpoint and your API key
ip = sys.argv[1]
api_key = sys.argv[2]
#ip = "1.1.1.1"
url = "https://api.criminalip.io/v1/ip/summary?ip={ip}".format(ip=ip)


# Send the API request
payload = {}
headers = {
    "x-api-key": api_key
}

response = requests.request("GET", url, headers=headers, data=payload)

# Parse the JSON response
data = json.loads(response.text)

# Connect to the MySQL database
cnx = mysql.connector.connect(
    user="user",
    password="1234",
    host="10.40.1.2",
    port=3306,
    database="customer",
    auth_plugin="mysql_native_password"
)

# Construct the INSERT statement
sql = """
INSERT INTO ip_data (
    ip,
    inbound,
    outbound,
    country,
    country_code,
    isp,
    status
) VALUES (
    %(ip)s,
    %(inbound)s,
    %(outbound)s,
    %(country)s,
    %(country_code)s,
    %(isp)s,
    %(status)s
)
"""

# Define the data to be inserted
insert_data = {
    "ip": data["ip"],
    "inbound": data["score"]["inbound"],
    "outbound": data["score"]["outbound"],
    "country": data["country"],
    "country_code": data["country_code"],
    "isp": data["isp"],
    "status": data["status"]
}

# Execute the INSERT statement
cursor = cnx.cursor()
cursor.execute(sql, insert_data)
cnx.commit()
