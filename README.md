![aimped](https://dev.aimped.ai/static/media/AimpedBirdLogo.0b3c7cc26d31afe7bd73db496acb01d1.svg)

# **aimped**

[![PyPI version](https://badge.fury.io/py/aimped.svg)](https://badge.fury.io/py/aimped)
[![Downloads](https://pepy.tech/badge/aimped)](https://pepy.tech/project/aimped)

**Aimped is a unique python library that provides classes and functions for only exclusively business-tailored AI-based models.**
In this version, we provide the following features:
API service, Sound processing tools and functions, NLP tools and functions, and a pipeline class for NLP tasks.

# Installation

```python
pip install aimped
```

# API Usage

## Configuration of the Library

```python
from aimped.services.api import AimpedAPI

# Create new instance Aimped
user_key = ''  # user_key received from A3M.
user_secret = ''  # user_secret received from A3M.
BASE_URL = 'https://aimped.ai'  # Aimped domain url

api_service = AimpedAPI(user_key, user_secret, {
  base_url: BASE_URL
})
```

## Preparation of the model input data

```python
model_id = ""   # ID of the model run. The model ID is available on the model description page under API usage. 
payload = {...}  # Model input examples (payload) are available in the api usage tab on the Model description page. 
```

## Usage of API Function

```python
result = api_service.run_mode(model_id, input_data)
```

## Usage of API Callback Function

```python
# return callback function

def callback(event, message, time, data=None):
    if event == 'start':
        print(f'Start event at {time}: {message}')
    elif event == 'proccess':
        print(f'Progress event at {time}: {message}')
    elif event == 'error':
        print(f'Error event at {time}: {message}')
    elif event == 'end':
        print(f'End event at {time}: {message}. Data: {data}')

result = api_service.run_model_callback(model_id, payload, callback)
```

## Usage of API File Upload

Some of the models supports file inputs. These inputs are accepted as URIs. Here is the usage of API for file uploads.

```python
input = aimped.file_upload(
    model_id,
    '/Users/joe/Downloads/xyz.pdf'  # sample file path to upload
    )
```

## Usage of API File Download

Some of the models supports file outputs as result. These outputs are created as URIs. Here is the usage of API for file downloads.

```python
  output_file = api_service.file_download_and_save(
    'input/application/model_{{modelId}}/user_{{userId}}/file_name',  # URI of the model output file in the result
    '/Users/joe/Downloads/123_file_name'  # sample local file path to save
    )
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
