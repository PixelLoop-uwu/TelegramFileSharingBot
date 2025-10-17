import aiohttp

from config import config

data = {
  "user_id": 6058443893,
  "files_data": [
  {
    "id": "n1kL2aP-9xYzQ-M64gh-k7P",
    "fullname": "goida.zip",
    "size": 113,
    "upload_date": [13, 10, 2025, 23, 56],
    "download_link": "",
    "downloads": 1
  },
  {
    "id": "a7Hk9Bq-4wErT-X12mn-p3R",
    "fullname": "project_alpha.zip",
    "size": 256,
    "upload_date": [12, 10, 2025, 18, 22],
    "download_link": ""
  },
  {
    "id": "z8Lp3Ck-7vUtY-Q89gh-l5F",
    "fullname": "images_pack.zip",
    "size": 512,
    "upload_date": [11, 10, 2025, 15, 10],
    "download_link": ""
  },
  {
    "id": "m5Rn7Dx-1yIoP-W23jk-r9T",
    "fullname": "docs_archive.zip",
    "size": 128,
    "upload_date": [10, 10, 2025, 9, 45],
    "download_link": ""
  },
  {
    "id": "f2Qb6Vs-8xRyL-A56mn-u4E",
    "fullname": "backup_2025.zip",
    "size": 1024,
    "upload_date": [9, 10, 2025, 20, 30],
    "download_link": ""
  },
  {
    "id": "k9Pn3Gh-2wQrT-B78lk-v1D",
    "fullname": "assets_pack.zip",
    "size": 350,
    "upload_date": [8, 10, 2025, 11, 5],
    "download_link": ""
  },
  {
    "id": "r1Mx4Ty-5eUiP-C90gh-m8N",
    "fullname": "music_library.zip",
    "size": 640,
    "upload_date": [7, 10, 2025, 14, 12],
    "download_link": ""
  },
  {
    "id": "b3Vk8Zj-9tRoL-D12mn-q2P",
    "fullname": "video_pack.zip",
    "size": 2048,
    "upload_date": [6, 10, 2025, 17, 50],
    "download_link": ""
  },
  {
    "id": "h6Ly2Jp-4uEiQ-E34kl-r7M",
    "fullname": "fonts_archive.zip",
    "size": 75,
    "upload_date": [5, 10, 2025, 10, 0],
    "download_link": ""
  },
  {
    "id": "t8Xo5Np-7yUrS-F56gh-z3K",
    "fullname": "scripts_pack.zip",
    "size": 180,
    "upload_date": [4, 10, 2025, 21, 15],
    "download_link": ""
  },
  {
    "id": "j4Ck9Vt-2pIoR-G78mn-x9H",
    "fullname": "textures.zip",
    "size": 300,
    "upload_date": [3, 10, 2025, 13, 40],
    "download_link": ""
  },
  {
    "id": "w7Pk1Qj-6rTyL-H90kl-y2B",
    "fullname": "templates.zip",
    "size": 220,
    "upload_date": [2, 10, 2025, 16, 5],
    "download_link": ""
  }
]
}

class client:
  def __init__(self, host = "127.0.0.1", port = config.api_port):
    self.port = port
    self.host = host

  async def get_user_files(self, user_id: int) -> dict:
    return data


  async def upload_file(self, file_id: str, chat_id: str, user_id: str) -> None:
    ...

  async def delete_file(self, file_id: str, user_id: str) -> bool | str:
    return True