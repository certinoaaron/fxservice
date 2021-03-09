FROM python:3.8 as base
COPY requierments.txt /app/
WORKDIR /app/
RUN pip install -r requierments.txt

FROM base 
COPY /app /app
ENTRYPOINT ["flask" , "run" ,"--host=0.0.0.0", "--port=5100"]
