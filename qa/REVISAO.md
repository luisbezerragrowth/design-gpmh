# Revisão do pacote 1.1.0-rc1

24/09/2026 · base DS 1.3.0-rc1 · em revisão.

## Estrutura e portabilidade

Núcleo único em `gpmh-design/`. Entradas de projeto para Cursor, Codex e Claude Code apontam para essa fonte. O documento universal e as instruções de Knowledge são gerados da mesma fonte por `tools/build_context.py`; o verificador detecta divergência. O resumo permanece abaixo de 10.000 caracteres.

YAML conferido com Ruby/Psych safe_load; links, versões, caminhos dos adaptadores, âncoras do documento único e referências de recursos passaram. Tokens e motor do núcleo foram comparados aos do kit. O importador recusa sobrescrita, caminhos inseguros e versão diferente. O gerador também valida o ZIP de produção realmente fornecido para a entrega.

Os scripts `check_distribution.py` e `check_packages.py` acompanham a fonte. Resultados detalhados em JSON são locais e ficam fora do Git. Os pacotes contêm os mesmos caminhos relativos após extração; a versão para GitHub exclui kit e fontes comerciais. Arquivos de distribuição anteriores preservados no acervo de origem.

## Revisão independente

Um agente sem histórico recebeu somente o documento universal e simulou:

- Carrossel de cinco telas, título longo, rosto no topo e somente Arial: reconheceu escala consistente, proteção da imagem, etapa provisória e necessidade de fonte real antes de fidelidade final.
- Landing com dado não verificado, download ausente, vento em fotografia e promessa de todos os celulares: separou a estrutura executável das dependências de evidência, entrega e movimento; não confundiu viewport com aparelho real.
- Post claro e humano com apenas Markdown: avançou em conceito e composição sem alegar acesso a imagens, logos ou fontes.

A revisão encontrou ambiguidades que foram corrigidas: autorização para editar copy aprovada; consulta visual condicionada a acesso real; calibração de master antes da sequência; inventário de fontes separado de redistribuição; pedido atual sem transformar suposição em fato; caminhos adaptados à leitura em arquivo único.

Outro agente auditou entradas, empacotamento e manutenção. Foram corrigidos resumo manual divergente, ausência de validação do ZIP de produção fornecido e omissão de Codex na lista de runtimes não homologados.

## Limites

A documentação oficial das ferramentas foi conferida e vinculada em `COMPATIBILIDADE.md`. Não houve instalação/invocação real deste pacote no Cursor, Codex, Claude Code, Lovable ou Manus para homologar acionamento e saída. Simulação independente avalia clareza das regras; não garante comportamento de todos os modelos. A primeira tarefa real em cada ambiente precisa confirmar leitura e ativos disponíveis.

Esta revisão antecedeu a publicação do repositório. Ela não representa deploy do site, envio ao cliente, alteração de tarefas externas nem homologação integral do design system.
