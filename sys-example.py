import sys

# Print the Python version
print(f"Python version: {sys.version}")

# Print the platform
print(f"Platform: {sys.platform}")

# Print command-line arguments
print("Command-line arguments:")
for arg in sys.argv:
    print(arg)

# Check if an argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <argument>")
    sys.exit(1)

# Process the argument
argument = sys.argv[1]
print(f"Received argument: {argument}")

# Use standard output
sys.stdout.write("Hello, World!\n")
