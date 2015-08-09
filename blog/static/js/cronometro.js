var reloj=document.getElementById("reloj");
var marcha=0;
var cro=0;
function iniciar() {
    if (marcha==0) {
        emp=new Date();
        elcrono=setInterval(tiempo,10); 
        marcha=1;
        document.getElementById("btnPlay_Restart").innerHTML = '<a class="btn offset-s4 col s1" id=restart onclick=lap() href="#"><i class="fa fa-refresh fa-fw fa-2x"></i></a>';
    }
}
function tiempo() {
    actual=new Date(); 
    cro=actual-emp;
    cr=new Date();
    cr.setTime(cro); 
    centesimas=cr.getMilliseconds();
    centesimas=centesimas/10;
    centesimas=Math.round(centesimas)
    segundos=cr.getSeconds();
    minutos=cr.getMinutes();
    if (centesimas<10) {centesimas="0"+centesimas;} 
    if (segundos<10) {segundos="0"+segundos;} 
    if (minutos<10) {minutos="0"+minutos;} 
    reloj.innerHTML= minutos+" : "+segundos+" : "+centesimas;
}

function parar() { 
    if (marcha==1) {
        clearInterval(elcrono);
        marcha=0;
        document.getElementById("btnPlay_Restart").innerHTML = '<a class="btn offset-s4 col s1" id=empezar onclick="continuar()" href="#"><i class="fa fa-play fa-fw fa-2x"></i></a>';
    }
}

function lap(){
    vuelta = reloj.innerHTML;
    getVueltas = document.getElementById("vueltas").innerHTML;
    document.getElementById("vueltas").innerHTML = getVueltas + "<br>" + vuelta;
}

function continuar() {
    if (marcha==0) { 
        emp2=new Date();
        emp2=emp2.getTime();
        emp3=emp2-cro;
        emp=new Date();
        emp.setTime(emp3);
        elcrono=setInterval(tiempo,10);
        marcha=1;
        document.getElementById("btnPlay_Restart").innerHTML = '<a class="btn offset-s4 col s1" id=restart onclick=lap() href="#"><i class="fa fa-refresh fa-fw fa-2x"></i></a>';
    }		
}

function reiniciar() {
    if (marcha==1) { 
        clearInterval(elcrono); 
        marcha=0;
    }
    cro=0;
    reloj.innerHTML = "00 : 00 : 00";
    document.getElementById("btnPlay_Restart").innerHTML = '<a class="btn offset-s4 col s1" id=empezar onclick="iniciar()" href="#"><i class="fa fa-play fa-fw fa-2x"></i></a>';
    document.getElementById("vueltas").innerHTML = "";
}