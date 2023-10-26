public class CreditCard {
    private String cardNumber;
    private double balance;

    public CreditCard(String cardNumber, double balance) {
        this.cardNumber = cardNumber;
        this.balance = balance;
    }

    public void deposit(double amount) {
        this.balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= this.balance) {
            this.balance -= amount;
        }
    }

    public double getBalance() {
        return this.balance;
    }

    public static void main(String[] args) {
        CreditCard account = new CreditCard("4329 4032 1292 2504", 1000);
        account.deposit(500);
        account.withdraw(200);
        System.out.println(account.getBalance());
    }
}
