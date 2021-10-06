var imagenes = ['img/fot1.jpg', 'img/fot2.jpg', '{% static "img/fot3.png" %)'],
    cont = 0;
function carrusel(conten) {
    conten.addEventListener('click', e => {
        let atras = conten.querySelector('.atras'),
            adelante = conten.querySelector('.adelante'),
            img = conten.querySelector('img'),
            tgt = e.target;

        if (tgt == atras) {
            if (cont > 0) {
                img.src = imagenes[cont - 1];
                cont--;
            } else {
                img.src = imagenes[imagenes.length - 1];
                cont = imagenes.length - 1;
            }
        } else if (tgt == adelante) {
            if (cont < imagenes.length - 1) {
                img.src = imagenes[cont + 1];
                cont++;
            } else {
                img.src = imagenes[0];
                cont = 0;
            }
        }
    });
}
document.addEventListener("DOMContentLoaded", () => {
    let conten = document.querySelector('.carrusel');

    carrusel(conten);
})