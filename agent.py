import sys
from llama_integration import parse_command
from chain_handler import execute_command

# Ambil command dari argument CLI
if len(sys.argv) > 1:
    command = sys.argv[1]
else:
    print("⚠️ Tidak ada perintah yang diberikan.")
    sys.exit(1)

# Parsing menggunakan LLaMA
parsed_command, command_type = parse_command(command)

# Eksekusi command menggunakan handler yang sesuai
result = execute_command(command_type, parsed_command)

# Output hasil eksekusi
print(f"📋 Command Type: {command_type}")
print(f"🔍 Executed: {parsed_command}")
print(f"\n✅ Result:\n{result}")