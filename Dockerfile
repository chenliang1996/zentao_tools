FROM harbor.local.kbd.com/cloud_atlas_base/python:v3.9
COPY . /zentao_tools
WORKDIR /zentao_tools
RUN /usr/local/python3/bin/python3.9 -m pip install --upgrade pip -i http://172.16.240.8/pypi/simple/ --trusted-host 172.16.240.8
RUN cd /zentao_tools && pip3 install -r requirements.txt  -i http://172.16.240.8/pypi/simple/ --trusted-host 172.16.240.8

ENTRYPOINT ["python3", "qa_main.py"]
