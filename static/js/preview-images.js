$(function () {
    $('.file-image-preview').on('click', function() {
        let previewModal = $('#previewImageModel');
        $(this).parent().parent().addClass('current-row');
        previewModal.find('.modal-body img').attr('src', $(this).data('origin'));
        previewModal.find('.modal-title').text($(this).data('title'))
    });
    $('body').on("keyup", function(e) {
         let previewImg;
         if (e.which === 37) {
            previewImg = $('.file-row.current-row').prev('.file-row');
         } else if (e.which === 39) {
            previewImg = $('.file-row.current-row').next('.file-row');
         }

         if (previewImg && previewImg.find('img').attr('src')) {
             $('.current-row').removeClass('current-row');
             previewImg.addClass('current-row');
             $('#previewImageModel .modal-body img').attr('src', previewImg.find('img').attr('src'));
         }
    });
});