#!/usr/bin/env python3
"""
File: bank_account.py
Description: Defines the BankAccount class for a simple banking system.
"""

class BankAccount:
    """
    A simple class representing a bank account.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with a starting balance.

        Args:
            initial_balance (float): The initial balance for the account (default is 0).
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        # Encapsulation: Using a private-like attribute (conventionally denoted by _)
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        # Format the balance to two decimal places for currency
        print(f"Current Balance: ${self._account_balance:.2f}")

#!/usr/bin/env python3
"""
File: main-0.py
Description: Interfaces with the BankAccount class using command line arguments
             to perform banking operations (deposit, withdraw, display).
"""
import sys
# Import the BankAccount class from the bank_account.py file
from bank_account import BankAccount

def main():
    """
    Main function to parse command-line arguments and perform banking operations.
    """
    # Create a BankAccount instance with an example starting balance
    # Set to 100 as per the original prompt for testing
    account = BankAccount(100.00)

    # 1. Check for minimum arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display (display does not require <amount>)")
        sys.exit(1)

    # 2. Parse the command argument (e.g., "deposit:50" or "display")
    arg_parts = sys.argv[1].split(':')
    command = arg_parts[0].lower()
    
    # Extract amount if it exists
    amount = None
    if len(arg_parts) > 1:
        try:
            # Convert the amount part to a float
            amount = float(arg_parts[1])
        except ValueError:
            print(f"Error: Amount '{arg_parts[1]}' must be a valid number.")
            sys.exit(1)

    # 3. Perform the requested operation
    if command == "deposit" and amount is not None:
        if amount > 0:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")
            
    elif command == "withdraw" and amount is not None:
        if amount > 0:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Error: Withdrawal amount must be positive.")

    elif command == "display":
        if amount is not None: # Check if an unexpected amount was provided for 'display'
             print("Warning: The 'display' command does not take an amount.")
        account.display_balance()
        
    else:
        # Catch cases like "deposit" without ":amount", or an invalid command
        if command in ["deposit", "withdraw"] and amount is None:
            print(f"Error: Command '{command}' requires an amount (e.g., {command}:50).")
        else:
            print(f"Invalid command: {command}")
            print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()        