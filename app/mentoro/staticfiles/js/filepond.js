$(function () {
    $('.course_create_pond').filepond();
    $('.course_create_pond').filepond('allowMultiple', false);
    $('.course_create_pond').filepond.setOptions({
        chunkUploads: true,
        chunkSize: 50000,
        server: {
            url: 'http://localhost:8000/fp',
            process: '/process/',
            patch: '/patch/',
            revert: '/revert/',
            fetch: '/fetch/?target=',
        }
    });
});