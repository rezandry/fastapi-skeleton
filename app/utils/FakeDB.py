class FakeDB:

    @classmethod
    def get_user(cls, username: str):
        FAKEDB = {
            "rezandry": {
                "username": "rezandry",
                "full_name": "Reza Andriyunanto",
                "email": "andriyunantoreza@example.com",
                "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
                "disabled": False,
            }
        }
        return FAKEDB.get(username)
