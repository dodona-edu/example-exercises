Schrijf een klasse `BankAccount` die een bankrekening voorstelt.

Een nieuwe rekening heeft een saldo van 0. De klasse moet het volgende ondersteunen:

- Een methode `Deposit(int amount)` die het bedrag bij het saldo optelt.
- Een methode `Withdraw(int amount)` die het bedrag van het saldo aftrekt.
- Een eigenschap `Balance` die het huidige saldo teruggeeft.

### Voorbeeld

```console?lang=csharp&prompt=>
> var account = new BankAccount();
> account.Deposit(100);
> account.Withdraw(30);
> account.Balance
70
```
