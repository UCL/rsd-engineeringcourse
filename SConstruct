import rsdpandoc.builders
import rsdpandoc.globbers

env=Environment(tools=['default',rsdpandoc.builders.add_builders])
env["HavePIL"]=True
env["HaveWSD"]=True
env["HaveWebKit"]=True

sources = [
	Glob("session*/*.md"),
]

rsdpandoc.globbers.mixed_html_layout(sources,env,asset_sources="session*/figures")
rsdpandoc.globbers.latex_layout(sources,env,asset_sources="session*/figures")
#rsdpandoc.globbers.latex_layout(sources,env)