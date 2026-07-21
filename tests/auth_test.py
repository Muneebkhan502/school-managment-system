def test_login_success(client,registered_user):
    #step1 login
    response = client.post("/auth/login", data={"username":registered_user["username"],"password":registered_user["password"]})
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

def test_login_failure(client, registered_user):
    response = client.post("/auth/login", data={"username":registered_user["username"],"password":"wrongpassword"})
    assert response.status_code == 401

def test_register_success(client):
    response = client.post("/users/", json = {
                                               "username": "Muneeb Khan",
                                               "email": "muno@example.com",
                                               "role": "admin",
                                               "password": "admin1234"
                                             })
    print(response.json)
    assert response.status_code == 201
    
# User with same username or email
def test_duplicate_user(client, registered_user):
    response = client.post("/users/", json = {
                                               "username": "testuser",
                                               "email": "testuser@example.com",
                                               "role": "admin",
                                               "password": "testpassword"
                                             })
    print(f"Registered User: {registered_user}")
    print(f"New User: {response.json}")
    assert response.status_code == 403

def test_invalid_token(client, registered_user):
    response = client.post("/auth/login", data={"username":registered_user["username"],"password":registered_user["password"]})
    headers = {"Authorization": f"Bearer {"wrong token"}"}
    response = client.get("/students/", headers=headers)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 401