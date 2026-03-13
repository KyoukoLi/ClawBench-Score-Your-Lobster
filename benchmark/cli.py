import click
from benchmark.evaluator import ClawEvaluator


@click.group()
def cli():
    """🦞 ClawBench - AI Agent 测评工具"""
    pass


@cli.command()
@click.option('--agent-url', default='http://localhost:8080', help='Agent 服务地址')
@click.option('--dimension', type=click.Choice(['all', 'search', 'reasoning', 'coding', 'safety', 'multi-turn']), default='all', help='测试维度')
def run(agent_url, dimension):
    """运行测评"""
    click.echo(click.style(f"🦞 ClawBench 启动 | 目标: {agent_url} | 维度: {dimension}", fg='cyan', bold=True))
    
    evaluator = ClawEvaluator(agent_url)
    results = evaluator.run_benchmark(dimension)
    
    click.echo(click.style("\n📊 测评结果", fg='yellow', bold=True))
    for dim, score in results.items():
        bar = '█' * int(score) + '░' * (10 - int(score))
        click.echo(f"  {dim:20} [{bar}] {score}/10")


if __name__ == '__main__':
    cli()
