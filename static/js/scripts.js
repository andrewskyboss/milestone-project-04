var scrollThreshold = 50;

/*----------- Mobile menu Open Close ----------*/
$('body').on('click', '.mobile-menu-trigger', function(e) {
	if(!$(this).hasClass('.mobile-menu-hidde')) {
		mobileMenuOpenClose(true);
	} else {
		mobileMenuOpenClose(false);
	}
	e.stopPropagation();
})
.on('click', function(e) {
	mobileMenuOpenClose(false);
});

function mobileMenuOpenClose(open) {
	open = (typeof open !== 'undefined') ? open : true;

	if(open) {
		$('.mobile-menu').show('slow').removeClass('hidden').addClass('visible');
		$('.mobile-menu-trigger').removeClass('mobile-menu-hidden').addClass('mobile-menu-visible');
		/*$('body').css('overflow', 'hidden');*/
	} else {
		$('.mobile-menu').removeClass('visible').addClass('hidden');
		$('.mobile-menu-trigger').removeClass('mobile-menu-visible').addClass('mobile-menu-hidden');
		/*$('body').css('overflow', 'auto');*/
	}
}

$(window).on('load', function() {
    // Initialize on-load animations
    $('body').addClass('on-load-animations-start');
});

$(window).on('load scroll', function(e) {
    // Handle scroll
    if($(document).scrollTop() > scrollThreshold) {
        $('body').addClass('scrolled');
    } else {
        $('body').removeClass('scrolled');
    }
});