$(function () {
    if (delete_file === 'True' && delete_directory === 'True') {
        $('.file-row').on('contextmenu', function(e) {
            e.preventDefault();
            $('.context-menu')
                .css('display', 'block')
                .css('top', e.pageY)
                .css('left', e.pageX)
            ;

            $('#delete-action').attr('href', $(this).data('delete-url'));

            $('body').on('click', function() {
                $('.context-menu')
                    .css('display', 'none')
            })

            $('#delete-action').on('click', function(e) {

                e.preventDefault();
                $('.confirm-delete').attr('href', $(this).attr('href'));
            })
        })
    }
});