import markdown

text_md = """
```python\nlogbook_entries = {\n    \"Monday\": {\n        \"Entry\": \"Initiated practical training with sketching exercise to conceptualize design ideas. Explored various concepts and layouts, capturing initial impressions and exploring design possibilities.\"\n    },\n    \"Tuesday\": {\n        \"Entry\": \"Digitized sketches using design software, creating digital prototypes. Familiarized myself with industry-standard tools, translating hand-drawn concepts into digital form for further refinement.\"\n    },\n    \"Wednesday\": {\n        \"Entry\": \"Refined designs, iterating through multiple versions to enhance functionality and aesthetics. Applied design principles, user-centered approach, and feedback from the team to optimize prototypes.\"\n    },\n    \"Thursday\": {\n        \"Entry\": \"Tested prototypes with users, conducting usability testing to evaluate effectiveness and gather feedback. Observed user interactions, noted pain points, and identified areas for improvement.\"\n    },\n    \"Friday\": {\n        \"Entry\": \"Finalized prototype, incorporating feedback and refining the design for clarity, usability, and aesthetics. Presented the polished prototype to team members for evaluation, showcasing the outcome of the week's practical training.\"\n    }\n}\n```
"""

html = markdown.markdown(text_md)
print(html)