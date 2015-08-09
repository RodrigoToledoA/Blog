$(function() {
    var progressbar = $( "#progressbar" ),
        progressLabel = $( ".progress-label" );
    progressbar.progressbar({
        value: false,
        change: function() {   
            progressLabel.text( progressbar.progressbar( "value" ) + "%" );
        },
    });


    setInterval(imagenAleatoria, 50);

    var progressValue = progressbar.progressbar( "value" ) || 0;
    function imagenAleatoria(){
        progressbar.progressbar( "value", progressValue + 2 );
        if (progressValue > 100){
            var numImagenes=6;
            var random = Math.random();
            var rand = Math.round((numImagenes-1)*random);

            imagenes = new Array;
            imagenes[0] = "/static/img/Andy.png";
            imagenes[1] = "/static/img/Logo%20Personal.gif";
            imagenes[2] = "/static/img/napBus.png";
            imagenes[3] = "/static/img/qr.png";
            imagenes[4] = "/static/img/poligonos.jpg";
            imagenes[5] = "/static/img/url.jpeg";
            var azar = imagenes[rand];
/*            document.getElementById("imagenes").innerHTML = '<img id=imagenes class="center" '+ azar +' width="400px" height="400px">';*/
            document.getElementById("imagenes").setAttribute("src", azar)
            Materialize.fadeInImage('#imagenes');
            progressValue = 0;
        }
        else { progressValue = progressValue + 1;
              setTimeout( progress, 80 );}
    }
    setTimeout( progress, 2000 );
});