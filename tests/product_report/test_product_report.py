from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Core-i913900k",
        "Kabum",
        "10-05-2023",
        "10-05-2030",
        "ABC123",
        "em um local seco",
    )
    expected_output = (
        "O produto Core-i913900k fabricado em 10-05-2023 por Kabum "
        "com validade até 10-05-2030 precisa ser armazenado "
        "em um local seco."
    )
    assert str(product) == expected_output
