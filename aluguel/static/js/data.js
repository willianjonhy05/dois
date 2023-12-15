document.addEventListener('DOMContentLoaded', function () {
    var dataInput = document.getElementById('id_data_nasc');

    dataInput.addEventListener('input', function () {
        formatarData(this);
    });

    function formatarData(input) {
        var inputValue = input.value.replace(/\D/g, '');

        if (inputValue.length > 0) {
            if (inputValue.length <= 2) {
                inputValue = inputValue.match(/.{1,2}/g).join('/');
            } else if (inputValue.length <= 4) {
                inputValue = inputValue.substring(0, 2) + '/' + inputValue.substring(2);
            } else {
                inputValue = inputValue.substring(0, 2) + '/' + inputValue.substring(2, 4) + '/' + inputValue.substring(4, 8);
            }
        }

        input.value = inputValue;
    }
});
