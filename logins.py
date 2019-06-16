def webapp_add_wsgi_middleware(app):
    from engineauth import middleware
    return middleware.AuthMiddleware(app)

engineauth = {
    'secret_key': 'CHANGE_TO_A_SECRET_KEY',
    'user_model': 'engineauth.models.User',
}

engineauth['provider.auth'] = {
    'user_model': 'engineauth.models.User',
    'session_backend': 'datastore',
}

# Facebook Authentication
engineauth['provider.facebook'] = {
    'client_id': '355347148510213',
    'client_secret': 'ba6b77d05b02e771804bfc6444105b90',
    'scope': 'email',
}

# # Google Plus Authentication
# engineauth['provider.google'] = {
#     'client_id': 'CHANGE_TO_GOOGLE_CLIENT_ID',
#     'client_secret': 'CHANGE_TO_GOOGLE_CLIENT_SECRET',
#     'api_key': 'CHANGE_TO_GOOGLE_API_KEY',
#     'scope': 'https://www.googleapis.com/auth/plus.me',
# }

# # Twitter Authentication
# engineauth['provider.twitter'] = {
#     'client_id': 'CHAGNE_TO_TWITTER_CONSUMER_KEY',
#     'client_secret': 'CHAGNE_TO_TWITTER_CONSUMER_SECRET',
# }

# LinkenIn Authentication
engineauth['provider.linkedin'] = {
    'client_id': '78zpejtkcky4xq',
    'client_secret': 'kFrNIfSxsqe9DKW3',
}