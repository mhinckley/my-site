$('.unlike-button').click(function(){
  var pk = $(this).attr('name');
  $.ajax({
           type: "POST",
           url: "{% url 'like_button' %}",
           data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
           dataType: "json",
           success: function(response) {
                  console.log('Post likes count is now ' + response.likes_count);
                  $('.post' + pk + ' .like_count').html(response.likes_count);
                  $('.post' + pk + ' .glyphicon').css('color', 'gray');
                  $('.post' + pk + ' .like_count').css('color', 'gray');
                  $('.post' + pk + ' .unlike-button').css('border-color', 'gray');
                  $('.post' + pk + ' .unlike-button').css('background', 'white');
                  console.log('This is unlike.');

            },
           error: function(response, e) {
                  console.log('Something went wrong.');
           }
      });
  })

$('.like-button').click(function(){
  var pk = $(this).attr('name');
  $.ajax({
           type: "POST",
           url: "{% url 'like_button' %}",
           data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
           dataType: "json",
           success: function(response) {
                  console.log('Post likes count is now ' + response.likes_count);
                  $('.post' + pk + ' .like_count').html(response.likes_count);
                  $('.post' + pk + ' .glyphicon').css('color', 'white');
                  $('.post' + pk + ' .like_count').css('color', 'white');
                  $('.post' + pk + ' .like-button').css('border-color', 'gray');
                  $('.post' + pk + ' .like-button').css('background', 'gray');
                  console.log('this is like.');
            },
           error: function(response, e) {
                  console.log('Something went wrong.');
           }
      });
})

$('.follow-button').click(function(){
  var pk = $(this).attr('name');
  $.ajax({
           type: "POST",
           url: "{% url 'follow_button' %}",
           data: {
               'pk': pk,
               'frequency': $(this).val().toLowerCase(),
               'csrfmiddlewaretoken': '{{ csrf_token }}'
             },
           dataType: "json",
           success: function(response) {
/*                              $('.post' + pk + ' .daily').html(response.total_daily);
                  $('.post' + pk + ' .weekly').html(response.total_weekly);
                  $('.post' + pk + ' .monthly').html(response.total_monthly); */
                  $('.post' + pk + ' .all').html(response.total_all);
            },
           error: function(response, e) {
                  console.log('Something went wrong.');
           }
      });
  })


$('.daily-btn').click(function(){
  var pk = $(this).attr('name');
  var clicks = $(this).data('clicks');
  if (clicks) {
    $('.post' + pk + ' .daily-btn').css('color', 'gray');
    $('.post' + pk + ' .daily-btn').css('font-color', 'gray');
    $('.post' + pk + ' .daily-btn').css('background', 'white');
    $('.post' + pk + ' .monthly-btn').css('color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('background', 'white');
    $('.post' + pk + ' .weekly-btn').css('color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('background', 'white');
  } else {
    $('.post' + pk + ' .daily-btn').css('color', 'white');
    $('.post' + pk + ' .daily-btn').css('font-color', 'white');
    $('.post' + pk + ' .daily-btn').css('background', 'gray');
    $('.post' + pk + ' .monthly-btn').css('color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('background', 'white');
    $('.post' + pk + ' .weekly-btn').css('color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('background', 'white');
  }
  $(this).data("clicks", !clicks);
})

$('.weekly-btn').click(function(){
  var pk = $(this).attr('name');
  var clicks = $(this).data('clicks');
  if (clicks) {
    $('.post' + pk + ' .weekly-btn').css('color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('background', 'white');
    $('.post' + pk + ' .daily-btn').css('color', 'gray');
    $('.post' + pk + ' .daily-btn').css('font-color', 'gray');
    $('.post' + pk + ' .daily-btn').css('background', 'white');
    $('.post' + pk + ' .monthly-btn').css('color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('background', 'white');
  } else {
    $('.post' + pk + ' .weekly-btn').css('color', 'white');
    $('.post' + pk + ' .weekly-btn').css('font-color', 'white');
    $('.post' + pk + ' .weekly-btn').css('background', 'gray');
    $('.post' + pk + ' .daily-btn').css('color', 'gray');
    $('.post' + pk + ' .daily-btn').css('font-color', 'gray');
    $('.post' + pk + ' .daily-btn').css('background', 'white');
    $('.post' + pk + ' .monthly-btn').css('color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('background', 'white');
  }
  $(this).data("clicks", !clicks);
})

$('.monthly-btn').click(function(){
  var pk = $(this).attr('name');
  var clicks = $(this).data('clicks');
  if (clicks) {
    $('.post' + pk + ' .monthly-btn').css('color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .monthly-btn').css('background', 'white');
    $('.post' + pk + ' .daily-btn').css('color', 'gray');
    $('.post' + pk + ' .daily-btn').css('font-color', 'gray');
    $('.post' + pk + ' .daily-btn').css('background', 'white');
    $('.post' + pk + ' .weekly-btn').css('color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('background', 'white');
  } else {
    $('.post' + pk + ' .monthly-btn').css('color', 'white');
    $('.post' + pk + ' .monthly-btn').css('font-color', 'white');
    $('.post' + pk + ' .monthly-btn').css('background', 'gray');
    $('.post' + pk + ' .daily-btn').css('color', 'gray');
    $('.post' + pk + ' .daily-btn').css('font-color', 'gray');
    $('.post' + pk + ' .daily-btn').css('background', 'white');
    $('.post' + pk + ' .weekly-btn').css('color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('font-color', 'gray');
    $('.post' + pk + ' .weekly-btn').css('background', 'white');
  }
  $(this).data("clicks", !clicks);
})