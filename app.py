from statistics import mean


produtos = [{"nome":"hidratante","avaliacoes":[2,3,2,1]},
            {"nome":"sabonete","avaliacoes":[5,4,5,5]},
            {"nome":"shampoo","avaliacoes":[3,4,5,2]}]

produtoMedia =[{"A media é ": mean(produto["avaliacoes"])}for produto in produtos ]

filtro = (4)

def produtodoRecomendacao(produtos,filtro): return sorted(filter(filtro,produtos),key=lambda x: x["media"],reverse=True)

print(produtodoRecomendacao)