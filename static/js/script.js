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

   $("#confirmPayment").click(function () {

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

   $("i.fa-thumbs-up, i.fa-thumbs-down").click(function () {
      if ($(this).hasClass("fa-thumbs-up")) {

         if ($(this).hasClass("far")) {

            $(this).removeClass("far ").addClass("fas")
            let idLike = $(this).parent().children("span:eq(0)").attr('id')
            let like = $("#" + idLike).data("like")
            $("#" + idLike).text(like + 1)

            $(this).parent().parent().children("div:eq(1)").children("i:eq(0)").removeClass("fas ").addClass("far ")
            let idDislike = $(this).parent().parent().children("div:eq(1)").children("span:eq(0)").attr('id')

            let dislike = $("#" + idDislike).data("dislike")
            $("#" + idDislike).text(dislike)

         } else {

            $(this).removeClass("fas").addClass("far")
            let idLike = $(this).parent().children("span:eq(0)").attr('id')
            let like = $("#" + idLike).data("like")
            $("#" + idLike).text(like)

         }

      } else if ($(this).hasClass("fa-thumbs-down")) {

         if ($(this).hasClass("far")) {

            $(this).removeClass("far ").addClass("fas")

            let idDislike = $(this).parent().children("span:eq(0)").attr('id')
            let dislike = $("#" + idDislike).data("dislike")
            $("#" + idDislike).text(dislike + 1)

            $(this).parent().parent().children("div:eq(0)").children("i:eq(0)").removeClass("fas ").addClass("far ")
            let idLike = $(this).parent().parent().children("div:eq(0)").children("span:eq(0)").attr('id')
            console.log(idLike)
            let like = $("#" + idLike).data("like")
            $("#" + idLike).text(like)

         } else {

            $(this).removeClass("fas").addClass("far")
            let idDislike = $(this).parent().children("span:eq(0)").attr('id')
            let dislike = $("#" + idDislike).data("dislike")
            $("#" + idDislike).text(dislike)

         }

      }
   })

   $("i.fa-thumbs-up").each(function (index) {
      let id = $(this).parent().children("span:eq(0)").attr('id')

      let text = $("#" + id).data("like")
      $("#" + id).text(text)
   })

   $("i.fa-thumbs-down").each(function (index) {
      let id = $(this).parent().children("span:eq(0)").attr('id')

      let text = $("#" + id).data("dislike")
      $("#" + id).text(text)
   })

   $(".buy").click(function () {
      let buttonBuy = this
      let form = $(buttonBuy).prev()
      var num = form.find("input[name='qty']").val()
      if (num != 0) {
         num = +num + 1
      }
      else {
         num = 1
      }
      form.find("input[name='qty']").val(num)
      let url = form.attr('action')
      let formData = form.serializeArray()
      $.post(url, formData, function (answer) {


         let qty = $(answer).find("#qty").text()
         let cartPrice = $(answer).find("#cartPrice").text()
         let totalPrice = $(answer).find("#totalPrice").text()
         if (qty == 1) {
            $("#total-1").text(qty + " item")
            $("#total-2").text(" " + qty + " item" + " ")
         }
         else {
            $("#total-1").text(qty + " itens")
            $("#total-2").text(" " + qty + " itens" + " ")
         }
         $("#price1").text("R$" + cartPrice)
         $("#price2").text("R$" + cartPrice)
         span.find("strong.totalPrice").text("R$" + totalPrice)

      })
   })

   $(".more").click(function () {
      this.blur()
      var input = $(this).parent().prev()
      var num = +input.val() + 1
      if (num < 100) {
         input.val(num)
         let form = $(this).parent().parent().parent()
         let url = form.attr('action')
         let formData = form.serializeArray()
         $.post(url, formData, function (answer) {
            console.log('O botão MAIS foi clicado')
            let qty = $(answer).find("#qty").text()
            let cartPrice = $(answer).find("#cartPrice").text()
            let totalPrice = $(answer).find("#totalPrice").text()
            if (qty == 1) {
               $("#total-1").text(qty + " item")
               $("#total-2").text(" " + qty + " item" + " ")
            }
            else {
               $("#total-1").text(qty + " itens")
               $("#total-2").text(" " + qty + " itens" + " ")
            }
            $("#price1").text("R$" + cartPrice)
            $("#price2").text("R$" + cartPrice)
            span.find("strong.totalPrice").text("R$" + totalPrice)
         })
      }
      else {
         return
      }
   })

   $(".less").click(function () {
      this.blur()
      var input = $(this).parent().next()
      var num = +input.val() - 1
      if (num <= 0) {
         num = 0
      }
      input.val(num)
      let form = $(this).parent().parent().parent()
      let url = form.attr('action')
      let formData = form.serializeArray()
      $.post(url, formData, function (answer) {

         console.log('O botão MENOS foi clicado')
         let qty = $(answer).find("#qty").text()
         let cartPrice = $(answer).find("#cartPrice").text()
         let totalPrice = $(answer).find("#totalPrice").text()
         if (num <= 0) {

            form.append('<input type="hidden" name="qty" value="0">')
            
            $("#total-1").text(qty + " itens")
            $("#total-2").text(" " + qty + " itens" + " ")
            let card = form.parent().parent().parent().parent()
            card.fadeTo("slow", 0.3, function () {
               $(this).prev().remove()
               $(this).remove()

               let cartPrice = $(answer).find("#cartPrice").text()
               $("#price1").text("R$" + cartPrice)
               $("#price2").text("R$" + cartPrice)

            })

         }
         else if (qty == 1) {
            $("#total-1").text(qty + " item")
            $("#total-2").text(" " + qty + " ites" + " ")
         }
         else {
            $("#total-1").text(qty + " itens")
            $("#total-2").text(" " + qty + " itens" + " ")
         }
         $("#price1").text("R$" + cartPrice)
         $("#price2").text("R$" + cartPrice)
         span.find("strong.totalPrice").text("R$" + totalPrice)

      })

   })

   $("#card").on("click", "a.remove", function () {

      console.log("Botão remover clicado")
      let form = $(this).parent().parent()
      form.append('<input type="hidden" name="qty" value="0">')
      let card = form.parent().parent().parent()
      let url = form.attr("action")
      let formData = form.serializeArray()
      $.post(url, formData, function (answer) {

         card.fadeTo("slow", 0.3, function () {
            $(this).prev().remove()
            $(this).remove()

            let qty = $(answer).find("#qty").text()
            let cartPrice = $(answer).find("#cartPrice").text()
            if (qty == 1) {
               $("#total-1").text(qty + " item")
               $("#total-2").text(" " + qty + " ites" + " ")
            }
            else {
               $("#total-1").text(qty + " itens")
               $("#total-2").text(" " + qty + " itens" + " ")
            }
            $("#price1").text("R$" + cartPrice)
            $("#price2").text("R$" + cartPrice)

         })
      })
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

function validSameAddressFunction() {

   let sameAddress = $("#same-address")

   let button = $("input[name='same-address']:checked")

   if (button.length === 0) {

      sameAddress.addClass("is-invalid")
      sameAddress.removeClass("is-valid")
      return false
   } else {
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
