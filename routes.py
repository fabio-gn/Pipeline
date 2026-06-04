from fastapi import APIRouter, Query
from area import calculate_triangle_area
import time

router = APIRouter()



@router.get("/trianglearea/")
def get_triangle_area(base: int, altezza: int):
    start = time.time()
    area = calculate_triangle_area(base, altezza)
    end = time.time()
    elapsed = end - start
    return {"area": area, "elapsed": elapsed}