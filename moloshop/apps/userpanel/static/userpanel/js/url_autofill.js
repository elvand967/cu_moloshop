
// moloshop/apps/userpanel/static/userpanel/js/url_autofill.js
// console.log("url_autofill.js загружен");

document.addEventListener('DOMContentLoaded', function () {
    console.log("url_autofill.js DOMContentLoaded");

    const urlSelect = document.querySelector('select[name="url"]');
    if (!urlSelect) {
        console.error("Не найден select с name='url'");
        return;
    }

    const dataJson = urlSelect.getAttribute('data-named-urls-json');
    if (!dataJson) {
        console.error("data-named-urls-json не найден на select");
        return;
    }

    let namedUrls;
    try {
        namedUrls = JSON.parse(dataJson);
        console.log("namedUrls parsed:", namedUrls);
    } catch (e) {
        console.error("Ошибка парсинга JSON из data-named-urls-json:", e);
        return;
    }

    // Обработчик выбора
    urlSelect.addEventListener('change', function () {
        const selectedFullName = urlSelect.value;
        console.log("Выбран URL:", selectedFullName);

        // Ищем в namedUrls объект с нужным full_name
        const selectedItem = namedUrls.find(item => item.full_name === selectedFullName);

        if (!selectedItem) {
            console.warn("Выбранный URL не найден в списке именованных URL");
            return;
        }

        // Заполняем поля slug и url_params
        const slugInput = document.querySelector('input[name="slug"]');
        const urlParamsTextarea = document.querySelector('textarea[name="url_params"]');

        if (slugInput) {
            // Берём путь pattern без параметров, например "policies/<slug:slug>/" → "policies"
            let slugValue = selectedItem.pattern;

            // Удаляем параметры из пути (то, что внутри < >)
            slugValue = slugValue.replace(/<[^>]+>/g, '').replace(/\/+$/, '');
            if (!slugValue) slugValue = selectedItem.name;  // fallback

            slugInput.value = slugValue;
        } else {
            console.warn("Поле slug не найдено");
        }

        if (urlParamsTextarea) {
            // Если params есть — сериализуем в JSON, иначе пустая строка
            const params = selectedItem.params || {};
            const paramsStr = Object.keys(params).length ? JSON.stringify(params, null, 2) : '';
            urlParamsTextarea.value = paramsStr;
        } else {
            console.warn("Поле url_params не найдено");
        }
    });

    console.log("Обработчик change для urlSelect добавлен");
});
