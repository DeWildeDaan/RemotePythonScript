import argparse

def main(required_arg, optional_arg=None):
    print(f"Required argument: {required_arg}")
    
    if optional_arg is not None:
        print(f"Optional argument: {optional_arg}")
    else:
        print("Optional argument not provided")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script with a required and an optional argument.")
    
    # Adding required argument
    parser.add_argument("required_arg", type=str, help="This argument is required.")
    
    # Adding optional argument
    parser.add_argument("--optional_arg", type=str, help="This argument is optional.")
    
    args = parser.parse_args()
    
    # Calling the main function with arguments
    main(args.required_arg, args.optional_arg)


# Execute the script:
# Passes the code to python as a string and executes it
# python3 -c "$(wget -q -O - https://raw.githubusercontent.com/DeWildeDaan/remotepythontest/main/script2.py)" value1 --optional_arg value2

# Downloads the script, exectutes it and removes it
# wget -q https://raw.githubusercontent.com/DeWildeDaan/remotepythontest/main/script2.py && (python3 script2.py value1 --optional_arg value2; rm script2.py)