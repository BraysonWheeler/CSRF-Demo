import jwt

secret = "secret123"
algo = "HS256"

def generate_jwt():
   return (jwt.encode({"id": "1"}, "secret123", algorithm=algo))

def validate_jwt(_jwt):
    try:
        jwt.decode(_jwt, secret , algorithms=[algo])
        return True
    except Exception as e:
        print(e)
        return False
    
def get_jwt_id(_jwt):
    try:
        decode = jwt.decode(_jwt, secret , algorithms=[algo])
        return decode["id"]
        
    except Exception as e:
        print(e)
        return False