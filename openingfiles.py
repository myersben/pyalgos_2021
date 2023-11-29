#This will open the readme.txt file safely with exception handeling if FileNotFoundError occurs
try:
    with open('README.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The program could not locate the file 'README.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")
