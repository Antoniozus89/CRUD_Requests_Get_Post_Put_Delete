from fastapi import FastAPI, HTTPException, Path
from typing import Dict

app = FastAPI()


users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}



@app.get('/users')
async def get_users():
    return users



@app.post('/user/{username}/{age}')
async def add_user(
        username: str = Path(..., min_length=5, max_length=20, description="Enter username", example="UrbanUser"),
        age: int = Path(..., ge=18, le=120, description="Enter age", example=24)
):

    new_id = str(max(map(int, users.keys()), default=0) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_id} is registered"



@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: str = Path(..., description="Enter User ID", example="1"),
        username: str = Path(..., min_length=5, max_length=20, description="Enter username", example="UrbanProfi"),
        age: int = Path(..., ge=18, le=120, description="Enter age", example=28)
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} has been updated"



@app.delete('/user/{user_id}')
async def delete_user(
        user_id: str = Path(..., description="Enter User ID", example="2")
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    del users[user_id]
    return f"User {user_id} has been deleted"


