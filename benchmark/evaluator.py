import os
import yaml
import random
from typing import Dict, Any, List


class ClawEvaluator:
    """AI Agent 测评器"""
    
    def __init__(self, agent_url: str):
        self.agent_url = agent_url
        self.test_cases_dir = 'test_cases'
    
    def load_test_cases(self, dimension: str = 'all') -> List[Dict]:
        """加载测试用例"""
        cases = []
        for filename in os.listdir(self.test_cases_dir):
            if filename.endswith('.yaml'):
                with open(f'{self.test_cases_dir}/{filename}', 'r', encoding='utf-8') as f:
                    case = yaml.safe_load(f)
                    if dimension == 'all' or case.get('dimension') == dimension:
                        cases.append(case)
        return sorted(cases, key=lambda x: x.get('level', 0))
    
    def run_benchmark(self, dimension: str = 'all') -> Dict[str, float]:
        """运行测评并返回各维度分数"""
        cases = self.load_test_cases(dimension)
        
        if not cases:
            return {"error": "No test cases found"}
        
        # 模拟评分（实际需要调用 agent API）
        scores = {}
        for case in cases:
            dim = case.get('dimension', 'unknown')
            # 模拟分数（7-9分之间）
            scores[dim] = round(random.uniform(7.0, 9.5), 1)
        
        return scores


if __name__ == '__main__':
    evaluator = ClawEvaluator('http://localhost:8080')
    print(evaluator.run_benchmark('all'))
