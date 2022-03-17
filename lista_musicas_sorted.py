musicas = [
    {"titulo": "thunderstruck", "tocou": 3},
    {"titulo": "one", "tocou": 4},
    {"titulo": "keep the faith", "tocou": 2},
    {"titulo": "Blaze of glory", "tocou": 6}
]
# Ordenar da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
# Resposta: [{'titulo': 'keep the faith', 'tocou': 2}, {'titulo': 'thunderstruck', 'tocou': 3}, {'titulo': 'one', 'tocou': 4}, {'titulo': 'Blaze of glory', 'tocou': 6}]

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda  musica: musica['tocou'], reverse=True))
[{'titulo': 'Blaze of glory', 'tocou': 6}, {'titulo': 'one', 'tocou': 4}, {'titulo': 'thunderstruck', 'tocou': 3}, {'titulo': 'keep the faith', 'tocou': 2}]

