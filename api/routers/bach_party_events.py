from fastapi import Depends, APIRouter, HTTPException
from queries.bach_party_events import BachPartyEventIn, BachPartyEventQueries
from typing import List, Union
from pydantic import BaseModel
from authenticator import authenticator


router = APIRouter()


class Error(BaseModel):
    message: str


class BachPartEvent(BaseModel):
    event_name: str
    description: str
    location: str
    event_date: str
    start_time: str
    end_time: str
    picture_url: str
    bach_party: str
    id: str


@router.get(
        "/api/{bach_party_id}/bach_party_events/",
        response_model=Union[Error, List[BachPartEvent]],
        tags=["BachPartEvent"]
        )
def get_all_bach_party_events(
    bach_party_id: int,
    account_data=Depends(authenticator.try_get_current_account_data),
    repo: BachPartyEventQueries = Depends()
):
    if account_data:
        try:
            return repo.get_all_bach_party_events(bach_party_id)
        except:
            raise HTTPException(status_code=404, detail="Bach Party Not Found")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")


@router.get(
        "/api/bach_party_events/{bach_party_event_id}/",
        response_model=Union[Error, BachPartEvent],
        tags=["BachPartEvent"]
        )
def get_bach_party_event(
    bach_party_event_id: int,
    account_data=Depends(authenticator.try_get_current_account_data),
    repo: BachPartyEventQueries = Depends()
):
    if account_data:
        try:
            return repo.get_bach_party_events(bach_party_event_id)
        except:
            raise HTTPException(status_code=404, detail="Bach Party Event Not Found")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")


@router.post(
        "/api/bach_party_events/create/",
        response_model=Union[Error, BachPartEvent],
        tags=["BachPartEvent"]
        )
def create_party_event(
    info: BachPartyEventIn,
    account_data=Depends(authenticator.try_get_current_account_data),
    repo: BachPartyEventQueries = Depends()
):
    if account_data:
        try:
            return repo.create_bach_party_event(info)
        except:
            raise HTTPException(status_code=400, detail="Could not create bach party event")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")


@router.put(
        "/api/{bach_party_event_id}/update/",
        response_model=Union[Error, BachPartEvent],
        tags=["BachPartEvent"]
        )
def update_party_event(
    bach_party_event_id: int,
    info: BachPartyEventIn,
    account_data=Depends(authenticator.try_get_current_account_data),
    repo: BachPartyEventQueries = Depends()
):
    if account_data:
        try:
            return repo.update_bach_party_events(info, bach_party_event_id)
        except:
            raise HTTPException(status_code=400, detail="Could not update bach party event")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")


@router.delete(
    "/api/{bach_party_event_id}/delete/",
    response_model=bool,
    tags=["BachPartEvent"],
)
def delete_favorite(
    bach_party_event_id: int,
    account_data: Depends(authenticator.try_get_current_account_data),
    repo: BachPartyEventQueries = Depends(),
) -> bool:
    if account_data:
        try:
            return repo.delete_bach_party_event(bach_party_event_id)
        except:
            raise HTTPException(status_code=400, detail="Could not delete bach party event")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")
