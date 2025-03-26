import os
import sys

from dotenv import load_dotenv

from camel.logger import set_log_level, get_logger
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.toolkits import ExcelToolkit, SearchToolkit, FileWriteToolkit, CodeExecutionToolkit

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from owl.utils import OwlRolePlaying, run_society
# from owl.utils import OwlRolePlaying

logger = get_logger(__name__)

def construct_society(question: str, model: str = "DEEPSEEK") -> OwlRolePlaying:
    model_platform = ModelPlatformType.DEEPSEEK if model == "DEEPSEEK" else ModelPlatformType.QWEN
    model_type = os.getenv("DEEPSEEK_API_MODEL_TYPE", ModelType.DEEPSEEK_CHAT) if model == "DEEPSEEK" else os.getenv("QWEN_API_MODEL_TYPE", ModelType.QWEN_QWQ_32B)

    max_tokens = os.getenv("LLM_MAX_TOKENS", 10000)

    logger.debug(f'create model: {model_platform} - {model_type}')

    models = {
        "user": ModelFactory.create(
            model_platform = model_platform,
            model_type = model_type,
            model_config_dict = {
                "temperature": 0,
                "max_tokens": max_tokens,
            },
        ),
        "assistant": ModelFactory.create(
            model_platform = model_platform,
            model_type = model_type,
            model_config_dict = {
                "temperature": 0,
                "max_tokens": max_tokens,
            },
        ),
    }

    tools = [
        *CodeExecutionToolkit(sandbox="subprocess", verbose=True).get_tools(),
        SearchToolkit().search_bing,
        SearchToolkit().search_baidu,
        # SearchToolkit().search_duckduckgo,
        # SearchToolkit().search_wiki,
        *ExcelToolkit().get_tools(),
        *FileWriteToolkit(output_dir="E:/Test/").get_tools(),
    ]

    user_agent_kwargs = {"model": models["user"]}
    assistant_agent_kwargs = {"model": models["assistant"], "tools": tools}

    task_kwargs = {
        "task_prompt": question,
        "with_task_specify": False,
    }

    return OwlRolePlaying(
        **task_kwargs,
        user_role_name = "user",
        user_agent_kwargs = user_agent_kwargs,
        assistant_role_name = "assistant",
        assistant_agent_kwargs = assistant_agent_kwargs,
        output_language = "Chinese",
    )

def main():
    load_dotenv()
    set_log_level(level=os.getenv("CAMEL_LOGGING_LEVEL", "INFO"))
    
    question = sys.argv[1] if len(sys.argv) > 1 else "搜索DeepSeek最近的相关新闻，整理成一份分析报告，所有资料保存到本地存储"
    society = construct_society(question, "QWQ")
    anwser, chat_history, token_count = run_society(society)
    print(f"Answer: {anwser}")

if __name__ == "__main__":
    main()