# Autonomous Website Scraping with OWL + FireCrawl MCP
 
This project leverages OWL (Optimized Workforce Learning) and FireCrawl MCP (Model Context Protocol) to automate content curation. The system scrapes top tech news websites, extracts relevant information, and compiles a summary report.

## Features

- Uses **FireCrawl MCP Server** for performing web scraping.
- Implements **OwlRolePlaying** for enhanced multi-agent task execution.
- Scrapes **TechCrunch, The Verge, and Wired** using **FireCrawl**.
- Extracts and summarizes **headlines, article summaries, and publication dates**.
- Generates a digest report **(Latest_tech_digest.md)** based on trends from these sources.
- Runs a default scraping task which can be updated before running the Script.

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/camel-ai/owl.git
   cd owl
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and add your API keys/configuration as needed.

## Usage

Navigate to the community use case directory before running the script:

```sh
cd community_usecase/Mcp_use_Case
```

Run the script using:

```sh
python Content_curator.py 
```
The script automatically executes the default task without taking additional input from the terminal.

## Configuration

- The script reads from `mcp_servers_config.json`, which is located in the same folder as Mcp_use_case.
- Modify the `default_task` section in `Content_curator.py` to adjust scraping and summarization behavior.

## Improvements & Customization

- The current implementation runs a **default task** and does not take task input from the terminal.
- To modify the scraping target or change the extracted details, update the `default_task` in `Content_curator.py`.
- The project is stored in the `Mcp_use_Case` folder inside `community_usecase` in the OWL directory.

## Error Handling

- Ensures **graceful cleanup** in case of failures.
- Implements **try-except** blocks to handle tool execution errors.
- Cancels running async tasks to **prevent memory leaks**.
- Supports **KeyboardInterrupt** for a safe shutdown.

## Cleanup & Shutdown

- The script **automatically disconnects MCP** after execution.
- Cancels remaining async tasks to **prevent memory leaks**.
- Special handling for **Windows platforms** is included to ensure smooth termination.

## Repository

For more details, visit the OWL repository: [OWL GitHub Repo](https://github.com/camel-ai/owl)


