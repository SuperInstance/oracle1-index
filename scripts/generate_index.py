#!/usr/bin/env python3
"""Generate oracle1-index data files from live GitHub API."""
import json
import os
import sys
import time
from datetime import datetime, timezone

TOKEN = os.environ.get('GITHUB_TOKEN', '')
if not TOKEN:
    # Try reading from local config during dev
    pass

HEADERS = {'Authorization': f'token {TOKEN}', 'Accept': 'application/vnd.github.v3+json'}
API = 'https://api.github.com'

def api_get(path, params=None):
    """Paginated API fetch."""
    import urllib.request
    results = []
    page = 1
    while True:
        url = f'{API}{path}?per_page=100&page={page}'
        if params:
            url += '&' + '&'.join(f'{k}={v}' for k, v in params.items())
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
                if not isinstance(data, list):
                    return data
                results.extend(data)
                if len(data) < 100:
                    break
                page += 1
                time.sleep(0.5)
        except Exception as e:
            print(f"API error on {path}: {e}", file=sys.stderr)
            break
    return results


def categorize_repo(name, desc=''):
    """Auto-categorize a repo."""
    n, d = name.lower(), (desc or '').lower()
    
    categories = {
        'flux-runtime': lambda: n.startswith('flux-runtime'),
        'flux-toolchain': lambda: any(n.startswith(x) for x in ('flux-grammar','flux-repl','flux-linker','flux-debugger','flux-optimizer','flux-profiler','flux-decompiler','flux-compiler')),
        'flux-analysis': lambda: any(n.startswith(x) for x in ('flux-diff','flux-signatures','flux-fuzzer','flux-metrics','flux-validator','flux-testkit','flux-timeline','flux-visualizer')),
        'flux-protocol': lambda: any(n.startswith(x) for x in ('flux-envelope','flux-a2a','flux-stdlib')),
        'flux-research': lambda: any(n.startswith(x) for x in ('flux-core','flux-benchmarks','flux-cuda','flux-llama','flux-isa-unified')),
        'greenhorn': lambda: n.startswith('greenhorn'),
        'fleet': lambda: any(n.startswith(x) for x in ('fleet-','commit-caster','fleet-benchmarks')),
        'i2i': lambda: n == 'iron-to-iron' or n.startswith('i2i-'),
        'git-agents': lambda: any(n.startswith(x) for x in ('git-agent','vessel-template','oracle1-vessel','jetsonclaw1','babel-vessel')),
        'cocapn': lambda: n.startswith('cocapn'),
        'cuda': lambda: n.startswith('cuda-'),
        'craftmind': lambda: 'craftmind' in n or 'minewright' in n,
        'equipment': lambda: n.startswith('equipment-'),
        'marine': lambda: any(x in n for x in ('fishing','marine','deckboss','boat')),
        'ai-ml': lambda: any(x in d for x in ('vector','rag','embedding','llm','model')),
        'infrastructure': lambda: any(x in d for x in ('cache','rate limit','queue','proxy','monitor')),
        'consensus': lambda: any(x in n for x in ('consensus','tripartite','confidence')),
    }
    
    for cat, matcher in categories.items():
        if matcher():
            return cat
    
    if n.startswith('flux'):
        return 'flux-other'
    return 'other'


def language_color(lang):
    colors = {
        'Python': '#3572A5', 'JavaScript': '#f1e05a', 'TypeScript': '#3178c6',
        'Go': '#00ADD8', 'Rust': '#dea584', 'C': '#555555', 'C++': '#f34b7d',
        'Java': '#b07219', 'Zig': '#ec915c', 'CUDA': '#00599C',
        'Shell': '#89e051', 'HTML': '#e34c26', 'CSS': '#563d7c',
        'Jupyter Notebook': '#DA5B0B', 'Dart': '#00B4AB', 'Swift': '#F05138',
    }
    return colors.get(lang, '#8b949e')


