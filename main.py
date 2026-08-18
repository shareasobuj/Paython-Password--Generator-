import random
import string

def generate_password(length=12):
    """নির্দিষ্ট দৈর্ঘ্যের একটি র্যান্ডম পাসওয়ার্ড তৈরি করার ফাংশন"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Random Password Generator ---")
    try:
        user_length = int(input("পাসওয়ার্ড কত অক্ষরের চান? (Default 12): ") or 12)
        new_password = generate_password(user_length)
        print(f"আপনার নতুন পাসওয়ার্ড: {new_password}")
    except ValueError:
        print("অনুগ্রহ করে একটি সঠিক সংখ্যা লিখুন।")
