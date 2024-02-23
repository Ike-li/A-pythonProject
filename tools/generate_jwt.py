import uuid

import jwt

from datetime import datetime, timedelta

# jwt secret
JWT_SECRET = "LQqZ5eA9jeNfmSX4CID8YfVqm0JTLGZK0guQI9O2O5LnP5drn4tRg70lVF1GOoUy"


def generate_jwt(ttl, data: dict = None):
    """生成jwt token
    ttl: 有效时间(秒)
    """
    payload = {
        "exp": datetime.utcnow() + timedelta(seconds=ttl),
    }
    if data:
        payload.update(data)

    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    # token = jwt.encode(payload, JWT_SECRET, algorithm="HS256").decode("ascii")
    return token


if __name__ == '__main__':
    device_id = str(uuid.uuid4())
    payload = generate_jwt(
        10000,
        data={"device_id": device_id}
    )
    print(device_id)
    print(payload)
