#!/usr/bin/env python3
"""Validate shared rules, adapters and optional authorized kit. No network."""
from pathlib import Path
import importlib.util,json,re,subprocess,tempfile,zipfile
R=Path(__file__).resolve().parents[1];S=R/'gpmh-design'

def load_module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

def frontmatter(path):
 text=path.read_text();front=text.split('---',2)[1]
 parsed=json.loads(subprocess.check_output(['ruby','-ryaml','-rjson','-e','puts JSON.generate(YAML.safe_load(STDIN.read))'],input=front.encode()))
 assert set(parsed)<= {'name','description','license','allowed-tools','metadata'}
 assert parsed['name']=='gpmh-design' and len(parsed['description'])<=1024 and '<' not in parsed['description'] and '>' not in parsed['description']
 assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',parsed['name']) and '[TODO:' not in text
 return parsed

parsed=frontmatter(S/'SKILL.md');version=json.loads((R/'VERSION.json').read_text())
assert parsed['metadata']['version']==version['skill']
assert parsed['metadata']['design-system']==version['designSystem']
assert json.loads((S/'assets/design-tokens.json').read_text())['version']==version['designSystem']
for path in [R/'.agents/skills/gpmh-design/SKILL.md',R/'.claude/skills/gpmh-design/SKILL.md']:
 frontmatter(path)
 assert (path.parent/'../../../gpmh-design/SKILL.md').resolve()==S/'SKILL.md'
 assert len(path.read_text())<1200
mdc=(R/'.cursor/rules/gpmh-design.mdc').read_text();assert 'alwaysApply: true' in mdc
for link in re.findall(r'@([^\s]+\.md)',mdc):assert (R/link).exists(),link

files=[S/'SKILL.md',*S.glob('references/*.md'),*R.glob('*.md'),R/'.agents/skills/gpmh-design/SKILL.md',R/'.claude/skills/gpmh-design/SKILL.md']
for path in files:
 for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
  if not link.startswith(('http','#','mailto:')):assert (path.parent/link).exists(),str(path)+': '+link

context=load_module('build_context',R/'tools/build_context.py')
assert context.OUTPUT.read_text()==context.render(),'Regenerate universal context'
universal=context.OUTPUT.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',universal))
for target in re.findall(r'\]\(#([^)]*)\)',universal):assert target in anchors,target
knowledge=(R/'INSTRUCOES-PROJETO.md').read_text();assert knowledge==context.render_knowledge();assert len(knowledge)<=10000
for text in [universal,knowledge]:
 for required in ['PP Neue Corp','#FF004C','500','750']:assert required in text,required
 assert '/Users/' not in text and 'mcp_token=' not in text

mod=load_module('attach',R/'tools/attach_brand_kit.py')
with tempfile.TemporaryDirectory(prefix='gpmh-skill-qa-') as temp:
 t=Path(temp);existing=t/'existing';existing.mkdir()
 try:mod.attach('missing.zip',existing);raise AssertionError('overwrite accepted')
 except ValueError:pass
 for filename in ('../escape','/absolute','folder\\escape'):
  bad=t/'bad.zip'
  with zipfile.ZipFile(bad,'w') as z:z.writestr(filename,'x')
  try:mod.attach(bad,t/'result');raise AssertionError('unsafe path accepted')
  except ValueError:pass
  assert not (t/'result').exists()
 bad=t/'version.zip'
 with zipfile.ZipFile(bad,'w') as z:
  for file in mod.REQUIRED:z.writestr(file,json.dumps({'version':'wrong'}) if file.endswith('.json') else 'x')
 try:mod.attach(bad,t/'result');raise AssertionError('wrong version accepted')
 except ValueError:pass
 assert not (t/'result').exists()

kit=S/'assets/brand-kit'
if kit.exists():
 for target in re.findall(r'`(gpmh-design/[^`]+)`',universal):assert (R/target).exists(),target
 assert (S/'assets/design-tokens.json').read_bytes()==(kit/'tokens/design-tokens.json').read_bytes()
 for name in ['brain-sculpture.js','brain-sculpture.css','brain-sculpture-poster.svg']:
  assert (S/'assets/motion'/name).read_bytes()==(kit/'modules'/name).read_bytes(),name

# The portable license changes only its asset-guide navigation; preserve attribution.
if kit.exists():
 core_license=(S/'assets/motion/BRAIN-SCULPTURE-LICENSE.md').read_text()
 kit_license=(kit/'modules/BRAIN-SCULPTURE-LICENSE.md').read_text()
 assert core_license.split('Esta licença refere-se')[0]==kit_license.split('Esta licença refere-se')[0]

result={'version':version,'yamlParser':'Ruby Psych safe_load','frontmatter':'pass','coreReferences':'pass','adapters':'pass','universalContext':'pass','universalCharacters':len(universal),'knowledgeCharacters':len(knowledge),'knowledgeLimit':10000,'attachedKit': 'pass' if kit.exists() else 'not attached; optional','rejectOverwrite':'pass','rejectUnsafePaths':'pass','rejectWrongVersion':'pass','productRuntimeTested':False}
(R/'qa/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
