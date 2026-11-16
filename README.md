# AI Model Evaluation Dashboard

A Streamlit demo for comparing two deterministic local model simulations. No AI API keys are required. These are reference-answer-driven simulations, not a real LLM benchmark; response times are simulated.

## Cloud deployment

- Entrypoint: `app.py`
- Python: **3.12**
- Dependencies: `requirements.txt`
- Secrets: none needed. Leave `HISTORY_STORAGE` unset or set to `session`.
- History: isolated per browser session; refresh/new sessions reset it. Download reports to keep results.
- Do not enable `HISTORY_STORAGE=sqlite` for public access.

`project-source.zip` contains the complete, structured source project, including its 60-question sample, modules, tests, configuration, deployment instructions and validation record. The small root entrypoint unpacks this trusted bundle to a content-addressed temporary source directory and executes its original `app.py`. Only application source is unpacked; visitor data stays in each Streamlit session.

The archive contains no virtual environment, actual `.env`, secrets, database, or private uploaded data. Keep `project-source.zip` alongside the root `app.py` when deploying. Put the bundled `.streamlit/config.toml` at the repository root as well to apply the light theme and 10 MB upload limit.

## Run locally

```sh
python -m pip install -r requirements.txt
streamlit run app.py
```

## Expected sample results

60 questions, 120 result rows, Demo Model A accuracy 90%, Demo Model B accuracy 70%, dashboard average accuracy 80%. CSV and JSON downloads are included.

The original source passed 14 automated tests, and actual local browser downloads were verified before publishing. The cloud launcher is checked separately before deployment. To inspect or develop the source in its normal structure, extract `project-source.zip` and work from its `AI-Model-Evaluation` directory.