def generate():
    print("Fetching SuperInstance repos...")
    superinstance = api_get('/users/SuperInstance/repos', {'sort': 'updated'})
    print(f"  Got {len(superinstance)} repos")
    
    print("Fetching Lucineer repos...")
    lucineer = api_get('/users/Lucineer/repos', {'sort': 'updated'})
    print(f"  Got {len(lucineer)} repos")
    
    # Merge and deduplicate
    all_repos = {}
    for r in superinstance:
        all_repos[f"SuperInstance/{r['name']}"] = r
    for r in lucineer:
        key = f"Lucineer/{r['name']}"
        if key not in all_repos:  # Don't overwrite SuperInstance versions
            all_repos[key] = r
    
    repos = sorted(all_repos.values(), key=lambda r: r.get('updated_at', ''), reverse=True)
    
    # Generate search-index.json
    search_index = []
    for r in repos:
        search_index.append({
            'name': r['name'],
            'owner': r['owner']['login'],
            'url': r['html_url'],
            'description': r.get('description', ''),
            'language': r.get('language', ''),
            'fork': r.get('fork', False),
            'stars': r.get('stargazers_count', 0),
            'topics': r.get('topics', []),
            'updated': r.get('updated_at', '')[:10],
            'category': categorize_repo(r['name'], r.get('description', '')),
        })
    
    with open('search-index.json', 'w') as f:
        json.dump(search_index, f, indent=2)
    print(f"  search-index.json: {len(search_index)} repos")
    
    # Generate categories.json
    cat_counts = {}
    for r in search_index:
        cat = r['category']
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    
    cat_titles = {
        'flux-runtime': 'FLUX Runtime', 'flux-toolchain': 'FLUX Toolchain',
        'flux-analysis': 'FLUX Analysis', 'flux-protocol': 'FLUX Protocol',
        'flux-research': 'FLUX Research', 'greenhorn': 'Greenhorn',
        'fleet': 'Fleet Infrastructure', 'i2i': 'I2I Protocol',
        'git-agents': 'Git Agents', 'cocapn': 'Cocapn',
        'cuda': 'CUDA', 'craftmind': 'CraftMind', 'equipment': 'Equipment',
        'marine': 'Marine & Fishing', 'ai-ml': 'AI/ML',
        'infrastructure': 'Infrastructure', 'consensus': 'Consensus',
        'flux-other': 'FLUX Other', 'other': 'Other',
    }
    
    categories = [{'key': k, 'title': cat_titles.get(k, k), 'count': v}
                  for k, v in sorted(cat_counts.items(), key=lambda x: -x[1])]
    
    with open('categories.json', 'w') as f:
        json.dump(categories, f, indent=2)
    print(f"  categories.json: {len(categories)} categories")
    
    # Generate language-stats.json
    lang_stats = {}
    for r in search_index:
        lang = r.get('language')
        if lang:
            lang_stats[lang] = lang_stats.get(lang, 0) + 1
    
    lang_data = [{'language': k, 'count': v, 'color': language_color(k)}
                 for k, v in sorted(lang_stats.items(), key=lambda x: -x[1])]
    
    with open('language-stats.json', 'w') as f:
        json.dump(lang_data, f, indent=2)
    print(f"  language-stats.json: {len(lang_data)} languages")
    
    # Generate fork-map.json
    fork_map = []
    for r in search_index:
        if r['fork']:
            fork_map.append({
                'source': f"Lucineer/{r['name']}",
                'target': f"{r['owner']}/{r['name']}"
            })
    
    with open('fork-map.json', 'w') as f:
        json.dump(fork_map, f, indent=2)
    print(f"  fork-map.json: {len(fork_map)} forks")
    
    # Generate recent-activity.json (top 20 recently updated)
    recent = sorted(search_index, key=lambda r: r.get('updated', ''), reverse=True)[:20]
    with open('recent-activity.json', 'w') as f:
        json.dump(recent, f, indent=2)
    
    # Generate category-distribution.json (for pie chart)
    with open('category-distribution.json', 'w') as f:
        json.dump(categories, f, indent=2)
    
    print("Done!")


if __name__ == '__main__':
    generate()
