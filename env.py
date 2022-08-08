host = "data.codeup.com"
username = "leavitt_1875"
password = "Pc4PrcXnnOhMCP8HmtEMaGgKD79V8xJ6"


def get_db_url(db_name):
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'