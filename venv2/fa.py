from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get('/python_req_1')
def python_req_1(name: str = None, age: int = None, salary: float = None, car: str = None):
    result = {
        'user_name': name,
        'user_age': age,
        'user_salary': salary,
        'user_car': car
    }

    return JSONResponse(content=result)

@app.route('/python_req_2', methods = ['GET', 'POST'])
async def python_req_2(request: Request):
    if request.method == 'GET':
        model = request.query_params.get('model')
        title = request.query_params.get('title')
        price = int(request.query_params.get('price')) + 10000
        options = request.query_params.get('options')
        
        result = {
            'car_model': model,
            'car_title': title,
            'car_price': price,
            'car_options': options
        }

    elif request.method == 'POST':
        data = await request.form()
        model = data.get('model')
        title = data.get('title')
        price = int(data.get('price')) + 100000
        options = data.get('options')
        
        result = {
            'car_model': model,
            'car_title': title,
            'car_price': price,
            'car_options': options
        }

    return JSONResponse(content=result, status_code=288)


if __name__ == '__main__':
    uvicorn.run("fa:app", host="0.0.0.0", port=5005)