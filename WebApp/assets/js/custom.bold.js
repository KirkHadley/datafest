jQuery( document ).ready( function( $ ){
	// Portfolio sorter initialization
	$( '.bold-portfolio' ).mixitup( {
		targetSelector: '.project',	// Class required on each portfolio item
		filterSelector: '.filter', // Class required on each filter link
		easing: 'snap'
	} );

	// Portfolio items zoom / popover
	$( '.image-popup' ).magnificPopup( {type: 'image' } );

	$( '.video-popup' ).magnificPopup( {type: 'iframe' } ); // Supports YouTube, Vimeo and Google Maps links.

	// Portfolio item :hover overlay
	$( '.project-wrap').hover(
		function () {
			$(this).find( '.project-links' ).animate( { top: 0 }, 'fast' );
		},
		function () {
			$(this).find( '.project-links' ).animate( { top: 100 + '%' }, 'fast' );
		}
	);

	// Full background image
	//$( '.fx-backstretch' ).backstretch("assets/img/backstretch.jpg"); // Replace backstrech.jpg with your own image if needed
});