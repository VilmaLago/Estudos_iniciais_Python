# Testes iniciais sobre dicionários dentro de dicionários.

users = {
    'vilmalago': {
        'first': 'vilma',
        'last': 'lago',
        'location': 'Florianópolis'
    },
    'joaomariolago': {
        'first': 'joão mário',
        'last': 'lago',
        'location': 'Florianópolis'
    }
}
for username, user_info in users.items():
    print("\nUsername: " +
        username + '.')
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print("\tFull name: " +
        full_name.title() + '.')
    print("\tLocation: " + location + '.')