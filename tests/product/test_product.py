from inventory_report.inventory.product import Product
from datetime import datetime
import pytest


@pytest.fixture
def sample_product():
    return Product(
        id=1,
        nome_do_produto="Arroz",
        nome_da_empresa="MarcaFácil",
        data_de_fabricacao=datetime.now(),
        data_de_validade=datetime.now().replace(year=datetime.now().year+1),
        numero_de_serie="123ABC",
        instrucoes_de_armazenamento="Manter em local seco e arejado",
    )


def test_cria_produto(sample_product):
    assert isinstance(sample_product.id, int)
    assert isinstance(sample_product.nome_da_empresa, str)
    assert isinstance(sample_product.nome_do_produto, str)
    assert isinstance(sample_product.data_de_fabricacao, str)
    assert isinstance(sample_product.data_de_validade, str)
    assert isinstance(sample_product.numero_de_serie, str)
    assert isinstance(sample_product.instrucoes_de_armazenamento, str)
