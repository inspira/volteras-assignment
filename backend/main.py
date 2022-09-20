from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/vehicle_data")
async def vehicle_data():
    return [
              { "id": 1, "timestamp": "2022-07-10 15:00:00.000", "speed": 36, "odometer": 10666, "soc": 34, "elevation": 972, "shift_state": "D" },
              { "id": 2, "timestamp": "2022-08-10 07:33:01.000", "speed": None, "odometer": 23435, "soc": 76, "elevation": 232, "shift_state": None }
            ]
