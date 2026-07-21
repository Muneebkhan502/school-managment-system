def test_get_student(client, registered_user):
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
    response = client.post("/students/",  headers=headers ,json = { 
                                                "first_name": "qasim",
                                                "last_name": "ali",
                                                "class_id": 1,
                                                "email": "qasim@example.com",
                                                "rollno": 101,
                                                "marks": 100,
                                                "contact_number": "123456789"
                                                })
    
    print(response.status_code)
    print(response.json())
    response = client.get("/students/", headers=headers)
    print(response.json())
    assert response.status_code == 200

def test_get_student_id(client, registered_user):
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
    response = client.post("/students/",  headers=headers ,json = { 
                                                "first_name": "qasim",
                                                "last_name": "ali",
                                                "class_id": 1,
                                                "email": "qasim@example.com",
                                                "rollno": 101,
                                                "marks": 100,
                                                "contact_number": "123456789"
                                                })
    
    print(response.status_code)
    print(response.json())
    std_id = response.json()["id"]
    print(std_id)
    response = client.get(f"/students/{std_id}", headers=headers)
    assert response.status_code == 200
    print(response.json())

def test_add_student(client,registered_user):
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
    response = client.post("/students/",  headers=headers ,json = { 
                                                "first_name": "qasim",
                                                "last_name": "ali",
                                                "class_id": 1,
                                                "email": "qasim@example.com",
                                                "rollno": 101,
                                                "marks": 100,
                                                "contact_number": "123456789"
                                                })
    
    print(response.status_code)
    print(response.json())
    assert response.status_code == 201

def test_update_student(client,registered_user):
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
    response = client.post("/students/",  headers=headers ,json = { 
                                                "first_name": "qasim",
                                                "last_name": "ali",
                                                "class_id": 1,
                                                "email": "qasim@example.com",
                                                "rollno": 101,
                                                "marks": 100,
                                                "contact_number": "123456789"
                                                })
    std_id = response.json()["id"]
    print(f"STUDENT ID: {std_id}")
    print(response.json())
    response = client.patch(f"/students/{std_id}", json = {
                                                    "first_name": "muneeb"
                                                    }, headers = headers)
    print(response.json)
    print(response.status_code)
    assert response.status_code == 200
    print(response.json())


def test_delete_student(client,registered_user):
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
    response = client.post("/students/",  headers=headers ,json = { 
                                                "first_name": "qasim",
                                                "last_name": "ali",
                                                "class_id": 1,
                                                "email": "qasim@example.com",
                                                "rollno": 101,
                                                "marks": 100,
                                                "contact_number": "123456789"
                                                })
    std_id = response.json()["id"]
    print(f"STUDENT ID: {std_id}")
    print(response.json())
    response = client.delete(f"/students/{std_id}", headers = headers)
    print(response.json)
    print(response.status_code)
    assert response.status_code == 204

def test_duplicate_student(client, registered_user):
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
    response = client.post("/students/",  headers=headers ,json = { 
                                                "first_name": "qasim",
                                                "last_name": "ali",
                                                "class_id": 1,
                                                "email": "qasim@example.com",
                                                "rollno": 101,
                                                "marks": 100,
                                                "contact_number": "123456789"
                                                })
    std_id = response.json()["id"]
    print(f"STUDENT ID: {std_id}")
    # Add anther student with same roll no
    response = client.post("/students/",  headers=headers ,json = { 
                                                "first_name": "sara",
                                                "last_name": "khan",
                                                "class_id": 1,
                                                "email": "sara@example.com",
                                                "rollno": 101,
                                                "marks": 87,
                                                "contact_number": "987654321"
                                                })
    print(response.json())
    print(response.status_code)
    assert response.status_code == 403