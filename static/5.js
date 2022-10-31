$(document).ready(function(){
    $.ajax({
      type: "GET",
      url: "http://spartacodingclub.shop/sparta_api/weather/seoul",
      data: {},
      success: function(response){
          $('#temp').text(response['temp'])
        }
      })
});

