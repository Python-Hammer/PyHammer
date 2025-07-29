from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.select_unit import router as select_unit_router
from routers.unit_info import router as unit_info_router

app = FastAPI()


app.include_router(select_unit_router)
app.include_router(unit_info_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
