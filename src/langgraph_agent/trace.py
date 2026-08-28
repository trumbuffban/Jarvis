trace = []

def add_trace(message: dict) -> None:
    trace.append(message)

def show_trace():
    for i in trace:
        print(i + "\n")
def clear_trace():
    trace.clear()
    