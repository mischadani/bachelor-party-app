from fastapi import Depends, APIRouter, HTTPException
from queries.charges import ChargeQueries, ChargeIn
from typing import List, Union, Optional
from pydantic import BaseModel
from authenticator import authenticator


router = APIRouter()


class Error(BaseModel):
    message: str


class Charge(BaseModel):
    id: int
    title: str
    bach_party: int
    amount: float
    description: Optional[str]
    account: int
    date: str


@router.get(
        "/api/{account_id}/charges/",
        response_model=Union[Error, List[Charge]],
        tags=["Charge"]
        )
def get_all_charges(
    account_id: int,
    account_data=Depends(authenticator.try_get_current_account_data),
    repo: ChargeQueries = Depends()
):
    if account_data:
        try:
            return repo.get_all_charges(account_id)
        except:
            raise HTTPException(status_code=404, detail="Charges Not Found")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")


@router.get(
        "/api/charges/{charge_id}/",
        response_model=Union[Error, Charge],
        tags=["Charge"]
        )
def get_charge(
    charge_id: int,
    account_data=Depends(authenticator.try_get_current_account_data),
    repo: ChargeQueries = Depends()
):
    if account_data:
        try:
            return repo.get_one_charge(charge_id)
        except:
            raise HTTPException(status_code=404, detail="Charge Not Found")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")


@router.post(
        "/api/charges/create/",
        response_model=Union[Error, Charge],
        tags=["Charge"]
        )
def create_charge(
    info: ChargeIn,
    account_data=Depends(authenticator.try_get_current_account_data),
    repo: ChargeQueries = Depends()
):
    if account_data:
        try:
            return repo.create_charge(info)
        except:
            raise HTTPException(status_code=400, detail="Could not create charge")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")


@router.put(
        "/api/{charge_id}/update/",
        response_model=Union[Error, Charge],
        tags=["Charge"]
        )
def update_charge(
    charge_id: int,
    info: ChargeIn,
    account_data=Depends(authenticator.try_get_current_account_data),
    repo: ChargeQueries = Depends()
):
    if account_data:
        try:
            return repo.update_charge(charge_id, info)
        except:
            raise HTTPException(status_code=400, detail="Could not update charge")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")


@router.delete(
    "/api/{charge_id}/delete/",
    response_model=bool,
    tags=["Charge"],
)
def delete_charge(
    charge_id: int,
    account_data: Depends(authenticator.try_get_current_account_data),
    repo: ChargeQueries = Depends(),
) -> bool:
    if account_data:
        try:
            return repo.delete_charge(charge_id)
        except:
            raise HTTPException(status_code=400, detail="Could not delete charge")
    else:
        raise HTTPException(status_code=400, detail="User not logged in")
