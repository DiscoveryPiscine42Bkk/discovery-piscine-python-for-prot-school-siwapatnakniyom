# i_got_that.py

def main():
    while True:
        user_input = input("Enter something (or type 'STOP' to quit): ")
        if user_input.upper() == "STOP":
            print("Stopping the program. Goodbye!")
            break
        else:
            print(f"You said: {user_input}")

if __name__ == "__main__":
    main()
