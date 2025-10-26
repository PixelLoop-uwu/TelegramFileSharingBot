import aiohttp
from config import config

class Client:
  def __init__(self, host="127.0.0.1", port=config.api_port):
    self.base_url = f"http://{host}:{port}"
    self.session = None

  async def __aenter__(self):
    self.session = aiohttp.ClientSession()
    return self

  async def __aexit__(self, exc_type, exc, tb):
    await self.session.close()


  async def _request(self, method, endpoint, params=None, json=None):
    url = f"{self.base_url}/{endpoint}"
    
    async with self.session.request(method=method.upper(), url=url, params=params, json=json) as request:
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
