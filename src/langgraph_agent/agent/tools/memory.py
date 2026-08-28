from langchain_core.tools import tool
from pathlib import Path
memory_path = Path(__file__).parent.parent.parent.parent.parent.resolve() / "data" / "memory.txt"
@tool
def w_memory(knowledge: str) -> str:
    ''' add knowlege into model's memory '''
    with open(memory_path,'a', encoding ="utf-8") as f:
        f.write("\n"+knowledge)
    return " Đã viết thành công"