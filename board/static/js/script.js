

$('.weekly-btn').click(function(){
  var pk = $(this).attr('name');
  $.ajax({
           type: "POST",
           url: "{% url 'weekly_button' %}",
           data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
           dataType: "json",
           success: function(response) {
                  console.log('Post weekly count is now ' + response.weekly_count);
                  $('.post' + pk + ' .daily_count').html(response.daily_count);
                  $('.post' + pk + ' .weekly_count').html(response.weekly_count);
                  $('.post' + pk + ' .monthly_count').html(response.monthly_count);
                  $('.post' + pk + ' .all_count').html(response.all_count);
            },
           error: function(response, e) {
                  console.log('Something went wrong.');
                  window.location.href = '{% url 'register' %}';
           }
      });
  })

$('.monthly-btn').click(function(){
  var pk = $(this).attr('name');
  $.ajax({
           type: "POST",
           url: "{% url 'monthly_button' %}",
           data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
           dataType: "json",
           success: function(response) {
                  console.log('Post monthly count is now ' + response.monthly_count);
                  $('.post' + pk + ' .daily_count').html(response.daily_count);
                  $('.post' + pk + ' .weekly_count').html(response.weekly_count);
                  $('.post' + pk + ' .monthly_count').html(response.monthly_count);
                  $('.post' + pk + ' .all_count').html(response.all_count);
            },
           error: function(response, e) {
                  console.log('Something went wrong.');
                  window.location.href = '{% url 'register' %}';
           }
      });
  })
