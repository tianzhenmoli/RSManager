
// psd_to_pic
$('#psd2pic').on('click', function () {
  var p = $(this);
  p.addClass("disabled");
  var names = [];
  $("#body_w li.selected img").each(function () {
    var name = $(this).attr("id");
    names.push(name);
  });
  var cur_url = $('#bread').find('li').attr("id");
  if (names.length > 0){
    $.ajax({
      url: '/psd2png/',
      data:{
        "names": names,
        "url": cur_url,
      },
      type:"POST",
      dataType: 'json',
      success:function (data) {
          if (data.status){
            p.removeClass("disabled");
            $('#body_w ul li').removeClass('selected');
            $('.select').removeClass('selected');
            counter();
            location.reload()
          }else{
              console.log(data.message);
          }
      }
    });
  }else{
    p.removeClass("disabled");
  }
});

// download zip
$('#down_load').on('click', function () {
  var b = $(this);
  b.addClass("disabled");
  var names = [];
  $("#body_w li.selected img").each(function () {
    var name = $(this).attr("id");
    names.push(name);
  });
  var cur_url = $('#bread').find('li').attr("id");
  if (names.length > 0){
    console.log(names);
    $.ajax({
      url: '/zipfile/',
      data:{
        "names": names,
        "url": cur_url,
      },
      type:"POST",
      dataType:'json',
      success:function (data) {
        if (data.status){
          b.removeClass("disabled");
          $('#body_w ul li').removeClass('selected');
          $('.select').removeClass('selected');
          counter();
          location.href = /download_file/ + data.data;
        }else {
          b.removeClass("disabled");
        }
      }
    });
  }else{
    b.removeClass("disabled");
  }
});

// 导航
$('#bread_true li button').on('click',function () {
    var dir_id = $(this).attr("id");
    var cur_url = $('#bread').find('li').attr("id");
    $.ajax({
       url: '/chdir/',
       data:{
           url: cur_url,
           id: dir_id,
       },
       type: "POST",
       dataType: 'json',
       success:function (data) {
         if (data.status){
            location.href = data.data;
          }
       }
   })
});

// 单击选中
var timeoutID = null;
$('#body_w ul li').click(function () {
  clearTimeout(timeoutID);
  timeoutID = setTimeout( ()=> {
      $(this).toggleClass('selected');
      if ($('li.selected').length == 0)
        $('.select').removeClass('selected');
      else
        $('.select').addClass('selected');
      counter();
  }, 300);
});

// 双击进入
$('#body_w ul li').dblclick(function () {
  clearTimeout(timeoutID);
  var name = $(this).find('img').attr("id");
  var cur_url = $('#bread').find('li').attr("id");
  console.log(name, cur_url);
  $.ajax({
    url: "/chdir/",
    data:{
      'dir': name,
      'url': cur_url,
    },
    type:"POST",
    dataType: 'json',
    success:function (data) {
      if (data.status){
        location.href = data.data;
      }else{
        location.reload()
      }
    }
  })
});

// 全选或取消选中
$('.select').click(function () {
  if ($('#body_w ul li.selected').length == 0) {
    $('#body_w ul li').addClass('selected');
    $('.select').addClass('selected');
  }
  else {
    $('#body_w ul li').removeClass('selected');
    $('.select').removeClass('selected');
  }
  counter();
});

// 选中计数
function counter() {
  if ($('#body_w ul li.selected').length > 0)
    $('.send').addClass('selected');
  else
    $('.send').removeClass('selected');
  $('.send').attr('data-counter',$('#body_w ul li.selected').length);
}

