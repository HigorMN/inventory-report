from collections import defaultdict
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    # cria um método estático para contar a quantidade de produtos por empresa
    @staticmethod
    def _get_company_count(data_list):
        # cria um defaultdict do tipo int para contagem
        company_count = defaultdict(int)
        # itera sobre os dados da lista de produtos
        for data in data_list:
            # incrementa a contagem para a empresa correspondente
            company_count[data["nome_da_empresa"]] += 1
        # retorna um dicionário com a contagem por empresa
        return company_count

    # cria um método estático para formatar a contagem por
    # empresa em uma string
    @staticmethod
    def _format_company_count(company_count):
        # cria a string de cabeçalho
        format_string = "Produtos estocados por empresa:\n"
        # itera sobre o dicionário com a contagem por empresa
        for (company, count) in company_count.items():
            # adiciona uma linha com a contagem para cada empresa
            format_string += f"- {company}: {count}\n"
        # retorna a string formatada
        return format_string

    # sobrescreve o método generate da classe pai SimpleReport
    @staticmethod
    def generate(data_list):
        # gera o relatório simples
        simple_report = SimpleReport.generate(data_list)
        # conta a quantidade de produtos por empresa
        company_count = CompleteReport._get_company_count(data_list)
        # formata a contagem por empresa em uma string
        company_count_string = CompleteReport._format_company_count(
            company_count
        )
        # retorna a string com o relatório simples e a contagem por empresa
        return f"{simple_report}\n{company_count_string}"
