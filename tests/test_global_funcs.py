from flaskr.global_funcs import get_ip

# Test the get_ip function when there is an assertion error.
# Warning - you may not get 100% coverage if you don't have a
# valid internet connection.


def test_ip():
    response = get_ip(True)
    assert response == '127.0.0.1'
