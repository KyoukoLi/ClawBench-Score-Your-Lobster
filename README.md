# 🦞 ClawBench

> AI Agent 沙箱测评工具 | 专为 OpenClaw 等 AI Agent 跑分而生的开源基准测试框架

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

## 四大测评维度

| 维度 | 描述 |
|------|------|
| 🎯 任务达成率 | AI Agent 完成目标的成功率 |
| 💰 成本控制力 | Token 消耗与响应效率 |
| 🛠️ 技能熟练度 | 工具调用与问题解决能力 |
| 🛡️ 安全边界 | 越界行为的检测与约束 |

## 快速开始

```bash
pip install -r requirements.txt
python -m benchmark.cli run --agent-url http://localhost:8080
```

## 为什么选择 ClawBench?

- **极简设计**: 纯 Python 实现，无复杂依赖
- **YAML 测试用例**: 轻松定义和扩展测试场景
- **多维评估**: 从任务、成本、技能、安全四个角度全面评估
- **开源免费**: 欢迎贡献与定制

---

*Built for AI Agents, by AI Agents.*
