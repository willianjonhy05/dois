function calcularDiferencaDias() {
    var dataInicial = new Date(document.getElementById('id_inicio_do_contrato').value.replace(/(\d{2})\/(\d{2})\/(\d{4})/, '$3-$2-$1'));
    var dataFinal = new Date(document.getElementById('id_fim_do_contrato').value.replace(/(\d{2})\/(\d{2})\/(\d{4})/, '$3-$2-$1'));
    var diferencaEmMilissegundos = dataFinal - dataInicial;
    var diferencaEmDias = Math.floor(diferencaEmMilissegundos / (1000 * 60 * 60 * 24));
    document.getElementById('id_total_diarias').value = diferencaEmDias;
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('id_inicio_do_contrato').addEventListener('change', calcularDiferencaDias);
    document.getElementById('id_fim_do_contrato').addEventListener('change', calcularDiferencaDias);
});
