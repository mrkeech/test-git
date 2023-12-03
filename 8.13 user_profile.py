def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('matthew', 'keech',
                             location='port st lucie',
                             field='programming')
print(user_profile)
