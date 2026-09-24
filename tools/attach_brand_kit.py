#!/usr/bin/env python3
"""Attach an authorized GPMH kit locally. Standard library; no network."""
import argparse,json,re,shutil,stat,tempfile,zipfile
from pathlib import Path,PurePosixPath
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'gpmh-design/assets/brand-kit'
REQUIRED={'tokens/design-tokens.json','modules/brain-sculpture.js','modules/BRAIN-SCULPTURE-LICENSE.md','assets/logos/gpmh-gptw-extenso-positivo.svg','assets/fonts/PPNeueCorp-NormalMedium.woff2','assets/fonts/PPNeueCorp-NormalUltrabold.woff2'}
def attach(source,destination=DEST):
    source=Path(source);destination=Path(destination)
    if destination.exists():raise ValueError('O kit de destino já existe. Preserve a versão anterior com outro nome antes de importar.')
    expected=json.loads((ROOT/'VERSION.json').read_text())['designSystem']
    with zipfile.ZipFile(source) as z:
        entries=z.infolist();names=[i.filename for i in entries]
        if len(names)!=len(set(names)):raise ValueError('ZIP contém nomes duplicados.')
        for item in entries:
            path=PurePosixPath(item.filename)
            if path.is_absolute() or '..' in path.parts or '\\' in item.filename or ':' in item.filename or stat.S_ISLNK(item.external_attr>>16):
                raise ValueError('Caminho inseguro ou link no ZIP.')
        if sum(i.file_size for i in entries)>150_000_000:raise ValueError('Kit maior que o limite previsto de150MB.')
        if not REQUIRED.issubset(names):raise ValueError('Estrutura incompleta: use o ZIP de produção GPMH.')
        tokens=json.loads(z.read('tokens/design-tokens.json'))
        if tokens.get('version')!=expected:raise ValueError('Versão do kit diferente da base da skill; atualizar referências antes de importar.')
        destination.parent.mkdir(parents=True,exist_ok=True)
        staging=Path(tempfile.mkdtemp(prefix='gpmh-kit-',dir=destination.parent))
        try:
            z.extractall(staging)
            # Remove machine-specific provenance from this distribution copy only.
            for file in staging.rglob('*'):
                if not file.is_file() or file.suffix not in {'.md','.json','.html','.css','.js','.svg'}:continue
                text=file.read_text()
                text=re.sub(r'/Users/[^/\s]+/Public/Materiais cursos/[^\n`]+','[prompt de curso no acervo de origem]',text)
                text=re.sub(r'/Users/[^/\s]+/[^\n`"<>]+','[caminho local no acervo de origem]',text)
                text=re.sub(r'https://[^\s"<>)]*cloudfront\.net/[^\s"<>)]*','[arquivo de geração no acervo de origem]',text)
                file.write_text(text)
            for manifest in ('assets/manifest.json','assets/delivery-manifest.json'):
                p=staging/manifest
                if not p.exists():continue
                data=json.loads(p.read_text());data['distributionNote']='Cópia de distribuição com caminhos pessoais desidentificados. Hashes do manifesto referem-se ao acervo de origem.'
                p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
            (staging/'DISTRIBUICAO-LOCAL.md').write_text('Cópia de produção para equipe autorizada. Licenças e fontes não são liberadas para redistribuição pública. Ver docs/ATIVOS-E-LICENCAS.md. Caminhos pessoais foram desidentificados; originais preservados.\n')
            staging.rename(destination)
        except Exception:
            shutil.rmtree(staging);raise
    return destination
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('kit',type=Path);args=parser.parse_args()
    try:print(attach(args.kit))
    except (ValueError,zipfile.BadZipFile,FileNotFoundError,json.JSONDecodeError) as exc:parser.exit(1,str(exc)+'\n')
