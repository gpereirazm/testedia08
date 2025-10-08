def criar_pessoa(nome: str, idade: int, id: int) -> dict:
  return {
      "id": id,
      "nome": nome,
      "idade": idade
  }

def adicionar_gostos(pessoas: list, gostos: list) -> list:
 
  gostos_map = {}
  for item_gosto in gostos:
    
    gostos_map[item_gosto["id"]] = item_gosto["gostos"]

  
  pessoas_com_gostos = []
  
 
  for pessoa in pessoas[:5]:
   
    pessoa_id = pessoa["id"]
    
  
    gostos_da_pessoa = gostos_map.get(pessoa_id, []) 
    
   
    pessoa_atualizada = pessoa.copy()
    pessoa_atualizada["gostos"] = gostos_da_pessoa
    
 
    pessoas_com_gostos.append(pessoa_atualizada)

  return pessoas_com_gostos


pessoas = [
    criar_pessoa("Guilherme", 18, 1),
    criar_pessoa("Felipe", 34, 2),
    criar_pessoa("Pedro", 28, 3),
    criar_pessoa("Luiz", 96, 4),
    criar_pessoa("Eric", 21, 5),
]

gostos = [
    {"id": 1, "gostos": ["Música", "Futebol", "Dinheiro"]},
    {"id": 2, "gostos": ["Dinheiro", "resenha", "festas"]},
    {"id": 3, "gostos": ["Viagem", "basquete", "jogos"]},
    {"id": 4, "gostos": ["Dança", "Esportes", "luta"]},
    {"id": 5, "gostos": ["Tecnologia", "Culinária", "internet"]},
]

resultado = adicionar_gostos(pessoas, gostos)
print(resultado)
