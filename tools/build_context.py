#!/usr/bin/env python3
"""Generate one portable Markdown context from the canonical GPMH skill."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / 'gpmh-design'
OUTPUT = ROOT / 'GPMH-IA-UNIVERSAL.md'
KNOWLEDGE_OUTPUT = ROOT / 'INSTRUCOES-PROJETO.md'
CHAPTERS = [
    ('processo', 'Processo de criação', 'SKILL.md'),
    ('crivo', 'Crivo de design', 'references/crivo-de-design.md'),
    ('evidencias', 'Evidências e limites', 'references/evidencias-e-limites.md'),
    ('ativos', 'Estado e ativos', 'references/estado-e-ativos.md'),
    ('formatos', 'Formatos e escalas', 'references/formatos.md'),
    ('imagem', 'Imagem e vídeo', 'references/imagem.md'),
    ('movimento', 'Web e movimento', 'references/web-e-movimento.md'),
    ('revisao', 'Revisão e entrega', 'references/revisao.md'),
]

def normalize_paths(content, kit_table=False):
    """Make top-level resource references explicit in a single-file context."""
    content = content.replace(
        'Todos os caminhos deste arquivo são relativos a esta pasta da skill, não ao diretório de trabalho do projeto.',
        'Neste documento único, os links de regras levam aos capítulos incluídos. Os caminhos com prefixo gpmh-design/ identificam recursos no pacote extraído; a tabela de ativos especifica seu próprio diretório-base.')
    content = content.replace(
        'Caminhos que começam por `assets/` nesta referência são relativos à raiz da skill.',
        'Os caminhos de recursos abaixo partem da raiz do pacote extraído.')
    pattern = r'`\.\./assets/([^`]*)`' if kit_table else r'`(?:\.\./)?assets/([^`]*)`'
    return re.sub(pattern, r'`gpmh-design/assets/\1`', content)

def render_knowledge():
    version = json.loads((ROOT / 'VERSION.json').read_text())
    content = (CORE / 'SKILL.md').read_text().split('---', 2)[2].lstrip()
    def link(match):
        label, target = match.groups()
        if target.startswith(('http:', 'https:', '#', 'mailto:')):
            return match.group(0)
        return f'[{label}](gpmh-design/{target})'
    content = normalize_paths(re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, content))
    # Knowledge links are project paths; the attached universal file is the fallback.
    content = content.replace(
        'Neste documento único, os links de regras levam aos capítulos incluídos. Os caminhos com prefixo gpmh-design/ identificam recursos no pacote extraído; a tabela de ativos especifica seu próprio diretório-base.',
        'Os links abaixo apontam ao núcleo no projeto. Sem acesso à pasta, leia os capítulos equivalentes em GPMH-IA-UNIVERSAL.md anexado.')
    header = f"# GPMH · instruções do projeto\n\nPacote {version['skill']} / DS {version['designSystem']} · {version['status']}.\n\n"
    header += 'Aplicar somente a trabalhos GPMH. Leia GPMH-IA-UNIVERSAL.md anexado ou LEIA-PRIMEIRO-IA.md no projeto. Confirme brevemente a versão e os ativos efetivamente acessíveis. O resumo abaixo é gerado do SKILL.md canônico; não manter uma segunda versão manual. Anexar texto não fornece binários de fontes, logos, imagens ou vídeos.\n\n'
    result = header + content
    if len(result) > 10000:
        raise ValueError('Conhecimento do projeto excede 10.000 caracteres.')
    return result

def render():
    version = json.loads((ROOT / 'VERSION.json').read_text())
    anchors = {(CORE / file).resolve(): anchor for anchor, _, file in CHAPTERS}
    anchors[(CORE / 'assets/design-tokens.json').resolve()] = 'tokens'
    output = [
        '# GPMH · base de design para qualquer IA',
        f"Pacote {version['skill']} · DS {version['designSystem']} · {version['date']} · {version['status']}.",
        'Este documento reúne as regras, referências e tokens em texto. Pode ser anexado a uma tarefa sem depender do histórico de conversa ou de pastas ocultas. Use somente para trabalhos GPMH.',
        '**Os binários não estão incorporados:** forneça os logos, fontes, imagens, vídeos e módulos necessários. Caminhos de ativos abaixo identificam o kit; não provam que o arquivo está acessível neste ambiente.',
        'Ao começar, confirme brevemente a versão lida e os ativos disponíveis. Aplique o briefing atual, consulte os capítulos pertinentes e continue etapas independentes quando faltar uma dependência. Não invente o conteúdo de um anexo inacessível.',
        'Arquivo gerado a partir de `gpmh-design/` por `tools/build_context.py`. Alterações devem ser feitas na fonte e regeneradas, evitando versões divergentes.',
        '## Índice\n\n' + '\n'.join(f'- [{title}](#{anchor})' for anchor, title, _ in CHAPTERS) + '\n- [Tokens completos](#tokens)',
    ]
    for anchor, title, file in CHAPTERS:
        path = CORE / file
        content = path.read_text()
        if content.startswith('---\n'):
            content = content.split('---', 2)[2].lstrip()

        def link(match):
            label, target = match.groups()
            if target.startswith(('http:', 'https:', '#', 'mailto:')):
                return match.group(0)
            resolved = (path.parent / target).resolve()
            if resolved in anchors:
                return f'[{label}](#{anchors[resolved]})'
            try:
                relative = resolved.relative_to(CORE).as_posix()
            except ValueError:
                relative = target
            return f'{label} (arquivo do pacote: `gpmh-design/{relative}`)'

        content = normalize_paths(re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, content), kit_table=anchor=='ativos')
        content = re.sub(r'^(#{1,4}) ', r'##\1 ', content, flags=re.M)
        output.append(f'<a id="{anchor}"></a>\n\n## {title}\n\nFonte: `gpmh-design/{file}`.\n\n{content.strip()}')
    tokens = json.loads((CORE / 'assets/design-tokens.json').read_text())
    output.append('<a id="tokens"></a>\n\n## Tokens completos\n\nValores da versão referenciada. Propostas e exceções de campanha conservam o status descrito acima; números de uma peça não são medidas universais. Caminhos de documentação no JSON, como modules/ e docs/, são relativos à raiz do kit de produção (gpmh-design/assets/brand-kit/ no pacote extraído).\n\n```json\n' + json.dumps(tokens, ensure_ascii=False, indent=2) + '\n```')
    return '\n\n'.join(output) + '\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the generated file is stale.')
    args = parser.parse_args()
    outputs = [(OUTPUT, render()), (KNOWLEDGE_OUTPUT, render_knowledge())]
    if args.check:
        if any(not path.exists() or path.read_text() != expected for path, expected in outputs):
            parser.exit(1, 'Documento desatualizado; execute tools/build_context.py.\n')
        print('Documento único e Knowledge correspondem à fonte.')
    else:
        for path, expected in outputs:
            path.write_text(expected)
            print(f'{path.name}: {len(expected)} caracteres.')

if __name__ == '__main__':
    main()
