# from fastapi import FastAPI, Response
#
# # I like to launch directly and not use the standard FastAPI startup
# import uvicorn
#
#
# app = FastAPI()
#
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World, from Eplanner_user!"}
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8012)
from app import create_app
from app import db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8012, debug=True)