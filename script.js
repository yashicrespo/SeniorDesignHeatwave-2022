



async function fetchdata(){
const url = 'https://dld12nqg91.execute-api.us-west-2.amazonaws.com/v1/id/0';
const response = await fetch(url);
const dat = await response.json();

 var tmp = [];
    for(var i = 0; i < dat.length; i += 32) {
        tmp.push(dat.slice(i, i + 32));
    }

var x = tmp;
var data = [{
    z: x,
    type: 'heatmap'
}];

Plotly.newPlot('myDiv', data);

  
  return dat;






  
 };
  
        fetchdata()
    


 