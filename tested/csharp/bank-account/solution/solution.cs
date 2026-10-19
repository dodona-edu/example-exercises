public class BankAccount
{
    public int Balance { get; private set; }

    public void Deposit(int amount)
    {
        Balance += amount;
    }

    public void Withdraw(int amount)
    {
        Balance -= amount;
    }
}
