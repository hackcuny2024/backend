from fastapi import APIRouter

from . import classes, classmates, messages


router = APIRouter()

router.include_router(classes.router, prefix="/classes")
router.include_router(classmates.router, prefix="/classmates")
router.include_router(messages.router, prefix="/messages")
