

# The Process of Building My First AI Agent

My goal is to build a **human-like AI agent**, something similar to **JARVIS from IRON MAN**, that can assist me and gradually understand me better over time.

I started with a simple **schedule-assistance agent**. At this early stage, it only has access to two basic tools: one `read_pandas` function and one `write_pandas` function for reading and modifying my schedule.

However, I don't want my agent to only manage schedules. I want it to eventually have **memory and knowledge like a brain**, so I created a `.txt` file to store information that the agent can remember and use in future interactions.

The agent is still in its **very early stages**. I'm using some free LLMs to build and test it, so the system may have relatively high latency. The workflow I designed may also be more complicated than necessary. The basic blueprint was inspired by ideas I found on the Internet, but I added some of my own "salt" to make it work better — at least, I think so :)))).

## Project Structure

* The project contains some strange parts, such as **Jupyter notebooks**. These were part of my initial development process, where I experimented with the agent in notebooks before moving everything into a proper project structure.
* I'm doing this intentionally because I want to learn **how to develop a project professionally**
* (I try uv project eventually and struggle with it for a long time, it have an specific error with my mac and take me lots of hours)

### Main Project

The main part of the project is the `src` folder, which contains the `langgraph_agent` package.

It is roughly divided into two parts:

* **Backend** — The AI agent itself, built with **LangGraph**. This is where the agent's workflow, memory, planning, execution, observation, and evaluation logic are implemented.
* **Frontend** — A very simple **Streamlit** interface. 

### Some Cons:
- Some SYSTEMPROMPT(I use AI to create it) isn't effective and meet the "Human-like" condition
- High latency 
- a chatbox don't have checkpointer and short-term memory
- I want to add HITL to my agent
- etc ... 
