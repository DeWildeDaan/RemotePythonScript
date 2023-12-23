print("Hello World")



# Execute the script:
# Passes the code to python as a string and executes it
# python3 -c "$(wget -q -O - https://raw.githubusercontent.com/DeWildeDaan/remotepythontest/main/script1.py)"

# Downloads the script, exectutes it and removes it
# wget -q https://raw.githubusercontent.com/DeWildeDaan/remotepythontest/main/script1.py && (python3 script1.py; rm script1.py)