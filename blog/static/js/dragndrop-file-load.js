let dropArea = document.getElementById('drop-area')
let uploadProgress = []
let progressBar = document.getElementById('progress-bar')

;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
})
function preventDefaults (e) {
      e.preventDefault()
      e.stopPropagation()
}
;['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
})
;['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false)
})
function highlight(e) {
    dropArea.classList.add('highlight')
}
function unhighlight(e) {
    dropArea.classList.remove('highlight')
}
dropArea.addEventListener('drop', handleDrop, false)
function handleDrop(e) {
      let dt = e.dataTransfer
      let files = dt.files
      handleFiles(files)
}

function handleFiles(files) {
      files = [...files]
      initializeProgress(files.length)

      window.items_cnt = 0;
      files.forEach(uploadFile)
      files.forEach(previewFile, function() {alert('done')})
}

function uploadFile(file, i, array) {
      var xhr = new XMLHttpRequest()
      var formData = new FormData()
      xhr.open('POST', url, true)

      xhr.upload.addEventListener("progress", function(e) {
            let p = (e.loaded * 100.0 / e.total) || 100;
            updateProgress(i, p || 100);

            if (p == 100) {
                window.items_cnt++;
            }
            if (window.items_cnt === array.length && p == 100)  {
                location.reload();
            }
      })
      xhr.addEventListener('readystatechange', function(e) {
            if (xhr.readyState == 4 && xhr.status == 200) {
              // Готово. Сообщаем пользователю
            }
            else if (xhr.readyState == 4 && xhr.status != 200) {
              // Ошибка. Сообщаем пользователю
            }
      })
      formData.append('file', file)
      formData.append('csrfmiddlewaretoken', csrf_token)
      xhr.send(formData);
}
function previewFile(file) {
      let reader = new FileReader()
      reader.readAsDataURL(file)
      reader.onloadend = function() {
            let img = document.createElement('img')
            img.src = reader.result
            document.getElementById('gallery').appendChild(img)
      }
}
function initializeProgress(numFiles) {
      progressBar.value = 0
      uploadProgress = []
      for (let i = numFiles; i > 0; i--) {
            uploadProgress.push(0)
      }
}

function updateProgress(fileNumber, percent) {
      uploadProgress[fileNumber] = percent
      let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length
      progressBar.value = total
}