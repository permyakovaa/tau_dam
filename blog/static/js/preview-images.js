$(function () {
    $('.file-image-preview').on('click', function() {
        let previewModal = $('#previewImageModel');
        previewModal.find('.modal-body').html('<img width="100%"/>')
        $(this).parent().parent().addClass('current-row');
        previewModal.find('.modal-body img').attr('src',  $(this).data('origin'));
        previewModal.find('.modal-title').text($(this).data('title'))
    });

    $('.pdf-image-preview').on('click', function() {
        let previewModal = $('#previewImageModel');
        previewModal.find('.modal-body').html('<iframe src="' +  $(this).data('origin') + '" width="100%" height="500px" type="application/pdf">')
        previewModal.find('.modal-title').text($(this).data('title'))
    });

    $('.video-image-preview').on('click', function() {
        let previewModal = $('#previewImageModel');
        previewModal.find('.modal-body').html('<video width="100%" controls></video>')
        previewModal.find('.modal-body video').attr('src', $(this).attr('src'));
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