"""A small factory that builds create/list/get routes for a SQLModel table.

Keeps the per-resource route modules DRY while leaving room for each to add
bespoke endpoints (e.g. stage transitions, payment) on top.
"""

from typing import TypeVar

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, SQLModel, select

from ..database import get_session

ModelT = TypeVar("ModelT", bound=SQLModel)


def build_crud_router(
    model: type[ModelT],
    create_schema: type[SQLModel],
    *,
    prefix: str,
    tag: str,
) -> APIRouter:
    """Return a router exposing POST (create), GET list, and GET by id for `model`.

    `create_schema` is the non-table input model used as the request body.
    """
    router = APIRouter(prefix=prefix, tags=[tag])

    @router.post("", response_model=model, status_code=status.HTTP_201_CREATED)
    def create(item: create_schema, session: Session = Depends(get_session)) -> ModelT:  # type: ignore[valid-type]
        record = model.model_validate(item)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record

    @router.get("", response_model=list[model])
    def list_all(
        offset: int = 0,
        limit: int = 100,
        session: Session = Depends(get_session),
    ) -> list[ModelT]:
        return session.exec(select(model).offset(offset).limit(limit)).all()

    @router.get("/{item_id}", response_model=model)
    def get_one(item_id: int, session: Session = Depends(get_session)) -> ModelT:
        record = session.get(model, item_id)
        if record is None:
            raise HTTPException(status_code=404, detail=f"{model.__name__} {item_id} not found")
        return record

    return router
