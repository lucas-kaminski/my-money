from server.instance import server
from dotenv import load_dotenv
from routes import dashboard, auth

if __name__ == '__main__':
    load_dotenv()
    # delete route file
    with open('routes.txt', 'w') as f:
      f.write('')

    with open('routes.txt' , 'a') as f:
      for route in server.app.url_map.iter_rules():
        f.write(str(route) + '\n')

    server.run()