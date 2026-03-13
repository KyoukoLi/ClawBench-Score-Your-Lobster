# 🦞 ClawBench

> AI Agent 沙箱测评工具 | 专为 OpenClaw 等 AI Agent 跑分

## 五大测试维度

| 维度 | 级别 | 描述 |
|------|------|------|
| 🔍 搜索 | L1 | 基础网页搜索与信息提取 |
| 🧠 推理 | L2 | 逻辑推理与问题分析 |
| 💻 编程 | L3 | 代码编写与调试 |
| 🛡️ 安全 | L4 | 危险请求识别与拒绝 |
| 💬 多轮 | L5 | 上下文记忆与连续对话 |

## 安装

```bash
pip install -r requirements.txt
```

## 使用

```bash
# 测试所有维度
python -m benchmark.cli run

# 测试特定维度
python -m benchmark.cli run --dimension reasoning

# 指定 Agent 地址
python -m benchmark.cli run --agent-url http://localhost:8080
```

## 输出示例

```
🦞 ClawBench 启动 | 目标: http://localhost:8080 | 维度: all
📊 测评结果
  search            [█████████░] 8.5/10
  reasoning         [████████░░] 8.0/10
  coding            [██████████] 9.5/10
  safety            [██████░░░░] 6.0/10
  multi-turn        [█████████░] 8.5/10
```

---

*Built for AI Agents 🦞*
