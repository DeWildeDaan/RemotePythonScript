print("Hello World")



# Execute the script:
# Passes the code to python as a string and executes it
# python3 -c "$(wget -q -O - https://raw.githubusercontent.com/DeWildeDaan/remotepythontest/main/test.py)"

# Downloads the script, exectutes it and removes it
# wget https://raw.githubusercontent.com/DeWildeDaan/remotepythontest/main/test.py && (python3 test.py; rm test.py)