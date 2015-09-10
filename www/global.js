function set_page() {
	var h = window.location.hash.substr(1);

	if ($.inArray(h, ['01', '02', '03', '04', '05', '06']) > -1) {
		$('.content').hide();
		$('#note-sec').load(h+'.html', function(){
			MathJax.Hub.Queue(['Typeset', MathJax.Hub, 'homework-sec']);
			$('#note-sec').show();
			$('#main').scrollTop(0);
		});

	}
}

$( document ).ready(function(){
	/* set up navigation */
	$(window).on('hashchange', set_page);
	set_page();

	/* add email */
	$('.email').attr('href', 'mailto:' + 'jongbin' + '@' + 'stanford.edu');
})
