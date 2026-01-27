from fastapi import Header, HTTPException
from shared.config import config

def admin_check(authorization: str = Header(...)):
  try:
    token = authorization.split(" ")[1] 
  except IndexError:
    raise HTTPException(401, "Invalid authorization header")

  if token != config.app_token:
    raise HTTPException(403, "No")
  return token