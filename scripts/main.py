import os
import json
from datetime import datetime
from fetchers import fetch_github_stats, verify_deployments, fetch_leetcode_stats
from generators import generate_markdown, generate_svg

def main():
    GITHUB_USERNAME = "kranthi-06"
    LEETCODE_USERNAME = "kasakranthi06"
    TOKEN = os.environ.get("GITHUB_TOKEN")
    
    print("Fetching GitHub Stats...")
    gh_stats = fetch_github_stats(GITHUB_USERNAME, TOKEN)
    
    print("Fetching LeetCode Stats...")
    lc_stats = fetch_leetcode_stats(LEETCODE_USERNAME)
    
    print("Verifying Deployments...")
    deployments = [
        {"name": "Portfolio", "url": "https://kasakranthikiran.vercel.app", "tech": "React, Framer Motion"},
        {"name": "LakshyaTrack", "url": "https://lakshyatrack.vercel.app/", "tech": "Next.js, TypeScript"},
        {"name": "Emergent", "url": "https://emergent-theta.vercel.app/dashboard", "tech": "IoT, React"},
        {"name": "AI Plant Disease", "url": "https://ai-plant-disease-analysis.vercel.app/", "tech": "PyTorch, OpenCV"},
        {"name": "Speech to Sign", "url": "", "tech": "TensorFlow, NLP"}
    ]
    deployment_stats, online_count = verify_deployments(deployments)
    
    current_date = datetime.utcnow().strftime("%B %d, %Y")
    
    data = {
        "gh": gh_stats,
        "lc": lc_stats,
        "deployments": deployment_stats,
        "online_deployments": online_count,
        "current_focus": "Agentic AI & Production Systems",
        "date": current_date
    }
    
    with open('dashboard_data.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print("Generating assets...")
    generate_markdown(data)
    generate_svg(data)
    print("Done!")

if __name__ == "__main__":
    main()
