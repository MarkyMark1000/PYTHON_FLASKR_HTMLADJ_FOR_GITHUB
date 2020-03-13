from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


# Test that the /hello path gives the string 'Hello World!'
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
