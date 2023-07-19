var $ = jQuery.noConflict();
$(document).ready(function() {
    // Получение URL-адреса сохранения данных из атрибута data
    var saveDataUrl = $('#reserve-form').data('save-url');

    // Обработка события отправки формы
    $('#reserve-modal').submit(function(event) {
        event.preventDefault();  // Предотвращаем отправку формы

        // Получение CSRF-токена из cookies
        var csrftoken = getCookie('csrftoken');

        // Получение данных из формы
        var formData = {
            date: $('#cdate').val(),
            time: $('#ctime').val(),
            seats: $('#cguests').val(),
            name: $('#cname').val(),
            email: $('#cemail').val(),
            phone: $('#cphone').val(),
            booking: $('#cbook').val(),
            csrfmiddlewaretoken: csrftoken  // Добавление CSRF-токена в данные запроса
        };

        // Отправка AJAX-запроса на сервер
        $.ajax({
            type: 'POST',
            url: saveDataUrl,  // Используем сохраненный URL-адрес
            data: formData,
            dataType: 'json',
            success: function(response) {
                // Обработка успешного ответа от сервера
                console.log('Data saved successfully');
                // Дополнительные действия при необходимости
            },
            error: function(xhr, status, error) {
                // Обработка ошибки при отправке запроса
                console.error('Error saving data:', error);
                // Дополнительные действия при необходимости
            }
        });
    });

    // Функция для получения значения CSRF-токена из cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
