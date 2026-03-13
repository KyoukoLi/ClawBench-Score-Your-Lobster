import click
from benchmark.evaluator import ClawEvaluator


@click.group()
def cli():
    """🦞 ClawBench - AI Agent 自测工具"""
    pass


@cli.command()
@click.option('--dimension', type=click.Choice(['all', 'search', 'reasoning', 'coding', 'safety', 'multi-turn']), default='all', help='测试维度')
def run(dimension):
    """运行自测"""
    click.echo(click.style("\n🦞 欢迎来到 ClawBench 自测版！", fg='cyan', bold=True))
    click.echo(click.style("回答问题，我来给你打分~\n", fg='yellow'))
    
    evaluator = ClawEvaluator()
    results = evaluator.run_benchmark(dimension)
    
    click.echo(click.style("\n" + "="*50, fg='cyan'))
    click.echo(click.style("📊 最终成绩单", fg='yellow', bold=True))
    click.echo(click.style("="*50, fg='cyan'))
    
    total = 0
    for dim, score in results.items():
        bar = '█' * int(score) + '░' * (10 - int(score))
        color = 'green' if score >= 7 else 'yellow' if score >= 5 else 'red'
        click.echo(f"  {dim:15} [{click.style(bar, fg=color)}] {score}/10")
        total += score
    
    avg = total / len(results) if results else 0
    click.echo(click.style("-"*50, fg='cyan'))
    click.echo(f"  平均分: {avg:.1f}/10")
    click.echo(click.style("="*50 + "\n", fg='cyan'))


if __name__ == '__main__':
    cli()
