import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# 1. GET request
print("🔹 GET Example")
response = requests.get(BASE_URL + "/1")
print(response.status_code, response.json())

# 2. POST request
print("\n🔹 POST Example")
new_post = {"title": "Hello", "body": "This is a test", "userId": 1}
response = requests.post(BASE_URL, json=new_post)
print(response.status_code, response.json())


# 3. PUT request (replace resource)
print("\n🔹 PUT Example")
update_post = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
response = requests.put(BASE_URL + "/1", json=update_post)
print(response.status_code, response.json())


# 4. PATCH request (partial update)
print("\n🔹 PATCH Example")
patch_post = {"title": "Partially Updated"}
response = requests.patch(BASE_URL + "/1", json=patch_post)
print(response.status_code, response.json())

# 5. DELETE request
print("\n🔹 DELETE Example")
response = requests.delete(BASE_URL + "/1")
print(response.status_code)

# 6. HEAD request (headers only)
print("\n🔹 HEAD Example")
response = requests.head(BASE_URL + "/1")
print(response.status_code, response.headers)

# 7. OPTIONS request (allowed methods)
print("\n🔹 OPTIONS Example")
response = requests.options(BASE_URL + "/1")
print(response.status_code, response.headers.get("Allow"))

# 8. Generic request()
print("\n🔹 Generic request() Example")
response = requests.request("GET", BASE_URL)
print(response.status_code, response.json()[:2])  # show first 2 posts
