### Workflow

```mermaid
flowchart TD
    A[User] --> B[Planner]
    B --> C[Executor]
    C --> D[Tools]
    D --> C
    C --> E[Observation]
    E --> F[Evaluator]
    F -->|Retry| C
    F -->|Final Answer| G[Memorize]
    G -->|END| H[OUTPUT]
    E --> I[(Work Memory)]
    I --> C
```
