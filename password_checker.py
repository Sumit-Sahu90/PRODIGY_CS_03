import re

def assess_password_strength(password):
    """Evaluate password strength and provide feedback"""
    
    strength_score = 0
    feedback = []
    
    # Criteria checks
    length = len(password)
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^a-zA-Z0-9]', password))
    common_patterns = bool(re.search(r'(123|abc|qwerty|password|admin)', password.lower()))
    
    # Length evaluation
    if length >= 16:
        strength_score += 3
        feedback.append("✓ Excellent length (16+ characters)")
    elif length >= 12:
        strength_score += 2
        feedback.append("✓ Good length (12-15 characters)")
    elif length >= 8:
        strength_score += 1
        feedback.append("✓ Minimum acceptable length (8-11 characters)")
    else:
        feedback.append("✗ Too short (minimum 8 characters required)")
    
    # Character diversity evaluation
    if has_lower:
        strength_score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")
    
    if has_upper:
        strength_score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")
    
    if has_digit:
        strength_score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    if has_special:
        strength_score += 2
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters (recommended)")
    
    # Penalty for common patterns
    if common_patterns:
        strength_score -= 2
        feedback.append("✗ Contains common patterns (weakens password)")
    
    # Determine strength level
    if strength_score >= 8:
        strength = "Very Strong"
        color = "\033[92m"  # Green
    elif strength_score >= 6:
        strength = "Strong"
        color = "\033[94m"  # Blue
    elif strength_score >= 4:
        strength = "Moderate"
        color = "\033[93m"  # Yellow
    elif strength_score >= 2:
        strength = "Weak"
        color = "\033[33m"  # Orange
    else:
        strength = "Very Weak"
        color = "\033[91m"  # Red
    
    # Additional entropy calculation (bits)
    char_variety = 0
    if has_lower: char_variety += 26
    if has_upper: char_variety += 26
    if has_digit: char_variety += 10
    if has_special: char_variety += 32  # Approximate common special chars
    
    if char_variety > 0:
        entropy = length * (char_variety ** 0.5)  # Simplified entropy estimation
        feedback.append(f"Estimated entropy: ~{int(entropy)} bits")
    
    return {
        'strength': strength,
        'score': strength_score,
        'feedback': feedback,
        'color': color
    }

def display_results(assessment):
    """Display the assessment results with formatting"""
    print("\nPassword Strength Assessment")
    print("----------------------------")
    print(f"{assessment['color']}Strength: {assessment['strength']} ({assessment['score']}/10)\033[0m")
    print("\nDetailed Feedback:")
    for item in assessment['feedback']:
        if item.startswith("✓"):
            print(f"\033[92m{item}\033[0m")  # Green for positive
        elif item.startswith("✗"):
            print(f"\033[91m{item}\033[0m")  # Red for negative
        else:
            print(item)
    print("\033[93mNote: This is a basic assessment. For critical accounts, use longer passphrases.\033[0m")

def main():
    print("Password Strength Evaluator")
    print("--------------------------")
    print("This tool assesses your password based on:")
    print("- Length (minimum 8 characters)")
    print("- Use of uppercase and lowercase letters")
    print("- Inclusion of numbers and special characters")
    print("- Avoidance of common patterns\n")
    
    while True:
        password = input("Enter password (input visible, be cautious): ")
        if not password:
            print("Password cannot be empty. Try again.")
            continue
        
        confirm = input("Confirm password: ")
        if password != confirm:
            print("Passwords don't match. Try again.")
            continue
        
        break
    
    assessment = assess_password_strength(password)
    display_results(assessment)

if __name__ == "__main__":
    main()