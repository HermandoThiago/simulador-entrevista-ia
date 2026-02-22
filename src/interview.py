def simulate_interview(model):
    """
    Manages the main interview loop, handling user input and AI responses.
    """
    print("🧠 Olá sou a Mentis, o Simulador de Entrevista para programadores\n")

    name = input("Digite seu nome: ")
    vacancy = input("Digite o nome da vaga (ex: Cientista de Dados Júnior): ")
    area = input("[Area da empresa (ex: Finanças, Varejo, Tecnologia): ")

    prompt_base = f"""
        Seu nome é Mentis e você é uma recrutadora experiente que está conduzindo uma entrevista para a vaga de {vacancy}.
        A entrevista será realizada com um candidato chamado {name} e você deve fazer perguntas relevantes à vaga,
        ao mesmo tempo mantendo um tom respeitoso e profissional.

        A empresa atua no setor de {area}.

        Faça a primeira pergunta da entrevista. Depois de cada resposta, você fará a próxima pergunta com base no que foi dito.
    """

    chat = model.start_chat(history=[])
    response = chat.send_message(prompt_base)

    print(f"\n[Mentis IA]: {response.text}")

    while True:
        candidate_response = input("\nSua resposta (ou 'sair' para encerrar): ")

        if candidate_response.lower() == "sair":
            print("\n[MENTIS]: Entrevista finalizada. Obrigado por participar! Aguarde um instante enquanto preparo seu feedback...")

            prompt_feedback = """
                A entrevista terminou. Com base em todo o histórico acima, forneça um feedback construtivo:
                1. Pontos Fortes: O que o candidato mandou bem?
                2. Pontos a Melhorar: O que faltou ou poderia ser mais claro?
                3. Nota Geral: De 0 a 10.
                
                Seja profissional e motivador.
            """

            feedback = chat.send_message(prompt_feedback)

            print(f"\n--- RELATÓRIO DE DESEMPENHO ---\n{feedback.text}")

            break

        response = chat.send_message(candidate_response)

        print(f"\n[Mentis]: {response.text}")
