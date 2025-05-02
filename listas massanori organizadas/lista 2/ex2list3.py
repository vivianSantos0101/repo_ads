while True:
    usuario = input(" digite aqui seu usuario: ")
    senha = input("digite sua senha: ")
    if senha == usuario:
      print("a senha não deve ser igual ao usuario. Digite outra vez: ")
      continue
    else:
      print("sua senha é valida!")
      break