# Funções do Python - Exercícios e Criações

Meu objetivo consiste em dominar esse tema do python, logo esse repositório é um jeito de eu deixar registrado todas as minhas práticas em funções. Práticas lidas de livros ou cursos e até criações por conta.

## Como chamar essas funções?

Aprendi que existem muitas maneiras, segue algumas de um exemplo de função que está no script ex19_teoria_conjuntos.py

Aqui estão algumas maneiras diferentes de chamar a função valor_em_conjunto:

    **Chamada direta:** Você pode chamar a função diretamente passando os argumentos necessários. Por exemplo: valor_em_conjunto(10, 20)

    **Armazenando a função em uma variável:** Você pode armazenar uma referência à função em uma variável e, em seguida, chamar a função através da variável. Por exemplo: fn = valor_em_conjunto; fn(10, 20)

    **Atribuindo a função a uma propriedade:** Você pode atribuir a função a uma propriedade de um objeto e, em seguida, chamar a função através da propriedade. Por exemplo: obj.fn = valor_em_conjunto; obj.fn(10, 20)

    **Passando a função como um argumento:** Você pode passar a função como um argumento para outra função e, em seguida, chamar a função dentro da segunda função. Por exemplo: outra_função(valor_em_conjunto, 10, 20)

    **Retornando a função de uma função:** Você pode retornar a função de uma função e, em seguida, chamar a função retornada. Por exemplo: fn = outra_função(); fn(10, 20)

    **Envolvendo a função em um closure:** Você pode envolver a função em um closure e, em seguida, chamar a função através do closure. Por exemplo: fn = (function(valor1) { return function(valor2) { return valor_em_conjunto(valor1, valor2); } })(10); fn(20)

    **Definindo a função como um método:** Você pode definir a função como um método de um objeto e, em seguida, chamar a função através do objeto. Por exemplo: obj.meu_metodo = function(valor1, valor2) { return valor_em_conjunto(valor1, valor2); }; obj.meu_metodo(10, 20)

    **Usando a função como um construtor:** Você pode usar a função como um construtor para criar um novo objeto e, em seguida, chamar um método no objeto. Por exemplo: obj = new ValorEmConjunto(10, 20); obj.meu_metodo()
