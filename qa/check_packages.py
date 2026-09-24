#!/usr/bin/env python3
"""Inspect generated ZIP contents and paths; no extraction or external services."""
import argparse,json,re,zipfile
from pathlib import Path,PurePosixPath
ROOT=Path(__file__).resolve().parents[1]

def validate(base):
 results=[]
 for filename,root in [('GPMH-DESIGN-SKILL-GITHUB.zip','GPMH-DESIGN-SKILL/'),('GPMH-DESIGN-SKILL-COMPLETA.zip','gpmh-design/'),('GPMH-DESIGN-CLIENTE.zip','GPMH-DESIGN-CLIENTE/')]:
  path=base/filename
  with zipfile.ZipFile(path) as z:
   names=z.namelist();assert len(names)==len(set(names)),'Duplicate members'
   assert z.testzip() is None,'CRC failure'
   assert all(n.startswith(root) and '..' not in PurePosixPath(n).parts for n in names),'Archive root'
   assert not any('__pycache__' in n or n.endswith('.pyc') or n.endswith('Icon\r') for n in names)
   portable=filename!='GPMH-DESIGN-SKILL-COMPLETA.zip'
   core=root+'gpmh-design/' if portable else root
   assert core+'SKILL.md' in names
   assert core+'references/evidencias-e-limites.md' in names
   assert core+'assets/motion/BRAIN-SCULPTURE-LICENSE.md' in names
   markdown=[core+'SKILL.md']+[n for n in names if n.startswith(core+'references/') and n.endswith('.md')]
   if portable:
    for file in ['README.md','AGENTS.md','CLAUDE.md','LEIA-PRIMEIRO-IA.md','INSTRUCOES-PROJETO.md','COMPATIBILIDADE.md','GPMH-IA-UNIVERSAL.md','qa/check_distribution.py','qa/check_packages.py','tools/build_context.py','.cursor/rules/gpmh-design.mdc','.agents/skills/gpmh-design/SKILL.md','.claude/skills/gpmh-design/SKILL.md']:
     assert root+file in names,file
    markdown += [root+f for f in ['README.md','AGENTS.md','CLAUDE.md','LEIA-PRIMEIRO-IA.md','COMPATIBILIDADE.md','.agents/skills/gpmh-design/SKILL.md','.claude/skills/gpmh-design/SKILL.md']]
    assert z.read(root+'GPMH-IA-UNIVERSAL.md')==(ROOT/'GPMH-IA-UNIVERSAL.md').read_bytes()
   for member in markdown:
    for link in re.findall(r'\]\(([^)]+)\)',z.read(member).decode()):
     if link.startswith(('http','#','mailto:')):continue
     parts=[]
     for part in (PurePosixPath(member).parent/PurePosixPath(link)).parts:
      if part=='..':parts.pop()
      elif part!='.':parts.append(part)
     target='/'.join(parts)
     assert target in names or any(n.startswith(target.rstrip('/')+'/') for n in names),(member,link)
   if filename=='GPMH-DESIGN-SKILL-GITHUB.zip':
    assert not any('/brand-kit/' in n or PurePosixPath(n).suffix in {'.otf','.ttf','.woff','.woff2','.zip'} for n in names),'Restricted asset leaked'
    for n in names:
     text=z.read(n).decode('utf-8')
     if n.endswith(('.md','.json','.html','.css','.js','.svg','.mdc')):
      assert '/Users/' not in text and 'mcp_token=' not in text,n
      assert not re.search(r'data:(?:font|application/(?:font|x-font))',text,re.I),n
   else:
    assert core+'assets/brand-kit/assets/fonts/PPNeueCorp-NormalMedium.woff2' in names
    assert core+'assets/brand-kit/assets/logos/gpmh-gptw-extenso-positivo.svg' in names
   if filename=='GPMH-DESIGN-CLIENTE.zip':
    assert root+'MANUAL-GPMH.html' in names and root+'GPMH-DESIGN-SYSTEM-KIT.zip' in names
   results.append({'file':filename,'entries':len(names),'crc':'pass','references':'pass','composition':'pass'})
 return results

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('folder',type=Path);args=parser.parse_args()
 results=validate(args.folder)
 (ROOT/'qa/zip-validation.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
