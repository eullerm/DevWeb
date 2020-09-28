$(function () {
   $('[data-toggle="tooltip"]').tooltip();
   $('[data-toggle="popover"]').popover();
})

$(document).ready(function () {
   $(".show-toast").click(function () {
      $("#myToast").toast({ delay: 3000 });
      $("#myToast").toast('show');;
   });
});

$('#myModal').on('shown.bs.modal', function () {
   $('#myInput').trigger('focus')
 })

var $range = document.querySelector('input'),
    $value = document.querySelector('span');

$range.addEventListener('input', function() {
  $value.textContent = this.value;
});