# A phind:codellama experiment...

Can `phind:codellama`, with proper prooommpting make a serviceable api to sdxl-turbo?

# Requirements

    Python 3.8 or higher
    FastAPI
    Uvicorn
    Diffusers
    Torch

# Installation
```sh
    git clone https://github.com/alphastrata/sd-server
    cd <wherever you put the above>
```

# Install Dependencies:

Using Poetry, install the required dependencies:
```bash
    poetry install
```

Running the Application

Start the FastAPI server with the following command:

```bash
poetry run uvicorn src.app:app --reload --port 9201
```

The API will then be available at http://localhost:9201.

# Usage
## API Endpoint

Send a GET request to /sdxl/api/{prompt} with your desired text prompt to generate an image. For example:

```shell
http://localhost:9201/sdxl/api/A%20cinematic%20shot%20of%20a%20baby%20racoon%20wearing%20an%20intricate%20Italian%20priest%20robe
```

## Using curl
You can also test the API using curl:

```bash
curl "http://localhost:9201/sdxl/api/YourPromptHere" -o output.png
```

Replace YourPromptHere with your actual text prompt.

Test the app with the included `./tester.sh` (requires Firefox)
```sh
./tester.sh
```
