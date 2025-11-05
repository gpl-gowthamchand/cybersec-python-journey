# Separate safe and unsafe passwords from a list (safe if length ≥ 8).

passwords = ["1234", "guest123", "rootpass", "hello", "admin2025"]

safe_passwords = []
unsafe_passwords = []

for pwd in passwords:
    if len(pwd) >= 8:
        safe_passwords.append(pwd)
    else:
        unsafe_passwords.append(pwd)


print(f"Safe passwords: {safe_passwords}")
print(f"Unsafe passwords: {unsafe_passwords}")


''' oneline version

safe = [p for p in passwords if len(p) >= 8]
unsafe = [p for p in passwords if len(p) < 8]

''' 