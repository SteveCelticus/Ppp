from fastapi import FastAPI, HTTPException,Request
from mediaflow_proxy.main import app as mediaflow_app
main_app = FastAPI()

main_app.router.include_router(mediaflow_app.router)
@app.get("/wow")
  return {"message": "This is the main app"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host="0.0.0.0", port=8080)