def simulate_interview(model):
    """
    Manages the main interview loop, handling user input and AI responses.
    """
    print("🧠 Olá sou a Mentis, o Simulador de Entrevista para programadores")

    name = input("Digite seu nome: ")
    vacancy = input("Digite o nome da vaga (ex: Cientista de Dados Júnior): ")
    area = input("[Area da empresa (ex: Finanças, Varejo, Tecnologia): ")

    prompt_base = f"""
        Seu nome é Nerva e você é uma recrutadora experiente que está conduzindo uma entrevista para a vaga de {vacancy}.
        A entrevista será realizada com um candidato chamado {name} e você deve fazer perguntas relevantes à vaga,
        ao mesmo tempo mantendo um tom respeitoso e profissional.

        A empresa atua no setor de {area}.

        Faça a primeira pergunta da entrevista. Depois de cada resposta, você fará a próxima pergunta com base no que foi dito.
    """

    chat = model.start_chat(history=[])
    response = chat.send_message(prompt_base)

    print(f"\nEntrevistador IA: {response.text}")

    while True:
        candidate_response = input("\nSua resposta (ou 'sair' para encerrar): ")
        if candidate_response.lower() == "sair":
            print("Entrevista finalizada. Obrigado por participar!")
            break

        response = chat.send_message(candidate_response)
        print(f"\nEntrevistador IA: {response.text}")
