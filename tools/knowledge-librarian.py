import os
import re
import json
import yaml
from pathlib import Path

class KnowledgeLibrarian:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path).resolve()
        self.cases_path = self.base_path / "knowledge-base" / "cases"
        self.index_file = self.base_path / "knowledge-base" / "knowledge-index.json"
        
        print(f"DEBUG: Base Path: {self.base_path}")
        print(f"DEBUG: Cases Path: {self.cases_path}")
        print(f"DEBUG: Index File: {self.index_file}")

    def extract_metadata(self, file_path: Path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        metadata = {}
        if match:
            try:
                metadata = yaml.safe_load(match.group(1))
            except Exception as e:
                print(f"DEBUG: Error parsing YAML in {file_path}: {e}")
        
        design_lang = ""
        # Updated regex to match the new template header
        design_match = re.search(r'## 1\. 核心视觉特征.*?\n(.*?)\n##', content, re.DOTALL)
        if design_match:
            design_lang = design_match.group(1).strip()
            
        return {
            "title": metadata.get("title", file_path.stem),
            "date": str(metadata.get("date", "")),
            "tags": metadata.get("tags", []),
            "summary": design_lang[:200] + "..." if len(design_lang) > 200 else design_lang,
            "path": str(file_path.relative_to(self.base_path))
        }

    def reindex(self):
        if not self.cases_path.exists():
            print(f"DEBUG: Cases path {self.cases_path} does not exist!")
            return

        index = []
        for file in self.cases_path.glob("*.md"):
            if file.name.lower() == "readme.md":
                continue
            print(f"DEBUG: Found case: {file.name}")
            index.append(self.extract_metadata(file))
        
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=4, ensure_ascii=False)
        
        print(f"SUCCESS: Knowledge index updated: {len(index)} cases indexed at {self.index_file}")

if __name__ == "__main__":
    # Get the root directory (parent of tools/)
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    lib = KnowledgeLibrarian(str(root_dir))
    lib.reindex()
