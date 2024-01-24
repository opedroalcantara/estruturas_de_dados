
// a função splice ele altera um array ela pode remover elementos 
// substituir elementos de um array 

//remover 1 elemnetos a partir de posição de indice de memoria 

let numeros = [1,2,3,4,5,]

numeros.splice(2,1)

console.log("resultado remoção", numeros)


let numeros2 = [1,2,3,4,5]

numeros2.splice(2,1,500)

console.log("resultado substituição de array", numeros2)