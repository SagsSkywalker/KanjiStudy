var data = [['185','72'],['170','56'],['168','60'],['179','68'],['182','72'],['188','77']]

//Cluster size given, 2

//k1 will be initial
var k1 = data[0]
//k2 will be second
var k2 = data[1]

//Used to calculate distances UwU
function calculateEuclidian(x,y){
    return Math.sqrt(Math.pow((y[0]-x[0]),2)+Math.pow((y[1]-x[1]),2))
}

//Gives which cluster to put
function giveCluster(x,y){
    if((parseFloat(x)-parseFloat(y)) >= 0){
        return 2
    }
    else{
        return 1
    }
}




//Calculate dk1
var dk1 = calculateEuclidian(k1,k1)

//Calculate dk2
var dk2 = calculateEuclidian(k1,k2)

var dataFinal = []
var dataWithClusters = []
var holder = [dk1,dk2]
var holder2 = [k1,giveCluster(holder[0],holder[1])]
dataWithClusters.push(holder2)
dataFinal.push(holder)

//Calculate dk1
var dk1 = calculateEuclidian(k1,k2)

//Calculate dk2
var dk2 = calculateEuclidian(k2,k2)

holder = [dk1,dk2]
var holder2 = [k2,giveCluster(holder[0],holder[1])]
dataFinal.push(holder)
dataWithClusters.push(holder2)


next = data[2]
//Calculate dk1
var dk1 = calculateEuclidian(k1,next)

//Calculate dk2
var dk2 = calculateEuclidian(k2,next)
holder = [dk1,dk2]
var holder2 = [next,giveCluster(holder[0],holder[1])]
dataFinal.push(holder)
dataWithClusters.push(holder2)

next = data[3]
//Calculate dk1
var dk1 = calculateEuclidian(k1,next)

//Calculate dk2
var dk2 = calculateEuclidian(k2,next)
holder = [dk1,dk2]
var holder2 = [next,giveCluster(holder[0],holder[1])]
dataFinal.push(holder)
dataWithClusters.push(holder2)

next = data[4]
//Calculate dk1
var dk1 = calculateEuclidian(k1,next)

//Calculate dk2
var dk2 = calculateEuclidian(k2,next)
holder = [dk1,dk2]
var holder2 = [next,giveCluster(holder[0],holder[1])]
dataFinal.push(holder)
dataWithClusters.push(holder2)

next = data[5]
//Calculate dk1
var dk1 = calculateEuclidian(k1,next)

//Calculate dk2
var dk2 = calculateEuclidian(k2,next)
holder = [dk1,dk2]
var holder2 = [next,giveCluster(holder[0],holder[1])]
dataFinal.push(holder)
dataWithClusters.push(holder2)
console.log(dataFinal)
console.log(dataWithClusters)

/*
Ok te preguntarás que diablos. Trataré de explicarme lo mejor que pueda. Igual el video es muy fácil de entender.
Básicamente, tienes tus datos, de esos, tú dices... Quiero que este par sea un Cluster y este otro sean el Cluster 2.
OJO, pueden haber cuantos clusters quieras, eso es el K. Eso es lo que quiero que puedas implementar, que puedan ser cuantos k se nos hinchen.
Una vez que definas los k, entonces empiezas a iterar todos los datos, calculando las distancias de un dato al k1, k2, k3, k4....
eso te dará una serie de numeros, el más corto es el que está dentro de ese cluster.
Al final se pone cada dato en cada cluster y ia
*/
