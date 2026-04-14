import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from generate_index import categorize_repo, language_color

class TestCategorize:
    def test_flux_runtime(self):
        assert categorize_repo('flux-runtime', '') == 'flux-runtime'
    def test_cuda(self):
        assert categorize_repo('cuda-genepool', '') == 'cuda'
    def test_greenhorn(self):
        assert categorize_repo('greenhorn-runtime', '') == 'greenhorn'
    def test_fleet(self):
        assert categorize_repo('fleet-mechanic', '') == 'fleet'
    def test_i2i(self):
        assert categorize_repo('iron-to-iron', '') == 'i2i'
    def test_git_agents(self):
        assert categorize_repo('oracle1-vessel', '') == 'git-agents'
    def test_cocapn(self):
        assert categorize_repo('cocapn', '') == 'cocapn'
    def test_unknown(self):
        assert categorize_repo('random-name', '') == 'other'
    def test_description_match(self):
        assert categorize_repo('my-repo', 'A vector database for embeddings') == 'ai-ml'

class TestLanguageColor:
    def test_python(self):
        assert language_color('Python') == '#3572A5'
    def test_rust(self):
        assert language_color('Rust') == '#dea584'
    def test_unknown(self):
        assert language_color('Brainfuck') == '#8b949e'
