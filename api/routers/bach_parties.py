from fastapi import (
    Depends,
    Response,
    APIRouter,
)
from authenticator import authenticator
from typing import List, Union, Optional
from queries.trips import (
    TripIn,
    TripOut,
    TripQueries,
    Error,
)
