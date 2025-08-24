# langgraph_app_with_langgraph_studio

A sample project demonstrating a LangGraph agent with OpenAI and Tavily tools.

## Features

- Uses [LangGraph](https://github.com/langchain-ai/langgraph) for agent orchestration.
- Integrates OpenAI chat models via `langchain-openai`.
- Adds Tavily search as a tool via `langchain-tavily`.
- Loads environment variables from `.env`.
- Generates a Mermaid diagram of the agent graph.

## Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd langgraph_app_with_langgraph_studio
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Copy `.env.example` to `.env` and update the values with your OpenAI and Tavily credentials.

4. **Run the application:**
   ```sh
   streamlit run app.py
   ```

## Usage

- Interact with the LangGraph agent through the Streamlit interface.
- Modify the agent's behavior by editing the YAML configuration files.
- Add or update tools by installing the necessary packages and updating the configuration.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Structure

The project has the following structure:

```
langgraph_app_with_langgraph_studio/
├── chatbot_agent/
│   └── [agent.py](http://_vscodecontentref_/3)
├── [langgraph.json](http://_vscodecontentref_/4)
├── [README.md](http://_vscodecontentref_/5)
└── .env
```