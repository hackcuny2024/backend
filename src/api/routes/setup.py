from fastapi import APIRouter

from . import classes, messages


router = APIRouter()

router.include_router(classes.router, prefix="/classes")
router.include_router(messages.router, prefix="/messages")
