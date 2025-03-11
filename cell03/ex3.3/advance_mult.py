# advanced_mult.py

def display_multiplication_table(n):
    """Displays the multiplication table for a given number n."""
    print(f"Multiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()  # Blank line after each table for better readability

def main():
    while True:
        try:
            start = int(input("Enter the starting number for tables (or type 'STOP' to quit): "))
            end = int(input("Enter the ending number for tables: "))
            
            # Validate the range input
            if start < 1 or end < 1 or start > end:
                print("Invalid range! Ensure start <= end and both are positive.")
                continue

            for num in range(start, end + 1):
                display_multiplication_table(num)
            break  # Exit after displaying the tables

        except ValueError:
            user_input = input("Invalid input! Type 'STOP' to quit or any other key to retry: ")
            if user_input.strip().upper() == 'STOP':
                print("Stopping the program. Goodbye!")
                break

if __name__ == "__main__":
    main()
