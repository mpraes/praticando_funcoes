import sys

if len(sys.argv) >= 3:
    script = sys.argv[0]
    encoding = sys.argv[1]
    error = sys.argv[2]
else:
    print("Este script precisa de pelo menos três argumentos.")
