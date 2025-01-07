from langflow.load import run_flow_from_json
input_value = str(input("Enter the prompt : "))
TWEAKS = {
  "ChatInput-7ahiF": {
    "files": "",
    "background_color": "",
    "chat_icon": "",
    "input_value": input_value,
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "ChatOutput-01rZN": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "Prompt-E28ks": {
    "template": "You are an expert in content analysis, tasked with providing insights into social media performance. Given the dataset of social media post data, analyze the content performance based on engagement metrics, post types, time of day, and audience interaction. Your goal is to derive actionable insights for improving content strategies, including recommendations on what type of content works best for increasing engagement.\n\nFor the analysis, focus on:\n- Engagement trends across different post types (Reels, Carousel, Static).\n- The impact of post timing on engagement.\n- Comparative analysis of performance metrics (likes, shares, comments, views).\n- Recommendations for optimizing content to increase audience engagement and reach.\n\nProvide answers that are concise, directly related to the content performance, and actionable for improving social media strategy.\n\nData:\n{input_data}\n\nNow, answer the following questions based on the content analysis of the data:\n{question}\n\nExample Outputs:\n● Carousel posts have 20% higher engagement than static posts.\n● Reels drive 2x more comments compared to other formats.\n● Posts with hashtags #travel and #nature receive 30% more likes than average.",
    "input_data": "",
    "question": ""
  },
  "AstraDB-4I2kB": {
    "advanced_search_filter": "{}",
    "api_endpoint": "db_endpoint",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "collection_name",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "db_token"
  },
  "File-CYA0k": {
    "path": "random_instagram_engagement_data.pdf",
    "concurrency_multithreading": 4,
    "silent_errors": False,
    "use_multithreading": False
  },
  "SplitText-TFvgW": {
    "chunk_overlap": 200,
    "chunk_size": 1000,
    "separator": "\n"
  },
  "OpenAIEmbeddings-tnYlD": {
    "chunk_size": 1000,
    "client": "",
    "default_headers": {},
    "default_query": {},
    "deployment": "",
    "dimensions": None,
    "embedding_ctx_length": 1536,
    "max_retries": 3,
    "model": "text-embedding-3-small",
    "model_kwargs": {},
    "openai_api_base": "",
    "openai_api_key": "openai_api",
    "openai_api_type": "",
    "openai_api_version": "",
    "openai_organization": "",
    "openai_proxy": "",
    "request_timeout": None,
    "show_progress_bar": False,
    "skip_empty": False,
    "tiktoken_enable": True,
    "tiktoken_model_name": ""
  },
  "OpenAIModel-pRY9E": {
    "api_key": "openai_api",
    "input_value": "",
    "json_mode": False,
    "max_tokens": None,
    "model_kwargs": {},
    "model_name": "gpt-3.5-turbo",
    "openai_api_base": "",
    "output_schema": {},
    "seed": 1,
    "stream": False,
    "system_message": "",
    "temperature": 0.1
  },
  "AstraDB-QbT5Z": {
    "advanced_search_filter": "{}",
    "api_endpoint": "db_endpoint",
    "batch_size": None,
    "bulk_delete_concurrency": None,
    "bulk_insert_batch_concurrency": None,
    "bulk_insert_overwrite_concurrency": None,
    "collection_indexing_policy": "",
    "collection_name": "collection_name",
    "embedding_choice": "Embedding Model",
    "keyspace": "",
    "metadata_indexing_exclude": "",
    "metadata_indexing_include": "",
    "metric": "cosine",
    "number_of_results": 4,
    "pre_delete_collection": False,
    "search_filter": {},
    "search_input": "",
    "search_score_threshold": 0,
    "search_type": "Similarity",
    "setup_mode": "Sync",
    "token": "db_token"
  },
  "ParseData-dDCzp": {
    "sep": "\n",
    "template": "{text}"
  }
}

result = run_flow_from_json(flow="content_analysis_module.json",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)