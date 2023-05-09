from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        with open(file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        if report_type == "simples":
            report = SimpleReport.generate(data)
        elif report_type == "completo":
            report = CompleteReport.generate(data)
        else:
            raise ValueError("Tipo de relatório inválido")

        return report
