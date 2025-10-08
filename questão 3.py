import pandas as pd
import os 

def exportar_csv(pessoas: list, nome_arquivo: str):
 
  print(f"Iniciando exportação para '{nome_arquivo}'...")
  
  df = pd.DataFrame(pessoas)
  
  df.to_csv(nome_arquivo, index=False)
  
  if os.path.exists(nome_arquivo):
      print(f"Sucesso! DataFrame exportado como '{nome_arquivo}'.")
  
      print(f"Caminho completo do arquivo: {os.path.abspath(nome_arquivo)}")
  else:
      print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado após a exportação.")


def criar_pessoa(nome: str, idade: int, id: int) -> dict:
  return {"id": id, "nome": nome, "idade": idade}


pessoas_com_gostos_final = [
    {'id': 1, 'nome': 'Guilherme', 'idade': 28, 'gostos': ['Música', 'Futebol', 'dinheiro']},
    {'id': 2, 'nome': 'felipe', 'idade': 24, 'gostos': ['dinheiro', 'resenha', "festas"]},
    {'id': 3, 'nome': 'pedro', 'idade': 30, 'gostos': ['Viagem', "basquete", "jogos"]},
    {'id': 4, 'nome': 'luiz', 'idade': 22, 'gostos': ["Dança", 'Esportes', "luta"]},
    {'id': 5, 'nome': 'Pedro', 'idade': 27, 'gostos': ['Tecnologia', 'Culinária', "internet"]}
]

nome_do_arquivo = "pessoas_exportadas.csv"
exportar_csv(pessoas_com_gostos_final, nome_do_arquivo)
