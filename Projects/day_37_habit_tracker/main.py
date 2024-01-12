import requests
from _datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "avazkhon124"
TOKEN = "dfhwhevo12aeribvoe"
ID = "graph1"
date_to_change = datetime(year=2024, month=1, day=11)
DATE = int(date_to_change.strftime("%Y%m%d"))

user_params = {
    "token": "dfhwhevo12aeribvoe",
    "username": "avazkhon124",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "How many pages i read",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


today = datetime.now()
post_endpoint = f"{graph_endpoint}/{ID}"
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages of a book have you read today?\n>>"),
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)

pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"
pixel_update_config = {
    "quantity": "5"
}

# response = requests.put(url=pixel_update, json=pixel_update_config, headers=headers)
# response.raise_for_status()
# print(response.text)

pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"

# response = requests.delete(url=pixel_delete, headers=headers)
# print(response.text)

































