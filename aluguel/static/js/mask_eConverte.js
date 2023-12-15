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

    // Função para enviar dados ao backend (Django)
    function enviarData() {
        // Obtenha o valor formatado do campo de entrada
        var valorFormatado = dataInput.value;

        // Converta para o formato esperado pelo Django (YYYY-MM-DD)
        var valorParaEnviar = converterParaFormatoDjango(valorFormatado);

        // Aqui você pode enviar o valorParaEnviar para o backend (por meio de AJAX, formulário, etc.)
        console.log("Valor para enviar ao backend:", valorParaEnviar);
    }

    // Função para converter o formato para o esperado pelo Django
    function converterParaFormatoDjango(valorFormatado) {
        var partes = valorFormatado.split('/');
        if (partes.length === 3) {
            return partes[2] + '-' + partes[1] + '-' + partes[0];
        }
        return valorFormatado; // Retorna sem alterações se não estiver no formato esperado
    }
});
