
import re

COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "letmein",
    "iloveyou", "welcome123"
}

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Consider adding numbers.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("Consider adding symbols.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("Choose a less predictable password.")

    if password.lower() in COMMON_PASSWORDS or len(password) < 8:
        strength = "WEAK"
    elif score >= 6 and len(password) >= 12:
        strength = "STRONG"
    elif score >= 4:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    return strength, feedback, score


def main():
    print("=" * 40)
    print("    PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    # Password will now be visible while typing
    password = input("Enter a test password: ")

    if not password:
        print("Please enter a password.")
        return

    strength, feedback, score = check_password(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Rule Score: {score}/6")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nAll configured checks passed.")

    print("\nPassword analysis complete.")


if __name__ == "__main__":
    main()
