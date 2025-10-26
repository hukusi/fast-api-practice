import requests

# res = requests.get("http://127.0.0.1:8000")
# res = requests.get("http://127.0.0.1:8000/sample")

# print(res.status_code)
# print(res.text)
# print(res.url)

# res = requests.get("http://127.0.0.1:8000/items/111")

# print(res.status_code)
# print(res.text)
# print(res.url)

# res = requests.get("http://127.0.0.1:8000/items/111/detail")

# print(res.status_code)
# print(res.text)
# print(res.url)


# res = requests.get("http://127.0.0.1:8000/items/sample")

# print(res.status_code)
# print(res.text)
# print(res.url)

# res = requests.get("http://127.0.0.1:8000/items/?skip=1&limit=2")

# print(res.status_code)
# print(res.text)
# print(res.url)

# res = requests.post("http://127.0.0.1:8000/items/", json={"name": "Tシャツ", "price": 2000, "description": "白Tシャツ"})

# print(res.status_code)
# print(res.text)
# print(res.url)

res = requests.get("http://127.0.0.1:8000/sample/", headers={"Authorization": "Bearer A1B2C3D4"})

print(res.status_code)
print(res.text)
print(res.headers)