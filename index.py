from flask import Flask, request, jsonify
from model import get_session, User

app = Flask(__name__)

@app.get("/")
async def server_read():
    return "Hola Aarón"

@app.route("/users", methods=["POST"])
async def create_user():
    user_data = request.json

    try:
        with get_session() as session:
            user = User(**user_data) 
            
            session.add(user)
            session.commit()

            return jsonify({"user": {
                "id": user.id,
                "name": user.name,
                "last_name": user.last_name
            }}), 201
        
    except Exception as e:
        return jsonify({"error":"No fue posible crear el usuario"}), 500
    
@app.route("/users/<int:user_id>", methods=["GET", "POST"])
async def get_user(user_id):
    print(user_id)
    try:

        with get_session() as session:
            user = session.query(User).filter(User.id == user_id).one_or_none()
            print(user)
        return jsonify({"user": {
            "id": user.id,
            "name": user.name,
            "last_name": user.last_name,
            "numbers": user.numbers,
            "address": user.address
        }}), 20
    
    except:
        return jsonify({"error":"No fue posible encontrar al usuario"}), 404
    
if __name__ == "__main__": #No estoy segura
    app.run()