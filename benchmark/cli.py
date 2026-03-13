import click
from benchmark.evaluator import ClawEvaluator


@click.group()
def cli():
    """ClawBench - AI Agent 沙箱测评工具"""
    pass


@cli.command()
@click.option('--agent-url', required=True, help='Agent 服务地址')
@click.option('--test-case', default='test_cases/level1_basic.yaml', help='测试用例路径')
def run(agent_url, test_case):
    """运行基准测试"""
    click.echo(click.style("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   🦞  C L A W B E N C H  v1.0                            ║
    ║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ║
    ║   ⚡ Initializing benchmark suite...                     ║
    ║   🎯 Target: {}                                    ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """.format(agent_url[:40]), fg='cyan', bold=True))
    
    click.echo(click.style(f"📂 Loading test case: {test_case}", fg='yellow'))
    
    evaluator = ClawEvaluator(agent_url)
    results = evaluator.run_test(test_case)
    
    click.echo(click.style("\n✅ Benchmark completed!", fg='green', bold=True))
    click.echo(f"📊 Results: {results}")


if __name__ == '__main__':
    cli()
