# Projeto Sistema de Controle de Saldo Bancário

Este projeto é um pequeno sistema de controle de saldo bancário desenvolvido em Python, ideal para estudos, testes e demonstração de conceitos básicos de programação orientada a objetos, manipulação de dados e interação via console.

## Funcionalidades
- **Registrar créditos (depósitos) e débitos (saques)**
- **Consultar saldo atualizado**
- **Visualizar histórico detalhado de todas as transações**
- **Validação de operações**: não permite saques que deixem o saldo negativo nem valores não positivos
- **Interface simples via terminal**
- **Testes automáticos inclusos**

## Como funciona
O sistema apresenta um menu interativo no terminal, onde o usuário pode:
1. Depositar valores
2. Sacar valores
3. Consultar o saldo atual
4. Visualizar o histórico de transações
5. Sair do sistema

Cada transação é registrada com:
- Tipo (crédito ou débito)
- Valor
- Status (sucesso ou falha)
- Saldo após a operação

## Exemplo de uso
```
--- Sistema Bancário ---
1. Depositar
2. Sacar
3. Consultar saldo
4. Ver histórico de transações
5. Sair
Escolha uma opção: 1
Digite o valor para depósito: 100
Depósito de R$ 100.00 realizado com sucesso.

Escolha uma opção: 2
Digite o valor para saque: 50
Saque de R$ 50.00 realizado com sucesso.

Escolha uma opção: 4
Histórico de transações:
Nº  Tipo     Valor      Status   Saldo após  
---------------------------------------------
1   credit   R$ 100.00  success  R$ 100.00   
2   debit    R$ 50.00   success  R$ 50.00    
```

## Como executar
1. Clone este repositório:
   ```
   git clone https://github.com/Victorcristo/projeto_saldo_bancario.git
   cd projeto_saldo_bancario
   ```
2. Execute o arquivo principal:
   ```
   python bank_account.py
   ```

## Testes automáticos
O arquivo inclui uma função de teste simples (`test_bank_account`) que pode ser executada para validar o funcionamento da classe `BankAccount`. Basta descomentar a linha correspondente no final do arquivo para rodar os testes.

## Contato
Fique à vontade para entrar em contato para sugestões, dúvidas ou oportunidades:
- [Seu LinkedIn](https://www.linkedin.com/in/victor-cristo/)
- [Seu Email](mailto:victor.alencar.oliveira@outlook.com)

---
