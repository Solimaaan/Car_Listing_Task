import random
from backend.state import CarState


def extract_image(state: CarState) -> CarState:
    image = state.get("image", None)

    car_type = random.choice(["sedan", "SUV", "hatchback", "coupe", "convertible"])
    
    state["output"]["car_body_type"] = car_type
    return state
