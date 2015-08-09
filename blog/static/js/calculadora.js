var reset = false;
function ejecutar(btn) {
    aprieta = btn.value;
    val =  document.getElementById("txbResultado").value;
    txbResultado = document.getElementById("txbResultado");
    if(reset == true) {
        if(aprieta=="*" || aprieta=="-" || aprieta=="+" || aprieta=="/" || aprieta=="=" || aprieta=="C"){
            txbResultado.setAttribute("value", "");
            reset = false;
        }
        else if (aprieta==".") {
                txbResultado.setAttribute("value", 0+aprieta);
                reset = false;
            }
        else{
                txbResultado.setAttribute("value", aprieta);
                reset = false;
            }
    }
    else{ if(aprieta=="C") {
            txbResultado.setAttribute("value", "");
        } 
    else if(aprieta=="=") {
        if(val.length!=0) {
            result = eval(val);
            txbResultado.setAttribute("value", result);
            reset = true;
        }
    }else if(val.length==0 && (aprieta =="*" || aprieta=="-" || aprieta=="+" || aprieta=="/" || aprieta=="=")){
            txbResultado.setAttribute("value", 0+aprieta);
        }else if(val.length==0 && aprieta=="."){
        txbResultado.setAttribute("value", 0+aprieta);
            }
        else{
            txbResultado.setAttribute("value", val+aprieta);
        }
        }
}
