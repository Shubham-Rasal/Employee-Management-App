import requests
url = "https://fdeployserver.up.railway.app"

# Request at /challenge
r = requests.get(url + "/challenge")
print(r.json())

num1 = r.json()["num1"]
num2 = r.json()["num2"]
token = r.json()["token"]

#Post token and sum to /deploy
r = requests.post(url + "/deploy", json={"token": token, "answer": num1 + num2})
if r.status_code == 400:
    print("Wrong answer")

# Print the response
if r.text == "OK":
    print("Deployed successfully")
else:
    print("Deploy failed")