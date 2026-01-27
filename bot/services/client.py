import aiohttp
from shared.config import config

class Client:
  def __init__(self, host=config.host, port=config.port):
    self.base_url = f"http://{host}:{port}"
    self.session = None
    self.header = {
      'Authorization': f'Bearer {config.app_token}',
      'Content-Type': 'application/json'
    }

  async def __aenter__(self):
    self.session = aiohttp.ClientSession()
    return self

  async def __aexit__(self, exc_type, exc, tb):
    await self.session.close()


  async def _request(self, method, endpoint, params=None, json=None):
    url = f"{self.base_url}/{endpoint}"
    
    async with self.session.request(
      method=method, 
      url=url, 
      params=params, 
      json=json, 
      headers=self.header
    ) as request:
      return await request.json()


  async def get_user_data(self, user_id) -> dict:
    return await self._request("GET", "user", params={"user_id": user_id})

  async def upload_file(self, file_url, file_name, user_id) -> dict:
    return await self._request("POST", "upload", json={
      "file_url": file_url,
      "file_name": file_name,
      "user_id": user_id
    })

  async def delete_file(self, file_id, user_id) -> dict:
    return await self._request("DELETE", "delete", json={
      "file_id": file_id,
      "user_id": user_id
    })


client = Client()
