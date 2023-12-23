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
