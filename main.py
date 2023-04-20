if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    import pyotp

    load_dotenv()

    base32secret = os.getenv('SECRET')
    totp = pyotp.TOTP(base32secret)

    print(os.getenv('PIN') + totp.now())
