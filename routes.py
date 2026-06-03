from fastapi import APIRouter, Query
from area import calculate_triangle_area

router = APIRouter()

@router.get("/trianglearea/")
def get_triangle_area(base: int, altezza: int) -> int:
    return calculate_triangle_area(base, altezza)