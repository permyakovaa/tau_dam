$(function () {
    if (delete_file === 'True' && delete_directory === 'True') {
        $('.file-row').on('contextmenu', function(e) {
            e.preventDefault();

            let rename_action = $('#rename-action');
            let delete_action = $('#delete-action');
            let download_action = $('#download-action');

            rename_action.css('display', 'none');
            download_action.css('display', 'none');
            $('.context-menu')
                .css('display', 'block')
                .css('top', e.pageY)
                .css('left', e.pageX)
            ;

            delete_action.attr('href', $(this).data('delete-url'));

            if ($(this).data('rename-url')) {
                rename_action.attr('href', $(this).data('rename-url'));
                rename_action.css('display', 'block');
            }

            if ($(this).data('download-url')) {
                download_action.attr('href', $(this).data('download-url'));
                download_action.css('display', 'block');
            }

            $('body').on('click', function() {
                $('.context-menu')
                    .css('display', 'none')
            })

            delete_action.on('click', function(e) {
                e.preventDefault();
                $('.confirm-delete').attr('href', $(this).attr('href'));
            })
        })
    }
});