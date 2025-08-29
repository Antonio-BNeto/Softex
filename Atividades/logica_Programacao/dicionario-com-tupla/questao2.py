agenda = {
    "Maria": ("(11) 9999-9999", "maria@email.com")
}

for key in agenda.keys():
    valores = agenda[key]
    print(f"{key} -> Telefone: {valores[0]} | Email: [{valores[1]}] (mailto:{valores[1]})")
