def login(session, url, username, password):
    return session.post(url, data={'username': username, 'password': password})
