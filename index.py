
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
            user = User(name=user_data.name, 
                        last_name=user_data.last_name, 
                        age=user_data.numbers,
                        addres=user_data.addres)
            
        new_user = session.add(user)
        session.commit()
        print(new_user)
        return jsonify({"user":new_user})
    except:
        return jsonify({"error":"No fue posible crear el usuario"})
    
@app.route("/users/<int:user_id>", methods=["GET"])
async def get_user(user_id):
    user_data = request.json

    try:
        with get_session() as session:
            user = session.query(User).filter(User.id == user_id)
     

        return jsonify({"user":user})
    except:
        return jsonify({"error":"No fue posible encontrar al usuario"})
    
if __name__ == "__main__": #No estoy segura
    app.run()