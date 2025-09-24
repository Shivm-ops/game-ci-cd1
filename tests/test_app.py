from app import app

def test_index_route():
    """Test if the main page loads correctly."""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Guess a number between 1 and 100" in response.data