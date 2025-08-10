document.addEventListener('DOMContentLoaded', function () {
    const urlField = document.querySelector('#id_url');
    const slugField = document.querySelector('#id_slug');
    const paramsField = document.querySelector('#id_url_params');

    fetch('/core/api/named-urls/')
        .then(response => response.json())
        .then(data => {
            if (!urlField) return;

            urlField.addEventListener('change', function () {
                const selected = data.find(item => item.name === urlField.value);
                if (selected) {
                    if (!slugField.value) {
                        slugField.value = selected.pattern
                            .replace(/<[^>]+>/g, '')
                            .replace(/\//g, '-')
                            .replace(/^-|-$/g, '');
                    }
                    if (selected.params) {
                        paramsField.value = JSON.stringify(selected.params);
                    }
                }
            });
        });
});
