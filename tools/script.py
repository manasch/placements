import datetime
import json
import os
import re

from collections import defaultdict, OrderedDict
from pathlib import Path

import requests

class Notion:
    def __init__(self):
        self.database_id = os.environ['DATABASE_ID']
        self.notion_token = os.environ['NOTION_TOKEN']
        self.endpoint = f"https://api.notion.com/v1/databases/{self.database_id}/query"
    
    def fetch(self):
        headers = {
            "Authorization": "Bearer " + self.notion_token,
            "Notion-Version": "2022-06-28"
        }

        try:
            data = requests.post(self.endpoint, headers=headers)
            data.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
        return data.json()

class Parser:
    def __init__(self, data):
        self.data = data
        self.store = defaultdict(lambda: defaultdict(list))
        self.match = re.compile("((\d+)-(\d+)-(\d+))")
    
    def parse(self):
        results = self.data.get("results")
        parsed = []
        for page in results:
            properties = page.get("properties")

            company = properties.get("Company").get("title")[0].get("plain_text")
            tier = properties.get("Tier").get("select").get("name") if properties.get("Tier").get("select") is not None else None
            register_date = properties.get("Register Deadline").get("date").get("start") if properties.get("Register Deadline").get("date") is not None else None
            job_status = [val.get("name") for val in properties.get("Job Status").get("multi_select")]
            test_date = properties.get("Test Date").get("date").get("start") if properties.get("Test Date").get("date") is not None else None
            test_mode = properties.get("Test").get("select").get("name") if properties.get("Test").get("select") is not None else None
            interview_date = properties.get("Interview Date").get("date").get("start") if properties.get("Interview Date").get("date") is not None else None
            process = properties.get("Process").get("select").get("name") if properties.get("Process").get("select") is not None else None

            parsed.append({
                "company": company,
                "tier": tier,
                "register_date": self.match.search(register_date).group(1) if register_date is not None else None,
                "job_status": job_status,
                "test_date": self.match.search(test_date).group(1) if test_date is not None else None,
                "test_mode": test_mode,
                "interview_date": self.match.search(interview_date).group(1) if interview_date is not None else None,
                "process": process
            })
        
        results.clear()
        
        '''
        Had to use defaultdicts for automatically storing data in this format:
        
        date: {
            register: []
            test: []
            interview: []
        }
        '''
        for item in parsed:
            reg_date = item.get("register_date")
            if reg_date:
                self.store[reg_date]["register"].append({
                    "company": item.get("company"),
                    "tier": item.get("tier"),
                    "job_status": item.get("job_status")
                })

            test_date = item.get("test_date")
            if test_date:
                self.store[test_date]["test"].append({
                    "company": item.get("company"),
                    "test_mode": item.get("test_mode")    
                })

            inter_date = item.get("interview_date")
            if inter_date:
                self.store[inter_date]["interview"].append({
                    "company": item.get("company"),
                    "process": item.get("process")
                })
        
        parsed.clear()
        return OrderedDict(sorted(self.store.items()))

class Schedule:
    def __init__(self, data):
        self.data = data
    
    def md(self, dest = Path.cwd()):
        output = [
            "---",
            "title: \"Schedule\"",
            "# date: 2023-09-30T23:25:54+05:30",
            "---",
            ""
        ]
        push = output.append

        for k, v in self.data.items():
            push(f"## {k}")
            push("")

            register = v.get("register")
            if register:
                push(f"### Register")
                push("")
                for item in register:
                    push("```md")
                    push(f"{item.get('company')}:")
                    push(f"- Tier: {item.get('tier')}")
                    push(f"- Offer: {', '.join(item.get('job_status')) if item.get('job_status') else 'Not Mentioned'}")
                    push("```")
                    push("")
            
            test = v.get("test")
            if test:
                push(f"### Test")
                push("")
                for item in test:
                    push("```md")
                    push(f"{item.get('company')}:")
                    push(f"- Test Mode: {item.get('test_mode') if item.get('test_mode') else 'Not Mentioned'}")
                    push("```")
                    push("")
            
            interview = v.get("interview")
            if interview:
                push(f"### Interview")
                push("")
                for item in interview:
                    push("```md")
                    push(f"{item.get('company')}:")
                    push(f"- Process: {item.get('process') if item.get('process') else 'Not Mentioned'}")
                    push("```")
                    push("")
            
            push("---")
            push("")
        
        with open(dest, "w") as f:
            f.write("\n".join(output))

def main():
    notion = Notion()
    data = notion.fetch()

    parser = Parser(data)
    res = parser.parse()
    
    schedule = Schedule(res)
    schedule.md(Path.cwd() / "content" / "schedule.md")

if __name__ == "__main__":
    main()