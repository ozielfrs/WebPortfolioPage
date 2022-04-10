(function () {
  'use strict'

  var forms = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
      }, false)
    })
})()

function not_valid() {
  var alertPlaceholder = document.getElementById('liveAlertPlaceholder')

  function alert(type = 'warning', message = 'Você deve preencher todos os campos corretamente') {
    var wrapper = document.createElement('div')
    wrapper.innerHTML = '<div class="alert alert-' + type + '" id="bigAlert" role="alert">' + message + '</div>'
    alertPlaceholder.append(wrapper)
  }

  if (alertPlaceholder.children.length == 0)
    alert()
}