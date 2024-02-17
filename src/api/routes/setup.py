from fastapi import APIRouter

from . import classes


router = APIRouter()

router.include_router(classes.router, prefix="/classes")
