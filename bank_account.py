"""
Sistema de Controle de Saldo Bancário
-------------------------------------
Permite registrar débitos e créditos, consultar saldo e histórico de transações.
"""
from typing import List, Dict

class BankAccount:
    """
    Classe que representa uma conta bancária simples.
    """
    def __init__(self):
        # Saldo inicial da conta
        self.balance: float = 0.0
        # Lista de dicionários para armazenar o histórico de transações
        self.transactions: List[Dict] = []