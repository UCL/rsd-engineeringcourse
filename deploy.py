# Modify the config files to the version used in deployment
import yaml

deployed_path="/training/engineering"

plugin=yaml.load(open('dexyplugin.yaml'))
plugin['reporter:supplementary']['supplementary-location']='../indigo'
plugin['reporter:supplementary']['root']=deployed_path
yaml.dump(plugin,open('dexyplugin.yaml','w'))

dexy=yaml.load(open('dexy.yaml'))
dexy['**/slides.md|jinja|hd|jinja|resub|pandoc|-reveal|resub|h'
     ][2]['resub']['expressions'][2][1]=deployed_path
yaml.dump(dexy,open('dexy.yaml','w'))
