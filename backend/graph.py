from search_tool import search_industry_ai_training
from llm import call_gemini
import os

def search_node(industry: str):
    results = search_industry_ai_training(industry)
    return results

def summarize_node(industry: str, search_results: list):
    snippets = "\n\n".join(
        [f"Source: {r['title']}\n{r['content']}" for r in search_results]
    )

    prompt = f"""
You are researching how the {industry} industry trains its employees on AI tools.
Below are raw web search snippets. Extract the key points as clean bullet points.
Focus on: specific training methods, tools/platforms used, and notable company examples.
Ignore irrelevant or duplicate information.

SEARCH RESULTS:
{snippets}

Return only bullet points, nothing else.
"""
    return call_gemini(prompt)

def report_node(industry: str, summary_bullets: str, search_results: list):
    sources = "\n".join([f"- {r['title']}: {r['url']}" for r in search_results])

    prompt = f"""
Using the bullet points below, write a structured case-study report on how the
{industry} industry trains employees on AI tools.

BULLET POINTS:
{summary_bullets}

Format the report with these sections:
1. Overview
2. Common Training Methods
3. Tools & Platforms Used
4. Notable Examples
5. Recommendations for Academic/University Adoption

Keep it concise and professional, suitable for a case-study submission.
"""
    report_body = call_gemini(prompt)

    full_report = f"# AI Adoption Case Study: {industry.title()} Industry\n\n{report_body}\n\n## Sources\n{sources}\n"

    os.makedirs("reports", exist_ok=True)
    filepath = f"../reports/{industry.lower().replace(' ', '_')}.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_report)

    return full_report

def run_pipeline(industry: str):
    """Runs the 3-step pipeline: search -> summarize -> report"""
    search_results = search_node(industry)
    summary = summarize_node(industry, search_results)
    report = report_node(industry, summary, search_results)
    return report