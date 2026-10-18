// Menú móvil, copiar IBAN y envío del formulario de contacto
(function () {
  var menu = document.querySelector('.menu');
  var boton = document.querySelector('.abre-menu');
  if (menu && boton) {
    boton.addEventListener('click', function () {
      var abierto = menu.classList.toggle('abierto');
      boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
  }
  document.querySelectorAll('.abre-sub').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.parentElement;
      var abierto = li.classList.toggle('sub-abierto');
      b.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
  });

  // Copiar IBAN
  document.querySelectorAll('.copiar').forEach(function (b) {
    b.addEventListener('click', function () {
      var aviso = b.closest('.iban').querySelector('.iban-aviso');
      var texto = b.getAttribute('data-copia');
      function seleccionar() {
        var span = b.closest('.iban').querySelector('#iban');
        var r = document.createRange(); r.selectNodeContents(span);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
        aviso.textContent = 'IBAN seleccionado: pulsa Ctrl+C o mantén pulsado para copiarlo.';
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(texto).then(function () {
          aviso.textContent = 'IBAN copiado. ¡Gracias por sumar!';
        }, seleccionar);
      } else { seleccionar(); }
    });
  });

  // Formulario (Formspree)
  var form = document.querySelector('.formulario');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var estado = form.querySelector('.form-estado');
      if (form.action.indexOf('TU_ID_DE_FORMSPREE') !== -1) {
        estado.textContent = 'El formulario aún no está activado. Escríbenos a asociacionbaolar@gmail.com';
        return;
      }
      estado.textContent = 'Enviando…';
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
        .then(function (r) {
          if (r.ok) { form.reset(); estado.textContent = '¡Gracias por tu mensaje! Te responderemos pronto.'; }
          else { estado.textContent = 'No se ha podido enviar. Prueba de nuevo o escríbenos a asociacionbaolar@gmail.com'; }
        })
        .catch(function () { estado.textContent = 'Sin conexión. Prueba de nuevo o escríbenos a asociacionbaolar@gmail.com'; });
    });
  }
})();
