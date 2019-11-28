from myflex.celery import app
import time

@app.task
def prueba_suma(x, y):
    time.sleep(50)
    return x + y


@app.task
def prueba_resta(x, y):
    return x - y