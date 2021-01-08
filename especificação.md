# Especificação do exercício

Escreva um script que determina se um determinado número inteiro recebido do usuário é um ano bissexto.
O script deverá imprimir na tela a seguinte mensagem:

```markdown
O ano [número enviado pelo usuário] é bissexto.
```

ou

```markdown
O ano [número enviado pelo usuário] não é bissexto.
```

dependendo do valor dado como entrada pelo usuário.

## Explicação

Um ano é bissexto se for um múltiplo de 4, mas não de 100.
Os séculos são casos especiais.
Se um ano for múltiplo de 100, então só é bissexto se também for múltiplo de 400.

Por exemplo:

- 1984, 2004, 2024 são bissextos porque são múltiplos de 4 e não são múltiplos de 100.
- 1800, 1900, 2100 não são bissextos apesar de serem múltiplos de 4 porque não são múltiplos de 400.
- 1600, 2000, 2400 são bissextos porque são múltiplos de 4 e de 400.
