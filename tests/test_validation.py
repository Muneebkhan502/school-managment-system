# We will pass here wrong data to endpoint to see is pydantic schema working as expacted
# for example we will add new student but with wrong data formate
def test_invalid_std_data(client, registered_user):
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
                                                # last name was required but we did not passed
                                                "class_id": "one", #class-id is expacted as a int but will passes as a str
                                                "email": "qasimexample.com",
                                                "rollno": 101,
                                                "marks": -40, # should be greater than 0
                                                "contact_number": "123456789"
                                                })
    
    print(response.status_code)
    print(response.json())
    assert response.status_code == 422