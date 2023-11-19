import requests, json

dict = [
    {
        "username": "amir",
        "id": 3,
        "first_name": "امیر",
        "last_name": "شریفی",
        "unread_count": 3
    },
    {
        "username": "reza",
        "id": 5,
        "first_name": "رضا",
        "last_name": "احمدی",
        "unread_count": 4
    },
    {
        "username": "ehsan",
        "id": 4,
        "first_name": "احسان",
        "last_name": "رجبی",
        "unread_count": 0
    },
    {
        "username": "ali",
        "id": 2,
        "first_name": "علی",
        "last_name": "احمدی",
        "unread_count": 1
    }
]

resp = requests.get(
    f"http://localhost:8002/api/chat/user/1/members/"
)

if json.loads(resp.text) == dict:
    print("\n############################################")
    print("################            ################")
    print("################ Well done! ################")
    print("################            ################")
    print("############################################\n")
else:
    print(json.dumps(json.loads(resp.text), indent = 4))