document.addEventListener('DOMContentLoaded', function () {
    const urlField = document.querySelector('#id_url');
    const slugField = document.querySelector('#id_slug');

    if (!urlField || !slugField) return;

    // Загружаем список путей
    fetch('/admin/api/named-urls/')
        .then(response => response.json())
        .then(data => {
            const pathByFullName = {};
            data.forEach(item => {
                pathByFullName[item.full_name] = item.path;
            });

            urlField.addEventListener('change', function () {
                const selected = this.value;
                const path = pathByFullName[selected];

                if (path && !slugField.value) {
                    slugField.value = path.replace(/\/$/, '').replace(/\//g, '-');
                }
            });
        })
        .catch(console.error);
});
