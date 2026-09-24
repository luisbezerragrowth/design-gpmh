# Como entregar à equipe

## Começar sem se perder

Extraia **GPMH-DESIGN-CLIENTE.zip**. A pasta contém:

1. **MANUAL-GPMH.html:** apresentação para cliente, direção e designers. Abrir no navegador. Feedback pode indicar capítulo, captura e resultado esperado.
2. **GPMH-DESIGN-SYSTEM-KIT.zip:** ativos e modelos para produção por designers, com suas condições de uso.
3. **LEIA-PRIMEIRO-IA.md:** entrada para qualquer agente com acesso à pasta.
4. **GPMH-IA-UNIVERSAL.md:** documento único para anexar em uma IA, com regras e tokens. Anexar também os ativos pertinentes; o texto não contém fontes/fotos/logos.
5. **INSTRUCOES-PROJETO.md:** resumo para conhecimento persistente de um projeto GPMH.
6. **COMPATIBILIDADE.md:** instalação e início no Cursor, Codex, Claude Code, Lovable, Manus e outros ambientes.

As pastas ocultas `.cursor`, `.agents` e `.claude` são adaptadores de projeto. Não as mova isoladamente: elas apontam para `gpmh-design/`, que é a fonte compartilhada. Se for instalar apenas uma skill, use o ZIP de skill completo, entregue separadamente.

## Texto para acompanhar o envio

> Segue a base de design da Great People Mental Health para revisão e uso da equipe. O manual apresenta a identidade e as aplicações; o kit contém os ativos; a base para IA orienta criação e revisão em diferentes ferramentas. Comecem pelo README e pelo guia de compatibilidade. Tipografia, cores, margens, hierarquia, recortes, imagem e movimento têm critérios explícitos. A consolidação está em revisão: comentários devem indicar o trecho, o problema e o resultado esperado. Usar com os ativos e licenças autorizados para a equipe.

Minuta preparada; nenhum envio foi feito.

## GitHub e manutenção

Fonte compartilhada no repositório privado [design-gpmh](https://github.com/luisbezerragrowth/design-gpmh). O ZIP GitHub exclui fontes comerciais e kit completo; cada destinatário autorizado anexa o kit à sua cópia. Uma mudança é feita na fonte `gpmh-design/` e o documento único é regenerado, evitando regras diferentes por ferramenta.

Não sobrescrever AGENTS.md, CLAUDE.md ou regras de um projeto existente sem preservar seu conteúdo. Integrar a entrada GPMH com o caminho real para o pacote. Não chamar o DS de oficial aprovado antes de decisão explícita.

## Hospedagem da apresentação

O ZIP Netlify já entregue é uma publicação separada do benchmark. Não subir esta pasta de instruções como site. Licenças e público de acesso seguem [DISTRIBUICAO.md](DISTRIBUICAO.md); um repositório privado não torna um site automaticamente privado.
