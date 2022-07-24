from datetime import date
import os
from dotenv import load_dotenv
load_dotenv()

SQL_INSERT_DATA = {
    "type_entries_categories": {
        "sql": "INSERT INTO type_entries_categories (ID, NAME, IS_DEBIT) VALUES (%s, %s, %s)",
        "values": [
            (1, "Receita", 0),
            (2, "Investimento", 1),
            (3, "Moradia", 1),
            (4, "Alimentação", 1),
            (5, "Saúde", 1),
            (6, "Educação", 1),
            (7, "Despesas pessoais", 1),
            (8, "Transporte", 1),
            (9, "Internet/TV/Celular", 1),
            (10, "Lazer", 1),
        ],
    },
    "type_entries_subcategories": {
        "sql": "INSERT INTO type_entries_subcategories (ID, NAME, CATEGORY_ID) VALUES (%s, %s, %s)",
        "values": [
            (1, "Salário", 1),
            (2, "13º Salário", 1),
            (3, "Férias", 1),
            (4, "Renda extra", 1),
            (5, "Investimentos", 1),
            (6, "Alugueis", 1),
            (7, "Reserva de Emergência", 2),
            (8, "Prestação/Aluguel", 3),
            (9, "Condomínio", 3),
            (10, "Imposto", 3),
            (11, "Mercado", 4),
            (12, "Refeição", 4),
            (13, "Lanches", 4),
            (14, "Café da manhã", 4),
            (15, "Plano de saúde", 5),
            (16, "Farmácia", 5),
            (17, "Exames", 5),
            (18, "Mensalidades", 6),
            (19, "Materiais", 6),
            (20, "Cursos", 6),
            (21, "Livros", 6),
            (22, "Cuidado e higiene pessoal", 7),
            (23, "Roupas e acessórios", 7),
            (24, "Presentes", 7),
            (25, "Compras", 7),
            (26, "Combustível", 8),
            (27, "Manutenção", 8),
            (28, "Impostos", 8),
            (29, "Seguros", 8),
            (30, "Estacionamento", 8),
            (31, "Transporte", 8),
            (32, "Assinatura", 8),
            (33, "Passeios", 9),
            (34, "Cinema/Teatro", 9),
            (35, "Viagens", 9),
        ],
    },
    "type_pix_keys": {
        "sql": "INSERT INTO type_pix_keys (ID, TYPE) VALUES (%s, %s)",
        "values": [
            (1, "CPF"),
            (2, "CNPJ"),
            (3, "E-mail"),
            (4, "Telefone"),
            (5, "Aleatória"),
        ],
    },
    "users": {
        "sql": "INSERT INTO users (ID, USERNAME, EMAIL, PASSWORD) VALUES (%s, %s, %s, %s)",
        "values": [
            (1, os.environ.get("DEVELOPMENT_USERNAME"), os.environ.get("DEVELOPMENT_EMAIL"), os.environ.get("DEVELOPMENT_PASSWORD")),
        ],
    },
    "banks": {
        "sql": "INSERT INTO banks (ID, ID_USER, NAME, AGENCY, ACCOUNT, OBSERVATION) VALUES (%s, %s, %s, %s, %s, %s)",
        "values": [
            (1, 1, "Banco do Brasil", "0001", "0001", ""),
            (2, 1, "Bradesco", "0001", "0001", ""),
            (3, 1, "Itaú", "0001", "0001", ""),
        ],
    },
    "pix": {
        "sql": "INSERT INTO pix (ID, ID_KEY_TYPE, ID_BANK, `KEY`) VALUES (%s, %s, %s, %s)",
        "values": [
            (1, 1, 1, "12345678901"),
            (2, 3, 2, os.environ.get("DEVELOPMENT_EMAIL")),
        ],
    },
    "entries": {
        "sql": "INSERT INTO entries (ID, ID_BANK, ID_CATEGORY_TYPE, ID_SUBCATEGORY_TYPE, DATE, VALUE, OBSERVATION) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        "values": [
            (1, 1, 1, 1, date.today(), 1000.00, "Salário do mês"),
            (2, 2, 1, 2, date.today(), 750.00, "13º Salário do mês"),
            (3, 1, 3, 8, date.today(), 500.25, "Aluguel"),
            (4, 1, 8, 26, date.today(), 150, "Gasolina"),
            (5, 2, 2, None, date.today(), 500.00, "Investimento em ações"),
        ],
    }
}
