# Crew-Ai-Test

We are Testin out Crew-Ai with Openai, Huggingfacehub, langchain model and exa

## Installation 

To install the necessary dependencies, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/alfastrek/crew-ai-test.git
cd project
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the requirements:

```bash
pip install -r requirements.txt
```

## Usage/Examples

To run the project, use the following command:

```bash
python main.py
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file:

`OPENAI_API_KEY` - Your OpenAI API key.

`OPENAI_MODEL_NAME` - The name of the OpenAI model you're using.

`HUGGINGFACEHUB_API_TOKEN` - Your Hugging Face Hub API token.

`EXA_API_KEY` - Your Exa API key.

`LANGCHAIN_API_KEY` - Your Langchain API key.

`LANGCHAIN_TRACING_V2` - Your Langchain Tracing V2 key.

## API Reference

#### Get item

```http
  GET /api/item
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- [@alfatrek](https://www.github.com/alfastrek)

(Created for Test Submission of Maheshwari Electrical Agency)

