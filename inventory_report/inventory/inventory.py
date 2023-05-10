from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json

# instalação do xmltodict
import xmltodict


class Inventory:
    # Método de classe para importar dados a partir de um arquivo
    #  e gerar um relatório
    @classmethod
    def import_data(cls, filepath, report_type):
        # Identifica o tipo de arquivo a partir da extensão do arquivo
        if filepath.endswith(".csv"):
            data_list = cls.read_csv_file(filepath)
        elif filepath.endswith(".json"):
            data_list = cls.read_json_file(filepath)
        elif filepath.endswith(".xml"):
            data_list = cls.read_xml_file(filepath)
        else:
            raise ValueError("Tipo de arquivo inválido")

        # Gera o relatório solicitado com base no tipo de relatório
        return cls.get_report_type(data_list, report_type)

    # Método de classe para gerar o tipo de relatório solicitado
    @classmethod
    def get_report_type(cls, product_list, report_type):
        # Gera um relatório simples
        if report_type == "simples":
            return SimpleReport.generate(product_list)
        # Gera um relatório completo
        elif report_type == "completo":
            return CompleteReport.generate(product_list)
        # Lança um erro se o tipo de relatório solicitado for inválido
        else:
            raise ValueError("Tipo de relatório inválido")

    # Método de classe para ler um arquivo CSV e retornar uma lista de
    # dicionários de produtos
    @classmethod
    def read_csv_file(cls, filepath):
        product_list_by_csv = []
        with open(filepath, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for item in csv_reader:
                product_list_by_csv.append(item)
        return product_list_by_csv

    # Método de classe para ler um arquivo JSON e retornar uma lista
    # de dicionários de produtos
    @classmethod
    def read_json_file(cls, filepath):
        with open(filepath, "r") as json_file:
            data_json = json.load(json_file)
            return data_json

    # Método de classe para ler um arquivo XML e retornar uma lista
    # de dicionários de produtos
    @classmethod
    def read_xml_file(cls, filepath):
        with open(filepath, "r") as xml_file:
            my_xml = xml_file.read()
            my_dict = xmltodict.parse(my_xml)
            return my_dict["dataset"]["record"]
