$(function() {
    const previewModal = $('#previewImageModel');
  
    $('.show-preview').on('click', function() {
        showPreview($(this));
    });
  
    $('body').on('keyup', function(e) {
        let previewImg;
        const currentRow = $('.file-row.current-row');
    
        if (e.which === 37) {
            previewImg = currentRow.prev('.file-row');
        } else if (e.which === 39) {
            previewImg = currentRow.next('.file-row');
        }
    
        if (previewImg) {
            showPreview(previewImg.find('.show-preview'));
        }
    });
  
    function showPreview(imageRow) {
        $('.current-row').removeClass('current-row');
        imageRow.closest('.row').addClass('current-row');
        let title = imageRow.data('title');
        let contentHtml = '';
        let originSrc = imageRow.data('origin');
        switch (imageRow.data('type')) {
            case 'image':
                contentHtml = `<img src="${originSrc}">`;
                break;
            case 'pdf':
                contentHtml = `<iframe src="${originSrc}" width="100%" height="500px" type="application/pdf">`;
                break;
            case 'video':
                contentHtml = `<video id="video-preview" width="100%" controls src="${originSrc}"></video>`;
                break;
            default:
            console.log('Error: unknown file format')
            break;
        }

        previewModal.find('.modal-body').html(contentHtml);
        previewModal.find('.modal-title').text(title);
    }
});