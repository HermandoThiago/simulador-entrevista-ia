from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from .functions import read_pdf

console = Console()

def simulate_interview(model):
    """
    Manages the main interview loop, handling user input and AI responses.
    """
    console.print(Panel.fit(
        "[bold cyan]🧠 MENTIS[/bold cyan] - [italic]Simulador de Entrevista para Programadores[/italic]",
        border_style="bright_blue"
    ))

    name = Prompt.ask("[bold green]Digite seu nome[/bold green]")
    vacancy = Prompt.ask("[bold green]Digite o nome da vaga[/bold green] (ex: Cientista de Dados Júnior):", default="Desenvolvedor Python júnior")
    area = Prompt.ask("[bold green]Área da empresa[/bold green] (ex: Finanças, Varejo, Tecnologia):", default="Tecnologia")
    curriculum_name = Prompt.ask("[bold green]Qual o nome do seu currículo?[/bold green] (caso tenha carregado algum)")

    curriculum = ""

    if curriculum_name:
        curriculum = read_pdf(curriculum_name)

    prompt_base = f"""
        Seu nome é Mentis e você é uma recrutadora experiente que está conduzindo uma entrevista para a vaga de {vacancy}.
        A entrevista será realizada com um candidato chamado {name} e você deve fazer perguntas relevantes à vaga,
        ao mesmo tempo mantendo um tom respeitoso e profissional.

        A empresa atua no setor de {area}.

        Com base nesse currículo (caso tenha algum):

        {curriculum}

        Faça a primeira pergunta da entrevista. Depois de cada resposta, você fará a próxima pergunta com base no que foi dito.
    """

    chat = model.start_chat(history=[])

    with console.status("[bold yellow]Iniciando entrevista...[/bold yellow]"):
        response = chat.send_message(prompt_base)

    console.print(f"\n[bold blue][MENTIS IA]:[/bold blue] {response.text}")

    while True:
        candidate_response = Prompt.ask(f"\n[bold green]{name}[/bold green] (ou 'sair')")

        if candidate_response.lower() == "sair":
            with console.status("[bold magenta]Analisando seu desempenho...[/bold magenta]"):

                prompt_feedback = """
                    A entrevista terminou. Com base em todo o histórico acima, forneça um feedback construtivo:
                    1. Pontos Fortes: O que o candidato mandou bem?
                    2. Pontos a Melhorar: O que faltou ou poderia ser mais claro?
                    3. Nota Geral: De 0 a 10.
                    
                    Seja profissional e motivador.
                """

                feedback = chat.send_message(prompt_feedback)

            console.print("\n")
            console.print(Panel(feedback.text, title="[bold white]RELATÓRIO DE DESEMPENHO[/bold white]", border_style="green", padding=(1, 2)))

            break

        with console.status("[italic white]Mentis está digitando...[/italic white]"):
            response = chat.send_message(candidate_response)

        console.print(f"\n[bold blue][MENTIS]:[/bold blue] {response.text}")
