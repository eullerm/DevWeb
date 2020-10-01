/// <reference path="../../typings/globals/jquery/index.d.ts" />


$(function () {
   $('[data-toggle="tooltip"]').tooltip();
   $('[data-toggle="popover"]').popover();

   $(".show-toast").click(function () {
      $("#myToast").toast({ delay: 3000 });
      $("#myToast").toast('show');;
   });

   $('#myModal').on('shown.bs.modal', function () {
      $('#myInput').trigger('focus')
   })

   $("#submit").click(function () {

      let name_valid = validNameFunction()
      let address_valid = validAddressFunction()
      let state_valid = validStateFunction()
      let county_valid = validCountyFunction()
      let zip_valid = validZipFunction()
      let sameAddress_valid = validSameAddressFunction()
      let payment_valid = validPaymentMetodFunction()
      let cardName_valid = validCardNameFunction()
      let cardNumber_valid = validCardNumberFunction()
      let cardExpiration_valid = validCardExpirationFunction()
      let cardCVV_valid = validCardCVVFunction()



      if (name_valid && address_valid && state_valid && county_valid && zip_valid && sameAddress_valid && payment_valid && cardName_valid && cardNumber_valid && cardExpiration_valid && cardCVV_valid) {
         alert("Tudo ok!")
      }
      else {
         alert("Deu erro!")
      }

   })

})

function validNameFunction() {

   let name = $("#name")

   if (name.val() == '') {
      name.addClass("is-invalid")
      name.removeClass("is-valid")
      return false
   } else {
      name.addClass("is-valid")
      name.removeClass("is-invalid")
      return true
   }

}

function validAddressFunction() {

   let address = $("#address")

   if (address.val() == '') {
      address.addClass("is-invalid")
      address.removeClass("is-valid")
      return false
   } else {
      address.addClass("is-valid")
      address.removeClass("is-invalid")
      return true
   }

}

function validStateFunction() {

   let state = $("#state")

   if (state.val() === "") {

      state.addClass("is-invalid")
      state.removeClass("is-valid")
      return false

   } else {

      state.addClass("is-valid")
      state.removeClass("is-invalid")
      return true
   }

}

function validCountyFunction() {

   let county = $("#county")

   if (county.val() == '') {
      county.addClass("is-invalid")
      county.removeClass("is-valid")
      return false
   } else {
      county.addClass("is-valid")
      county.removeClass("is-invalid")
      return true
   }

}

function validZipFunction() {

   let zip = $("#zip")

   if (zip.val() == '') {
      zip.addClass("is-invalid")
      zip.removeClass("is-valid")
      return false
   } else {
      zip.addClass("is-valid")
      zip.removeClass("is-invalid")
      return true
   }

}

function validSameAddressFunction(){

   let sameAddress = $("#same-address")

   let button = $("input[name='same-address']:checked")

   if(button.length === 0){

      sameAddress.addClass("is-invalid")
      sameAddress.removeClass("is-valid")
      return false
   }else{
      sameAddress.addClass("is-valid")
      sameAddress.removeClass("is-invalid")
      return true
   }

}

function validPaymentMetodFunction() {

   let credit = $("#credit")
   let debit = $("#debit")
   let paypal = $("#paypal")
   let boleto = $("#boleto")
   let transference = $("#transference")

   let button = $("input[name='paymentMethod']:checked")

   if (button.length === 0) {
      credit.addClass("is-invalid")
      debit.addClass("is-invalid")
      paypal.addClass("is-invalid")
      boleto.addClass("is-invalid")
      transference.addClass("is-invalid")

      credit.removeClass("is-valid")
      debit.removeClass("is-valid")
      paypal.removeClass("is-valid")
      boleto.removeClass("is-valid")
      transference.removeClass("is-valid")

      return false
   } else {
      credit.addClass("is-valid")
      debit.addClass("is-valid")
      paypal.addClass("is-valid")
      boleto.addClass("is-valid")
      transference.addClass("is-valid")

      credit.removeClass("is-invalid")
      debit.removeClass("is-invalid")
      paypal.removeClass("is-invalid")
      boleto.removeClass("is-invalid")
      transference.removeClass("is-invalid")
      return true
   }

}

function validCardNameFunction() {

   let cc_name = $("#cc-name")

   if (cc_name.val() == '') {
      cc_name.addClass("is-invalid")
      cc_name.removeClass("is-valid")
      return false
   } else {
      cc_name.addClass("is-valid")
      cc_name.removeClass("is-invalid")
      return true
   }

}

function validCardNumberFunction() {

   let cc_number = $("#cc-number")

   if (cc_number.val() == '') {
      cc_number.addClass("is-invalid")
      cc_number.removeClass("is-valid")
      return false
   } else {
      cc_number.addClass("is-valid")
      cc_number.removeClass("is-invalid")
      return true
   }

}

function validCardExpirationFunction() {

   let cc_expiration = $("#cc-expiration")

   if (cc_expiration.val() == '') {
      cc_expiration.addClass("is-invalid")
      cc_expiration.removeClass("is-valid")
      return false
   } else {
      cc_expiration.addClass("is-valid")
      cc_expiration.removeClass("is-invalid")
      return true
   }

}

function validCardCVVFunction() {

   let cc_cvv = $("#cc-cvv")

   if (cc_cvv.val() == '') {
      cc_cvv.addClass("is-invalid")
      cc_cvv.removeClass("is-valid")
      return false
   } else {
      cc_cvv.addClass("is-valid")
      cc_cvv.removeClass("is-invalid")
      return true
   }

}
