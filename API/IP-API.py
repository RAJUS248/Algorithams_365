import urllib.request
import json

"""
The below function prints Country, Region, Zip code, Latitude and Longitude based on the given IP address
some example of popular IP address:
| IP Address       | ISP / Org        | Country       | Region / City              | Zip Code | Latitude | Longitude |
| ---------------- | ---------------- | ------------- | -------------------------- | -------- | -------- | --------- |
| `8.8.8.8`        | Google LLC       | United States | California / Mountain View | 94035    | 37.386   | -122.0838 |
| `1.1.1.1`        | Cloudflare, Inc  | Australia     | Brisbane / Queensland      | 4000     | -27.4679 | 153.0278  |
| `208.67.222.222` | OpenDNS (Cisco)  | United States | California / San Jose      | 95134    | 37.387   | -121.887  |
| `9.9.9.9`        | Quad9 Foundation | United States | New York                   | 10001    | 40.7128  | -74.0060  |
| `4.2.2.2`        | Level 3 / Lumen  | United States | Colorado                   | 80124    | 39.55    | -104.87   |

"""
def info_from_IP(IP_address):

    # IP API whuch return info based on the IP address
    url = f"http://ip-api.com/json/{IP_address}"

    with urllib.request.urlopen(url) as response:
        info = json.loads(response.read())

    
    print("The Internet service provider of the given IP address is : ", info.get("isp"))
    print("Country name :", info.get("country"))
    print("Region name :", info.get("regionName"))
    print("Zip Code : ", info.get("zip"))
    print(f"Latitude : {info.get("lat")} and Longitude : {info.get("lon")}")
    

info_from_IP('184.168.103.43')