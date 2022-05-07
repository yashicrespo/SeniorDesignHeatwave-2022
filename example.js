document.getElementById('button3').addEventListener
('click', loadREST);


function loadREST(){
    fetch('https://picsum.photo/list')
        
    .then(function(response){
        console.log(response);

    })
}


