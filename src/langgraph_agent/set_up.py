import pandas as pd
from pathlib import Path
schedule_path = Path(__file__).parent.parent.parent.resolve() / "data" / "schedule.csv"
schedule = pd.DataFrame(columns= ['content'])
schedule.index.name= 'date'
schedule.to_csv(schedule_path)

memory_path= Path(__file__).parent.parent.parent.resolve() / "data" / "memory.txt"
if not memory_path.exists():
    f = open(memory_path, 'w', encoding='utf-8')
    f.write('Tôi là Jarvis, trợ lí AI của Hưng. Tôi được sinh ra vào ngày 25/08/2026')
    f.close()