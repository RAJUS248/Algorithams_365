import urllib.request
import json

"""
- This function returns the delivery status of the Post Offices of that pincode
if Delivery Status is:
Delivery - post office handles delivering letters/parcels in its area.

Non-Delivery - it exists for administrative purposes (like sorting, forwarding, or handling customer services) 
but doesn't directly deliver the mail.

"""
def check_delivery_status(pincode):
    
    try:
        # if length of PIN code is not equal to six digit
        if len(str(pincode)) != 6:
            raise ValueError("Invalid PIN code")
        
        # Postal Free API
        url = f"https://api.postalpincode.in/pincode/{pincode}"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        # returns a list of post offices and each value is stored in from of dictionary
        # using .get() because the data is dictionary by.get("key") returns data or None
        post_offices = data[0].get("PostOffice")

        # handle if the post_offices has data or not
        if not post_offices:
            print("No Post-office found for the given PIN code")
            return

        # running a loop to extract only post_office name and delivery status from post_offices
        for office in post_offices:
            print(office["Name"], "-", office["DeliveryStatus"])

    except ValueError as e:
        print("Error : ", e)
    
check_delivery_status(560001)

"""
Range of PIN Codes of Bengaluru : 560001 to 562161
"""