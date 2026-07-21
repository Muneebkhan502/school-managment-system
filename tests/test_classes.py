def test_get_class(client, registered_user):
    # step 1: logged in to add student
    response = client.post("/auth/login", data={"username":registered_user["username"],"password":registered_user["password"]})
    print(response.json())
    # step 2: get token 
    token = response.json()["access_token"]
    # step 3: attach token in header to use for verification
    headers = {"Authorization": f"Bearer {token}"}
    # step 4: add student
    # first we have to add class 
    response = client.post("/classes/", json = {"class_name": "10th", "section": "A"})
    print(response.status_code)
    print(response.json())
    id = response.json()["id"]
    print(id)
    # Add atleast one student to get class
    response = client.post("/students/", json={
                                                "first_name": "sara",
                                                "last_name": "khan",
                                                "class_id": 1,
                                                "email": "sara@example.com",
                                                "rollno": 101,
                                                "marks": 87,
                                                "contact_number": "987654321"
                                              }, headers = headers)
    print(response.json())
    response = client.get(f"/classes/{id}")
    print(response.json())
    assert response.status_code == 200
    