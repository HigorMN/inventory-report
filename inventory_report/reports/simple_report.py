from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(products):
        # Cria uma lista  que contém todas as datas de fabricação dos
        # produtos em ordem crescente.
        dates_fabrication = sorted(
            [p["data_de_fabricacao"] for p in products]
        )

        # Encontra a data de validade mais próxima
        closest_expiration_date = min(
            [
                p["data_de_validade"]
                for p in products
                if datetime.strptime(p["data_de_validade"], "%Y-%m-%d")
                > datetime.now()
            ]
        )

        # Armazena o nome da empresa que possui a maior quantidade
        # de produtos na lista
        company_with_most_products = Counter(
            [p["nome_da_empresa"] for p in products]
        ).most_common(1)[0][0]

        # Retorna uma string contendo as informações do relatório simplificado
        return (
            f"Data de fabricação mais antiga: {dates_fabrication[0]}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )
