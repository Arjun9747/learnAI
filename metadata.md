# LangChain + OpenAI Result

## Flow

String

```text
   │
   ▼
LLM
   │
   ▼
AIMessage
```

## Command run

```bash
(.venv) PS C:\Users\arjun\Downloads\Learn- AI\learnAI> & "c:\Users\arjun\Downloads\Learn- AI\learnAI\.venv\Scripts\python.exe" "c:/Users/arjun/Downloads/Learn- AI/learnAI/test_langchain.py"
```

## Output

```text
TYPE:
<class 'langchain_core.messages.ai.AIMessage'>

FULL RESULT:
content='The capital of France is Paris.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 7, 'prompt_tokens': 14, 'total_tokens': 21, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_98f538dc1a', 'id': 'chatcmpl-EBE0bYuClKZXqDbURjrUKs8N6WweZ', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019fea68-c9e1-7523-84a0-1f0a69ec6a2e-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 14, 'output_tokens': 7, 'total_tokens': 21, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

CONTENT:
The capital of France is Paris.
```

## Token usage

- Input/prompt tokens: 14
- Output/completion tokens: 7
- Total tokens: 21

