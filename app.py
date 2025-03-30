from statistics import mean

print("bem vindo! Está com duvida em qual produto escolher?")
input("vamos te ajudar! insira 3 produtos dos quais você precisa a seguir")

nomeDoProduto1= input("digite o nome do seu produto 1: ")
n = int(input('Digite a quantidade de Avaliações : '))
valores1 = list()
for c in range(1, n + 1):
    x = int(input(f'Digite o {c}ª valor de 1 a 5: '))
    valores1.append(x)
nomeDoProduto2= input("digite o nome do seu produto 2: ")
y = int(input('Digite a quantidade de Avaliações : '))
valores2 = list()
for c in range(1, y + 1):
    x = int(input(f'Digite o {c}ª valor de 1 a 5: '))
    valores2.append(x)
nomeDoProduto3= input("digite o nome do seu produto 3: ")
z = int(input('Digite a quantidade de Avaliações : '))
valores3 = list()
for c in range(1, z + 1):
    x = int(input(f'Digite o {c}ª valor de 1 a 5: '))
    valores3.append(x)

produtos = [{"nome":nomeDoProduto1,"avaliacoes":valores1},
            {"nome":nomeDoProduto2,"avaliacoes":valores2},
            {"nome":nomeDoProduto3,"avaliacoes":valores3}] #criando uma tabela de produtos

produtoMedia =[{"media": mean(produto["avaliacoes"]),'nome':produto['nome']}for produto in produtos ] #fazendo a media

def criarFiltro(nota):
    def filtrado(produto):
        return produto["media"]>=nota
    return filtrado 
    
filtro = criarFiltro(4) #closure

def produtodoRecomendacao(produtos,filtro): return sorted(filter(filtro,produtos),key=lambda x: x["media"],reverse=True)
recomedar = produtodoRecomendacao(produtoMedia,filtro) #parametro de recomendação
print (recomedar)
for produto in recomedar:
    print(f"{produto['nome']}-media{produto['media']:.2f}") #Fim :)