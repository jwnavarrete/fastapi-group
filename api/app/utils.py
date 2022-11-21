from passlib.context import CryptContext
from pytz import timezone
from datetime import datetime
UTC = timezone('UTC')


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password : str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    