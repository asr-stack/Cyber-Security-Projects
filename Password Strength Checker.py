import re

def check_password_strength(password):
    score = 0
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"[0-9]", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    # Calculate score (each satisfied condition adds 1 point)
    score = sum(strength_criteria.values())

    # Determine strength level
    if score == 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    return strength, strength_criteria

# User input
password = input("Enter a password: ")
strength, criteria = check_password_strength(password)

# Display results
print(f"Password Strength: {strength}")
print("Criteria Check:")
for key, value in criteria.items():
    print(f"- {key.capitalize()}: {'✔️' if value else '❌'}")
