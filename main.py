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

app = create_app()

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=8012)