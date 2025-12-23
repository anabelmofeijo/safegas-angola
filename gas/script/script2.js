//FUNÇÃO DATA
function date(){
    let date = new Date();
    let m = date.getMonth();
    let mes = '';
    let d = date.getDay();
    let a = date.getFullYear()
    switch(m){
        case 1:{
            mes = "Jan"
        }
        case 5:{
            mes = "Mai"
        }
        case 6:{
            mes = 'Jun'
        }
        case 7:{
            mes = 'Jul'
        }
    }
    document.getElementById('date').innerHTML=mes+" "+d+", "+a
}
setInterval(date,1000)


