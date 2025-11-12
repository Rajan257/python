# from typing import List,Union,Tuple

# n : int = 5

# name: str = "Rajan"

# def sum(a:int, b:int)->int:
#     return a+b




from typing import Union, Tuple, List, Optional, Annotated, TypeAlias

# --- Type Aliases for better readability ---
UserID: TypeAlias = Union[int, str]
Point3D: TypeAlias = Tuple[float, float, float]
ScoreList: TypeAlias = List[int]

# --- Variables with Annotations ---
user_id: UserID = "user_123"
coordinates: Point3D = (10.5, 20.0, -5.5)
scores: ScoreList = [85, 92, 78]

# --- Annotated variable (adds metadata) ---
age: Annotated[int, "Must be non-negative"] = 21

# --- Optional type (can be int or None) ---
middle_name: Optional[str] = None

# --- A function that returns the full name ---
def get_full_name(first_name: str, last_name: str, middle: Optional[str] = None) -> str:
    if middle:
        return f"{first_name} {middle} {last_name}"
    return f"{first_name} {last_name}"

# --- Function using Tuple and List ---
def average_scores(scores: List[int]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

# --- Function using Union return type ---
def find_user_score(user_id: UserID) -> Union[int, str]:
    # Simulate lookup
    if user_id == "user_123" or user_id == 123:
        return 90
    else:
        return "User not found"

# --- Function using a Tuple return ---
def get_user_location(user_id: UserID) -> Tuple[float, float]:
    # Just returning dummy lat/lng
    return (28.6139, 77.2090)  # Delhi, India

# --- Function using Annotated types ---
def increase_age(user_age: Annotated[int, "Must be non-negative"]) -> int:
    return user_age + 1

# --- Main Program ---
if __name__ == "__main__":
    print("User ID:", user_id)
    print("Coordinates:", coordinates)
    print("Scores:", scores)
    print("Average Score:", average_scores(scores))

    full_name = get_full_name("Rajan", "Rai", middle_name)
    print("Full Name:", full_name)

    score = find_user_score(user_id)
    print("User Score:", score)

    location = get_user_location(user_id)
    print("User Location (Lat, Long):", location)

    new_age = increase_age(age)
    print("Age next year:", new_age)
