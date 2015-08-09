function ejecutar(btn){
    aprieta = btn.value;
    monto1 =  document.getElementById("txbMonto1").value;
    monto2 = document.getElementById("txbMonto2").value;
    moneda1 = document.getElementById("cmb1").selectedIndex;
    moneda2 = document.getElementById("cmb2").selectedIndex;

    if (aprieta=="Clear"){

        document.getElementById("txb1").innerHTML = '<input class="txb_Montos white-text" type="text" id=txbMonto1 value="">';
        document.getElementById("txb2").innerHTML = '<input class="txb_Montos white-text" type="text" id=txbMonto2 value="">';
    }

    switch (moneda1){
        case 0:
            cotizacion1 = 0.11271;
            break;
        case 1:
            cotizacion1 = 1;
            break;
        case 2:
            cotizacion1 = 0.10524;
            break;
        case 3:
            cotizacion1 = 0.07575;
            break;
        case 4:
            cotizacion1 = 68.8824;
            break;
        case 5:
            cotizacion1 = 2.90185;
            break;
        case 6:
            cotizacion1 = 0.340699;
            break;
    }

    switch (moneda2){
        case 0:
            cotizacion2 = 0.11271;
            break;
        case 1:
            cotizacion2 = 1;
            break;
        case 2:
            cotizacion2 = 0.10524;
            break;
        case 3:
            cotizacion2 = 0.07575;
            break;
        case 4:
            cotizacion2 = 68.8824;
            break;
        case 5:
            cotizacion2= 2.90185;
            break;
        case 6:
            cotizacion2 = 0.340699;
            break;
    }
    if (aprieta=="Convert"){
        if (monto1 != ""){
            aux = (monto1/cotizacion1)*cotizacion2;
            document.getElementById("txbMonto2").setAttribute("value", aux);
        }
        else{
            aux = monto2/cotizacion2*cotizacion1;
            document.getElementById("txbMonto1").setAttribute("value", aux);
        } 
    }
}