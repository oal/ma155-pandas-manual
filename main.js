
$(function() {	
	$('.menu a').on('click', function() {
		console.log($(this).text())
		$('.content').load(encodeURI('html/'+$(this).text()+'.ipynb'), function(){console.log(123)});
	})
})