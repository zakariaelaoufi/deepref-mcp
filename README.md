# DeepRef - Research Copilot with Citation Retriever

<!-- Logo placeholder - add your logo here -->
<div align="center">
    <img width="1920" height="480" alt="DeepRef Logo" src="https://github.com/user-attachments/assets/1c337262-2ad6-48b0-81cb-a9a1223482db" />
<p><em>Your AI-powered research assistant for academic paper discovery and citation</em></p>
</div>

## 🎯 Overview

DeepRef is an intelligent research copilot that leverages Model Context Protocol (MCP) to bridge the gap between large language models and scholarly databases. It enables researchers, students, and academics to quickly discover, retrieve, and cite relevant academic papers from multiple authoritative sources.

### Key Features

- **Multi-Database Search**: Query arXiv, Semantic Scholar, and PubMed simultaneously
- **Intelligent Citation Retrieval**: Automatically formats and structures citations with abstracts
- **MCP Integration**: Seamless connection between AI models and scholarly APIs
- **Real-time Results**: Fast, contextual paper discovery based on research queries
- **Structured Data**: Clean, standardized paper metadata across all sources

## 🏗️ Architecture

DeepRef acts as an MCP (Model Context Protocol) server that:

1. **Receives** research queries from the LLM
2. **Queries** multiple scholarly APIs (arXiv, Semantic Scholar, PubMed)
3. **Structures** citations, abstracts, and metadata
4. **Injects** relevant papers into the model's context
5. **Delivers** trustworthy, referenced information to users

```
┌─────────────┐    ┌──────────────┐    ┌─────────────────┐
│    User     │───▶│   LLM/AI     │───▶│   DeepRef MCP   │
│   Query     │    │   Agent      │    │    Server       │
└─────────────┘    └──────────────┘    └─────────┬───────┘
                                                 │
                        ┌────────────────────────┼────────────────────────┐
                        │                        │                        │
                   ┌────▼────┐              ┌────▼────┐              ┌────▼────┐
                   │  arXiv  │              │Semantic │              │ PubMed  │
                   │   API   │              │Scholar  │              │   API   │
                   └─────────┘              └─────────┘              └─────────┘
```

## 🚀 Installation

### Prerequisites

- Python 3.10+
- UV package manager (recommended) or pip

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/DeepRef.git
   cd DeepRef
   ```

2. **Install dependencies**:
   ```bash
   # Using UV (recommended)
   uv pip install -r requirements.txt
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Add your OpenAI API key to .env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🎮 Usage

### Running the MCP Server

Start the DeepRef MCP server:

```bash
python src/server.py
```

Start the MCP Inspector:

```bash
mcp dev src/server.py
```

### Using the CLI Assistant

Run the interactive CLI assistant:

```bash
python .\example\deepref_assistant.py
```

### Example Queries

```
> What are the latest developments in transformer architectures?
> Find papers about COVID-19 vaccine efficacy studies
> Search for research on quantum computing applications in machine learning
```

## 📊 Demo

<!-- Screenshots section - add your demo images here -->

### MCP Inspector
<img width="1919" height="911" alt="Capture d'écran 2025-09-06 175116" src="https://github.com/user-attachments/assets/51cb15c8-a609-4204-8a0c-39a3ea821265" />

### Search Results
<img width="1817" height="611" alt="Capture d'écran 2025-09-06 172119" src="https://github.com/user-attachments/assets/e4b3a48b-c6e2-4ae0-ab6f-1175c3ddbede" />

## 🔧 Configuration

### Supported Databases

- **arXiv**: Pre-print repository for physics, mathematics, computer science, and more
- **Semantic Scholar**: AI-powered academic search engine
- **PubMed**: Biomedical literature database

### Search Parameters

```python
# Customize your search
search_papers(
    query="your research query",
    max_results=10,  # Papers per database
    sources=['arxiv', 'semantic scholar', 'pubmed']  # Select specific sources
)
```

## 📁 Project Structure

```
DeepRef/
├── src/
│   ├── models/
│   │   └── paper.py           # Paper data model
│   ├── providers/
│   │   ├── arXiv_provider.py      # arXiv API integration
│   │   ├── semantic_scholar_provider.py  # Semantic Scholar API
│   │   └── pubmed_provider.py     # PubMed API integration
│   ├── tools/
│   │   └── search.py          # MCP tool registration
│   └── server.py              # MCP server entry point
├── example/
│   └── deepref_assistant.py   # CLI assistant example
├── requirements.txt
└── README.md
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://github.com/zakariaelaoufi/deepref-mcp/blob/master/CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/zakariaelaoufi/deepref-mcp/blob/master/LICENSE) file for details.

## 🙏 Acknowledgments

- [arXiv](https://arxiv.org/) for providing open access to scientific papers
- [Semantic Scholar](https://www.semanticscholar.org/) for their comprehensive academic database
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/) for biomedical literature access
- [Model Context Protocol](https://modelcontextprotocol.io/) for enabling seamless AI integrations

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/zakariaelaoufi/deepref-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/zakariaelaoufi/deepref-mcp/discussions)

---

<div align="center">
  <p>Made with ❤️ for the research community</p>
</div>
