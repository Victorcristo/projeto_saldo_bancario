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
    
    def get_balance(self) -> float:
        """
        Retorna o saldo atual da conta.
        """
        return self.balance

    def get_transactions(self) -> List[Dict]:
        """
        Retorna o histórico de transações da conta.
        :return: Lista de dicionários com as transações
        """
        return self.transactions
    

def main():
    """
    Função principal do sistema bancário.
    Cria uma conta, exibe o menu e processa as escolhas do usuário.
    """
    account = BankAccount()
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar saldo")
        print("4. Ver histórico de transações")
        print("5. Sair")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            try:
                amount = float(input("Digite o valor para depósito: "))
                account.deposit(amount)
            except ValueError:
                print("Valor inválido. Digite um número.")
        elif choice == '2':
            try:
                amount = float(input("Digite o valor para saque: "))
                account.withdraw(amount)
            except ValueError:
                print("Valor inválido. Digite um número.")
        elif choice == '3':
            print(f"Saldo atual: R$ {account.get_balance():.2f}")
        elif choice == '4':
            print("\nHistórico de transações:")
            trans = account.get_transactions()
            if not trans:
                print("Nenhuma transação registrada.")
            else:
                print(f"{'Nº':<3} {'Tipo':<8} {'Valor':<10} {'Status':<8} {'Saldo após':<12}")
                print("-" * 45)
                for idx, t in enumerate(trans, 1):
                    print(f"{idx:<3} {t['type']:<8} R$ {t['amount']:<8.2f} {t['status']:<8} R$ {t['balance_after']:<10.2f}")
        elif choice == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()