"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    ano=int(input("Digite um ano:\n"))

    def testebisexto(ano):
      if (ano%4)==0:
        if (ano%100)==0:
          if (ano%400)==0:
            return True
          else:
              return False
        else:
           return True
      else:
        return False

    if(testebisexto(ano)):
      print(f"O ano {ano} é bissexto.")
    else:
      print(f"O ano {ano} não é bissexto.")
    
if __name__ == '__main__':
    main()
