# Dicionário de pontos turísticos
pontos_turisticos = {
    (-22.9519, -43.2105): "Cristo Redentor (RJ)",
    (-12.9717, -38.5111): "Elevador Lacerda (Salvador)",
    (-7.2210, -35.8731): "Aquele Velho (Campina Grande - PB)"
}

# Programa principal
print("=== PONTOS TURÍSTICOS ===")
print("Digite as coordenadas para encontrar um ponto turístico")

try:
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))

    ponto = pontos_turisticos[(latitude, longitude)]
    
    if ponto:
        print(f"\nPonto turístico encontrado: {ponto}")
    else:
        print(f"\nNão há ponto turístico registrado nas coordenadas ({latitude, longitude})")
        
except ValueError:
    print("Erro: Digite coordenadas válidas (números)")