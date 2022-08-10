from typing import List
import os
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

#from . import models, schemas
#from .database import SessionLocal, engine

import models, schemas
from database import SessionLocal, engine

import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    #app.run(host="0.0.0.0")
    print("Running " + os.getenv("CDSW_IP_ADDRESS") + ":" + os.getenv("CDSW_PUBLIC_PORT") )
    uvicorn.run("main:app",reload=False, host="127.0.0.1", port=int(os.getenv("CDSW_PUBLIC_PORT")))  

    
    
@app.get("/")
def main():
    print("Running " + os.getenv("CDSW_IP_ADDRESS") + ":" + os.getenv("CDSW_PUBLIC_PORT") )

#    return RedirectResponse(url="/docs/")


@app.get("/records/", response_model=List[schemas.Record])
def show_records(db: Session = Depends(get_db)):
    records = db.query(models.Record).all()
    return records