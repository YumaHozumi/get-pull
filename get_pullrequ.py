import requests
from settings import *
import json
from sqlalchemy.orm import sessionmaker
from database import engine
from models import PullReq, Base

SessionClass = sessionmaker(bind=engine)  # セッションを作るクラスを作成
session = SessionClass()
Base.metadata.create_all(engine)

url = "https://api.github.com/repos/{}/{}/pulls?state=open&sort=updated&direction=desc".format(OWNER, REPOSITORY)
headers = {"content-type": "application/json"}
res = requests.get(url, headers)
datas = res.json()
# print(data[0]["id"])
for data in datas:
    req = session.query(PullReq).filter(PullReq.pullreq_id == data["id"]).first()
    if not req:
        pull = PullReq(pullreq_id=data["id"])
        session.add(pull)
        session.commit()
    else: print("test")

# print(json.dumps(data, indent=4))
session.close()