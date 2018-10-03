var cluserSize = 2;
var data = [['185','72'],['170','56'],['168','60'],['179','68'],['182','72'],['188','77']]

//Cluster size given, 2
var Clusers_Base = [];
var Clusters = [];
var distancesHolder = [];

for(var i = 0; i < cluserSize; i++){
    Clusers_Base.push(data[i]);
    Clusters.push([]);
    distancesHolder.push(0);
}

function calculateEuclidian(sampleMain, sampleCluster){
    return Math.sqrt(Math.pow((sampleCluster[0]-sampleMain[0]),2)+Math.pow((sampleCluster[1]-sampleMain[1]),2))
}

function assignCluster(euclidianDistances){
    var minVal = euclidianDistances[0];
    var minVal_Counter = 0;
    for(var i = 0; i < euclidianDistances.length; i++){
        if(minVal > euclidianDistances[i]){
            minVal = euclidianDistances[i];
            minVal_Counter = i;
        }
    }
    return minVal_Counter;
}

var sample = data[0];

for(var i = 0; i < data.length; i++){
    sample = data[i];
    for(var j = 0; j < cluserSize; j++){
        distancesHolder[j] = calculateEuclidian(sample, Clusers_Base[j]);
    }
    Clusters[assignCluster(distancesHolder)].push(sample);
}

console.log(Clusters);

/*
Ok te preguntarás que diablos. Trataré de explicarme lo mejor que pueda. Igual el video es muy fácil de entender.
Básicamente, tienes tus datos, de esos, tú dices... Quiero que este par sea un Cluster y este otro sean el Cluster 2.
OJO, pueden haber cuantos clusters quieras, eso es el K. Eso es lo que quiero que puedas implementar, que puedan ser cuantos k se nos hinchen.
Una vez que definas los k, entonces empiezas a iterar todos los datos, calculando las distancias de un dato al k1, k2, k3, k4....
eso te dará una serie de numeros, el más corto es el que está dentro de ese cluster.
Al final se pone cada dato en cada cluster y ia
*/
