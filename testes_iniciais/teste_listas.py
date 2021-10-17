# Testes iniciais para aprender sobre listas.

# Create a new list with aliens:
aliens = []

for alien_number in range(20):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'medium',
    }
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(new_alien)
print('...')
print("The total number of aliens created was: " +
    str(len(aliens)) + '.')

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'slow'
        alien['points'] = 10
print(aliens[:5])
