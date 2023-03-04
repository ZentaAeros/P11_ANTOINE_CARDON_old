from server import app

client = app.test_client()

def test_login_page():
    response = client.get('/')
    assert response.status_code == 200
    
def test_login_with_valid_mail():
    email = 'john@simplylift.co'
    response = client.post('/showSummary', data={'email':email})
    assert response.status_code == 200

def test_login_with_bad_mail():
    email = 'thismaildoesnotexist@gudlft.co'
    response = client.post('/showSummary', data={'email':email})
    assert response.status_code == 401

def test_login_with_empty_mail():
    email = ""
    response = client.post('/showSummary', data={'email':email})
    assert response.status_code == 401
