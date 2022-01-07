FROM jupyter/datascience-notebook:r-4.1.2

# Install essential Python packages
RUN python3 -m pip --no-cache-dir install \
    "tensorly==0.4.3" \
    git+https://github.com/ahwillia/tensortools

EXPOSE 8888
ADD ./jupyter_notebook_config.py /root/.jupyter/
WORKDIR /project
ENTRYPOINT ["jupyter", "lab", "--allow-root"]
