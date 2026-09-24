# Como usar em cada ferramenta

Pacotes completos para baixar: [release pública no GitHub](https://github.com/luisbezerragrowth/design-gpmh/releases/tag/v1.1.0-rc1), sem login ou convite. Use GPMH-DESIGN-CLIENTE.zip para receber tudo ou GPMH-DESIGN-SKILL-COMPLETA.zip para importar somente a skill. As condições de uso dos ativos permanecem em [DISTRIBUICAO.md](DISTRIBUICAO.md).

Conferência documental: 24/09/2026. Compatibilidade de formato não significa que uma sessão já leu o conteúdo. Peça uma confirmação curta da versão e dos ativos acessíveis antes da primeira peça. Não é necessário instalar um MCP para usar as regras.

## Cursor

Abra a pasta extraída como projeto. `.cursor/rules/gpmh-design.mdc` mantém a entrada comum no contexto; `alwaysApply: true` vale neste projeto GPMH. A regra aponta para `LEIA-PRIMEIRO-IA.md` e `gpmh-design/SKILL.md`. Ao incorporar a outro repositório, leve o núcleo e ajuste referências; preserve regras já existentes.

O formato MDC e a pasta `.cursor/rules` seguem a [documentação do Cursor](https://cursor.com/docs/rules).

## Codex

Abra o projeto. `AGENTS.md` aponta para a entrada comum. O adaptador `.agents/skills/gpmh-design/SKILL.md` permite descoberta como skill de repositório; pode ser selecionado no menu de skills da interface. CLI/IDE também permitem `/skills` ou menção com `$`. Leve a pasta toda para manter referências resolvíveis.

Para uso pessoal, pode instalar a pasta completa do ZIP de skill pelo instalador de skills do ambiente. Evite manter uma versão pessoal antiga concorrendo com a do projeto.

Mecanismos documentados em [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) e [skills do Codex](https://learn.chatgpt.com/docs/build-skills).

## Claude Code

Abra o projeto e use `/gpmh-design`. `CLAUDE.md` e `.claude/skills/gpmh-design/SKILL.md` encaminham à mesma fonte. O adaptador depende da pasta `gpmh-design/` na raiz deste pacote; não o copie sozinho.

Para instalar só a skill em outro projeto, extraia **GPMH-DESIGN-SKILL-COMPLETA.zip** e copie a pasta completa `gpmh-design/` para `.claude/skills/gpmh-design/` desse projeto. Para uso pessoal, o destino é `~/.claude/skills/gpmh-design/`. Preserve versões existentes e não mantenha cópias divergentes. No Windows, `~` representa a pasta do usuário.

Esses locais e a invocação seguem a [documentação do Claude Code](https://code.claude.com/docs/en/skills).

## Lovable

Cole o conteúdo de **INSTRUCOES-PROJETO.md** em **Project settings → Knowledge** do projeto GPMH. O arquivo está abaixo do limite documentado de 10.000 caracteres. Depois disponibilize **GPMH-IA-UNIVERSAL.md** e os ativos necessários pelo contexto do projeto/repositório. Se o ambiente não aceitar o anexo, cole os capítulos pertinentes ou adicione o arquivo ao projeto e peça sua leitura explícita.

Não colocar a identidade GPMH no conhecimento geral de um workspace com outros clientes. Não presumir leitura de todo ZIP anexado. A documentação também descreve leitura de `AGENTS.md` na raiz de repositórios acessíveis ao agente: [Knowledge do Lovable](https://docs.lovable.dev/features/knowledge).

## Manus

Em **Skills → + Add → Upload a skill**, importe **GPMH-DESIGN-SKILL-COMPLETA.zip** ou a pasta `gpmh-design/` extraída. Depois selecione a skill com `/` ao iniciar a tarefa. Compartilhe os ativos somente com destinatários autorizados.

A documentação prevê importação por ZIP/pasta e importação via GitHub para repositório público com SKILL.md na raiz. Neste repositório, o arquivo canônico está na subpasta `gpmh-design/SKILL.md`; por isso, use o ZIP de skill ou a pasta extraída para importar. Referência: [skills no Manus](https://help.manus.im/en/articles/14753565-how-to-share-and-use-skills-in-manus).

## Qualquer outra IA

Anexe **GPMH-IA-UNIVERSAL.md**, os arquivos visuais pertinentes e o briefing. Se não houver anexo, cole primeiro **INSTRUCOES-PROJETO.md** e depois os capítulos necessários do documento completo. A versão única contém regras, referências e tokens em texto, sem depender de pastas ocultas. Não inclui os binários do kit. Se a IA não enxergar imagens, ela pode preparar conceito e especificação, mas precisa declarar essa limitação na revisão visual.

## O que foi testado

Validação local: caminhos dos adaptadores, referências do núcleo, versões, documento agregado, limite do texto para Knowledge, igualdade dos tokens/motor, integridade e composição dos ZIPs. Revisão independente de regras e casos de uso documentada em `qa/REVISAO.md`.

Não foram executadas sessões de produção no Cursor, Codex, Claude Code, Lovable ou Manus para homologar acionamento, upload ou saída deste pacote. Esta preparação também não instala a skill no perfil do usuário. Mudanças de interface, limite de plano, tamanho de upload e capacidade de leitura podem exigir ajuste. Quando não houver descoberta automática, usar a entrada Markdown explícita.
