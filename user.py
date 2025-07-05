
users = {}

def add_user(name, email, password):
    """Add a user to the users dict."""
    users[email] = {'name': name, 'password': password}
