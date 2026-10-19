Write a class `BankAccount` that models a bank account.

A new account has a balance of 0. The class should support the following:

- A method `Deposit(int amount)` which adds the amount to the balance.
- A method `Withdraw(int amount)` which subtracts the amount from the balance.
- A property `Balance` which returns the current balance.

### Example

```console?lang=csharp&prompt=>
> var account = new BankAccount();
> account.Deposit(100);
> account.Withdraw(30);
> account.Balance
70
```
