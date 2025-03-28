from statistics import mean


produtos = [{"nome":"hidratante","avaliacoes":[2,3,2,1]},
            {"nome":"sabonete","avaliacoes":[5,4,5,5]},
            {"nome":"shampoo","avaliacoes":[4,4,5,5]}] #criando uma tabela de produtos

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