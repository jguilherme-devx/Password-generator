import secrets
import time
import string


print("\033[36m[Gerador de senhas automaticas]\033[0m")

time.sleep(0.5)
print("gerando senha...")
time.sleep(0.7)

characters = string.ascii_letters + string.digits

password = ''.join(secrets.choice(characters) for _ in range(12))

print(f"senha: {password}")
