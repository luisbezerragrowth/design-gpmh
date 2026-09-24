#!/usr/bin/env python3
"""Build GitHub sources, standalone private skill and client handoff. No upload."""
import argparse,hashlib,json,zipfile
from build_context import OUTPUT as CONTEXT_OUTPUT, KNOWLEDGE_OUTPUT, render, render_knowledge
from attach_brand_kit import attach
import tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SKILL=ROOT/'gpmh-design'
def eligible(p):return p.is_file() and p.name not in {'.DS_Store','Icon\r'} and '__pycache__' not in p.parts and p.suffix!='.pyc'
def zip_write(dest,items):
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p,name in sorted(items,key=lambda pair:pair[1]):z.write(p,name)
    with zipfile.ZipFile(dest) as z:
        if z.testzip():raise ValueError('ZIP corrompido')
        return {'file':dest.name,'bytes':dest.stat().st_size,'files':len(z.namelist()),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--manual',type=Path,required=True);parser.add_argument('--kit',type=Path,required=True);parser.add_argument('--out',type=Path,required=True);a=parser.parse_args()
    for p in (a.manual,a.kit,SKILL/'assets/brand-kit/tokens/design-tokens.json'):
        if not p.is_file():parser.error('Arquivo necessário ausente: '+str(p))
    version=json.loads((ROOT/'VERSION.json').read_text())
    if json.loads((SKILL/'assets/brand-kit/tokens/design-tokens.json').read_text())['version']!=version['designSystem']:parser.error('Versões divergentes')
    # Validate the actual supplied delivery kit, not only the attached working copy.
    with tempfile.TemporaryDirectory(prefix='gpmh-handoff-check-') as temp:
        checked=attach(a.kit,Path(temp)/'kit')
        if (checked/'tokens/design-tokens.json').read_bytes()!=(SKILL/'assets/design-tokens.json').read_bytes():parser.error('Tokens do ZIP de entrega divergem da fonte')
    CONTEXT_OUTPUT.write_text(render())
    KNOWLEDGE_OUTPUT.write_text(render_knowledge())
    a.out.mkdir(parents=True,exist_ok=True)
    source=[]
    for p in ROOT.rglob('*'):
        rel=p.relative_to(ROOT)
        if not eligible(p) or 'brand-kit' in rel.parts or rel.parts[0]=='.git' or (rel.parts[0]=='qa' and p.suffix=='.json') or p.suffix in {'.zip','.otf','.ttf','.woff','.woff2'} or p.name.startswith('.env') or p.name=='MANUAL-GPMH.html':continue
        source.append((p,'GPMH-DESIGN-SKILL/'+rel.as_posix()))
    skill=[(p,'gpmh-design/'+p.relative_to(SKILL).as_posix()) for p in SKILL.rglob('*') if eligible(p)]
    result=[zip_write(a.out/'GPMH-DESIGN-SKILL-GITHUB.zip',source),zip_write(a.out/'GPMH-DESIGN-SKILL-COMPLETA.zip',skill)]
    client=[(a.manual,'GPMH-DESIGN-CLIENTE/MANUAL-GPMH.html'),(a.kit,'GPMH-DESIGN-CLIENTE/GPMH-DESIGN-SYSTEM-KIT.zip')]
    client += [(p,'GPMH-DESIGN-CLIENTE/'+p.relative_to(ROOT).as_posix()) for p,_ in source if not p.is_relative_to(SKILL)]
    client += [(p,'GPMH-DESIGN-CLIENTE/'+name) for p,name in skill]
    result.append(zip_write(a.out/'GPMH-DESIGN-CLIENTE.zip',client))
    (ROOT/'qa/package-check.json').parent.mkdir(exist_ok=True)
    (ROOT/'qa/package-check.json').write_text(json.dumps({'versions':version,'artifacts':result},indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
