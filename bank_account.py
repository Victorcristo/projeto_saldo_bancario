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
        
    def deposit(self, amount: float) -> None:
        """
        Realiza um depósito na conta.
        :param amount: Valor a ser depositado (deve ser positivo)
        """
        if amount <= 0:
            # Não permite depósito de valores não positivos
            self.transactions.append({
                "type": "credit",
                "amount": amount,
                "status": "failed",
                "balance_after": self.balance
            })
            print("Valor de depósito deve ser positivo.")
            return
        self.balance += amount
        self.transactions.append({
            "type": "credit",
            "amount": amount,
            "status": "success",
            "balance_after": self.balance
        })
        print(f"Depósito de R$ {amount:.2f} realizado com sucesso.")
    
    def withdraw(self, amount: float) -> bool:
        """
        Realiza um saque na conta.
        :param amount: Valor a ser sacado (deve ser positivo)
        :return: True se o saque foi realizado, False caso contrário
        """
        if amount <= 0:
            self.transactions.append({
                "type": "debit",
                "amount": amount,
                "status": "failed",
                "balance_after": self.balance
            })
            print("Valor de saque deve ser positivo.")
            return False
        if amount > self.balance:
            # Não permite saque que deixe saldo negativo
            self.transactions.append({
                "type": "debit",
                "amount": amount,
                "status": "failed",
                "balance_after": self.balance
            })
            print("Saldo insuficiente para saque.")
            return False
        self.balance -= amount
        self.transactions.append({
            "type": "debit",
            "amount": amount,
            "status": "success",
            "balance_after": self.balance
        })
        print(f"Saque de R$ {amount:.2f} realizado com sucesso.")
        return True