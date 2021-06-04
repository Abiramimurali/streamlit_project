FROM python:3.9
COPY . .
RUN pip install --no-cache-dir pandas 
RUN pip install --no-cache-dir pymongo 
RUN pip install --no-cache-dir Pillow 
RUN pip install --no-cache-dir numpy 
RUN pip install --no-cache-dir streamlit 
RUN pip install --no-cache-dir plotly
RUN pip install  --no-cache-dir pymongo[srv]
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]

