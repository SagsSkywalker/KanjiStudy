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

/**
 * Convert data in CSV (comma separated value) format to a javascript array.
 *
 * Values are separated by a comma, or by a custom one character delimeter.
 * Rows are separated by a new-line character.
 *
 * Leading and trailing spaces and tabs are ignored.
 * Values may optionally be enclosed by double quotes.
 * Values containing a special character (comma's, double-quotes, or new-lines)
 *   must be enclosed by double-quotes.
 * Embedded double-quotes must be represented by a pair of consecutive 
 * double-quotes.
 *
 * Example usage:
 *   var csv = '"x", "y", "z"\n12.3, 2.3, 8.7\n4.5, 1.2, -5.6\n';
 *   var array = csv2array(csv);
 *  
 * Author: Jos de Jong, 2010
 * 
 * @param {string} data      The data in CSV format.
 * @param {string} delimeter [optional] a custom delimeter. Comma ',' by default
 *                           The Delimeter must be a single character.
 * @return {Array} array     A two dimensional array containing the data
 * @throw {String} error     The method throws an error when there is an
 *                           error in the provided data.
 */ 
function csv2array(data, delimeter) {
    // Retrieve the delimeter
    if (delimeter == undefined) 
      delimeter = ',';
    if (delimeter && delimeter.length > 1)
      delimeter = ',';
  
    // initialize variables
    var newline = '\n';
    var eof = '';
    var i = 0;
    var c = data.charAt(i);
    var row = 0;
    var col = 0;
    var array = new Array();
  
    while (c != eof) {
      // skip whitespaces
      while (c == ' ' || c == '\t' || c == '\r') {
        c = data.charAt(++i); // read next char
      }
      
      // get value
      var value = "";
      if (c == '\"') {
        // value enclosed by double-quotes
        c = data.charAt(++i);
        
        do {
          if (c != '\"') {
            // read a regular character and go to the next character
            value += c;
            c = data.charAt(++i);
          }
          
          if (c == '\"') {
            // check for escaped double-quote
            var cnext = data.charAt(i+1);
            if (cnext == '\"') {
              // this is an escaped double-quote. 
              // Add a double-quote to the value, and move two characters ahead.
              value += '\"';
              i += 2;
              c = data.charAt(i);
            }
          }
        }
        while (c != eof && c != '\"');
        
        if (c == eof) {
          throw "Unexpected end of data, double-quote expected";
        }
  
        c = data.charAt(++i);
      }
      else {
        // value without quotes
        while (c != eof && c != delimeter && c!= newline && c != ' ' && c != '\t' && c != '\r') {
          value += c;
          c = data.charAt(++i);
        }
      }
  
      // add the value to the array
      if (array.length <= row) 
        array.push(new Array());
      array[row].push(value);
      
      // skip whitespaces
      while (c == ' ' || c == '\t' || c == '\r') {
        c = data.charAt(++i);
      }
  
      // go to the next row or column
      if (c == delimeter) {
        // to the next column
        col++;
      }
      else if (c == newline) {
        // to the next row
        col = 0;
        row++;
      }
      else if (c != eof) {
        // unexpected character
        throw "Delimiter expected after character " + i;
      }
      
      // go to the next character
      c = data.charAt(++i);
    }  
    
    return array;
  }