
function initEditControlPage() {
	$('a.control-edit-form-link').click(function(event){

		var link = $(this);
		$.ajax ({
			'url': link.attr('href'),
			'dataType': 'html',
			'type': 'get',
			'success': function(data, status, xhr) {
				//check if we got successful responce from the server
				if(status != 'success') {
					alert('Unknown server error.Please try later');
				return false;
				}
				//update modal window with arrived content from the server
				var modal = $('#myModal'),
				html = $(data), form = html.find ('#content-column form');
				modal.find('.modal-title').html(html.find('#content-column h2').text());
				modal.find('.modal-body').html(form);


				// init our edit form


				// setup and show modal window finally and avoid ocassionally modalwindow closing
				modal.modal({
					'keyboard': false,
					'backdrop': false,
					'show' : true
			});

				//setup and show modal window finally
				modal.modal('show');
			},
			'error': function(){
				alert('Unknown server error.Please try later');
				return false
			}
		});
		return false;
	});
}

//function initGroupSelector() {
//  // look up select element with groups and attach our even handler
//  // on field "change" event
//  $('#group-selector select').change(function(event){
//    // get value of currently selected group option
//    var group = $(this).val();
//
//    if (group) {
//      // set cookie with expiration date 1 year since now;
//      // cookie creation function takes period in days
//      $.cookie('current_group', group, {'path': '/', 'expires': 365});
//    } else {
//      // otherwise we delete the cookie
//      $.removeCookie('current_group', {'path': '/'});
//    }
//
//    // and reload a page
//    location.reload(true);
//
//    return true;
//  });
//}
//function initDateFields() {
//	 $('input.dateinput').datetimepicker({
//		 'format' : 'YYYY-MM-DD',
//		}).on('dp.hide',function(event){
//		$(this).blur();
//	});
//}


//function initEditStudentForm(form, modal) {
//	//attach datepicker
//	initDateFields();
//	//close modal window on Cancel button click
//	form.find('input[name="cancel_button"]').click(function(event){
//		modal.modal('hide');
//		return false;
//	});
//	//make form work in AJAX mode
//	form.ajaxForm({
//		'dataType':'html',
//		'error': function() {
//			alert('Unknown server error.Please try later');
//			return false;
//		},
//		'success': function(data,status,xhr) {
//			var html = $(data), newform =html.find('#content-column form');
//			//copy alert to modal window
//			modal.find('.modal-body').html(html.find('.alert'));
//
//			//copy form to modal if we found it in server response
//			if (newform.length > 0) {
//
//				modal.find('.modal-body').append(newform);
//
//				// initialize form fields and buttons
//				initEditStudentForm(newform, modal);
//
//			} else {
//
//				// if no form, it means success and we need to reload page
//				// to get updated students list;
//				// reload after 2 seconds, so that user can read
//				// success message
//				setTimeout(function(){location.reload(true);}, 1800);
//
//			}
//		}
//	});
//}


// function updatePageContext() {
//     var url = window.location.href;
//     $.ajax({
//         'url': url,
//         'dataType': 'html',
//         'type': 'get',
//         'success': function(data, status, xhr){
//             // check if we got successfull response from the server
//             if (status != 'success') {
//                 alert('Ошибка на сервере, попробуйте пожалуйста позже.');
//                 return false;
//             }
//             // update modal window with arrived content from the server
//             var table = $('.table'), newpage = $(data), newtable = newpage.find('.table');
//             table.html(newtable);
//             initEditStudentPage();
//         },
//
//         'error': function(){
//             alert('Ошибка на сервере, попробуйте пожалуйста позже.');
//             return false;
//         }
//     });
//     return false;
// }


// function loader() {
//
// i = 0;
// setInterval(function() {
//   i = ++i % 4;
//   $("#loading").html("Loading "+Array(i+1).join("."));
//    }, 800);
// }


$(document).ready(function(){
  //initJournal();
  //initGroupSelector();
  //initDateFields();
  initEditControlPage();
  //loader();


});
