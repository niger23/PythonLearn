import datetime

def log(res, data):
    now = datetime.datetime.now()
    file = open('Seminars/Seminar009/bot_calc/db.csv', 'a')
    file.write(f'{now} users input: {res} and get: {data} \n')
    file.close()